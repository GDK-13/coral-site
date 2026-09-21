# coral.assincrono

## Visão geral

`coral.assincrono` oferece timeout, cancelamento e agrupamento sobre o modelo assíncrono existente. Use quando uma tarefa assíncrona precisa de limite de tempo, cancelamento cooperativo ou espera agrupada.

<!-- AUTO:MODULO -->

**Importação:** `coral.assincrono`  
**Categoria:** runtime  

timeout, cancelamento e agrupamento sobre o modelo assíncrono existente

### Superfície pública detectada

`ErroTempoEsgotado`, `aguardar_com_timeout`, `cancelar_tarefa`, `grupo_tarefas`

<!-- /AUTO:MODULO -->

## Quando usar

Use quando uma tarefa assíncrona precisa de limite de tempo, cancelamento cooperativo ou espera agrupada.

Entre as entradas públicas detectadas estão `ErroTempoEsgotado`, `aguardar_com_timeout`, `cancelar_tarefa`, `grupo_tarefas`.

## Começando

Uma importação seletiva começa assim:

```coral
de coral.assincrono importe ErroTempoEsgotado, aguardar_com_timeout, cancelar_tarefa
```

Depois da importação, use o hover e o preenchimento do VS Code para consultar a assinatura exata disponível na release.

## Cuidados

Cancelamento é cooperativo. O código assíncrono chamado precisa permitir que a tarefa seja interrompida.

## Relações com outros módulos

Na mesma área, veja também `coral.comum`, `coral.conversoes`, `coral.entrada`, `coral.tipos`.

## Referência da API

<!-- AUTO:API -->

### Funções

#### `async aguardar_com_timeout(esperavel: Awaitable[Any], segundos: float)`

Aguarda ``esperavel`` por no máximo ``segundos``.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `esperavel` | `Awaitable[Any]` | obrigatório | posicional |
| `segundos` | `float` | obrigatório | posicional |

**Retorno:** `não declarado`

**Exceções observáveis no corpo:** `ErroValor`, `ErroTempoEsgotado`

#### `cancelar_tarefa(tarefa: Any, motivo: str | None = None) -> bool`

Solicita cancelamento cooperativo de uma tarefa asyncio.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `tarefa` | `Any` | obrigatório | posicional |
| `motivo` | `str \| None` | `None` | posicional |

**Retorno:** `bool`

**Exceções observáveis no corpo:** `ErroValor`

#### `async grupo_tarefas(*esperaveis: Awaitable[Any]) -> tuple[Any, ...]`

Aguarda vários awaitables e preserva a ordem dos resultados.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `*esperaveis` | `Awaitable[Any]` | obrigatório | variádico |

**Retorno:** `tuple[Any, ...]`

### Exceções

#### `ErroTempoEsgotado(...)`

Uma operação assíncrona excedeu o limite solicitado.

<!-- /AUTO:API -->
