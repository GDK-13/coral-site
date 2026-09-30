# coral.web.servidor

## Visão geral

`coral.web.servidor` oferece um servidor HTTP local para desenvolvimento, demonstrações e integração entre módulos Coral. Criar o objeto servidor não abre porta; isso só acontece quando `iniciar()` é chamado.

<!-- AUTO:MODULO -->

**Importação:** `coral.web.servidor`  
**Categoria:** web  

servidor HTTP local de desenvolvimento com rotas literais, gráficos interativos e limites explícitos

### Superfície pública detectada

`ErroServidorHTTP`, `ErroRotaHTTP`, `ErroLimiteCorpoHTTP`, `RequisicaoHTTP`, `RespostaServidorHTTP`, `ServidorHTTP`, `HOST_PADRAO`, `PORTA_PADRAO`, `LIMITE_CORPO_PADRAO`, `LIMITE_ARQUIVO_PADRAO`, `TEMPO_LIMITE_CORPO_PADRAO`, `resposta_bytes`, `resposta_texto`, `resposta_html`, `resposta_grafico`, `resposta_json`, `resposta_arquivo`, `criar_servidor`

<!-- /AUTO:MODULO -->

## Quando usar

Use para expor rotas locais, respostas de texto, HTML, JSON, arquivos ou gráficos durante desenvolvimento e experimentação. O módulo não é apresentado como servidor de hospedagem de produção.

## Começando

```coral
de coral.web.servidor importe criar_servidor, resposta_texto

crie a função inicio com requisicao
    retorne resposta_texto("Servidor Coral local")
fim

defina servidor como criar_servidor()
execute servidor.adicionar_rota("GET", "/", inicio)
execute servidor.iniciar()
mostre servidor.url_base
execute servidor.encerrar()
```

:::resultado
O servidor abre uma porta local somente após `iniciar()`, mostra sua URL base e fecha o socket quando `encerrar()` é chamado.
:::

## Respostas estruturadas

As funções `resposta_texto`, `resposta_html`, `resposta_json`, `resposta_arquivo` e `resposta_grafico` constroem respostas sem conversões silenciosas. Arquivos permanecem sob a raiz declarada e o corpo da requisição possui limite explícito.

## Integração com gráficos

`resposta_grafico` adapta uma especificação de `coral.graficos` para HTML interativo. A adaptação não inicia servidor nem abre porta por conta própria.

## Referência da API

<!-- AUTO:API -->

### Funções

#### `resposta_bytes`

Executa a operação `resposta_bytes` disponibilizada por `coral.web.servidor`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `corpo` | Valor correspondente a corpo. | `Any` | obrigatório |
| `status` | Valor correspondente a status. | `int` | `200` |
| `cabecalhos` | Valor correspondente a cabecalhos. | `Any` | `None` |
| `tipo_conteudo` | Valor correspondente a tipo conteudo. | `str` | `'application/octet-stream'` |

**Retorno**

Retorna um valor declarado como `RespostaServidorHTTP`.

:::details Detalhes técnicos

**Assinatura:** `resposta_bytes(corpo: Any, status: int = 200, cabecalhos: Any = None, *, tipo_conteudo: str = 'application/octet-stream') -> RespostaServidorHTTP`

**Origem da implementação:** `coral.web.servidor`

**Arquivo na release:** `coral/web/servidor.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `corpo` | posicional |
| `status` | posicional |
| `cabecalhos` | posicional |
| `tipo_conteudo` | nomeado |

:::

#### `resposta_texto`

Executa a operação `resposta_texto` disponibilizada por `coral.web.servidor`.

**Exemplo**

```coral
crie a função inicio com requisicao
    retorne resposta_texto("Servidor Coral local")
fim

defina servidor como criar_servidor()
```

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `texto` | Texto processado pela operação. | `Any` | obrigatório |
| `status` | Valor correspondente a status. | `int` | `200` |
| `cabecalhos` | Valor correspondente a cabecalhos. | `Any` | `None` |
| `codificacao` | Codificação de texto usada na leitura ou escrita. | `str` | `'utf-8'` |

**Retorno**

Retorna um valor declarado como `RespostaServidorHTTP`.

:::details Detalhes técnicos

**Assinatura:** `resposta_texto(texto: Any, status: int = 200, cabecalhos: Any = None, *, codificacao: str = 'utf-8') -> RespostaServidorHTTP`

**Origem da implementação:** `coral.web.servidor`

**Arquivo na release:** `coral/web/servidor.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `texto` | posicional |
| `status` | posicional |
| `cabecalhos` | posicional |
| `codificacao` | nomeado |

**Exceções diretamente observáveis no corpo:** `ErroValor`

:::

#### `resposta_html`

Executa a operação `resposta_html` disponibilizada por `coral.web.servidor`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `conteudo` | Conteúdo processado ou armazenado. | `Any` | obrigatório |
| `status` | Valor correspondente a status. | `int` | `200` |
| `cabecalhos` | Valor correspondente a cabecalhos. | `Any` | `None` |

**Retorno**

Retorna um valor declarado como `RespostaServidorHTTP`.

:::details Detalhes técnicos

**Assinatura:** `resposta_html(conteudo: Any, status: int = 200, cabecalhos: Any = None) -> RespostaServidorHTTP`

**Origem da implementação:** `coral.web.servidor`

**Arquivo na release:** `coral/web/servidor.py`

:::

#### `resposta_grafico`

Adapta um gráfico Coral para resposta HTML sem iniciar servidor.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `grafico` | Valor correspondente a grafico. | `Any` | obrigatório |
| `status` | Valor correspondente a status. | `int` | `200` |
| `cabecalhos` | Valor correspondente a cabecalhos. | `Any` | `None` |
| `limite_pontos` | Valor correspondente a limite pontos. | `int` | `200000` |

**Retorno**

Retorna um valor declarado como `RespostaServidorHTTP`.

:::details Detalhes técnicos

**Assinatura:** `resposta_grafico(grafico: Any, status: int = 200, cabecalhos: Any = None, *, limite_pontos: int = 200000) -> RespostaServidorHTTP`

**Origem da implementação:** `coral.web.servidor`

**Arquivo na release:** `coral/web/servidor.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `grafico` | posicional |
| `status` | posicional |
| `cabecalhos` | posicional |
| `limite_pontos` | nomeado |

:::

#### `resposta_json`

Executa a operação `resposta_json` disponibilizada por `coral.web.servidor`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valor` | Valor processado pela operação. | `Any` | obrigatório |
| `status` | Valor correspondente a status. | `int` | `200` |
| `cabecalhos` | Valor correspondente a cabecalhos. | `Any` | `None` |

**Retorno**

Retorna um valor declarado como `RespostaServidorHTTP`.

:::details Detalhes técnicos

**Assinatura:** `resposta_json(valor: Any, status: int = 200, cabecalhos: Any = None) -> RespostaServidorHTTP`

**Origem da implementação:** `coral.web.servidor`

**Arquivo na release:** `coral/web/servidor.py`

**Exceções diretamente observáveis no corpo:** `ErroFormato`

:::

#### `resposta_arquivo`

Executa a operação `resposta_arquivo` disponibilizada por `coral.web.servidor`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `raiz` | Valor correspondente a raiz. | `Any` | obrigatório |
| `caminho_relativo` | Valor correspondente a caminho relativo. | `Any` | obrigatório |
| `status` | Valor correspondente a status. | `int` | `200` |
| `cabecalhos` | Valor correspondente a cabecalhos. | `Any` | `None` |
| `limite_arquivo` | Valor correspondente a limite arquivo. | `int` | `LIMITE_ARQUIVO_PADRAO` |

**Retorno**

Retorna um valor declarado como `RespostaServidorHTTP`.

:::details Detalhes técnicos

**Assinatura:** `resposta_arquivo(raiz: Any, caminho_relativo: Any, status: int = 200, cabecalhos: Any = None, *, limite_arquivo: int = LIMITE_ARQUIVO_PADRAO) -> RespostaServidorHTTP`

**Origem da implementação:** `coral.web.servidor`

**Arquivo na release:** `coral/web/servidor.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `raiz` | posicional |
| `caminho_relativo` | posicional |
| `status` | posicional |
| `cabecalhos` | posicional |
| `limite_arquivo` | nomeado |

**Exceções diretamente observáveis no corpo:** `ErroValor`, `ErroServidorHTTP`

:::

#### `criar_servidor`

Cria servidor sem abrir a porta; chame ``iniciar`` ou use ``com``.

**Exemplo**

```coral
fim

defina servidor como criar_servidor()
execute servidor.adicionar_rota("GET", "/", inicio)
execute servidor.iniciar()
mostre servidor.url_base
```

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `host` | Valor correspondente a host. | `str` | `HOST_PADRAO` |
| `porta` | Valor correspondente a porta. | `int` | `PORTA_PADRAO` |
| `**opcoes` | Valor correspondente a opcoes. | `Any` | obrigatório |

**Retorno**

Retorna um valor declarado como `ServidorHTTP`.

:::details Detalhes técnicos

**Assinatura:** `criar_servidor(host: str = HOST_PADRAO, porta: int = PORTA_PADRAO, **opcoes: Any) -> ServidorHTTP`

**Origem da implementação:** `coral.web.servidor`

**Arquivo na release:** `coral/web/servidor.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `host` | posicional |
| `porta` | posicional |
| `**opcoes` | variádico nomeado |

:::

### Classes e protocolos

#### `RequisicaoHTTP`

Requisição materializada antes da chamada ao tratador da rota.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `metodo` | Valor correspondente a metodo. | `str` | obrigatório |
| `caminho` | Caminho do arquivo ou diretório usado pela operação. | `str` | obrigatório |
| `consulta` | Valor correspondente a consulta. | `tuple[tuple[str, str], ...]` | obrigatório |
| `cabecalhos` | Valor correspondente a cabecalhos. | `tuple[tuple[str, str], ...]` | obrigatório |
| `corpo_bytes` | Valor correspondente a corpo bytes. | `bytes` | obrigatório |
| `cliente` | Valor correspondente a cliente. | `str` | obrigatório |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `metodo` | Valor correspondente a metodo. | `str` | obrigatório |
| `caminho` | Caminho do arquivo ou diretório usado pela operação. | `str` | obrigatório |
| `consulta` | Valor correspondente a consulta. | `tuple[tuple[str, str], ...]` | obrigatório |
| `cabecalhos` | Valor correspondente a cabecalhos. | `tuple[tuple[str, str], ...]` | obrigatório |
| `corpo_bytes` | Valor correspondente a corpo bytes. | `bytes` | obrigatório |
| `cliente` | Valor correspondente a cliente. | `str` | obrigatório |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `cabecalho` | Executa a operação `cabecalho` disponibilizada por `coral.web.servidor`. | `str \| None` |
| `texto` | Executa a operação `texto` disponibilizada por `coral.web.servidor`. | `str` |
| `json` | Executa a operação `json` disponibilizada por `coral.web.servidor`. | `Any` |
| `formulario` | Executa a operação `formulario` disponibilizada por `coral.web.servidor`. | `tuple[tuple[str, str], ...]` |

:::details Detalhes técnicos

**Assinatura:** `RequisicaoHTTP(metodo: str, caminho: str, consulta: tuple[tuple[str, str], ...], cabecalhos: tuple[tuple[str, str], ...], corpo_bytes: bytes, cliente: str)`

**Origem da implementação:** `coral.web.servidor`

**Arquivo na release:** `coral/web/servidor.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `cabecalho` | método | `cabecalho(nome: str, padrao: str \| None = None) -> str \| None` |
| `texto` | método | `texto(codificacao: str = 'utf-8', *, erros: str = 'strict') -> str` |
| `json` | método | `json() -> Any` |
| `formulario` | método | `formulario() -> tuple[tuple[str, str], ...]` |

:::

#### `RespostaServidorHTTP`

Resposta pronta para serialização pelo servidor local.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `status` | Valor correspondente a status. | `int` | obrigatório |
| `cabecalhos` | Valor correspondente a cabecalhos. | `tuple[tuple[str, str], ...]` | obrigatório |
| `corpo_bytes` | Valor correspondente a corpo bytes. | `bytes` | obrigatório |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `status` | Valor correspondente a status. | `int` | obrigatório |
| `cabecalhos` | Valor correspondente a cabecalhos. | `tuple[tuple[str, str], ...]` | obrigatório |
| `corpo_bytes` | Valor correspondente a corpo bytes. | `bytes` | obrigatório |

:::details Detalhes técnicos

**Assinatura:** `RespostaServidorHTTP(status: int, cabecalhos: tuple[tuple[str, str], ...], corpo_bytes: bytes)`

**Origem da implementação:** `coral.web.servidor`

**Arquivo na release:** `coral/web/servidor.py`

:::

#### `ServidorHTTP`

Servidor HTTP pequeno, explícito e orientado a desenvolvimento local.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `host` | Valor correspondente a host. | `str` | `HOST_PADRAO` |
| `porta` | Valor correspondente a porta. | `int` | `PORTA_PADRAO` |
| `limite_corpo` | Valor correspondente a limite corpo. | `int` | `LIMITE_CORPO_PADRAO` |
| `tempo_limite_corpo` | Valor correspondente a tempo limite corpo. | `float` | `TEMPO_LIMITE_CORPO_PADRAO` |
| `raiz_arquivos` | Valor correspondente a raiz arquivos. | `Any` | `None` |
| `permitir_externo` | Controla se deve permitir externo. | `bool` | `False` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `ativo` | Indica o estado de ativo. | `bool` |
| `porta` | Executa a operação `porta` disponibilizada por `coral.web.servidor`. | `int` |
| `url_base` | Executa a operação `url_base` disponibilizada por `coral.web.servidor`. | `str` |
| `ultimo_erro` | Executa a operação `ultimo_erro` disponibilizada por `coral.web.servidor`. | `BaseException \| None` |
| `adicionar_rota` | Adiciona rota. | `'ServidorHTTP'` |
| `adicionar_arquivo` | Adiciona arquivo. | `'ServidorHTTP'` |
| `iniciar` | Inicia o valor solicitado. | `'ServidorHTTP'` |
| `encerrar` | Encerra o valor solicitado. | `None` |

:::details Detalhes técnicos

**Assinatura:** `ServidorHTTP(host: str = HOST_PADRAO, porta: int = PORTA_PADRAO, *, limite_corpo: int = LIMITE_CORPO_PADRAO, tempo_limite_corpo: float = TEMPO_LIMITE_CORPO_PADRAO, raiz_arquivos: Any = None, permitir_externo: bool = False)`

**Origem da implementação:** `coral.web.servidor`

**Arquivo na release:** `coral/web/servidor.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `host` | posicional |
| `porta` | posicional |
| `limite_corpo` | nomeado |
| `tempo_limite_corpo` | nomeado |
| `raiz_arquivos` | nomeado |
| `permitir_externo` | nomeado |

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `ativo` | propriedade | `ativo() -> bool` |
| `porta` | propriedade | `porta() -> int` |
| `url_base` | propriedade | `url_base() -> str` |
| `ultimo_erro` | propriedade | `ultimo_erro() -> BaseException \| None` |
| `adicionar_rota` | método | `adicionar_rota(metodo: str, caminho: str, tratador: TratadorHTTP) -> 'ServidorHTTP'` |
| `adicionar_arquivo` | método | `adicionar_arquivo(caminho_rota: str, caminho_arquivo: Any, *, limite_arquivo: int = LIMITE_ARQUIVO_PADRAO, cabecalhos: Any = None) -> 'ServidorHTTP'` |
| `iniciar` | método | `iniciar() -> 'ServidorHTTP'` |
| `encerrar` | método | `encerrar() -> None` |

:::

### Exceções

#### `ErroServidorHTTP`

Falha operacional do servidor HTTP local da Coral.

:::details Detalhes técnicos

**Assinatura:** `ErroServidorHTTP(...)`

**Origem da implementação:** `coral.web.servidor`

**Arquivo na release:** `coral/web/servidor.py`

:::

#### `ErroRotaHTTP`

Definição de rota não obedece ao contrato literal do servidor.

:::details Detalhes técnicos

**Assinatura:** `ErroRotaHTTP(...)`

**Origem da implementação:** `coral.web.servidor`

**Arquivo na release:** `coral/web/servidor.py`

:::

#### `ErroLimiteCorpoHTTP`

Corpo de requisição excedeu o limite declarado pelo servidor.

:::details Detalhes técnicos

**Assinatura:** `ErroLimiteCorpoHTTP(...)`

**Origem da implementação:** `coral.web.servidor`

**Arquivo na release:** `coral/web/servidor.py`

:::

### Constantes e aliases

#### `HOST_PADRAO`

Expõe a constante pública `HOST_PADRAO`.

:::details Detalhes técnicos

**Assinatura:** `HOST_PADRAO`

**Origem da implementação:** `coral.web.servidor`

**Arquivo na release:** `coral/web/servidor.py`

**Valor declarado:** `'127.0.0.1'`

:::

#### `PORTA_PADRAO`

Expõe a constante pública `PORTA_PADRAO`.

:::details Detalhes técnicos

**Assinatura:** `PORTA_PADRAO`

**Origem da implementação:** `coral.web.servidor`

**Arquivo na release:** `coral/web/servidor.py`

**Valor declarado:** `0`

:::

#### `LIMITE_CORPO_PADRAO`

Expõe a constante pública `LIMITE_CORPO_PADRAO`.

:::details Detalhes técnicos

**Assinatura:** `LIMITE_CORPO_PADRAO`

**Origem da implementação:** `coral.web.servidor`

**Arquivo na release:** `coral/web/servidor.py`

**Valor declarado:** `1 * 1024 * 1024`

:::

#### `LIMITE_ARQUIVO_PADRAO`

Expõe a constante pública `LIMITE_ARQUIVO_PADRAO`.

:::details Detalhes técnicos

**Assinatura:** `LIMITE_ARQUIVO_PADRAO`

**Origem da implementação:** `coral.web.servidor`

**Arquivo na release:** `coral/web/servidor.py`

**Valor declarado:** `8 * 1024 * 1024`

:::

#### `TEMPO_LIMITE_CORPO_PADRAO`

Expõe a constante pública `TEMPO_LIMITE_CORPO_PADRAO`.

:::details Detalhes técnicos

**Assinatura:** `TEMPO_LIMITE_CORPO_PADRAO`

**Origem da implementação:** `coral.web.servidor`

**Arquivo na release:** `coral/web/servidor.py`

**Valor declarado:** `10.0`

:::

<!-- /AUTO:API -->
