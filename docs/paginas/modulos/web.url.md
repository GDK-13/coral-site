# coral.web.url

## Visão geral

`coral.web.url` manipula URLs e consultas como dados textuais. Ele codifica UTF 8, preserva ordem e chaves repetidas e não realiza acesso externo.

<!-- AUTO:MODULO -->

**Importação:** `coral.web.url`  
**Categoria:** web  

URLs e consultas UTF 8 manipuladas localmente, sem acesso à rede

### Superfície pública detectada

`ErroURL`, `EnderecoURL`, `codificar_consulta`, `ler_consulta`, `juntar`, `decompor`

<!-- /AUTO:MODULO -->

## Quando usar

Use para montar consultas, decompor endereços ou resolver referências relativas antes de passá las para outra camada. Se você precisa efetuar uma requisição, use `coral.web.http`.

## Começando

```coral
de coral.web.url importe codificar_consulta, juntar, decompor

defina consulta como codificar_consulta([["tag", "coral"], ["tag", "web"], ["q", "ação"]])
defina endereco como juntar("https://exemplo.test/docs/", "busca?" + consulta)
defina partes como decompor(endereco)
mostre partes.caminho
```

:::resultado
A URL é composta e decomposta apenas como texto; nenhuma conexão de rede é aberta.
:::

## Consultas repetidas

`codificar_consulta` e `ler_consulta` preservam chaves repetidas, campos vazios e ordem. Isso evita perder informação ao trabalhar com formulários e filtros.

## Referência da API

<!-- AUTO:API -->

### Funções

#### `codificar_consulta`

Codifica pares ordenados em UTF 8 preservando chaves repetidas.

**Exemplo**

```coral
de coral.web.url importe codificar_consulta, juntar, decompor

defina consulta como codificar_consulta([["tag", "coral"], ["tag", "web"], ["q", "ação"]])
defina endereco como juntar("https://exemplo.test/docs/", "busca?" + consulta)
defina partes como decompor(endereco)
mostre partes.caminho
```

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `parametros` | Valor correspondente a parametros. | `Any` | obrigatório |

**Retorno**

Retorna um valor declarado como `str`.

:::details Detalhes técnicos

**Assinatura:** `codificar_consulta(parametros: Any) -> str`

**Origem da implementação:** `coral.web.url`

**Arquivo na release:** `coral/web/url.py`

:::

#### `ler_consulta`

Lê consulta em UTF 8, preservando ordem, vazios e duplicatas.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `texto` | Texto processado pela operação. | `Any` | obrigatório |

**Retorno**

Retorna um valor declarado como `tuple[tuple[str, str], ...]`.

:::details Detalhes técnicos

**Assinatura:** `ler_consulta(texto: Any) -> tuple[tuple[str, str], ...]`

**Origem da implementação:** `coral.web.url`

**Arquivo na release:** `coral/web/url.py`

**Exceções diretamente observáveis no corpo:** `ErroURL`

:::

#### `juntar`

Resolve referência contra uma base usando apenas regras textuais de URL.

**Exemplo**

```coral
de coral.web.url importe codificar_consulta, juntar, decompor

defina consulta como codificar_consulta([["tag", "coral"], ["tag", "web"], ["q", "ação"]])
defina endereco como juntar("https://exemplo.test/docs/", "busca?" + consulta)
defina partes como decompor(endereco)
mostre partes.caminho
```

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `base` | Base usada pela conversão ou cálculo. | `Any` | obrigatório |
| `referencia` | Valor correspondente a referencia. | `Any` | obrigatório |

**Retorno**

Retorna um valor declarado como `str`.

:::details Detalhes técnicos

**Assinatura:** `juntar(base: Any, referencia: Any) -> str`

**Origem da implementação:** `coral.web.url`

**Arquivo na release:** `coral/web/url.py`

**Exceções diretamente observáveis no corpo:** `ErroURL`

:::

#### `decompor`

Decompõe uma URL com esquema explícito sem realizar acesso externo.

**Exemplo**

```coral
de coral.web.url importe codificar_consulta, juntar, decompor

defina consulta como codificar_consulta([["tag", "coral"], ["tag", "web"], ["q", "ação"]])
defina endereco como juntar("https://exemplo.test/docs/", "busca?" + consulta)
defina partes como decompor(endereco)
mostre partes.caminho
```

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `endereco` | Valor correspondente a endereco. | `Any` | obrigatório |

**Retorno**

Retorna um valor declarado como `EnderecoURL`.

:::details Detalhes técnicos

**Assinatura:** `decompor(endereco: Any) -> EnderecoURL`

**Origem da implementação:** `coral.web.url`

**Arquivo na release:** `coral/web/url.py`

**Exceções diretamente observáveis no corpo:** `ErroURL`

:::

### Classes e protocolos

#### `EnderecoURL`

Componentes textuais de uma URL com esquema explícito.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `esquema` | Valor correspondente a esquema. | `str` | obrigatório |
| `autoridade` | Valor correspondente a autoridade. | `str` | obrigatório |
| `host` | Valor correspondente a host. | `str \| None` | obrigatório |
| `porta` | Valor correspondente a porta. | `int \| None` | obrigatório |
| `caminho` | Caminho do arquivo ou diretório usado pela operação. | `str` | obrigatório |
| `consulta` | Valor correspondente a consulta. | `str` | obrigatório |
| `fragmento` | Valor correspondente a fragmento. | `str` | obrigatório |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `esquema` | Valor correspondente a esquema. | `str` | obrigatório |
| `autoridade` | Valor correspondente a autoridade. | `str` | obrigatório |
| `host` | Valor correspondente a host. | `str \| None` | obrigatório |
| `porta` | Valor correspondente a porta. | `int \| None` | obrigatório |
| `caminho` | Caminho do arquivo ou diretório usado pela operação. | `str` | obrigatório |
| `consulta` | Valor correspondente a consulta. | `str` | obrigatório |
| `fragmento` | Valor correspondente a fragmento. | `str` | obrigatório |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `parametros` | Consulta decodificada preservando ordem e chaves repetidas. | `tuple[tuple[str, str], ...]` |
| `reconstruir` | Reconstrói a URL sem acessar a rede. | `str` |

:::details Detalhes técnicos

**Assinatura:** `EnderecoURL(esquema: str, autoridade: str, host: str \| None, porta: int \| None, caminho: str, consulta: str, fragmento: str)`

**Origem da implementação:** `coral.web.url`

**Arquivo na release:** `coral/web/url.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `parametros` | propriedade | `parametros() -> tuple[tuple[str, str], ...]` |
| `reconstruir` | método | `reconstruir() -> str` |

:::

### Exceções

#### `ErroURL`

URL ou consulta não obedece ao contrato esperado.

:::details Detalhes técnicos

**Assinatura:** `ErroURL(...)`

**Origem da implementação:** `coral.web.url`

**Arquivo na release:** `coral/web/url.py`

:::

<!-- /AUTO:API -->
