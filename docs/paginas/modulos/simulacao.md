# coral.simulacao

## Visão geral

tempo de mundo, ciclos, sistemas recorrentes e campos ambientais

<!-- AUTO:MODULO -->

**Importação:** `coral.simulacao`  
**Categoria:** simulacao  

tempo de mundo, ciclos, sistemas recorrentes e campos ambientais

### Superfície pública detectada

`CONTRATO`, `SEGUNDO`, `MINUTO`, `HORA`, `DIA`, `TempoMundo`, `FaseCiclo`, `EstadoCiclo`, `TransicaoCiclo`, `ResultadoTransicoesCiclo`, `Ciclo`, `PassoSistema`, `ResultadoSistema`, `ErroPassoExcessivo`, `Sistema`, `Simulacao`, `CampoAmbiental`, `ciclo_dia_noite`, `criar_simulacao`

<!-- /AUTO:MODULO -->

## Papel no ecossistema

`coral.simulacao` organiza tempo de mundo, ciclos, sistemas recorrentes e campos ambientais em uma camada independente de interface gráfica. O objetivo é separar o tempo do domínio do relógio real da máquina e permitir que a mesma simulação seja avançada por comandos, testes ou um loop externo.

## Conceitos principais

### Tempo de mundo

`TempoMundo` mantém o instante simulado, escala temporal e estado de pausa. `avancar` move o tempo explicitamente. `atualizar` recebe um delta externo e aplica a escala configurada, permitindo conectar a simulação a um loop sem misturar tempo de parede e tempo do mundo.

### Ciclos

`Ciclo` divide o tempo em fases com duração conhecida. A consulta de fase é direta e transições longas podem ser agregadas quando materializar cada mudança individual seria excessivo.

### Sistemas recorrentes

`Sistema` executa uma ação em intervalos regulares. O modo `fixo` chama a ação uma vez por ocorrência e protege contra avanços que exigiriam chamadas demais. O modo `agregado` representa várias ocorrências em um único `PassoSistema`, adequado para grandes saltos de tempo.

### Orquestração

`Simulacao` reúne tempo, ciclos e sistemas. Sistemas são ordenados por prioridade e ordem de registro. O mesmo avanço também publica eventos de execução e transição de ciclos.

### Campos ambientais

`CampoAmbiental` transforma um `CampoProcedural`, função ou constante em um campo numérico consultável. Ele também pode materializar valores em uma camada de `coral.mundo` dentro de limites explícitos.

## Quando usar

Use este módulo para relógios de jogo, simulações científicas simplificadas, fábricas, ecologia, logística, calendários, regeneração de recursos e qualquer sistema que precise evoluir de forma controlada e reproduzível ao longo do tempo.

## Começando

Um exemplo mínimo da release:

```coral
crie uma simulacao chamada sim
defina a escala temporal de sim como 60
avance a simulacao sim por 2 horas
mostre sim.tempo.calendario()
```

Um sistema recorrente pode acumular várias execuções em um único passo:

```coral
de coral.simulacao importe Sistema

crie a função produzir com passo
    mostre passo.execucoes
fim

crie uma simulacao chamada fabrica
execute fabrica.adicionar_sistema(Sistema("producao", produzir, intervalo=10, modo="agregado"))
avance a simulacao fabrica por 1 minuto
```

## API essencial

| Entrada | Papel |
|---|---|
| `TempoMundo` | relógio semântico, escala temporal e pausa |
| `Ciclo` / `FaseCiclo` | fases temporais repetíveis ou finitas |
| `Sistema` | processo recorrente em modo fixo ou agregado |
| `PassoSistema` | contexto de uma chamada ou lote de execuções |
| `Simulacao` | orquestra tempo, ciclos, sistemas e eventos |
| `CampoAmbiental` | campo numérico consultável ou materializável em mapa |
| `ciclo_dia_noite` | atalho para um ciclo recorrente de dia e noite |

## Fluxos comuns

1. Crie uma `Simulacao` e configure a escala do tempo quando necessário.
2. Registre ciclos que descrevem fases do ambiente ou processo.
3. Registre sistemas recorrentes com intervalo, prioridade e modo adequados.
4. Avance a simulação explicitamente em testes ou use `atualizar` a partir de um loop externo.
5. Persista o estado temporal quando precisar retomar a mesma simulação depois.

## Erros e casos de borda

No modo fixo, um salto muito grande pode gerar `ErroPassoExcessivo` quando excede o limite de chamadas configurado. O modo agregado evita essa explosão quando a lógica pode trabalhar com `passo.execucoes`. Mapas ilimitados exigem limites explícitos para materializar um campo ambiental.

## Boas práticas

* Prefira modo agregado para sistemas em que várias ocorrências podem ser resumidas matematicamente.
* Use modo fixo apenas quando cada ocorrência individual produz efeitos que não podem ser agrupados.
* Não persista callbacks implicitamente. Recrie os mesmos sistemas com as mesmas ações antes de aplicar o estado portável.
* Mantenha aleatoriedade reproduzível separada em `coral.procedural` quando o resultado da simulação depender de geração.

## Integração com outros módulos

`coral.tempo_eventos` fornece relógio simulado e eventos. `coral.procedural` fornece campos e geração determinística. `coral.mundo` recebe campos materializados em mapas. `coral.agentes` pode ser atualizado por sistemas recorrentes, como regeneração de energia ou consumo de recursos.

## Testabilidade e previsibilidade

A simulação pode ser avançada com durações explícitas, sem depender do relógio real. Isso permite testes rápidos e determinísticos. Para sistemas agregados, valide `execucoes`, duração representada e próximo instante. Para ciclos, valide a fase em instantes conhecidos e as transições em intervalos longos.

## Compatibilidade e evolução

A fundação de simulação temporal foi promovida na linha 1.5.11 e permanece disponível na **Coral 1.5.12**. A 1.5.12 preserva a superfície funcional e concentra suas mudanças na infraestrutura de validação da linguagem.

## Referência da API

<!-- AUTO:API -->

### Funções

#### `ciclo_dia_noite`

Executa a operação `ciclo_dia_noite` disponibilizada por `coral.simulacao`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `dia` | Valor correspondente a dia. | `float` | `12 * HORA` |
| `noite` | Valor correspondente a noite. | `float` | `12 * HORA` |
| `inicio` | Valor inicial do intervalo ou processo. | `float` | `0.0` |
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | `'dia_noite'` |

**Retorno**

Retorna um valor declarado como `Ciclo`.

:::details Detalhes técnicos

**Assinatura:** `ciclo_dia_noite(*, dia: float = 12 * HORA, noite: float = 12 * HORA, inicio: float = 0.0, nome: str = 'dia_noite') -> Ciclo`

**Origem da implementação:** `coral.simulacao`

**Arquivo na release:** `coral/simulacao.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `dia` | nomeado |
| `noite` | nomeado |
| `inicio` | nomeado |
| `nome` | nomeado |

:::

#### `criar_simulacao`

Cria simulacao.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `**opcoes` | Valor correspondente a opcoes. | `Any` | obrigatório |

**Retorno**

Retorna um valor declarado como `Simulacao`.

:::details Detalhes técnicos

**Assinatura:** `criar_simulacao(**opcoes: Any) -> Simulacao`

**Origem da implementação:** `coral.simulacao`

**Arquivo na release:** `coral/simulacao.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `**opcoes` | variádico nomeado |

:::

### Classes e protocolos

#### `TempoMundo`

Relógio semântico de mundo sobre :class:`RelogioSimulado`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `instante` | Valor correspondente a instante. | `float` | `0.0` |
| `escala` | Valor correspondente a escala. | `float` | `1.0` |
| `pausado` | Valor correspondente a pausado. | `bool` | `False` |
| `eventos` | Fonte ou conjunto de eventos associado à operação. | `Eventos \| None` | `None` |
| `relogio` | Relógio usado para controlar tempo ou atualização. | `RelogioSimulado \| None` | `None` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `relogio` | Obtém relogio. | `RelogioSimulado` |
| `agora` | Obtém o instante civil atual. | `float` |
| `instante` | Executa a operação `instante` disponibilizada por `coral.simulacao`. | `float` |
| `escala` | Executa a operação `escala` disponibilizada por `coral.simulacao`. | `float` |
| `pausado` | Executa a operação `pausado` disponibilizada por `coral.simulacao`. | `bool` |
| `dia` | Executa a operação `dia` disponibilizada por `coral.simulacao`. | `int` |
| `hora` | Executa a operação `hora` disponibilizada por `coral.simulacao`. | `int` |
| `minuto` | Executa a operação `minuto` disponibilizada por `coral.simulacao`. | `int` |
| `segundo` | Executa a operação `segundo` disponibilizada por `coral.simulacao`. | `float` |
| `calendario` | Executa a operação `calendario` disponibilizada por `coral.simulacao`. | `dict[str, Any]` |
| `avancar` | Avança explicitamente o tempo do mundo, independentemente da pausa. | `float` |
| `atualizar` | Aplica um delta externo respeitando pausa e escala temporal. | `float` |
| `pausar` | Pausa o valor solicitado. | `None` |
| `retomar` | Retoma o valor solicitado. | `None` |
| `definir_escala` | Define escala. | `float` |

:::details Detalhes técnicos

**Assinatura:** `TempoMundo(instante: float = 0.0, *, escala: float = 1.0, pausado: bool = False, eventos: Eventos \| None = None, relogio: RelogioSimulado \| None = None) -> None`

**Origem da implementação:** `coral.simulacao`

**Arquivo na release:** `coral/simulacao.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `instante` | posicional |
| `escala` | nomeado |
| `pausado` | nomeado |
| `eventos` | nomeado |
| `relogio` | nomeado |

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `relogio` | propriedade | `relogio() -> RelogioSimulado` |
| `agora` | método | `agora() -> float` |
| `instante` | propriedade | `instante() -> float` |
| `escala` | propriedade | `escala() -> float` |
| `pausado` | propriedade | `pausado() -> bool` |
| `dia` | propriedade | `dia() -> int` |
| `hora` | propriedade | `hora() -> int` |
| `minuto` | propriedade | `minuto() -> int` |
| `segundo` | propriedade | `segundo() -> float` |
| `calendario` | método | `calendario() -> dict[str, Any]` |
| `avancar` | método | `avancar(duracao: Any) -> float` |
| `atualizar` | método | `atualizar(dt_externo: Any) -> float` |
| `pausar` | método | `pausar() -> None` |
| `retomar` | método | `retomar() -> None` |
| `definir_escala` | método | `definir_escala(escala: Any, *, emitir: bool = True) -> float` |

:::

#### `FaseCiclo`

Representa FaseCiclo na API de `coral.simulacao`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | obrigatório |
| `duracao` | Valor correspondente a duracao. | `float` | obrigatório |
| `metadados` | Valor correspondente a metadados. | `Mapping[str, Any]` | `field(default_factory=dict, compare=False)` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | obrigatório |
| `duracao` | Valor correspondente a duracao. | `float` | obrigatório |
| `metadados` | Valor correspondente a metadados. | `Mapping[str, Any]` | `field(default_factory=dict, compare=False)` |

:::details Detalhes técnicos

**Assinatura:** `FaseCiclo(nome: str, duracao: float, metadados: Mapping[str, Any] = field(default_factory=dict, compare=False))`

**Origem da implementação:** `coral.simulacao`

**Arquivo na release:** `coral/simulacao.py`

:::

#### `EstadoCiclo`

Representa EstadoCiclo na API de `coral.simulacao`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `ciclo` | Valor correspondente a ciclo. | `str` | obrigatório |
| `fase` | Valor correspondente a fase. | `str` | obrigatório |
| `indice_fase` | Valor correspondente a indice fase. | `int` | obrigatório |
| `progresso` | Valor correspondente a progresso. | `float` | obrigatório |
| `instante_na_fase` | Valor correspondente a instante na fase. | `float` | obrigatório |
| `volta` | Valor correspondente a volta. | `int` | obrigatório |
| `encerrado` | Valor correspondente a encerrado. | `bool` | `False` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `ciclo` | Valor correspondente a ciclo. | `str` | obrigatório |
| `fase` | Valor correspondente a fase. | `str` | obrigatório |
| `indice_fase` | Valor correspondente a indice fase. | `int` | obrigatório |
| `progresso` | Valor correspondente a progresso. | `float` | obrigatório |
| `instante_na_fase` | Valor correspondente a instante na fase. | `float` | obrigatório |
| `volta` | Valor correspondente a volta. | `int` | obrigatório |
| `encerrado` | Valor correspondente a encerrado. | `bool` | `False` |

:::details Detalhes técnicos

**Assinatura:** `EstadoCiclo(ciclo: str, fase: str, indice_fase: int, progresso: float, instante_na_fase: float, volta: int, encerrado: bool = False)`

**Origem da implementação:** `coral.simulacao`

**Arquivo na release:** `coral/simulacao.py`

:::

#### `TransicaoCiclo`

Representa TransicaoCiclo na API de `coral.simulacao`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `ciclo` | Valor correspondente a ciclo. | `str` | obrigatório |
| `instante` | Valor correspondente a instante. | `float` | obrigatório |
| `de_fase` | Valor correspondente a de fase. | `str` | obrigatório |
| `para_fase` | Valor correspondente a para fase. | `str` | obrigatório |
| `volta` | Valor correspondente a volta. | `int` | obrigatório |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `ciclo` | Valor correspondente a ciclo. | `str` | obrigatório |
| `instante` | Valor correspondente a instante. | `float` | obrigatório |
| `de_fase` | Valor correspondente a de fase. | `str` | obrigatório |
| `para_fase` | Valor correspondente a para fase. | `str` | obrigatório |
| `volta` | Valor correspondente a volta. | `int` | obrigatório |

:::details Detalhes técnicos

**Assinatura:** `TransicaoCiclo(ciclo: str, instante: float, de_fase: str, para_fase: str, volta: int)`

**Origem da implementação:** `coral.simulacao`

**Arquivo na release:** `coral/simulacao.py`

:::

#### `ResultadoTransicoesCiclo`

Representa ResultadoTransicoesCiclo na API de `coral.simulacao`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `quantidade` | Quantidade de itens solicitada. | `int` | obrigatório |
| `transicoes` | Valor correspondente a transicoes. | `tuple[TransicaoCiclo, ...]` | obrigatório |
| `agregado` | Valor correspondente a agregado. | `bool` | obrigatório |
| `estado_inicial` | Valor correspondente a estado inicial. | `EstadoCiclo` | obrigatório |
| `estado_final` | Valor correspondente a estado final. | `EstadoCiclo` | obrigatório |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `quantidade` | Quantidade de itens solicitada. | `int` | obrigatório |
| `transicoes` | Valor correspondente a transicoes. | `tuple[TransicaoCiclo, ...]` | obrigatório |
| `agregado` | Valor correspondente a agregado. | `bool` | obrigatório |
| `estado_inicial` | Valor correspondente a estado inicial. | `EstadoCiclo` | obrigatório |
| `estado_final` | Valor correspondente a estado final. | `EstadoCiclo` | obrigatório |

:::details Detalhes técnicos

**Assinatura:** `ResultadoTransicoesCiclo(quantidade: int, transicoes: tuple[TransicaoCiclo, ...], agregado: bool, estado_inicial: EstadoCiclo, estado_final: EstadoCiclo)`

**Origem da implementação:** `coral.simulacao`

**Arquivo na release:** `coral/simulacao.py`

:::

#### `Ciclo`

Ciclo temporal configurável com consulta O(1) da fase corrente.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | obrigatório |
| `fases` | Valor correspondente a fases. | `Iterable[FaseCiclo \| tuple[str, float]]` | obrigatório |
| `inicio` | Valor inicial do intervalo ou processo. | `float` | `0.0` |
| `repetir` | Valor correspondente a repetir. | `bool` | `True` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `estado_em` | Executa a operação `estado_em` disponibilizada por `coral.simulacao`. | `EstadoCiclo` |
| `transicoes_entre` | Executa a operação `transicoes_entre` disponibilizada por `coral.simulacao`. | `ResultadoTransicoesCiclo` |

:::details Detalhes técnicos

**Assinatura:** `Ciclo(nome: str, fases: Iterable[FaseCiclo \| tuple[str, float]], *, inicio: float = 0.0, repetir: bool = True) -> None`

**Origem da implementação:** `coral.simulacao`

**Arquivo na release:** `coral/simulacao.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `nome` | posicional |
| `fases` | posicional |
| `inicio` | nomeado |
| `repetir` | nomeado |

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `estado_em` | método | `estado_em(instante: Any) -> EstadoCiclo` |
| `transicoes_entre` | método | `transicoes_entre(inicio: Any, fim: Any, *, limite_materializacao: int = 1024) -> ResultadoTransicoesCiclo` |

:::

#### `PassoSistema`

Representa PassoSistema na API de `coral.simulacao`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `sistema` | Valor correspondente a sistema. | `str` | obrigatório |
| `inicio` | Valor inicial do intervalo ou processo. | `float` | obrigatório |
| `fim` | Valor final do intervalo ou processo. | `float` | obrigatório |
| `duracao` | Valor correspondente a duracao. | `float` | obrigatório |
| `execucoes` | Valor correspondente a execucoes. | `int` | obrigatório |
| `intervalo` | Valor correspondente a intervalo. | `float` | obrigatório |
| `contexto` | Valor correspondente a contexto. | `Any` | `None` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `sistema` | Valor correspondente a sistema. | `str` | obrigatório |
| `inicio` | Valor inicial do intervalo ou processo. | `float` | obrigatório |
| `fim` | Valor final do intervalo ou processo. | `float` | obrigatório |
| `duracao` | Valor correspondente a duracao. | `float` | obrigatório |
| `execucoes` | Valor correspondente a execucoes. | `int` | obrigatório |
| `intervalo` | Valor correspondente a intervalo. | `float` | obrigatório |
| `contexto` | Valor correspondente a contexto. | `Any` | `None` |

:::details Detalhes técnicos

**Assinatura:** `PassoSistema(sistema: str, inicio: float, fim: float, duracao: float, execucoes: int, intervalo: float, contexto: Any = None)`

**Origem da implementação:** `coral.simulacao`

**Arquivo na release:** `coral/simulacao.py`

:::

#### `ResultadoSistema`

Representa ResultadoSistema na API de `coral.simulacao`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `sistema` | Valor correspondente a sistema. | `str` | obrigatório |
| `execucoes` | Valor correspondente a execucoes. | `int` | obrigatório |
| `chamadas` | Valor correspondente a chamadas. | `int` | obrigatório |
| `resultados` | Valor correspondente a resultados. | `tuple[Any, ...]` | obrigatório |
| `proximo_instante` | Valor correspondente a proximo instante. | `float` | obrigatório |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `sistema` | Valor correspondente a sistema. | `str` | obrigatório |
| `execucoes` | Valor correspondente a execucoes. | `int` | obrigatório |
| `chamadas` | Valor correspondente a chamadas. | `int` | obrigatório |
| `resultados` | Valor correspondente a resultados. | `tuple[Any, ...]` | obrigatório |
| `proximo_instante` | Valor correspondente a proximo instante. | `float` | obrigatório |

:::details Detalhes técnicos

**Assinatura:** `ResultadoSistema(sistema: str, execucoes: int, chamadas: int, resultados: tuple[Any, ...], proximo_instante: float)`

**Origem da implementação:** `coral.simulacao`

**Arquivo na release:** `coral/simulacao.py`

:::

#### `Sistema`

Processo temporal recorrente independente de RPG e de interface gráfica.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | obrigatório |
| `acao` | Valor correspondente a acao. | `Callable[[PassoSistema], Any]` | obrigatório |
| `intervalo` | Valor correspondente a intervalo. | `float` | `1.0` |
| `prioridade` | Valor correspondente a prioridade. | `int` | `0` |
| `modo` | Valor correspondente a modo. | `str` | `'agregado'` |
| `ativo` | Valor correspondente a ativo. | `bool` | `True` |
| `max_chamadas_por_avanco` | Valor correspondente a max chamadas por avanco. | `int` | `10000` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `preparar` | Executa a operação `preparar` disponibilizada por `coral.simulacao`. | `None` |
| `ativar` | Executa a operação `ativar` disponibilizada por `coral.simulacao`. | `None` |
| `desativar` | Executa a operação `desativar` disponibilizada por `coral.simulacao`. | `None` |
| `estado_portatil` | Retorna somente o estado temporal reconstruível do sistema. | `dict[str, Any]` |
| `aplicar_estado_portatil` | Executa a operação `aplicar_estado_portatil` disponibilizada por `coral.simulacao`. | `None` |
| `executar_ate` | Executa ate. | `ResultadoSistema` |

:::details Detalhes técnicos

**Assinatura:** `Sistema(nome: str, acao: Callable[[PassoSistema], Any], *, intervalo: float = 1.0, prioridade: int = 0, modo: str = 'agregado', ativo: bool = True, max_chamadas_por_avanco: int = 10000) -> None`

**Origem da implementação:** `coral.simulacao`

**Arquivo na release:** `coral/simulacao.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `nome` | posicional |
| `acao` | posicional |
| `intervalo` | nomeado |
| `prioridade` | nomeado |
| `modo` | nomeado |
| `ativo` | nomeado |
| `max_chamadas_por_avanco` | nomeado |

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `preparar` | método | `preparar(instante: float) -> None` |
| `ativar` | método | `ativar() -> None` |
| `desativar` | método | `desativar() -> None` |
| `estado_portatil` | método | `estado_portatil() -> dict[str, Any]` |
| `aplicar_estado_portatil` | método | `aplicar_estado_portatil(dados: Mapping[str, Any]) -> None` |
| `executar_ate` | método | `executar_ate(fim: float, *, contexto: Any = None) -> ResultadoSistema` |

:::

#### `Simulacao`

Orquestrador leve para tempo, ciclos e sistemas recorrentes.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `tempo` | Valor correspondente a tempo. | `TempoMundo \| None` | `None` |
| `eventos` | Fonte ou conjunto de eventos associado à operação. | `Eventos \| None` | `None` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `ciclos` | Executa a operação `ciclos` disponibilizada por `coral.simulacao`. | `tuple[Ciclo, ...]` |
| `sistemas` | Executa a operação `sistemas` disponibilizada por `coral.simulacao`. | `tuple[Sistema, ...]` |
| `ciclo` | Executa a operação `ciclo` disponibilizada por `coral.simulacao`. | `Ciclo` |
| `sistema` | Executa a operação `sistema` disponibilizada por `coral.simulacao`. | `Sistema` |
| `adicionar_ciclo` | Adiciona ciclo. | `Ciclo` |
| `adicionar_sistema` | Adiciona sistema. | `Sistema` |
| `criar_sistema` | Cria sistema. | `Sistema` |
| `avancar` | Avança o valor solicitado. | `tuple[ResultadoSistema, ...]` |
| `atualizar` | Atualiza o valor solicitado. | `tuple[ResultadoSistema, ...]` |
| `estado_portatil` | Estado temporal sem callbacks, apropriado para persistência explícita. | `dict[str, Any]` |
| `aplicar_estado_portatil` | Executa a operação `aplicar_estado_portatil` disponibilizada por `coral.simulacao`. | `None` |

:::details Detalhes técnicos

**Assinatura:** `Simulacao(*, tempo: TempoMundo \| None = None, eventos: Eventos \| None = None) -> None`

**Origem da implementação:** `coral.simulacao`

**Arquivo na release:** `coral/simulacao.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `tempo` | nomeado |
| `eventos` | nomeado |

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `ciclos` | propriedade | `ciclos() -> tuple[Ciclo, ...]` |
| `sistemas` | propriedade | `sistemas() -> tuple[Sistema, ...]` |
| `ciclo` | método | `ciclo(nome: str) -> Ciclo` |
| `sistema` | método | `sistema(nome: str) -> Sistema` |
| `adicionar_ciclo` | método | `adicionar_ciclo(ciclo: Ciclo) -> Ciclo` |
| `adicionar_sistema` | método | `adicionar_sistema(sistema: Sistema) -> Sistema` |
| `criar_sistema` | método | `criar_sistema(nome: str, acao: Callable[[PassoSistema], Any], **opcoes: Any) -> Sistema` |
| `avancar` | método | `avancar(duracao: Any, *, contexto: Any = None) -> tuple[ResultadoSistema, ...]` |
| `atualizar` | método | `atualizar(dt_externo: Any, *, contexto: Any = None) -> tuple[ResultadoSistema, ...]` |
| `estado_portatil` | método | `estado_portatil() -> dict[str, Any]` |
| `aplicar_estado_portatil` | método | `aplicar_estado_portatil(estado: Mapping[str, Any]) -> None` |

:::

#### `CampoAmbiental`

Campo numérico de simulação que pode ser consultado ou materializado.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | obrigatório |
| `fonte` | Fonte explícita usada pela operação; quando omitida, vale o comportamento padrão do módulo. | `CampoProcedural \| Callable[..., float] \| float` | obrigatório |
| `unidade` | Valor correspondente a unidade. | `str \| None` | `None` |
| `minimo` | Limite mínimo considerado pela operação. | `float \| None` | `None` |
| `maximo` | Limite máximo considerado pela operação. | `float \| None` | `None` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `valor_em` | Executa a operação `valor_em` disponibilizada por `coral.simulacao`. | `float` |
| `materializar` | Executa a operação `materializar` disponibilizada por `coral.simulacao`. | `int` |

:::details Detalhes técnicos

**Assinatura:** `CampoAmbiental(nome: str, fonte: CampoProcedural \| Callable[..., float] \| float, *, unidade: str \| None = None, minimo: float \| None = None, maximo: float \| None = None) -> None`

**Origem da implementação:** `coral.simulacao`

**Arquivo na release:** `coral/simulacao.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `nome` | posicional |
| `fonte` | posicional |
| `unidade` | nomeado |
| `minimo` | nomeado |
| `maximo` | nomeado |

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `valor_em` | método | `valor_em(celula_ou_coordenadas: Any) -> float` |
| `materializar` | método | `materializar(mapa: Any, *, camada: str \| None = None, limites: Any = None, causa: Any = 'campo_ambiental') -> int` |

:::

### Exceções

#### `ErroPassoExcessivo`

Um sistema de passo fixo exigiria chamadas demais em um único avanço.

:::details Detalhes técnicos

**Assinatura:** `ErroPassoExcessivo(...)`

**Origem da implementação:** `coral.simulacao`

**Arquivo na release:** `coral/simulacao.py`

:::

### Constantes e aliases

#### `CONTRATO`

Expõe a constante pública `CONTRATO`.

:::details Detalhes técnicos

**Assinatura:** `CONTRATO`

**Origem da implementação:** `coral.simulacao`

**Arquivo na release:** `coral/simulacao.py`

**Valor declarado:** `'coral.simulacao/1'`

:::

#### `SEGUNDO`

Expõe a constante pública `SEGUNDO`.

:::details Detalhes técnicos

**Assinatura:** `SEGUNDO`

**Origem da implementação:** `coral.simulacao`

**Arquivo na release:** `coral/simulacao.py`

**Valor declarado:** `1.0`

:::

#### `MINUTO`

Expõe a constante pública `MINUTO`.

:::details Detalhes técnicos

**Assinatura:** `MINUTO`

**Origem da implementação:** `coral.simulacao`

**Arquivo na release:** `coral/simulacao.py`

**Valor declarado:** `60.0`

:::

#### `HORA`

Expõe a constante pública `HORA`.

:::details Detalhes técnicos

**Assinatura:** `HORA`

**Origem da implementação:** `coral.simulacao`

**Arquivo na release:** `coral/simulacao.py`

**Valor declarado:** `60.0 * MINUTO`

:::

#### `DIA`

Expõe a constante pública `DIA`.

:::details Detalhes técnicos

**Assinatura:** `DIA`

**Origem da implementação:** `coral.simulacao`

**Arquivo na release:** `coral/simulacao.py`

**Valor declarado:** `24.0 * HORA`

:::

<!-- /AUTO:API -->
