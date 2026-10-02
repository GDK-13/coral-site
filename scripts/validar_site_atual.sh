#!/usr/bin/env bash
set -Eeuo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd -- "$SCRIPT_DIR/.." && pwd)"

cd "$ROOT"

VERSION="$(python - <<'PY'
from pathlib import Path
import json
p = Path('docs/dados/versao.json')
data = json.loads(p.read_text(encoding='utf-8'))
print(data['coral'])
PY
)"
REPORT="$ROOT/resultado_validacao_site_${VERSION//./_}.txt"
: > "$REPORT"

run() {
  printf '\n==> %s\n' "$1" | tee -a "$REPORT"
  shift
  "$@" 2>&1 | tee -a "$REPORT"
}

printf 'Validação local do Site Coral %s\n' "$VERSION" | tee -a "$REPORT"
printf 'Raiz: %s\n' "$ROOT" | tee -a "$REPORT"
printf 'Python: %s\n' "$(python --version 2>&1)" | tee -a "$REPORT"

run "Regenerando documentação sem reimportar a release" \
  python tools/atualizar_docs.py --somente-gerar

run "Testando o realce de sintaxe" \
  python tools/test_syntax_highlight.py

run "Executando o validador estrutural do site" \
  python tools/validar_site.py

run "Verificando sintaxe dos utilitários Python" \
  python -m compileall -q tools

printf '\n==> Conferindo identidade da release atual\n' | tee -a "$REPORT"
python - <<'PY' 2>&1 | tee -a "$REPORT"
from pathlib import Path
import json

root = Path('.')
versao = json.loads((root / 'docs/dados/versao.json').read_text(encoding='utf-8'))
coral = versao['coral']
extensao = versao['extensao_vscode']
livro = versao['livro']

assert coral and extensao and livro, versao
assert versao.get('estavel') is True, versao

index = (root / 'index.html').read_text(encoding='utf-8')
for esperado in (
    coral,
    extensao,
    livro,
    f'coral-{coral}.pyz',
):
    assert esperado in index, esperado

release = (root / 'docs/paginas/release.md').read_text(encoding='utf-8')
assert f'Coral {coral}' in release or coral in release, coral

intro = (root / 'docs/paginas/introducao.md').read_text(encoding='utf-8')
assert 'Português corrente' in intro

livro_md = (root / 'docs/paginas/livro.md').read_text(encoding='utf-8')
pdf = root / f'downloads/Coral_{livro}_Livro_Oficial.pdf'
assert pdf.is_file() and pdf.stat().st_size > 100_000, pdf
assert pdf.name in index, pdf.name

landing_low = index.casefold()
for proibido in ('roadmap', 'checkpoint', 'congelamento', 'linha 1.5', 'linha 1.6'):
    assert proibido not in landing_low, proibido
assert 'Notas de versão' in index

if coral == '1.7.2':
    assert extensao == '0.74.0', versao
    assert livro == '1.7.0', versao
    diagnosticos = (root / 'docs/paginas/diagnosticos.md').read_text(encoding='utf-8')
    for esperado in ('R102', 'R110', 'R203', 'exceptionInfo.details.diagnostico'):
        assert esperado in diagnosticos, esperado
    tipos = (root / 'docs/paginas/modulos/tipos.md').read_text(encoding='utf-8')
    assert 'valor for do tipo inteiro' in tipos

print(f'OK: identidade Coral {coral}, VS Code {extensao} e Livro {livro} confirmadas.')
PY

find tools -type d -name '__pycache__' -prune -exec rm -rf {} +
find tools -type f -name '*.pyc' -delete

printf '\n==> Resultado\n' | tee -a "$REPORT"
printf 'Todos os gates locais do site foram concluídos com sucesso.\n' | tee -a "$REPORT"
printf 'Relatório: %s\n' "$REPORT" | tee -a "$REPORT"
