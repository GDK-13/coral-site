# Workflow oficial do site da Coral

Este documento define como manter a landing page e a documentação do repositório `coral-site` atualizadas sem transformar cada release em uma edição manual de dezenas de arquivos HTML.

## 1. Princípio

O site separa três tipos de conteúdo:

* **automático:** versões, módulos, superfície pública detectável, comandos CLI, inventário de exemplos e changelog;
* **semiautomático:** criação de páginas para módulos novos e relatórios de diferenças entre releases;
* **manual:** explicações, tutoriais, decisões de uso, exemplos comentados e boas práticas.

O gerador pode atualizar blocos mecânicos, mas não deve apagar texto pedagógico escrito fora deles.

## 2. Documentação multipágina

A documentação não é mais um único `docs.html` gigante.

A entrada oficial é:

```text
docs/index.html
```

As páginas gerais são geradas separadamente:

```text
docs/instalacao.html
docs/primeiro-programa.html
docs/projetos.html
docs/vscode.html
docs/testes.html
docs/repl_cli.html
docs/exemplos.html
docs/livro.html
docs/release.html
```

Cada módulo também recebe sua própria página:

```text
docs/modulos/aleatorio.html
docs/modulos/jogos.html
docs/modulos/mundo.html
...
```

O arquivo raiz `docs.html` existe apenas como redirecionamento de compatibilidade para `docs/index.html`.

## 3. Regra da navegação

A coluna da esquerda é a navegação global da documentação.

A coluna da direita, **Nesta página**, contém somente os títulos `##` e `###` da página atual.

Assim, abrir `coral.aleatorio` mostra no índice da direita apenas itens como:

```text
Visão geral
Operações publicadas pela release
Quando usar
Começando
Cuidados
Relações com outros módulos
```

Ela nunca deve repetir a lista inteira da documentação.

Os módulos são divididos em dois grupos de navegação:

* **Módulos principais:** `coral.numerico`, `coral.sistema`, `coral.laboratorio`, `coral.hardware`, `coral.mundo`, `coral.regras`, `coral.rpg` e `coral.jogos`;
* **Outros módulos:** superfícies complementares e especializadas.

A classificação vem do campo `destaque` de `docs/dados/modulos.json`, preenchido pelo importador da release. O grupo principal fica aberto nas páginas gerais e nas páginas principais; o grupo complementar abre quando uma de suas páginas está ativa.

A coluna **Nesta página** continua sendo local. Em **todas as páginas de módulo** ela mostra apenas títulos `##`. Conceitos internos em `###` e entradas individuais da API em `####` permanecem navegáveis no conteúdo, mas não poluem o índice lateral.

## 4. Fontes editáveis

Os HTMLs públicos são artefatos gerados. O conteúdo editorial vive em Markdown:

```text
docs/paginas/
├── introducao.md
├── instalacao.md
├── primeiro_programa.md
├── projetos.md
├── vscode.md
├── testes.md
├── repl_cli.md
├── exemplos.md
├── livro.md
├── release.md
└── modulos/
```

Para corrigir uma explicação, edite o Markdown correspondente e regenere o site.

## 5. Estrutura completa

```text
coral-site/
├── .vscode/
│   └── tasks.json
├── assets/
│   ├── css/
│   │   └── styles.css
│   ├── icons/
│   ├── images/
│   └── js/
│       └── site.js
├── docs/
│   ├── index.html                 # gerado
│   ├── instalacao.html            # gerado
│   ├── ...
│   ├── modulos/
│   │   ├── aleatorio.html         # gerado
│   │   └── ...
│   ├── dados/
│   │   ├── versao.json
│   │   ├── modulos.json
│   │   ├── cli.json
│   │   ├── exemplos.json
│   │   ├── navegacao.json
│   │   ├── sintaxe.json
│   │   └── snapshot_release.json
│   ├── paginas/                   # editar aqui
│   │   ├── introducao.md
│   │   ├── ...
│   │   └── modulos/
│   ├── changelog/
│   └── REVISAO_PENDENTE.md
├── templates/
│   └── docs.html
├── tools/
│   ├── atualizar_docs.py
│   ├── api_docs.py
│   ├── site_renderer.py
│   ├── syntax_highlight.py
│   ├── test_syntax_highlight.py
│   └── validar_site.py
├── docs.html                      # redirecionamento
├── index.html
├── README.md
└── WORKFLOW_SITE_CORAL.md
```

## 6. Atualização editorial comum

Depois de editar um Markdown:

```bash
python tools/atualizar_docs.py --somente-gerar
```

Também funciona:

```bash
python tools/atualizar_docs.py
```

No VS Code use a tarefa:

```text
Coral Site: Atualizar documentação
```

O gerador recria todas as páginas públicas, os links relativos, o índice local de cada página e a navegação anterior e próxima.

## 7. Atualização após uma nova release Coral

Use o ZIP oficial completo:

```bash
python tools/atualizar_docs.py /caminho/Coral_1.5.12_Completo.zip
```

O importador atualiza:

* versão do runtime;
* versão da extensão Coral Language;
* edição do Livro;
* módulos publicados;
* operações detectáveis dos módulos;
* comandos e subcomandos CLI;
* inventário de exemplos `.coral`;
* changelog;
* contrato sintático para o realce estático (`docs/dados/sintaxe.json`);
* snapshot da release anterior;
* blocos automáticos das páginas de módulos.

Depois ele regenera todas as páginas HTML.

## 8. Blocos automáticos e referência de API

Páginas de módulos usam dois blocos mecânicos:

```text
<!-- AUTO:MODULO -->
...
<!-- /AUTO:MODULO -->

<!-- AUTO:API -->
...
<!-- /AUTO:API -->
```

`AUTO:MODULO` mantém metadados da superfície publicada. `AUTO:API` é construído por `tools/api_docs.py` a partir do código da própria release e combina duas camadas. A primeira é didática e prioriza descrição curta, exemplo quando houver uso real na página, parâmetros com significado e retorno em linguagem legível. A segunda fica recolhida em **Detalhes técnicos** e preserva assinatura exata, origem, arquivo da implementação, modo dos parâmetros, exceções diretamente observáveis e outras evidências estruturais.

`Quando usar`, `Em palavras`, `Cuidados` e `Erros comuns` não são repetidos mecanicamente em cada símbolo. Eles entram apenas quando o conteúdo editorial acrescenta contexto real. O gerador também reaproveita a tabela manual **API essencial** como evidência editorial, sem substituir a informação técnica da release nem inventar tipos ausentes.

Somente esses blocos são substituídos durante a importação. Conceitos, tutoriais, decisões de uso, exemplos comentados, erros comuns e boas práticas permanecem sob revisão humana.

Os módulos principais recebem a camada editorial mais extensa, com foco também na arquitetura de domínio. Os **módulos secundários** não são tratados como simples fichas: cada página deve conter visão geral, papel no ecossistema, conceitos principais, quando usar, exemplo validado, API essencial, fluxos comuns, erros e casos de borda, boas práticas, integração, testabilidade/previsibilidade, compatibilidade e a referência automática completa da API. A diferença entre os grupos é de prioridade e profundidade de domínio, não de qualidade documental.

Outras páginas usam blocos equivalentes para versão da extensão, CLI, exemplos, edição do Livro e changelog.

## 9. Realce de sintaxe Coral

O realce da documentação é estático e gerado no servidor pelo `tools/syntax_highlight.py`. Somente cercas `coral` e `coral-*` recebem realce. Blocos `bash`, `text`, `json`, `toml` e outras linguagens permanecem intactos.

Ao importar uma release, `tools/atualizar_docs.py` lê estaticamente `esquema_sintatico.py`, `lexico.py` e `identificadores.py` do ZIP oficial e regenera `docs/dados/sintaxe.json`. Nenhum código Python da release é executado para descobrir a sintaxe.

O renderer reconhece strings, comentários, números, caminhos `coral.*`, lexemas sintáticos e chamadas tradicionais com parênteses. Formas naturais dependentes de contexto semântico não são inventadas por regex.

A implementação deve manter a fidelidade do clipboard: o texto recuperado de um bloco realçado precisa ser idêntico ao Markdown original.

A especificação completa está em `REALCE_SINTAXE.md`.

## 10. Validação automatizada

Antes de publicar ou depois de importar uma release:

```bash
python tools/validar_site.py
```

O gate cobre testes unitários do realce, whitelist de linguagens, strings e escapes, comentários, ponto decimal, identificadores, caminhos de módulo, chamadas naturais não inferidas, segurança HTML, fidelidade dos blocos de código, links, âncoras e IDs.

## 11. `REVISAO_PENDENTE.md`

Depois de importar uma release, leia:

```text
docs/REVISAO_PENDENTE.md
```

Ele informa módulos novos, removidos ou alterados, mudanças de CLI e mudanças na biblioteca de exemplos.

O gerador detecta diferenças, mas não decide sozinho como uma funcionalidade nova deve ser ensinada.

## 12. Fonte única de versão

`docs/dados/versao.json` alimenta landing e documentação.

Exemplo:

```json
{
  "coral": "1.5.12",
  "extensao_vscode": "0.43.0",
  "livro": "1.5.8",
  "estavel": true
}
```

O HTML também recebe valores de fallback durante a geração para continuar legível quando aberto diretamente.

## 13. Revisão local

Sirva o repositório:

```bash
python -m http.server 8000
```

Confira pelo menos:

```text
http://localhost:8000/
http://localhost:8000/docs/
http://localhost:8000/docs/instalacao.html
http://localhost:8000/docs/modulos/jogos.html
```

Antes da inspeção visual, rode:

```bash
python tools/validar_site.py
```

Revise:

* landing;
* página inicial da documentação;
* uma página geral;
* um módulo principal;
* um módulo complementar;
* tema claro e escuro;
* busca local da página;
* coluna **Nesta página**;
* sidebar recolhida e expandida;
* menu mobile;
* foco por teclado;
* `REVISAO_PENDENTE.md`.

## 14. Publicação

Depois da revisão:

```bash
git status
git add .
git commit -m "Atualiza documentação para Coral 1.5.12"
git push
```

Com GitHub Pages apontado para `main`, a publicação ocorre após o push.

## 15. Fluxo resumido

```text
Coral finalizada
       ↓
ZIP oficial completo
       ↓
python tools/atualizar_docs.py Coral_X.Y.Z_Completo.zip
       ↓
comparação com snapshot anterior
       ↓
dados mecânicos atualizados
       ↓
blocos automáticos sincronizados
       ↓
páginas HTML separadas regeneradas
       ↓
REVISAO_PENDENTE.md
       ↓
revisão humana
       ↓
preview local
       ↓
git commit + git push
       ↓
GitHub Pages atualizado
```

## 16. Identidade visual

Landing, documentação e páginas geradas seguem a identidade oficial da Coral já consolidada no projeto.

O gerador não pode trocar por conta própria a paleta, Fraunces, Atkinson Hyperlegible, JetBrains Mono, regras de acessibilidade ou o padrão de anéis.
