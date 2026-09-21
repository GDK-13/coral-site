# Site da Coral

Site estático da Coral preparado para GitHub Pages, com landing page e documentação regenerável a partir de Markdown e dos contratos da release oficial.

## Uso rápido

Editar documentação:

```bash
python tools/atualizar_docs.py
```

Importar uma nova release:

```bash
python tools/atualizar_docs.py /caminho/Coral_1.5.10_Completo.zip
```

Gerar sitemap/robots com o domínio real (antes de publicar):

```bash
python tools/atualizar_docs.py --somente-gerar --url-base=https://SEU-DOMINIO
```

Pré visualizar localmente:

```bash
python -m http.server 8000
```

Depois abra `http://localhost:8000/` para a landing e `http://localhost:8000/docs/` para a documentação.

## Arquivos principais

* `index.html`: landing page
* `404.html`: página de erro temática
* `robots.txt` / `sitemap.xml`: SEO (domínio placeholder — regenere com `--url-base`)
* `assets/fonts/`: fontes oficiais self-hosted (WOFF2)
* `assets/images/compartilhar.png`: imagem de compartilhamento OG/Twitter (1200×630)
* `docs/index.html`: entrada da documentação multipágina
* `docs/*.html`: páginas gerais geradas
* `docs/modulos/*.html`: uma página gerada por módulo, separada entre módulos principais e complementares
* `docs.html`: redirecionamento de compatibilidade para `docs/index.html`
* `docs/paginas/`: conteúdo editorial em Markdown
* `assets/css/styles.css`: estilos do site (as regras `@font-face` ficam em `fontes-arquivo.css`/`fontes-embutidas.css`, escolhidas por protocolo)
* `assets/js/site.js`: tema, menus, TOC, âncoras e o motor + a paleta da busca global
* `docs/dados/`: dados mecânicos compartilhados (inclui `indice_busca.json`/`.js`, o índice da busca global)
* `templates/docs.html`: estrutura HTML da documentação
* `tools/atualizar_docs.py`: importador de releases e orquestrador (gera também sitemap/robots)
* `tools/api_docs.py`: extrator estático da API pública da release
* `tools/site_renderer.py`: renderer multipágina, navegação e índice de busca
* `.vscode/tasks.json`: tarefas rápidas do VS Code
* `WORKFLOW_SITE_CORAL.md`: workflow completo de manutenção e publicação

## Módulos principais

A documentação dá prioridade editorial a `coral.numerico`, `coral.sistema`, `coral.laboratorio`, `coral.hardware`, `coral.mundo`, `coral.regras`, `coral.rpg` e `coral.jogos`. Esses módulos recebem guias aprofundados e aparecem separados dos módulos complementares na barra lateral.

A classificação é mantida no campo `destaque` do inventário de módulos, e o gerador preserva essa hierarquia ao importar novas releases.

## Identidade visual

A implementação segue as referências oficiais da identidade visual da Coral. A landing e a documentação compartilham a mesma paleta, tipografia, padrão de anéis e regras de acessibilidade. As fontes (Fraunces, Atkinson Hyperlegible, JetBrains Mono) são servidas localmente de `assets/fonts/`, sem dependência de CDNs — o site funciona integralmente offline.

O símbolo circular com `C` continua sendo um placeholder até o SVG final da marca ser definido.

A auditoria de conformidade contra a identidade consolidada e o registro das correções aplicadas ficam em `CORRECOES_IDENTIDADE_VISUAL.md`. O registro das melhorias de nível superior (busca global, fontes self-hosted, SEO/compartilhamento, âncoras copiáveis, micro-interações) fica em `MELHORIAS_SITE.md`.

O realce de sintaxe Coral está implementado no renderer estático. A especificação e os critérios de aceite ficam em `REALCE_SINTAXE.md`; o contrato importado da release fica em `docs/dados/sintaxe.json`.

## Validação rápida

Antes de publicar, execute:

```bash
python tools/validar_site.py
```

Esse gate verifica o realce léxico Coral, fidelidade do texto copiado, whitelist de linguagens, contrato sintático, links locais, âncoras e IDs.

## Funcionalidades da documentação

* **Busca global (paleta de comandos)**: abre com o botão de lupa, tecla `/` ou `Ctrl/Cmd+K` em qualquer página (inclusive a landing e a 404). Multi-termo (AND com fallback para resultados parciais), ignora acentos, tolera erros de digitação, entende plurais, ranqueia por título/seção/corpo, sugere "você quis dizer", mostra visitados recentemente e destaca as ocorrências na página atual. Funciona em http e via `file://` (duplo clique no `index.html`).
* **Âncoras copiáveis**: cada título de seção tem um `#` discreto que copia o link direto da seção.
* **Compartilhamento**: todas as páginas têm metadados Open Graph/Twitter com imagem de cartão em `assets/images/compartilhar.png`.
* **Alternância de tema** claro/escuro persistida, respeitando `prefers-color-scheme`.
