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

## Papel no ecossistema

Fornece infraestrutura compartilhada de tempo injetável, eventos, filas e cancelamento. É a base adequada para código que precisa ser determinístico em testes e ainda operar com relógio real em produção.

## Conceitos principais

### Fonte de tempo

`FonteTempo` é o contrato. `RelogioMonotonico` mede duração real e `RelogioSimulado` permite controlar o instante.

### Duração

`validar_duracao` e `normalizar_dt` uniformizam valores temporais usados por bibliotecas.

### Eventos

`Evento` é o registro; `Eventos` é o barramento local capaz de publicar, enfileirar e propagar conforme sua API.

### Cancelamento

`TokenCancelamento` representa cancelamento cooperativo e `OperacaoCancelada` é a falha correspondente.

### Hierarquia

`Eventos` pode ter um barramento pai, permitindo composição de escopos sem um barramento global obrigatório.

## Quando usar

Use este módulo quando o problema corresponder diretamente aos conceitos acima. Por ser um módulo complementar, ele normalmente entra em um programa para resolver uma responsabilidade específica e deve permanecer desacoplado da lógica central sempre que possível.

## Começando

```coral
de coral.tempo_eventos importe RelogioSimulado, Eventos

defina relogio como RelogioSimulado(0)
defina eventos como Eventos(relogio=relogio)
mostre relogio.agora()
execute relogio.avancar(0.5)
mostre relogio.agora()
```

## API essencial

| Entrada | Papel |
|---|---|
| `RelogioMonotonico` | tempo real monotônico |
| `RelogioSimulado` | tempo controlado |
| `Evento` | registro de evento |
| `Eventos` | barramento |
| `TokenCancelamento` | cancelamento cooperativo |
| `validar_duracao` | normalizar duração |
| `normalizar_dt` | normalizar avanço |

A seção **Referência da API** no fim desta página contém a superfície pública completa detectada na release, com assinaturas, parâmetros, retornos e docstrings quando presentes.

## Fluxos comuns

1. Escolha relógio real ou simulado na fronteira de composição.
2. Construa eventos com nomes e dados explícitos.
3. Use o barramento para desacoplar produtor e consumidores.
4. Passe token de cancelamento a operações longas que podem parar em pontos seguros.

## Erros e casos de borda

Relógio civil não é substituto de monotônico para medir duração. Cancelamento não desfaz automaticamente efeitos já realizados. Eventos reentrantes podem formar cadeias difíceis de explicar se não houver política de ordem.

## Boas práticas

* Injete relógio em código temporal.
* Prefira `RelogioSimulado` em testes.
* Mantenha nomes de eventos estáveis e dados serializáveis quando houver replay.
* Use cancelamento cooperativo em pontos seguros.

## Integração com outros módulos

É infraestrutura para `coral.regras`, observadores, sequências e replay. `coral.datas` cobre tempo civil e calendários, enquanto este módulo cobre tempo de execução.

## Testabilidade e previsibilidade

Controle o relógio e a fila em testes. Isso elimina esperas reais e torna ordem e instante dos eventos verificáveis.

## Compatibilidade e evolução

A documentação desta página descreve a superfície detectada na **Coral 1.5.9**. O gerador do site atualiza automaticamente o inventário e a referência da API quando uma nova release é importada, mas o texto pedagógico desta seção permanece sob revisão humana.

## Referência da API

<!-- AUTO:API -->

### Funções

#### `validar_duracao`

Normaliza uma duração pública para segundos finitos não negativos.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valor` | Valor processado pela operação. | `Any` | obrigatório |
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | `'duração'` |
| `permitir_none` | Controla se deve permitir none. | `bool` | `False` |
| `permitir_zero` | Controla se deve permitir zero. | `bool` | `True` |

**Retorno**

Retorna um valor declarado como `float | None`.

:::details Detalhes técnicos

**Assinatura:** `validar_duracao(valor: Any, nome: str = 'duração', *, permitir_none: bool = False, permitir_zero: bool = True) -> float \| None`

**Origem da implementação:** `coral.tempo_eventos`

**Arquivo na release:** `coral/tempo_eventos.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `valor` | posicional |
| `nome` | posicional |
| `permitir_none` | nomeado |
| `permitir_zero` | nomeado |

**Exceções diretamente observáveis no corpo:** `ValueError`

:::

#### `normalizar_dt`

Normaliza avanço de simulação.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valor` | Valor processado pela operação. | `Any` | obrigatório |
| `compatibilidade_negativo_zero` | Valor correspondente a compatibilidade negativo zero. | `bool` | `True` |

**Retorno**

Retorna um valor declarado como `float`.

:::details Detalhes técnicos

**Assinatura:** `normalizar_dt(valor: Any, *, compatibilidade_negativo_zero: bool = True) -> float`

**Origem da implementação:** `coral.tempo_eventos`

**Arquivo na release:** `coral/tempo_eventos.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `valor` | posicional |
| `compatibilidade_negativo_zero` | nomeado |

**Exceções diretamente observáveis no corpo:** `ValueError`

:::

### Classes e protocolos

#### `FonteTempo`

Define o contrato público de FonteTempo.

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `agora` | Obtém o instante civil atual. | `float` |
| `passo` | Avança o estado controlado por um passo. | `float` |

:::details Detalhes técnicos

**Assinatura:** `FonteTempo(...)`

**Origem da implementação:** `coral.tempo_eventos`

**Arquivo na release:** `coral/tempo_eventos.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `agora` | método | `agora() -> float` |
| `passo` | método | `passo() -> float` |

:::

#### `RelogioMonotonico`

Relógio real baseado em ``perf_counter`` e apropriado para durações.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `fonte` | Fonte explícita usada pela operação; quando omitida, vale o comportamento padrão do módulo. | `Callable[[], float]` | `time.perf_counter` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `agora` | Obtém o instante civil atual. | `float` |
| `passo` | Avança o estado controlado por um passo. | `float` |

:::details Detalhes técnicos

**Assinatura:** `RelogioMonotonico(fonte: Callable[[], float] = time.perf_counter)`

**Origem da implementação:** `coral.tempo_eventos`

**Arquivo na release:** `coral/tempo_eventos.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `agora` | método | `agora() -> float` |
| `passo` | método | `passo() -> float` |

:::

#### `RelogioSimulado`

Relógio controlado pelo programa, sem dormir nem consultar o sistema.

**Exemplo**

```coral
de coral.tempo_eventos importe RelogioSimulado, Eventos

defina relogio como RelogioSimulado(0)
defina eventos como Eventos(relogio=relogio)
mostre relogio.agora()
execute relogio.avancar(0.5)
mostre relogio.agora()
```

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `inicial` | Valor correspondente a inicial. | `float` | `0.0` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `agora` | Obtém o instante civil atual. | `float` |
| `avancar` | Avança o valor solicitado. | `float` |
| `passo` | Avança o estado controlado por um passo. | `float` |
| `definir` | Define o valor solicitado. | `float` |

:::details Detalhes técnicos

**Assinatura:** `RelogioSimulado(inicial: float = 0.0)`

**Origem da implementação:** `coral.tempo_eventos`

**Arquivo na release:** `coral/tempo_eventos.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `agora` | método | `agora() -> float` |
| `avancar` | método | `avancar(dt: Any) -> float` |
| `passo` | método | `passo() -> float` |
| `definir` | método | `definir(instante: Any) -> float` |

:::

#### `TokenCancelamento`

Representa cancelamento cooperativo.

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `cancelado` | Indica o estado de cancelado. | `bool` |
| `motivo` | Obtém motivo. | `str \| None` |
| `cancelar` | Cancela o valor solicitado. | `None` |
| `verificar` | Executa a operação `verificar` disponibilizada por `coral.tempo_eventos`. | `None` |

:::details Detalhes técnicos

**Assinatura:** `TokenCancelamento()`

**Origem da implementação:** `coral.tempo_eventos`

**Arquivo na release:** `coral/tempo_eventos.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `cancelado` | propriedade | `cancelado() -> bool` |
| `motivo` | propriedade | `motivo() -> str \| None` |
| `cancelar` | método | `cancelar(motivo: str = 'Operação cancelada pelo usuário.') -> None` |
| `verificar` | método | `verificar() -> None` |

:::

#### `Evento`

Representa registro de evento.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | obrigatório |
| `args` | Valor correspondente a args. | `tuple[Any, ...]` | `()` |
| `kwargs` | Valor correspondente a kwargs. | `Mapping[str, Any]` | `field(default_factory=dict)` |
| `origem` | Origem usada pela operação. | `str \| None` | `None` |
| `sequencia` | Valor correspondente a sequencia. | `int` | `0` |
| `instante` | Valor correspondente a instante. | `float \| None` | `None` |
| `cancelavel` | Valor correspondente a cancelavel. | `bool` | `False` |
| `cancelado` | Valor correspondente a cancelado. | `bool` | `False` |
| `motivo_cancelamento` | Valor correspondente a motivo cancelamento. | `str \| None` | `None` |
| `consumido` | Valor correspondente a consumido. | `bool` | `False` |
| `metadados` | Valor correspondente a metadados. | `Mapping[str, Any]` | `field(default_factory=dict)` |
| `causa_sequencia` | Valor correspondente a causa sequencia. | `int \| None` | `None` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | obrigatório |
| `args` | Valor correspondente a args. | `tuple[Any, ...]` | `()` |
| `kwargs` | Valor correspondente a kwargs. | `Mapping[str, Any]` | `field(default_factory=dict)` |
| `origem` | Origem usada pela operação. | `str \| None` | `None` |
| `sequencia` | Valor correspondente a sequencia. | `int` | `0` |
| `instante` | Valor correspondente a instante. | `float \| None` | `None` |
| `cancelavel` | Valor correspondente a cancelavel. | `bool` | `False` |
| `cancelado` | Valor correspondente a cancelado. | `bool` | `False` |
| `motivo_cancelamento` | Valor correspondente a motivo cancelamento. | `str \| None` | `None` |
| `consumido` | Valor correspondente a consumido. | `bool` | `False` |
| `metadados` | Valor correspondente a metadados. | `Mapping[str, Any]` | `field(default_factory=dict)` |
| `causa_sequencia` | Valor correspondente a causa sequencia. | `int \| None` | `None` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `cancelar` | Cancela o valor solicitado. | `None` |
| `consumir` | Executa a operação `consumir` disponibilizada por `coral.tempo_eventos`. | `None` |

:::details Detalhes técnicos

**Assinatura:** `Evento(nome: str, args: tuple[Any, ...] = (), kwargs: Mapping[str, Any] = field(default_factory=dict), origem: str \| None = None, sequencia: int = 0, instante: float \| None = None, cancelavel: bool = False, cancelado: bool = False, motivo_cancelamento: str \| None = None, consumido: bool = False, metadados: Mapping[str, Any] = field(default_factory=dict), causa_sequencia: int \| None = None)`

**Origem da implementação:** `coral.tempo_eventos`

**Arquivo na release:** `coral/tempo_eventos.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `cancelar` | método | `cancelar(motivo: str \| None = None) -> None` |
| `consumir` | método | `consumir() -> None` |

:::

#### `Eventos`

Barramento local compatível com ``coral.regras.Eventos``.

**Exemplo**

```coral
de coral.tempo_eventos importe RelogioSimulado, Eventos

defina relogio como RelogioSimulado(0)
defina eventos como Eventos(relogio=relogio)
mostre relogio.agora()
execute relogio.avancar(0.5)
mostre relogio.agora()
```

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `pai` | Valor correspondente a pai. | `'Eventos \| None'` | `None` |
| `relogio` | Relógio usado para controlar tempo ou atualização. | `FonteTempo \| None` | `None` |
| `fonte_instante` | Valor correspondente a fonte instante. | `Callable[[], float] \| None` | `None` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `pendentes` | Obtém pendentes. | `int` |
| `pai` | Obtém pai. | `'Eventos \| None'` |
| `relogio` | Obtém relogio. | `FonteTempo \| None` |
| `definir_fonte_instante` | Define fonte instante. | `None` |
| `possui_fonte_instante` | Indica se possui fonte instante. | `bool` |
| `definir_pai` | Define pai. | `None` |
| `quando` | Executa a operação `quando` disponibilizada por `coral.tempo_eventos`. | `não declarado` |
| `remover` | Remove o valor solicitado. | `bool` |
| `emitir` | Emite o valor solicitado. | `int` |
| `emitir_evento` | Emite evento. | `Evento` |
| `enfileirar` | Enfileira o valor solicitado. | `Evento` |
| `enfileirar_evento` | Enfileira evento. | `Evento` |
| `processar` | Processa o valor solicitado. | `tuple[Evento, ...]` |
| `emitir_propagado` | Emite propagado. | `int` |
| `emitir_evento_propagado` | Emite evento propagado. | `Evento` |

:::details Detalhes técnicos

**Assinatura:** `Eventos(*, pai: 'Eventos \| None' = None, relogio: FonteTempo \| None = None, fonte_instante: Callable[[], float] \| None = None)`

**Origem da implementação:** `coral.tempo_eventos`

**Arquivo na release:** `coral/tempo_eventos.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `pai` | nomeado |
| `relogio` | nomeado |
| `fonte_instante` | nomeado |

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `pendentes` | propriedade | `pendentes() -> int` |
| `pai` | propriedade | `pai() -> 'Eventos \| None'` |
| `relogio` | propriedade | `relogio() -> FonteTempo \| None` |
| `definir_fonte_instante` | método | `definir_fonte_instante(fonte: Callable[[], float] \| None) -> None` |
| `possui_fonte_instante` | propriedade | `possui_fonte_instante() -> bool` |
| `definir_pai` | método | `definir_pai(pai: 'Eventos \| None') -> None` |
| `quando` | método | `quando(nome: str, funcao: Callable[..., Any], *, prioridade: str \| int = 'normal', receber_evento: bool = False, max_execucoes: int \| None = None, cooldown: float = 0.0)` |
| `remover` | método | `remover(nome: str, funcao: Callable[..., Any]) -> bool` |
| `emitir` | método | `emitir(nome: str, *args, **kwargs) -> int` |
| `emitir_evento` | método | `emitir_evento(nome: str, *args, origem: str \| None = None, cancelavel: bool = False, metadados: Mapping[str, Any] \| None = None, **kwargs) -> Evento` |
| `enfileirar` | método | `enfileirar(nome: str, *args, origem: str \| None = None, **kwargs) -> Evento` |
| `enfileirar_evento` | método | `enfileirar_evento(nome: str, *args, origem: str \| None = None, cancelavel: bool = False, metadados: Mapping[str, Any] \| None = None, **kwargs) -> Evento` |
| `processar` | método | `processar(limite: int \| None = None) -> tuple[Evento, ...]` |
| `emitir_propagado` | método | `emitir_propagado(nome: str, *args, origem: str \| None = None, **kwargs) -> int` |
| `emitir_evento_propagado` | método | `emitir_evento_propagado(nome: str, *args, origem: str \| None = None, cancelavel: bool = False, metadados: Mapping[str, Any] \| None = None, **kwargs) -> Evento` |

:::

### Exceções

#### `OperacaoCancelada`

Operação cooperativa interrompida antes de uma fase segura.

:::details Detalhes técnicos

**Assinatura:** `OperacaoCancelada(...)`

**Origem da implementação:** `coral.tempo_eventos`

**Arquivo na release:** `coral/tempo_eventos.py`

:::

### Constantes e aliases

#### `CONTRATO`

Expõe a constante pública `CONTRATO`.

:::details Detalhes técnicos

**Assinatura:** `CONTRATO`

**Origem da implementação:** `coral.tempo_eventos`

**Arquivo na release:** `coral/tempo_eventos.py`

**Valor declarado:** `'coral.tempo_eventos/1'`

:::

<!-- /AUTO:API -->
