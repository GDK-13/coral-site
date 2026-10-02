#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib
import json
import re
import sys
import tempfile
from pathlib import Path
from typing import Any

from atualizar_docs import open_release_zip

ROOT = Path(__file__).resolve().parents[1]
DOCS_SOURCE = ROOT / "docs" / "paginas"
DATA = ROOT / "docs" / "dados"
MANIFEST = DATA / "validacao_exemplos.json"

FENCE_RE = re.compile(r"```([^\n`]*)\n(.*?)\n```", re.S)
IMPORT_RE = re.compile(r"^\s*de\s+(coral(?:\.[\w.]+)*)\s+importe\s+(.+?)\s*$", re.M)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def json_load(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def coral_blocks() -> list[dict[str, Any]]:
    blocks: list[dict[str, Any]] = []
    for path in sorted(DOCS_SOURCE.rglob("*.md")):
        rel = path.relative_to(ROOT).as_posix()
        ordinal = 0
        for match in FENCE_RE.finditer(path.read_text(encoding="utf-8")):
            language = match.group(1).strip().casefold()
            if language != "coral" and not language.startswith("coral-"):
                continue
            ordinal += 1
            code = match.group(2)
            blocks.append({"arquivo": rel, "bloco": ordinal, "codigo": code})
    return blocks


def block_signature(blocks: list[dict[str, Any]]) -> str:
    digest = hashlib.sha256()
    for item in blocks:
        digest.update(item["arquivo"].encode("utf-8"))
        digest.update(b"\0")
        digest.update(str(item["bloco"]).encode("ascii"))
        digest.update(b"\0")
        digest.update(item["codigo"].encode("utf-8"))
        digest.update(b"\0")
    return digest.hexdigest()


def module_contract() -> dict[str, set[str]]:
    modules = json_load(DATA / "modulos.json", [])
    contract: dict[str, set[str]] = {}
    for module in modules:
        names = set(str(x) for x in module.get("operacoes", []))
        names.update(str(entry.get("nome", "")) for entry in module.get("api", []))
        names.discard("")
        contract[str(module.get("importacao", ""))] = names
    return contract


def audit_imports(blocks: list[dict[str, Any]]) -> tuple[int, list[str]]:
    contract = module_contract()
    errors: list[str] = []
    checked = 0
    for item in blocks:
        for match in IMPORT_RE.finditer(item["codigo"]):
            module = match.group(1)
            raw_names = match.group(2)
            checked += 1
            if module not in contract:
                errors.append(
                    f"{item['arquivo']} bloco {item['bloco']}: módulo importado não existe na release: {module}"
                )
                continue
            for raw in raw_names.split(","):
                name = raw.strip().split(" como ", 1)[0].strip()
                if not name or name == "*":
                    continue
                if name not in contract[module]:
                    errors.append(
                        f"{item['arquivo']} bloco {item['bloco']}: {module}.{name} não pertence à superfície pública atual"
                    )
    return checked, errors


def release_payload(zip_path: Path, version: str) -> tuple[bytes, dict[str, bytes]]:
    with open_release_zip(zip_path) as zf:
        runtime_candidates = [
            name for name in zf.namelist()
            if name.endswith(f"/Projeto/dist/coral-{version}.pyz")
            or name.endswith(f"/Instalacao/Runtime/coral-{version}.pyz")
        ]
        if not runtime_candidates:
            raise RuntimeError(f"runtime coral-{version}.pyz não encontrado na release")
        runtime_candidates.sort(key=lambda name: (0 if "/Projeto/dist/" in name else 1, len(name), name))
        runtime = zf.read(runtime_candidates[0])
        examples = {
            name.split("Coral/", 1)[-1]: zf.read(name)
            for name in zf.namelist()
            if name.startswith("Coral/Exemplos/") and name.endswith(".coral")
        }
    return runtime, examples


def import_compiler(runtime_path: Path):
    runtime_str = str(runtime_path)
    sys.path.insert(0, runtime_str)
    try:
        module = importlib.import_module("coral.tradutor")
        return module.compilar_validado
    except Exception:
        if runtime_str in sys.path:
            sys.path.remove(runtime_str)
        raise


def compile_blocks(blocks: list[dict[str, Any]], runtime_bytes: bytes) -> list[str]:
    errors: list[str] = []
    with tempfile.TemporaryDirectory(prefix="coral-site-runtime-") as tmp:
        runtime = Path(tmp) / "runtime.pyz"
        runtime.write_bytes(runtime_bytes)
        compilar_validado = import_compiler(runtime)
        for item in blocks:
            label = f"{item['arquivo']} bloco {item['bloco']}"
            try:
                result = compilar_validado(item["codigo"], label)
                compile(result.codigo, label, "exec")
            except Exception as exc:
                errors.append(f"{label}: {type(exc).__name__}: {exc}")
    return errors


def compile_official_leaf_examples(examples: dict[str, bytes], runtime_bytes: bytes) -> tuple[int, list[str]]:
    """Valida exemplos oficiais que não dependem de contexto de projeto.

    Projetos_Completos possuem módulos locais e formas naturais declaradas no
    próprio projeto, portanto são inventariados e cobertos pelos gates da
    distribuição Coral, mas não são compilados como arquivos isolados aqui.
    """
    errors: list[str] = []
    candidates = {
        name: data for name, data in examples.items()
        if not name.startswith("Exemplos/Projetos_Completos/")
    }
    with tempfile.TemporaryDirectory(prefix="coral-site-runtime-") as tmp:
        runtime = Path(tmp) / "runtime.pyz"
        runtime.write_bytes(runtime_bytes)
        compilar_validado = import_compiler(runtime)
        for name, payload in sorted(candidates.items()):
            try:
                code = payload.decode("utf-8")
                result = compilar_validado(code, name)
                compile(result.codigo, name, "exec")
            except Exception as exc:
                errors.append(f"{name}: {type(exc).__name__}: {exc}")
    return len(candidates), errors


def official_signature(examples: dict[str, bytes]) -> str:
    digest = hashlib.sha256()
    for name, payload in sorted(examples.items()):
        digest.update(name.encode("utf-8"))
        digest.update(b"\0")
        digest.update(hashlib.sha256(payload).digest())
    return digest.hexdigest()


def validate(zip_path: Path, write_manifest: bool = True) -> dict[str, Any]:
    version_data = json_load(DATA / "versao.json", {})
    version = str(version_data.get("coral", ""))
    if not version:
        raise RuntimeError("versão Coral atual ausente em docs/dados/versao.json")

    blocks = coral_blocks()
    runtime_bytes, official_examples = release_payload(zip_path, version)
    errors: list[str] = []

    checked_imports, import_errors = audit_imports(blocks)
    errors.extend(import_errors)
    errors.extend(compile_blocks(blocks, runtime_bytes))

    official_count, official_errors = compile_official_leaf_examples(official_examples, runtime_bytes)
    errors.extend(official_errors)

    inventory = json_load(DATA / "exemplos.json", {"arquivos": []})
    site_inventory = sorted(str(x) for x in inventory.get("arquivos", []))
    release_inventory = sorted(official_examples)
    if site_inventory != release_inventory:
        missing = sorted(set(release_inventory) - set(site_inventory))
        extra = sorted(set(site_inventory) - set(release_inventory))
        if missing:
            errors.append("exemplos oficiais ausentes no inventário do site: " + ", ".join(missing[:12]))
        if extra:
            errors.append("exemplos inexistentes na release ainda listados pelo site: " + ", ".join(extra[:12]))

    if errors:
        raise RuntimeError("\n".join(errors))

    manifest = {
        "coral": version,
        "fonte_release": zip_path.name,
        "runtime_sha256": sha256_bytes(runtime_bytes),
        "blocos_site": len(blocks),
        "blocos_site_validos": len(blocks),
        "imports_verificados": checked_imports,
        "assinatura_blocos_site": block_signature(blocks),
        "exemplos_oficiais_total": len(official_examples),
        "exemplos_oficiais_isolados_validados": official_count,
        "assinatura_exemplos_oficiais": official_signature(official_examples),
        "politica": "todo bloco Coral publicável compila com o runtime corrente e todo import explícito pertence à superfície pública corrente",
    }
    if write_manifest:
        MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser(description="Valida os exemplos do Site Coral contra o runtime da release corrente.")
    parser.add_argument("release", type=Path, help="ZIP completo ou Entrega Final da mesma versão publicada pelo site")
    parser.add_argument("--sem-gravar", action="store_true", help="Valida sem atualizar docs/dados/validacao_exemplos.json")
    args = parser.parse_args()
    if not args.release.is_file():
        parser.error(f"release não encontrada: {args.release}")
    try:
        manifest = validate(args.release, write_manifest=not args.sem_gravar)
    except Exception as exc:
        print("VALIDAÇÃO DOS EXEMPLOS: FALHA", file=sys.stderr)
        print(exc, file=sys.stderr)
        return 1
    print("VALIDAÇÃO DOS EXEMPLOS: OK")
    print(f"Blocos Coral do site: {manifest['blocos_site_validos']}")
    print(f"Imports públicos verificados: {manifest['imports_verificados']}")
    print(f"Exemplos oficiais inventariados: {manifest['exemplos_oficiais_total']}")
    print(f"Exemplos oficiais isolados compilados: {manifest['exemplos_oficiais_isolados_validados']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
