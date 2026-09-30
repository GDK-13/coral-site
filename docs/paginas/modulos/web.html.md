# coral.web.html

## Visão geral

`coral.web.html` compõe HTML localmente com escape separado para texto e atributos. Importar o módulo ou renderizar um documento não abre navegador, porta ou conexão de rede.

<!-- AUTO:MODULO -->

**Importação:** `coral.web.html`  
**Categoria:** web  

composição e serialização HTML local com escape por contexto

### Superfície pública detectada

`ErroHTML`, `ElementoHTML`, `FragmentoHTML`, `DocumentoHTML`, `escapar_texto`, `escapar_atributo`, `elemento`, `fragmento`, `documento`, `renderizar`, `tabela`

<!-- /AUTO:MODULO -->

## Quando usar

Use quando precisar gerar relatórios, fragmentos, tabelas ou páginas HTML a partir de dados Coral. Para endereços e consultas, use `coral.web.url`; para rede, use `coral.web.http` ou `coral.web.servidor`.

## Começando

```coral
de coral.web.html importe documento, elemento, tabela, renderizar

defina registros como [{"nome": "A < B", "valor": 3}, {"nome": "C & D", "valor": 7}]
defina grade como tabela(registros, [["nome", "Nome"], ["valor", "Valor"]])
defina titulo como elemento("h1", {}, "Relatório <Coral>")
defina pagina como documento("Dados & Web", [titulo, grade], "pt-BR")
mostre renderizar(pagina)
```

:::resultado
O conteúdo textual é escapado no contexto correto e o programa produz uma página HTML como texto local.
:::

## Segurança de contexto

Texto comum não vira marcação confiável automaticamente. A superfície também recusa atributos de evento inline e esquemas executáveis em atributos de URL.

## Referência da API

<!-- AUTO:API -->

### Funções

#### `escapar_texto`

Escapa um valor para o contexto de texto de um elemento HTML.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valor` | Valor processado pela operação. | `Any` | obrigatório |

**Retorno**

Retorna um valor declarado como `str`.

:::details Detalhes técnicos

**Assinatura:** `escapar_texto(valor: Any) -> str`

**Origem da implementação:** `coral.web.html`

**Arquivo na release:** `coral/web/html.py`

:::

#### `escapar_atributo`

Escapa um valor para atributo entre aspas duplas.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valor` | Valor processado pela operação. | `Any` | obrigatório |

**Retorno**

Retorna um valor declarado como `str`.

:::details Detalhes técnicos

**Assinatura:** `escapar_atributo(valor: Any) -> str`

**Origem da implementação:** `coral.web.html`

**Arquivo na release:** `coral/web/html.py`

:::

#### `elemento`

Cria um elemento validado; texto em ``filhos`` será escapado ao renderizar.

**Exemplo**

```coral
de coral.web.html importe documento, elemento, tabela, renderizar

defina registros como [{"nome": "A < B", "valor": 3}, {"nome": "C & D", "valor": 7}]
defina grade como tabela(registros, [["nome", "Nome"], ["valor", "Valor"]])
defina titulo como elemento("h1", {}, "Relatório <Coral>")
defina pagina como documento("Dados & Web", [titulo, grade], "pt-BR")
mostre renderizar(pagina)
```

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | obrigatório |
| `atributos` | Valor correspondente a atributos. | `Any` | `None` |
| `filhos` | Valor correspondente a filhos. | `Any` | `None` |

**Retorno**

Retorna um valor declarado como `ElementoHTML`.

:::details Detalhes técnicos

**Assinatura:** `elemento(nome: str, atributos: Any = None, filhos: Any = None) -> ElementoHTML`

**Origem da implementação:** `coral.web.html`

**Arquivo na release:** `coral/web/html.py`

**Exceções diretamente observáveis no corpo:** `ErroHTML`

:::

#### `fragmento`

Agrupa nós preservando a ordem sem criar marcação adicional.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `filhos` | Valor correspondente a filhos. | `Any` | `None` |

**Retorno**

Retorna um valor declarado como `FragmentoHTML`.

:::details Detalhes técnicos

**Assinatura:** `fragmento(filhos: Any = None) -> FragmentoHTML`

**Origem da implementação:** `coral.web.html`

**Arquivo na release:** `coral/web/html.py`

:::

#### `documento`

Cria documento completo; título e corpo seguem a mesma política de escape.

**Exemplo**

```coral
de coral.web.html importe documento, elemento, tabela, renderizar

defina registros como [{"nome": "A < B", "valor": 3}, {"nome": "C & D", "valor": 7}]
defina grade como tabela(registros, [["nome", "Nome"], ["valor", "Valor"]])
defina titulo como elemento("h1", {}, "Relatório <Coral>")
defina pagina como documento("Dados & Web", [titulo, grade], "pt-BR")
mostre renderizar(pagina)
```

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `titulo` | Valor correspondente a titulo. | `Any` | obrigatório |
| `corpo` | Valor correspondente a corpo. | `Any` | obrigatório |
| `idioma` | Valor correspondente a idioma. | `str` | `'pt-BR'` |

**Retorno**

Retorna um valor declarado como `DocumentoHTML`.

:::details Detalhes técnicos

**Assinatura:** `documento(titulo: Any, corpo: Any, idioma: str = 'pt-BR') -> DocumentoHTML`

**Origem da implementação:** `coral.web.html`

**Arquivo na release:** `coral/web/html.py`

**Exceções diretamente observáveis no corpo:** `ErroHTML`

:::

#### `renderizar`

Serializa um nó ou valor em memória, sem efeitos externos.

**Exemplo**

```coral
de coral.web.html importe documento, elemento, tabela, renderizar

defina registros como [{"nome": "A < B", "valor": 3}, {"nome": "C & D", "valor": 7}]
defina grade como tabela(registros, [["nome", "Nome"], ["valor", "Valor"]])
defina titulo como elemento("h1", {}, "Relatório <Coral>")
defina pagina como documento("Dados & Web", [titulo, grade], "pt-BR")
mostre renderizar(pagina)
```

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `no` | Valor correspondente a no. | `Any` | obrigatório |

**Retorno**

Retorna um valor declarado como `str`.

:::details Detalhes técnicos

**Assinatura:** `renderizar(no: Any) -> str`

**Origem da implementação:** `coral.web.html`

**Arquivo na release:** `coral/web/html.py`

:::

#### `tabela`

Monta tabela a partir de registros comuns com colunas explícitas.

**Exemplo**

```coral
de coral.web.html importe documento, elemento, tabela, renderizar

defina registros como [{"nome": "A < B", "valor": 3}, {"nome": "C & D", "valor": 7}]
defina grade como tabela(registros, [["nome", "Nome"], ["valor", "Valor"]])
defina titulo como elemento("h1", {}, "Relatório <Coral>")
defina pagina como documento("Dados & Web", [titulo, grade], "pt-BR")
mostre renderizar(pagina)
```

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `registros` | Valor correspondente a registros. | `Iterable[Any]` | obrigatório |
| `colunas` | Valor correspondente a colunas. | `Any` | obrigatório |

**Retorno**

Retorna um valor declarado como `ElementoHTML`.

:::details Detalhes técnicos

**Assinatura:** `tabela(registros: Iterable[Any], colunas: Any) -> ElementoHTML`

**Origem da implementação:** `coral.web.html`

**Arquivo na release:** `coral/web/html.py`

**Exceções diretamente observáveis no corpo:** `ErroHTML`

:::

### Classes e protocolos

#### `ElementoHTML`

Elemento validado com atributos e filhos em ordem estável.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | obrigatório |
| `atributos` | Valor correspondente a atributos. | `tuple[tuple[str, Any], ...]` | `()` |
| `filhos` | Valor correspondente a filhos. | `tuple[Any, ...]` | `()` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | obrigatório |
| `atributos` | Valor correspondente a atributos. | `tuple[tuple[str, Any], ...]` | `()` |
| `filhos` | Valor correspondente a filhos. | `tuple[Any, ...]` | `()` |

:::details Detalhes técnicos

**Assinatura:** `ElementoHTML(nome: str, atributos: tuple[tuple[str, Any], ...] = (), filhos: tuple[Any, ...] = ())`

**Origem da implementação:** `coral.web.html`

**Arquivo na release:** `coral/web/html.py`

:::

#### `FragmentoHTML`

Sequência de nós sem elemento contêiner adicional.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `filhos` | Valor correspondente a filhos. | `tuple[Any, ...]` | obrigatório |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `filhos` | Valor correspondente a filhos. | `tuple[Any, ...]` | obrigatório |

:::details Detalhes técnicos

**Assinatura:** `FragmentoHTML(filhos: tuple[Any, ...])`

**Origem da implementação:** `coral.web.html`

**Arquivo na release:** `coral/web/html.py`

:::

#### `DocumentoHTML`

Documento HTML completo com idioma e UTF 8 declarados.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `titulo` | Valor correspondente a titulo. | `str` | obrigatório |
| `corpo` | Valor correspondente a corpo. | `FragmentoHTML` | obrigatório |
| `idioma` | Valor correspondente a idioma. | `str` | `'pt-BR'` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `titulo` | Valor correspondente a titulo. | `str` | obrigatório |
| `corpo` | Valor correspondente a corpo. | `FragmentoHTML` | obrigatório |
| `idioma` | Valor correspondente a idioma. | `str` | `'pt-BR'` |

:::details Detalhes técnicos

**Assinatura:** `DocumentoHTML(titulo: str, corpo: FragmentoHTML, idioma: str = 'pt-BR')`

**Origem da implementação:** `coral.web.html`

**Arquivo na release:** `coral/web/html.py`

:::

### Exceções

#### `ErroHTML`

Falha de composição ou serialização HTML controlada pela Coral.

:::details Detalhes técnicos

**Assinatura:** `ErroHTML(...)`

**Origem da implementação:** `coral.web.html`

**Arquivo na release:** `coral/web/html.py`

:::

<!-- /AUTO:API -->
