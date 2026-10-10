#!/usr/bin/env bash
set -Eeuo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd -- "$SCRIPT_DIR/.." && pwd)"

cd "$ROOT"

RELEASE_ZIP="${1:-}"

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

if [[ -n "$RELEASE_ZIP" ]]; then
  run "Revalidando exemplos contra o runtime da release" \
    python tools/validar_exemplos_release.py "$RELEASE_ZIP"
fi

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
pdfs = versao.get('livro_pdfs') or []
if pdfs:
    assert len(pdfs) >= 1, pdfs
    for item in pdfs:
        rel = item.get('arquivo') if isinstance(item, dict) else str(item)
        pdf = root / rel
        assert pdf.is_file() and pdf.stat().st_size > 100_000, pdf
else:
    pdf = root / f'downloads/Coral_{livro}_Livro_Oficial.pdf'
    assert pdf.is_file() and pdf.stat().st_size > 100_000, pdf

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
elif coral == '1.7.3':
    assert extensao == '0.74.4', versao
    assert livro == '1.7.0', versao
    tipos = (root / 'docs/paginas/linguagem/tipos_tipagem.md').read_text(encoding='utf-8')
    classes = (root / 'docs/paginas/linguagem/classes_objetos.md').read_text(encoding='utf-8')
    principal = (root / 'docs/paginas/linguagem/programa_principal.md').read_text(encoding='utf-8')
    for esperado in ('lista de decimal', 'texto ou nulo'):
        assert esperado in tipos, esperado
    for esperado in ('herda de A e B', 'chame o método pai'):
        assert esperado in classes, esperado
    assert 'programa principal' in principal
elif coral == '1.7.4':
    assert extensao == '0.75.2', versao
    assert livro == '1.7.0', versao
    vscode = (root / 'docs/paginas/vscode.md').read_text(encoding='utf-8')
    projetos = (root / 'docs/paginas/projetos.md').read_text(encoding='utf-8')
    release = (root / 'docs/paginas/release.md').read_text(encoding='utf-8')
    for esperado in ('Realce semântico por papel', 'dieta do tipo Dieta', 'Inserir estrutura básica do coral.toml'):
        assert esperado in vscode, esperado
    for esperado in ('Interfaces públicas entre módulos', 'Analise_1_7_4/Cadastro'):
        assert esperado in projetos, esperado
    assert '## Coral 1.7.4' in release
elif coral == '1.7.5':
    assert extensao == '0.76.0', versao
    assert livro == '1.7.5', versao
    assert len(versao.get('livro_pdfs') or []) == 2, versao
    tipos = (root / 'docs/paginas/linguagem/tipos_tipagem.md').read_text(encoding='utf-8')
    funcoes = (root / 'docs/paginas/linguagem/funcoes_escopo.md').read_text(encoding='utf-8')
    vscode = (root / 'docs/paginas/vscode.md').read_text(encoding='utf-8')
    release = (root / 'docs/paginas/release.md').read_text(encoding='utf-8')
    for esperado in ('for do tipo Animal', 'modelos.Animal', 'e_tipo'):
        assert esperado in tipos, esperado
    for esperado in ('Chamadas explícitas multilinha', 'chame somar com'):
        assert esperado in funcoes, esperado
    for esperado in ('Coral Language 0.76.0', 'documento aberto', 'chamadas multilinha'):
        assert esperado in vscode, esperado
    assert '## Coral 1.7.5' in release
elif coral == '1.7.8':
    assert extensao == '0.79.0', versao
    assert livro == '1.7.8', versao
    assert len(versao.get('livro_pdfs') or []) == 2, versao
    assert len(versao.get('livro_htmls') or []) == 2, versao
    release = (root / 'docs/paginas/release.md').read_text(encoding='utf-8')
    projetos = (root / 'docs/paginas/projetos.md').read_text(encoding='utf-8')
    arquivos = (root / 'docs/paginas/modulos/arquivos.md').read_text(encoding='utf-8')
    esquemas = (root / 'docs/paginas/modulos/esquemas.md').read_text(encoding='utf-8')
    livro_md = (root / 'docs/paginas/livro.md').read_text(encoding='utf-8')
    for esperado in ('## Coral 1.7.6', '## Coral 1.7.7', '## Coral 1.7.8'):
        assert esperado in release, esperado
    for esperado in ('Ambientes reproduzíveis', 'coral.lock', 'Imports multilinha'):
        assert esperado in projetos, esperado
    for esperado in ('Leitura gradual e CSV', 'ler_lotes_csv', 'escrever_csv'):
        assert esperado in arquivos, esperado
    for esperado in ('Validação não converte', 'validar_registros', 'Importador_Validado'):
        assert esperado in esquemas, esperado
    assert 'Livro Oficial Coral 1.7.8' in livro_md
    assert 'livros/1.7.8/index.html' in index

print(f'OK: identidade Coral {coral}, VS Code {extensao} e Livro {livro} confirmadas.')
PY

find tools -type d -name '__pycache__' -prune -exec rm -rf {} +
find tools -type f -name '*.pyc' -delete

printf '\n==> Resultado\n' | tee -a "$REPORT"
printf 'Todos os gates locais do site foram concluídos com sucesso.\n' | tee -a "$REPORT"
printf 'Relatório: %s\n' "$REPORT" | tee -a "$REPORT"
