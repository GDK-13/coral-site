# coral.sequencias_reativas

## Visão geral

`coral.sequencias_reativas` oferece sequências temporais reutilizáveis de eventos. Use para organizar sequências temporais reutilizáveis de eventos em sistemas reativos.

<!-- AUTO:MODULO -->

**Importação:** `coral.sequencias_reativas`  
**Categoria:** reativo  

sequências temporais reutilizáveis de eventos

### Superfície pública detectada

`AcaoSequencia`, `SequenciaDoisPassos`

<!-- /AUTO:MODULO -->

## Quando usar

Use para organizar sequências temporais reutilizáveis de eventos em sistemas reativos.

Entre as entradas públicas detectadas estão `AcaoSequencia`, `SequenciaDoisPassos`.

## Começando

Uma importação seletiva começa assim:

```coral
de coral.sequencias_reativas importe AcaoSequencia, SequenciaDoisPassos
```

Depois da importação, use o hover e o preenchimento do VS Code para consultar a assinatura exata disponível na release.

## Cuidados

Mantenha a ordem e as condições de avanço explícitas para facilitar inspeção e replay.

## Relações com outros módulos

Na mesma área, veja também `coral.observadores_reativos`, `coral.rastreamento_reativo`, `coral.replay_reativo`.

## Referência da API

<!-- AUTO:API -->

### Classes e protocolos

#### `SequenciaDoisPassos(eventos: Eventos, primeiro: str, segundo: str, acao: AcaoSequencia, janela: float | None = None, nome: str = 'sequencia')`

Entrada pública `SequenciaDoisPassos` da superfície `coral.sequencias_reativas`.

**Atributos declarados**

| Nome | Tipo | Padrão |
|---|---|---|
| `eventos` | `Eventos` | obrigatório |
| `primeiro` | `str` | obrigatório |
| `segundo` | `str` | obrigatório |
| `acao` | `AcaoSequencia` | obrigatório |
| `janela` | `float \| None` | `None` |
| `nome` | `str` | `'sequencia'` |

**Métodos e propriedades públicas**

| Nome | Tipo | Assinatura | Retorno | Descrição |
|---|---|---|---|---|
| `resetar` | método | `resetar() -> None` | `None` | Sem docstring própria na release. |

### Constantes e aliases

#### `AcaoSequencia`

Alias público de tipo ou valor.

**Valor declarado:** `Callable[[Evento, Evento], Any]`

<!-- /AUTO:API -->
