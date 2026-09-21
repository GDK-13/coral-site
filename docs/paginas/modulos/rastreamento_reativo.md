# coral.rastreamento_reativo

## Visão geral

`coral.rastreamento_reativo` oferece rastreamento estruturado e proteção de ciclos reativos. Use para registrar a cadeia de reações e proteger o sistema contra ciclos reativos.

<!-- AUTO:MODULO -->

**Importação:** `coral.rastreamento_reativo`  
**Categoria:** reativo  

rastreamento estruturado e proteção de ciclos reativos

### Superfície pública detectada

`MODOS_RASTREAMENTO`, `ErroCicloReativo`, `EntradaRastreamentoReativo`, `RastreamentoReativo`

<!-- /AUTO:MODULO -->

## Quando usar

Use para registrar a cadeia de reações e proteger o sistema contra ciclos reativos.

Entre as entradas públicas detectadas estão `MODOS_RASTREAMENTO`, `ErroCicloReativo`, `EntradaRastreamentoReativo`, `RastreamentoReativo`.

## Começando

Uma importação seletiva começa assim:

```coral
de coral.rastreamento_reativo importe MODOS_RASTREAMENTO, ErroCicloReativo, EntradaRastreamentoReativo
```

Depois da importação, use o hover e o preenchimento do VS Code para consultar a assinatura exata disponível na release.

## Cuidados

O rastreamento ajuda a explicar por que uma reação aconteceu. Não o remova de fluxos complexos apenas para esconder um ciclo.

## Relações com outros módulos

Na mesma área, veja também `coral.observadores_reativos`, `coral.replay_reativo`, `coral.sequencias_reativas`.

## Referência da API

<!-- AUTO:API -->

### Classes e protocolos

#### `EntradaRastreamentoReativo(sequencia: int | None, instante: float | None, tipo: str, nome: str, decisao: str, causa_sequencia: int | None = None, prioridade: int | None = None, condicao: str | None = None, resultado_condicao: bool | None = None, detalhes: Mapping[str, Any] = field(default_factory=dict))`

Entrada pública `EntradaRastreamentoReativo` da superfície `coral.rastreamento_reativo`.

**Atributos declarados**

| Nome | Tipo | Padrão |
|---|---|---|
| `sequencia` | `int \| None` | obrigatório |
| `instante` | `float \| None` | obrigatório |
| `tipo` | `str` | obrigatório |
| `nome` | `str` | obrigatório |
| `decisao` | `str` | obrigatório |
| `causa_sequencia` | `int \| None` | `None` |
| `prioridade` | `int \| None` | `None` |
| `condicao` | `str \| None` | `None` |
| `resultado_condicao` | `bool \| None` | `None` |
| `detalhes` | `Mapping[str, Any]` | `field(default_factory=dict)` |

**Métodos e propriedades públicas**

| Nome | Tipo | Assinatura | Retorno | Descrição |
|---|---|---|---|---|
| `como_dict` | método | `como_dict() -> dict[str, Any]` | `dict[str, Any]` | Sem docstring própria na release. |

#### `RastreamentoReativo(modo: str = 'desligado')`

Entrada pública `RastreamentoReativo` da superfície `coral.rastreamento_reativo`.

**Métodos e propriedades públicas**

| Nome | Tipo | Assinatura | Retorno | Descrição |
|---|---|---|---|---|
| `historico` | propriedade | `historico() -> tuple[EntradaRastreamentoReativo, ...]` | `tuple[EntradaRastreamentoReativo, ...]` | Sem docstring própria na release. |
| `limpar` | método | `limpar() -> None` | `None` | Sem docstring própria na release. |
| `registrar` | método | `registrar(*, sequencia: int \| None, instante: float \| None, tipo: str, nome: str, decisao: str, causa_sequencia: int \| None = None, prioridade: int \| None = None, condicao: str \| None = None, resultado_condicao: bool \| None = None, detalhes: Mapping[str, Any] \| None = None) -> EntradaRastreamentoReativo \| None` | `EntradaRastreamentoReativo \| None` | Sem docstring própria na release. |
| `como_dados` | método | `como_dados() -> list[dict[str, Any]]` | `list[dict[str, Any]]` | Sem docstring própria na release. |
| `resumo_texto` | método | `resumo_texto() -> str` | `str` | Sem docstring própria na release. |

### Exceções

#### `ErroCicloReativo(...)`

O ciclo reativo excedeu o limite seguro configurado.

### Constantes e aliases

#### `MODOS_RASTREAMENTO`

Constante pública do módulo.

**Valor declarado:** `frozenset({'desligado', 'resumido', 'detalhado'})`

<!-- /AUTO:API -->
