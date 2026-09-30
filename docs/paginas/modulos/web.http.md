# coral.web.http

## Visão geral

`coral.web.http` é o cliente HTTP geral da Coral. Respostas preservam status, cabeçalhos e corpo em bytes; texto e JSON são interpretações explícitas feitas somente quando o programa pede.

<!-- AUTO:MODULO -->

**Importação:** `coral.web.http`  
**Categoria:** web  

cliente HTTP limitado com bytes, timeout, redirecionamentos e TLS verificado

### Superfície pública detectada

`ErroHTTP`, `ErroLimiteHTTP`, `ErroRedirecionamentoHTTP`, `RespostaHTTP`, `TEMPO_LIMITE_PADRAO`, `LIMITE_RESPOSTA_PADRAO`, `MAX_REDIRECIONAMENTOS_PADRAO`, `requisitar`, `obter`, `enviar`, `codificar_formulario`

<!-- /AUTO:MODULO -->

## Quando usar

Use para GET, POST e outras requisições HTTP com timeout, limite de resposta, redirecionamentos controlados, proxy explícito e verificação TLS. Para montar URLs sem rede, use `coral.web.url`.

## Começando

```coral
de coral.web.http importe obter

defina resposta como obter("https://exemplo.test/dados", tempo_limite=2, limite_resposta=4096)
mostre resposta.status
mostre resposta.texto("utf-8")
```

:::resultado
A resposta mantém o corpo bruto e só o converte para texto quando `texto()` é chamado. O exemplo depende de um endereço HTTP realmente acessível.
:::

## Limites e redirecionamentos

Timeout e limite de resposta são parte do contrato. Redirecionamentos possuem teto e métodos com efeito não são repetidos implicitamente. HTTPS verifica certificado e hostname por padrão.

## Formulários

`codificar_formulario` preserva campos repetidos em UTF 8 e pode ser combinado com `enviar` quando o servidor espera `application/x-www-form-urlencoded`.

## Referência da API

<!-- AUTO:API -->

### Funções

#### `requisitar`

Executa uma requisição HTTP limitada e retorna resposta inspecionável.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `metodo` | Valor correspondente a metodo. | `str` | obrigatório |
| `url` | Valor correspondente a url. | `str` | obrigatório |
| `cabecalhos` | Valor correspondente a cabecalhos. | `Any` | `None` |
| `corpo` | Valor correspondente a corpo. | `Any` | `None` |
| `tempo_limite` | Valor correspondente a tempo limite. | `float` | `TEMPO_LIMITE_PADRAO` |
| `codificacao_corpo` | Valor correspondente a codificacao corpo. | `str \| None` | `None` |
| `limite_resposta` | Valor correspondente a limite resposta. | `int` | `LIMITE_RESPOSTA_PADRAO` |
| `seguir_redirecionamentos` | Valor correspondente a seguir redirecionamentos. | `bool \| None` | `None` |
| `max_redirecionamentos` | Valor correspondente a max redirecionamentos. | `int` | `MAX_REDIRECIONAMENTOS_PADRAO` |
| `proxy` | Valor correspondente a proxy. | `Any` | `None` |
| `contexto_tls` | Valor correspondente a contexto tls. | `ssl.SSLContext \| None` | `None` |

**Retorno**

Retorna um valor declarado como `RespostaHTTP`.

:::details Detalhes técnicos

**Assinatura:** `requisitar(metodo: str, url: str, cabecalhos: Any = None, corpo: Any = None, tempo_limite: float = TEMPO_LIMITE_PADRAO, *, codificacao_corpo: str \| None = None, limite_resposta: int = LIMITE_RESPOSTA_PADRAO, seguir_redirecionamentos: bool \| None = None, max_redirecionamentos: int = MAX_REDIRECIONAMENTOS_PADRAO, proxy: Any = None, contexto_tls: ssl.SSLContext \| None = None) -> RespostaHTTP`

**Origem da implementação:** `coral.web.http`

**Arquivo na release:** `coral/web/http.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `metodo` | posicional |
| `url` | posicional |
| `cabecalhos` | posicional |
| `corpo` | posicional |
| `tempo_limite` | posicional |
| `codificacao_corpo` | nomeado |
| `limite_resposta` | nomeado |
| `seguir_redirecionamentos` | nomeado |
| `max_redirecionamentos` | nomeado |
| `proxy` | nomeado |
| `contexto_tls` | nomeado |

**Exceções diretamente observáveis no corpo:** `ErroValor`, `ErroHTTP`

:::

#### `obter`

Atalho para GET com as mesmas regras de :func:`requisitar`.

**Exemplo**

```coral
de coral.web.http importe obter

defina resposta como obter("https://exemplo.test/dados", tempo_limite=2, limite_resposta=4096)
mostre resposta.status
mostre resposta.texto("utf-8")
```

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `url` | Valor correspondente a url. | `str` | obrigatório |
| `cabecalhos` | Valor correspondente a cabecalhos. | `Any` | `None` |
| `tempo_limite` | Valor correspondente a tempo limite. | `float` | `TEMPO_LIMITE_PADRAO` |
| `**opcoes` | Valor correspondente a opcoes. | `Any` | obrigatório |

**Retorno**

Retorna um valor declarado como `RespostaHTTP`.

:::details Detalhes técnicos

**Assinatura:** `obter(url: str, cabecalhos: Any = None, tempo_limite: float = TEMPO_LIMITE_PADRAO, **opcoes: Any) -> RespostaHTTP`

**Origem da implementação:** `coral.web.http`

**Arquivo na release:** `coral/web/http.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `url` | posicional |
| `cabecalhos` | posicional |
| `tempo_limite` | posicional |
| `**opcoes` | variádico nomeado |

:::

#### `enviar`

Atalho para POST; redirecionamentos exigem opt-in por padrão.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `url` | Valor correspondente a url. | `str` | obrigatório |
| `corpo` | Valor correspondente a corpo. | `Any` | obrigatório |
| `cabecalhos` | Valor correspondente a cabecalhos. | `Any` | `None` |
| `tempo_limite` | Valor correspondente a tempo limite. | `float` | `TEMPO_LIMITE_PADRAO` |
| `**opcoes` | Valor correspondente a opcoes. | `Any` | obrigatório |

**Retorno**

Retorna um valor declarado como `RespostaHTTP`.

:::details Detalhes técnicos

**Assinatura:** `enviar(url: str, corpo: Any, cabecalhos: Any = None, tempo_limite: float = TEMPO_LIMITE_PADRAO, **opcoes: Any) -> RespostaHTTP`

**Origem da implementação:** `coral.web.http`

**Arquivo na release:** `coral/web/http.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `url` | posicional |
| `corpo` | posicional |
| `cabecalhos` | posicional |
| `tempo_limite` | posicional |
| `**opcoes` | variádico nomeado |

:::

#### `codificar_formulario`

Codifica formulário ``application/x-www-form-urlencoded`` em UTF 8.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `campos` | Valor correspondente a campos. | `Any` | obrigatório |

**Retorno**

Retorna um valor declarado como `bytes`.

:::details Detalhes técnicos

**Assinatura:** `codificar_formulario(campos: Any) -> bytes`

**Origem da implementação:** `coral.web.http`

**Arquivo na release:** `coral/web/http.py`

:::

### Classes e protocolos

#### `RespostaHTTP`

Resposta HTTP materializada com corpo preservado em bytes.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `status` | Valor correspondente a status. | `int` | obrigatório |
| `cabecalhos` | Valor correspondente a cabecalhos. | `tuple[tuple[str, str], ...]` | obrigatório |
| `corpo_bytes` | Valor correspondente a corpo bytes. | `bytes` | obrigatório |
| `url` | Valor correspondente a url. | `str` | obrigatório |
| `metodo` | Valor correspondente a metodo. | `str` | obrigatório |
| `redirecionamentos` | Valor correspondente a redirecionamentos. | `int` | `0` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `status` | Valor correspondente a status. | `int` | obrigatório |
| `cabecalhos` | Valor correspondente a cabecalhos. | `tuple[tuple[str, str], ...]` | obrigatório |
| `corpo_bytes` | Valor correspondente a corpo bytes. | `bytes` | obrigatório |
| `url` | Valor correspondente a url. | `str` | obrigatório |
| `metodo` | Valor correspondente a metodo. | `str` | obrigatório |
| `redirecionamentos` | Valor correspondente a redirecionamentos. | `int` | `0` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `sucesso` | Indica o estado de sucesso. | `bool` |
| `cabecalho` | Obtém o último valor de um cabeçalho sem alterar a resposta. | `str \| None` |
| `texto` | Decodifica o corpo sob demanda usando codificação explícita. | `str` |
| `json` | Decodifica JSON sem transformar erro de formato em erro de transporte. | `Any` |

:::details Detalhes técnicos

**Assinatura:** `RespostaHTTP(status: int, cabecalhos: tuple[tuple[str, str], ...], corpo_bytes: bytes, url: str, metodo: str, redirecionamentos: int = 0)`

**Origem da implementação:** `coral.web.http`

**Arquivo na release:** `coral/web/http.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `sucesso` | propriedade | `sucesso() -> bool` |
| `cabecalho` | método | `cabecalho(nome: str, padrao: str \| None = None) -> str \| None` |
| `texto` | método | `texto(codificacao: str = 'utf-8', *, erros: str = 'strict') -> str` |
| `json` | método | `json() -> Any` |

:::

### Exceções

#### `ErroHTTP`

Falha de transporte ou política do cliente HTTP da Coral.

:::details Detalhes técnicos

**Assinatura:** `ErroHTTP(...)`

**Origem da implementação:** `coral.web.http`

**Arquivo na release:** `coral/web/http.py`

:::

#### `ErroLimiteHTTP`

Resposta excedeu um limite declarado pelo programa.

:::details Detalhes técnicos

**Assinatura:** `ErroLimiteHTTP(...)`

**Origem da implementação:** `coral.web.http`

**Arquivo na release:** `coral/web/http.py`

:::

#### `ErroRedirecionamentoHTTP`

Cadeia de redirecionamento viola o contrato configurado.

:::details Detalhes técnicos

**Assinatura:** `ErroRedirecionamentoHTTP(...)`

**Origem da implementação:** `coral.web.http`

**Arquivo na release:** `coral/web/http.py`

:::

### Constantes e aliases

#### `TEMPO_LIMITE_PADRAO`

Expõe a constante pública `TEMPO_LIMITE_PADRAO`.

:::details Detalhes técnicos

**Assinatura:** `TEMPO_LIMITE_PADRAO`

**Origem da implementação:** `coral.web.http`

**Arquivo na release:** `coral/web/http.py`

**Valor declarado:** `10.0`

:::

#### `LIMITE_RESPOSTA_PADRAO`

Expõe a constante pública `LIMITE_RESPOSTA_PADRAO`.

:::details Detalhes técnicos

**Assinatura:** `LIMITE_RESPOSTA_PADRAO`

**Origem da implementação:** `coral.web.http`

**Arquivo na release:** `coral/web/http.py`

**Valor declarado:** `8 * 1024 * 1024`

:::

#### `MAX_REDIRECIONAMENTOS_PADRAO`

Expõe a constante pública `MAX_REDIRECIONAMENTOS_PADRAO`.

:::details Detalhes técnicos

**Assinatura:** `MAX_REDIRECIONAMENTOS_PADRAO`

**Origem da implementação:** `coral.web.http`

**Arquivo na release:** `coral/web/http.py`

**Valor declarado:** `5`

:::

<!-- /AUTO:API -->
