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

if coral == '1.6.0':
    assert 'Coesão Interna' in release
    assert 'coral.release.arquitetura/1' in release
    assert 'coral.release.runtime_stdlib/1' in release
    assert 'Coesão interna com fronteiras verificáveis' in index
    assert extensao == '0.53.0', versao
    assert livro == '1.5.8', versao

    persistencia = (root / 'docs/paginas/modulos/persistencia.md').read_text(encoding='utf-8')
    for esperado in ('VERSOES_LEITURA', 'VERSAO_ESCRITA', 'politica_persistencia'):
        assert esperado in persistencia, esperado

print(f'OK: identidade Coral {coral}, VS Code {extensao} e Livro {livro} confirmadas.')
PY

find tools -type d -name '__pycache__' -prune -exec rm -rf {} +
find tools -type f -name '*.pyc' -delete

printf '\n==> Resultado\n' | tee -a "$REPORT"
printf 'Todos os gates locais do site foram concluídos com sucesso.\n' | tee -a "$REPORT"
printf 'Relatório: %s\n' "$REPORT" | tee -a "$REPORT"
