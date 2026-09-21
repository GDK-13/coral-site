# coral.tempo_eventos

## Visão geral

`coral.tempo_eventos` oferece fontes de tempo, cancelamento e eventos determinísticos. Use para fontes de tempo, cancelamento e eventos determinísticos em código que precisa controlar quando algo acontece.

<!-- AUTO:MODULO -->

**Importação:** `coral.tempo_eventos`  
**Categoria:** eventos  

fontes de tempo, cancelamento e eventos determinísticos

### Superfície pública detectada

`CONTRATO`, `validar_duracao`, `normalizar_dt`, `FonteTempo`, `RelogioMonotonico`, `RelogioSimulado`, `OperacaoCancelada`, `TokenCancelamento`, `Evento`, `Eventos`

<!-- /AUTO:MODULO -->

## Quando usar

Use para fontes de tempo, cancelamento e eventos determinísticos em código que precisa controlar quando algo acontece.

Entre as entradas públicas detectadas estão `CONTRATO`, `validar_duracao`, `normalizar_dt`, `FonteTempo`, `RelogioMonotonico`, `RelogioSimulado`.

## Começando

Uma importação seletiva começa assim:

```coral
de coral.tempo_eventos importe CONTRATO, validar_duracao, normalizar_dt
```

Depois da importação, use o hover e o preenchimento do VS Code para consultar a assinatura exata disponível na release.

## Cuidados

Para testes, fontes de tempo controláveis tornam o comportamento temporal repetível.

## Relações com outros módulos

Consulte a navegação lateral para módulos que fornecem dados, sistema, texto ou runtime complementar.

## Referência da API

<!-- AUTO:API -->

### Funções

#### `validar_duracao(valor: Any, nome: str = 'duração', *, permitir_none: bool = False, permitir_zero: bool = True) -> float | None`

Normaliza uma duração pública para segundos finitos não negativos.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `valor` | `Any` | obrigatório | posicional |
| `nome` | `str` | `'duração'` | posicional |
| `permitir_none` | `bool` | `False` | nomeado |
| `permitir_zero` | `bool` | `True` | nomeado |

**Retorno:** `float | None`

**Exceções observáveis no corpo:** `ValueError`

#### `normalizar_dt(valor: Any, *, compatibilidade_negativo_zero: bool = True) -> float`

Normaliza avanço de simulação.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `valor` | `Any` | obrigatório | posicional |
| `compatibilidade_negativo_zero` | `bool` | `True` | nomeado |

**Retorno:** `float`

**Exceções observáveis no corpo:** `ValueError`

### Classes e protocolos

#### `FonteTempo(...)`

Entrada pública `FonteTempo` da superfície `coral.tempo_eventos`.

**Métodos e propriedades públicas**

| Nome | Tipo | Assinatura | Retorno | Descrição |
|---|---|---|---|---|
| `agora` | método | `agora() -> float` | `float` | Sem docstring própria na release. |
| `passo` | método | `passo() -> float` | `float` | Sem docstring própria na release. |

#### `RelogioMonotonico(fonte: Callable[[], float] = time.perf_counter)`

Relógio real baseado em ``perf_counter`` e apropriado para durações.

**Métodos e propriedades públicas**

| Nome | Tipo | Assinatura | Retorno | Descrição |
|---|---|---|---|---|
| `agora` | método | `agora() -> float` | `float` | Sem docstring própria na release. |
| `passo` | método | `passo() -> float` | `float` | Sem docstring própria na release. |

#### `RelogioSimulado(inicial: float = 0.0)`

Relógio controlado pelo programa, sem dormir nem consultar o sistema.

**Métodos e propriedades públicas**

| Nome | Tipo | Assinatura | Retorno | Descrição |
|---|---|---|---|---|
| `agora` | método | `agora() -> float` | `float` | Sem docstring própria na release. |
| `avancar` | método | `avancar(dt: Any) -> float` | `float` | Sem docstring própria na release. |
| `passo` | método | `passo() -> float` | `float` | Sem docstring própria na release. |
| `definir` | método | `definir(instante: Any) -> float` | `float` | Sem docstring própria na release. |

#### `TokenCancelamento()`

Entrada pública `TokenCancelamento` da superfície `coral.tempo_eventos`.

**Métodos e propriedades públicas**

| Nome | Tipo | Assinatura | Retorno | Descrição |
|---|---|---|---|---|
| `cancelado` | propriedade | `cancelado() -> bool` | `bool` | Sem docstring própria na release. |
| `motivo` | propriedade | `motivo() -> str \| None` | `str \| None` | Sem docstring própria na release. |
| `cancelar` | método | `cancelar(motivo: str = 'Operação cancelada pelo usuário.') -> None` | `None` | Sem docstring própria na release. |
| `verificar` | método | `verificar() -> None` | `None` | Sem docstring própria na release. |

#### `Evento(nome: str, args: tuple[Any, ...] = (), kwargs: Mapping[str, Any] = field(default_factory=dict), origem: str | None = None, sequencia: int = 0, instante: float | None = None, cancelavel: bool = False, cancelado: bool = False, motivo_cancelamento: str | None = None, consumido: bool = False, metadados: Mapping[str, Any] = field(default_factory=dict), causa_sequencia: int | None = None)`

Entrada pública `Evento` da superfície `coral.tempo_eventos`.

**Atributos declarados**

| Nome | Tipo | Padrão |
|---|---|---|
| `nome` | `str` | obrigatório |
| `args` | `tuple[Any, ...]` | `()` |
| `kwargs` | `Mapping[str, Any]` | `field(default_factory=dict)` |
| `origem` | `str \| None` | `None` |
| `sequencia` | `int` | `0` |
| `instante` | `float \| None` | `None` |
| `cancelavel` | `bool` | `False` |
| `cancelado` | `bool` | `False` |
| `motivo_cancelamento` | `str \| None` | `None` |
| `consumido` | `bool` | `False` |
| `metadados` | `Mapping[str, Any]` | `field(default_factory=dict)` |
| `causa_sequencia` | `int \| None` | `None` |

**Métodos e propriedades públicas**

| Nome | Tipo | Assinatura | Retorno | Descrição |
|---|---|---|---|---|
| `cancelar` | método | `cancelar(motivo: str \| None = None) -> None` | `None` | Sem docstring própria na release. |
| `consumir` | método | `consumir() -> None` | `None` | Sem docstring própria na release. |

#### `Eventos(*, pai: 'Eventos | None' = None, relogio: FonteTempo | None = None, fonte_instante: Callable[[], float] | None = None)`

Barramento local compatível com ``coral.regras.Eventos``.

**Métodos e propriedades públicas**

| Nome | Tipo | Assinatura | Retorno | Descrição |
|---|---|---|---|---|
| `pendentes` | propriedade | `pendentes() -> int` | `int` | Sem docstring própria na release. |
| `pai` | propriedade | `pai() -> 'Eventos \| None'` | `'Eventos \| None'` | Sem docstring própria na release. |
| `relogio` | propriedade | `relogio() -> FonteTempo \| None` | `FonteTempo \| None` | Sem docstring própria na release. |
| `definir_fonte_instante` | método | `definir_fonte_instante(fonte: Callable[[], float] \| None) -> None` | `None` | Sem docstring própria na release. |
| `possui_fonte_instante` | propriedade | `possui_fonte_instante() -> bool` | `bool` | Sem docstring própria na release. |
| `definir_pai` | método | `definir_pai(pai: 'Eventos \| None') -> None` | `None` | Sem docstring própria na release. |
| `quando` | método | `quando(nome: str, funcao: Callable[..., Any], *, prioridade: str \| int = 'normal', receber_evento: bool = False, max_execucoes: int \| None = None, cooldown: float = 0.0)` | `não declarado` | Sem docstring própria na release. |
| `remover` | método | `remover(nome: str, funcao: Callable[..., Any]) -> bool` | `bool` | Sem docstring própria na release. |
| `emitir` | método | `emitir(nome: str, *args, **kwargs) -> int` | `int` | Sem docstring própria na release. |
| `emitir_evento` | método | `emitir_evento(nome: str, *args, origem: str \| None = None, cancelavel: bool = False, metadados: Mapping[str, Any] \| None = None, **kwargs) -> Evento` | `Evento` | Sem docstring própria na release. |
| `enfileirar` | método | `enfileirar(nome: str, *args, origem: str \| None = None, **kwargs) -> Evento` | `Evento` | Sem docstring própria na release. |
| `enfileirar_evento` | método | `enfileirar_evento(nome: str, *args, origem: str \| None = None, cancelavel: bool = False, metadados: Mapping[str, Any] \| None = None, **kwargs) -> Evento` | `Evento` | Sem docstring própria na release. |
| `processar` | método | `processar(limite: int \| None = None) -> tuple[Evento, ...]` | `tuple[Evento, ...]` | Sem docstring própria na release. |
| `emitir_propagado` | método | `emitir_propagado(nome: str, *args, origem: str \| None = None, **kwargs) -> int` | `int` | Sem docstring própria na release. |
| `emitir_evento_propagado` | método | `emitir_evento_propagado(nome: str, *args, origem: str \| None = None, cancelavel: bool = False, metadados: Mapping[str, Any] \| None = None, **kwargs) -> Evento` | `Evento` | Sem docstring própria na release. |

### Exceções

#### `OperacaoCancelada(...)`

Operação cooperativa interrompida antes de uma fase segura.

### Constantes e aliases

#### `CONTRATO`

Constante pública do módulo.

**Valor declarado:** `'coral.tempo_eventos/1'`

<!-- /AUTO:API -->
