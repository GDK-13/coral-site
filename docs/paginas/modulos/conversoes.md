# coral.conversoes

## Visão geral

`coral.conversoes` oferece conversões explícitas entre valores Coral. Use para converter valores de forma explícita entre inteiro, decimal, texto e booleano.

<!-- AUTO:MODULO -->

**Importação:** `coral.conversoes`  
**Categoria:** runtime  

conversões explícitas entre valores Coral

### Superfície pública detectada

`ErroConversao`, `inteiro`, `decimal`, `texto`, `booleano`

<!-- /AUTO:MODULO -->

## Quando usar

Use para converter valores de forma explícita entre inteiro, decimal, texto e booleano.

Entre as entradas públicas detectadas estão `inteiro`, `decimal`, `texto`, `booleano`.

## Começando

A release inclui um exemplo real em `Exemplos/Dados/01_entrada_conversoes_e_texto.coral`:

```coral
de coral.entrada importe ler_linha
de coral.conversoes importe inteiro, decimal
de coral.formatacao importe montar_texto

defina nome como ler_linha("Nome: ")
defina idade como inteiro(ler_linha("Idade: "))
defina altura como decimal(ler_linha("Altura em metros: "))
mostre montar_texto("Olá, ", nome, ". Idade: ", idade, ". Altura: ", altura)
```

## Cuidados

Conversões podem falhar quando a entrada não representa o tipo de destino. Valide entrada externa quando necessário.

## Relações com outros módulos

Na mesma área, veja também `coral.assincrono`, `coral.comum`, `coral.entrada`, `coral.tipos`.

## Referência da API

<!-- AUTO:API -->

### Funções

#### `inteiro(valor: Any, padrao: Any = _AUSENTE) -> int | Any`

Converte para inteiro de forma estrita, com padrão opcional.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `valor` | `Any` | obrigatório | posicional |
| `padrao` | `Any` | `_AUSENTE` | posicional |

**Retorno:** `int | Any`

**Exceções observáveis no corpo:** `TypeError`, `ValueError`

#### `decimal(valor: Any, padrao: Any = _AUSENTE) -> float | Any`

Converte para decimal finito, aceitando ponto ou vírgula decimal em texto.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `valor` | `Any` | obrigatório | posicional |
| `padrao` | `Any` | `_AUSENTE` | posicional |

**Retorno:** `float | Any`

**Exceções observáveis no corpo:** `ValueError`, `TypeError`

#### `texto(valor: Any, padrao: Any = _AUSENTE) -> str | Any`

Produz texto com grafia coerente para os literais básicos da Coral.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `valor` | `Any` | obrigatório | posicional |
| `padrao` | `Any` | `_AUSENTE` | posicional |

**Retorno:** `str | Any`

#### `booleano(valor: Any, padrao: Any = _AUSENTE) -> bool | Any`

Converte apenas representações booleanas explícitas e não vazias.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `valor` | `Any` | obrigatório | posicional |
| `padrao` | `Any` | `_AUSENTE` | posicional |

**Retorno:** `bool | Any`

**Exceções observáveis no corpo:** `TypeError`, `ValueError`

### Exceções

#### `ErroConversao(valor: Any, destino: str, mensagem: str | None = None, *, causa: BaseException | None = None)`

Um valor não pôde ser convertido para o tipo Coral solicitado.

**Implementação:** `coral.erros`

<!-- /AUTO:API -->
