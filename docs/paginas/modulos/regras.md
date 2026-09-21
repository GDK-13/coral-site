# coral.regras

## Visão geral

`coral.regras` é o motor reativo da Coral. Ele reúne condições, ações, eventos, temporização, observadores e sequências para expressar comportamento que reage ao estado sem espalhar condicionais e callbacks por todo o programa.

<!-- AUTO:MODULO -->

**Importação:** `coral.regras`  
**Categoria:** regras  

regras reativas, eventos, temporizadores e observadores

### Superfície pública detectada

`Condicao`, `Acao`, `MODOS_REGRA`, `Regra`, `GrupoRegras`, `Debounce`, `Temporizador`, `Eventos`, `MotorRegras`, `ObservadorMudanca`, `ObservadorEspacial`, `SequenciaDoisPassos`, `regra`

<!-- /AUTO:MODULO -->

## Papel no ecossistema

Regras decide **quando** algo deve acontecer. O domínio continua em `coral.mundo` ou outro módulo, a apresentação continua em `coral.jogos` e o motor conecta essas partes por estado e eventos.

## Conceitos principais

### Regra

`Regra` combina condição e ação. O helper `regra()` cria uma regra com modo, prioridade, limite de execuções e cooldown.

### Motor

`MotorRegras` reúne regras, eventos, relógio e rastreamento. Ele é a unidade que avalia condições e coordena disparos.

### Eventos

`Eventos` é um barramento local. Ele pode emitir eventos para desacoplar componentes sem transformar um módulo em dependência direta de outro.

### Tempo

`Debounce` e `Temporizador` modelam padrões temporais recorrentes. A integração com fontes de tempo controláveis permite testes determinísticos.

### Observadores e sequências

`ObservadorMudanca`, `ObservadorEspacial` e `SequenciaDoisPassos` cobrem padrões comuns sem obrigar cada aplicação a reimplementar detecção de transição.

## Quando usar

Use quando a lógica é naturalmente descrita como condição, reação, evento ou transição. Para um cálculo linear simples, uma função comum continua sendo mais clara.

## Começando

Trecho do exemplo oficial `Exemplos/Regras/01_eventos_observacao_e_tempo.coral`:

```coral
defina vida como 10
defina estado como "normal"

regra "ferido" quando vida for menor ou igual a 5 então
    defina estado como "ferido"
fim

quando vida mudar
    mostre vida
fim

avalie as regras
defina vida como 4
avalie as regras
```

## API essencial

| Entrada | Papel | Assinatura |
|---|---|---|
| `Regra` | condição e ação | `Regra(nome: str, condicao: Condicao, acao: Acao, modo: str = 'ao_ativar', habilitada: bool = True, ativa: bool = False, execucoes: int = 0, prioridade: str \| int = 'normal', max_execucoes: int \| None = None, cooldown: float = 0.0, ultimo_disparo: float \| None = None, motivo_ultima_supressao: str \| None = None, ultima_condicao: bool \| None = None)` |
| `GrupoRegras` | agrupar regras | `GrupoRegras(nome: str, regras: tuple[Regra, ...])` |
| `MotorRegras` | coordenar avaliação | `MotorRegras(*, relogio: FonteTempo \| None = None, eventos: Eventos \| None = None, rastreamento: RastreamentoReativo \| str \| None = None)` |
| `Eventos` | barramento local | `Eventos(*, pai: 'Eventos \| None' = None, relogio: FonteTempo \| None = None, fonte_instante: Callable[[], float] \| None = None)` |
| `Debounce` | adiar reação até estabilização | `Debounce(intervalo: float, acao: Acao, nome: str = 'debounce', restante: float \| None = None, pendente: bool = False, contexto_mais_recente: Any = None)` |
| `Temporizador` | executar ação por tempo | `Temporizador(intervalo: float, acao: Acao, repetir: bool = False, nome: str = 'temporizador', restante: float \| None = None, ativo: bool = True)` |
| `ObservadorMudanca` | observar valor | `ObservadorMudanca(nome: str, leitor: LeitorValor, acao: AcaoMudanca, modo: str = 'mudanca', limite: Any = None)` |
| `ObservadorEspacial` | observar relação espacial | `ObservadorEspacial(nome: str, leitor: LeitorValor, referencia: Any, acao: Callable[[Any, Any, Any], Any], relacao: str, transicao: str = 'entrar', limite: Any = None, obter: Callable[[Any], Any] \| None = None, obter_referencia: Callable[[Any], Any] \| None = None)` |
| `SequenciaDoisPassos` | reconhecer sequência de eventos | `SequenciaDoisPassos(eventos: Eventos, primeiro: str, segundo: str, acao: AcaoSequencia, janela: float \| None = None, nome: str = 'sequencia')` |
| `regra` | helper de criação | `regra(nome: str, quando: Condicao, entao: Acao, *, modo: str = 'ao_ativar', prioridade: str \| int = 'normal', max_execucoes: int \| None = None, cooldown: float = 0.0) -> Regra` |

## Modos e frequência de disparo

Escolha o modo da regra de acordo com a semântica desejada: uma regra que dispara ao entrar em condição não deve ser confundida com uma regra que repete enquanto a condição permanece verdadeira. `max_execucoes` e `cooldown` acrescentam limites explícitos.

## Prioridade e composição

Prefira várias regras pequenas e nomeadas a uma regra enorme com muitas responsabilidades. Use grupos quando o conjunto formar uma unidade de configuração ou ciclo de vida.

## Erros, ciclos e rastreamento

Condições e ações são fornecidas pelo programa e podem falhar. Cadeias reativas também podem criar realimentação. Quando uma sequência fica difícil de explicar, use `coral.rastreamento_reativo` em vez de remover diagnósticos para esconder o ciclo.

## Boas práticas

* Nomeie regras pelo comportamento observado.
* Mantenha condição sem efeitos colaterais quando possível.
* Use eventos para comunicação entre domínios.
* Use relógio controlável em testes.
* Prefira cooldown, debounce e temporizador oficiais a contadores manuais espalhados pelo código.

## Integração com outros módulos

`coral.tempo_eventos` fornece infraestrutura temporal. `coral.observadores_reativos` e `coral.rastreamento_reativo` aprofundam observação e diagnóstico. `coral.mundo` e `coral.jogos` podem compartilhar o mesmo barramento sem se acoplar diretamente.

## Testabilidade

A release fornece tempo simulado e caminhos headless. Teste a mudança de estado e os eventos primeiro; depois teste a camada visual separadamente.

## Referência da API

<!-- AUTO:API -->

### Funções

#### `regra(nome: str, quando: Condicao, entao: Acao, *, modo: str = 'ao_ativar', prioridade: str | int = 'normal', max_execucoes: int | None = None, cooldown: float = 0.0) -> Regra`

Entrada pública `regra` da superfície `coral.regras`.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `nome` | `str` | obrigatório | posicional |
| `quando` | `Condicao` | obrigatório | posicional |
| `entao` | `Acao` | obrigatório | posicional |
| `modo` | `str` | `'ao_ativar'` | nomeado |
| `prioridade` | `str \| int` | `'normal'` | nomeado |
| `max_execucoes` | `int \| None` | `None` | nomeado |
| `cooldown` | `float` | `0.0` | nomeado |

**Retorno:** `Regra`

### Classes e protocolos

#### `Regra(nome: str, condicao: Condicao, acao: Acao, modo: str = 'ao_ativar', habilitada: bool = True, ativa: bool = False, execucoes: int = 0, prioridade: str | int = 'normal', max_execucoes: int | None = None, cooldown: float = 0.0, ultimo_disparo: float | None = None, motivo_ultima_supressao: str | None = None, ultima_condicao: bool | None = None)`

Entrada pública `Regra` da superfície `coral.regras`.

**Atributos declarados**

| Nome | Tipo | Padrão |
|---|---|---|
| `nome` | `str` | obrigatório |
| `condicao` | `Condicao` | obrigatório |
| `acao` | `Acao` | obrigatório |
| `modo` | `str` | `'ao_ativar'` |
| `habilitada` | `bool` | `True` |
| `ativa` | `bool` | `False` |
| `execucoes` | `int` | `0` |
| `prioridade` | `str \| int` | `'normal'` |
| `max_execucoes` | `int \| None` | `None` |
| `cooldown` | `float` | `0.0` |
| `ultimo_disparo` | `float \| None` | `None` |
| `motivo_ultima_supressao` | `str \| None` | `None` |
| `ultima_condicao` | `bool \| None` | `None` |

**Métodos e propriedades públicas**

| Nome | Tipo | Assinatura | Retorno | Descrição |
|---|---|---|---|---|
| `avaliar` | método | `avaliar(contexto: Any, *, instante: float \| None = None) -> bool` | `bool` | Sem docstring própria na release. |

#### `GrupoRegras(nome: str, regras: tuple[Regra, ...])`

Entrada pública `GrupoRegras` da superfície `coral.regras`.

**Atributos declarados**

| Nome | Tipo | Padrão |
|---|---|---|
| `nome` | `str` | obrigatório |
| `regras` | `tuple[Regra, ...]` | obrigatório |

**Métodos e propriedades públicas**

| Nome | Tipo | Assinatura | Retorno | Descrição |
|---|---|---|---|---|
| `habilitar` | método | `habilitar() -> None` | `None` | Sem docstring própria na release. |
| `desabilitar` | método | `desabilitar() -> None` | `None` | Sem docstring própria na release. |

#### `Debounce(intervalo: float, acao: Acao, nome: str = 'debounce', restante: float | None = None, pendente: bool = False, contexto_mais_recente: Any = None)`

Entrada pública `Debounce` da superfície `coral.regras`.

**Atributos declarados**

| Nome | Tipo | Padrão |
|---|---|---|
| `intervalo` | `float` | obrigatório |
| `acao` | `Acao` | obrigatório |
| `nome` | `str` | `'debounce'` |
| `restante` | `float \| None` | `None` |
| `pendente` | `bool` | `False` |
| `contexto_mais_recente` | `Any` | `None` |

**Métodos e propriedades públicas**

| Nome | Tipo | Assinatura | Retorno | Descrição |
|---|---|---|---|---|
| `notificar` | método | `notificar(contexto: Any = None) -> None` | `None` | Sem docstring própria na release. |
| `atualizar` | método | `atualizar(dt: float) -> bool` | `bool` | Sem docstring própria na release. |

#### `Temporizador(intervalo: float, acao: Acao, repetir: bool = False, nome: str = 'temporizador', restante: float | None = None, ativo: bool = True)`

Entrada pública `Temporizador` da superfície `coral.regras`.

**Atributos declarados**

| Nome | Tipo | Padrão |
|---|---|---|
| `intervalo` | `float` | obrigatório |
| `acao` | `Acao` | obrigatório |
| `repetir` | `bool` | `False` |
| `nome` | `str` | `'temporizador'` |
| `restante` | `float \| None` | `None` |
| `ativo` | `bool` | `True` |

**Métodos e propriedades públicas**

| Nome | Tipo | Assinatura | Retorno | Descrição |
|---|---|---|---|---|
| `atualizar` | método | `atualizar(contexto: Any, dt: float) -> int` | `int` | Sem docstring própria na release. |

#### `Eventos(*, pai: 'Eventos | None' = None, relogio: FonteTempo | None = None, fonte_instante: Callable[[], float] | None = None)`

Barramento local compatível com ``coral.regras.Eventos``.

**Implementação:** `coral.tempo_eventos`

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

#### `MotorRegras(*, relogio: FonteTempo | None = None, eventos: Eventos | None = None, rastreamento: RastreamentoReativo | str | None = None)`

Entrada pública `MotorRegras` da superfície `coral.regras`.

**Métodos e propriedades públicas**

| Nome | Tipo | Assinatura | Retorno | Descrição |
|---|---|---|---|---|
| `adicionar` | método | `adicionar(regra: Regra) -> Regra` | `Regra` | Sem docstring própria na release. |
| `regra` | método | `regra(nome: str, condicao: Condicao, acao: Acao, *, modo: str = 'ao_ativar', prioridade: str \| int = 'normal', max_execucoes: int \| None = None, cooldown: float = 0.0) -> Regra` | `Regra` | Sem docstring própria na release. |
| `obter_regra` | método | `obter_regra(nome: str) -> Regra` | `Regra` | Sem docstring própria na release. |
| `habilitar_regra` | método | `habilitar_regra(nome: str) -> Regra` | `Regra` | Sem docstring própria na release. |
| `desabilitar_regra` | método | `desabilitar_regra(nome: str) -> Regra` | `Regra` | Sem docstring própria na release. |
| `criar_grupo` | método | `criar_grupo(nome: str, regras: list[str] \| tuple[str, ...]) -> GrupoRegras` | `GrupoRegras` | Sem docstring própria na release. |
| `obter_grupo` | método | `obter_grupo(nome: str) -> GrupoRegras` | `GrupoRegras` | Sem docstring própria na release. |
| `habilitar_grupo` | método | `habilitar_grupo(nome: str) -> GrupoRegras` | `GrupoRegras` | Sem docstring própria na release. |
| `desabilitar_grupo` | método | `desabilitar_grupo(nome: str) -> GrupoRegras` | `GrupoRegras` | Sem docstring própria na release. |
| `observar_mudanca` | método | `observar_mudanca(nome: str, leitor, acao) -> ObservadorMudanca` | `ObservadorMudanca` | Sem docstring própria na release. |
| `observar_passar_de` | método | `observar_passar_de(nome: str, leitor, limite, acao) -> ObservadorMudanca` | `ObservadorMudanca` | Sem docstring própria na release. |
| `observar_cair_abaixo_de` | método | `observar_cair_abaixo_de(nome: str, leitor, limite, acao) -> ObservadorMudanca` | `ObservadorMudanca` | Sem docstring própria na release. |
| `observar_entrada_regiao` | método | `observar_entrada_regiao(nome: str, leitor, regiao_alvo, acao, **opcoes) -> ObservadorEspacial` | `ObservadorEspacial` | Sem docstring própria na release. |
| `observar_saida_regiao` | método | `observar_saida_regiao(nome: str, leitor, regiao_alvo, acao, **opcoes) -> ObservadorEspacial` | `ObservadorEspacial` | Sem docstring própria na release. |
| `observar_proximidade` | método | `observar_proximidade(nome: str, leitor, referencia, limite, acao, **opcoes) -> ObservadorEspacial` | `ObservadorEspacial` | Sem docstring própria na release. |
| `observar_toque` | método | `observar_toque(nome: str, leitor, referencia, acao, **opcoes) -> ObservadorEspacial` | `ObservadorEspacial` | Sem docstring própria na release. |
| `observar_intersecao` | método | `observar_intersecao(nome: str, leitor, referencia, acao, **opcoes) -> ObservadorEspacial` | `ObservadorEspacial` | Sem docstring própria na release. |
| `observar_regioes_mapa` | método | `observar_regioes_mapa(nome: str, alvo: Any, mapa, regioes, resolvedor, *, identificador_alvo: Any = None)` | `não declarado` | Observa transições discretas usando o mesmo barramento do motor. |
| `sequencia` | método | `sequencia(nome: str, primeiro: str, segundo: str, acao, *, janela: float \| None = None) -> SequenciaDoisPassos` | `SequenciaDoisPassos` | Sem docstring própria na release. |
| `debounce` | método | `debounce(segundos: float, acao: Acao, *, nome: str = 'debounce') -> Debounce` | `Debounce` | Sem docstring própria na release. |
| `ativar_regra_durante` | método | `ativar_regra_durante(nome: str, segundos: float) -> Regra` | `Regra` | Sem docstring própria na release. |
| `ativar_regra_ate` | método | `ativar_regra_ate(nome: str, condicao: Condicao) -> Regra` | `Regra` | Sem docstring própria na release. |
| `depois_de` | método | `depois_de(segundos: float, acao: Acao, *, nome: str = 'depois') -> Temporizador` | `Temporizador` | Sem docstring própria na release. |
| `a_cada` | método | `a_cada(segundos: float, acao: Acao, *, nome: str = 'intervalo') -> Temporizador` | `Temporizador` | Sem docstring própria na release. |
| `instante_atual` | método | `instante_atual() -> float` | `float` | Sem docstring própria na release. |
| `avaliar` | método | `avaliar(contexto: Any) -> tuple[str, ...]` | `tuple[str, ...]` | Sem docstring própria na release. |
| `atualizar` | método | `atualizar(contexto: Any, dt: float \| None = None) -> tuple[str, ...]` | `tuple[str, ...]` | Sem docstring própria na release. |
| `processar_ciclo` | método | `processar_ciclo(contexto: Any = None, *, limite_reacoes: int = 1000) -> tuple[Evento, ...]` | `tuple[Evento, ...]` | Sem docstring própria na release. |
| `emitir_evento` | método | `emitir_evento(nome: str, *args, **kwargs) -> int` | `int` | Emite um evento de regra pelo barramento compartilhado, sem conhecer consumidores. |
| `atualizar_por_relogio` | método | `atualizar_por_relogio(contexto: Any) -> tuple[str, ...]` | `tuple[str, ...]` | Sem docstring própria na release. |

#### `ObservadorMudanca(nome: str, leitor: LeitorValor, acao: AcaoMudanca, modo: str = 'mudanca', limite: Any = None)`

Entrada pública `ObservadorMudanca` da superfície `coral.regras`.

**Implementação:** `coral.observadores_reativos`

**Atributos declarados**

| Nome | Tipo | Padrão |
|---|---|---|
| `nome` | `str` | obrigatório |
| `leitor` | `LeitorValor` | obrigatório |
| `acao` | `AcaoMudanca` | obrigatório |
| `modo` | `str` | `'mudanca'` |
| `limite` | `Any` | `None` |

**Métodos e propriedades públicas**

| Nome | Tipo | Assinatura | Retorno | Descrição |
|---|---|---|---|---|
| `passar_de` | método | `passar_de(nome: str, leitor: LeitorValor, limite: Any, acao: AcaoMudanca) -> 'ObservadorMudanca'` | `'ObservadorMudanca'` | Sem docstring própria na release. |
| `cair_abaixo_de` | método | `cair_abaixo_de(nome: str, leitor: LeitorValor, limite: Any, acao: AcaoMudanca) -> 'ObservadorMudanca'` | `'ObservadorMudanca'` | Sem docstring própria na release. |
| `inicializado` | propriedade | `inicializado() -> bool` | `bool` | Sem docstring própria na release. |
| `valor_anterior` | propriedade | `valor_anterior() -> Any` | `Any` | Sem docstring própria na release. |
| `avaliar` | método | `avaliar(contexto: Any) -> bool` | `bool` | Sem docstring própria na release. |

#### `ObservadorEspacial(nome: str, leitor: LeitorValor, referencia: Any, acao: Callable[[Any, Any, Any], Any], relacao: str, transicao: str = 'entrar', limite: Any = None, obter: Callable[[Any], Any] | None = None, obter_referencia: Callable[[Any], Any] | None = None)`

Entrada pública `ObservadorEspacial` da superfície `coral.regras`.

**Implementação:** `coral.observadores_reativos`

**Atributos declarados**

| Nome | Tipo | Padrão |
|---|---|---|
| `nome` | `str` | obrigatório |
| `leitor` | `LeitorValor` | obrigatório |
| `referencia` | `Any` | obrigatório |
| `acao` | `Callable[[Any, Any, Any], Any]` | obrigatório |
| `relacao` | `str` | obrigatório |
| `transicao` | `str` | `'entrar'` |
| `limite` | `Any` | `None` |
| `obter` | `Callable[[Any], Any] \| None` | `None` |
| `obter_referencia` | `Callable[[Any], Any] \| None` | `None` |

**Métodos e propriedades públicas**

| Nome | Tipo | Assinatura | Retorno | Descrição |
|---|---|---|---|---|
| `entrar_em_regiao` | método | `entrar_em_regiao(nome, leitor, regiao_alvo, acao, *, obter = None, obter_referencia = None)` | `não declarado` | Sem docstring própria na release. |
| `sair_de_regiao` | método | `sair_de_regiao(nome, leitor, regiao_alvo, acao, *, obter = None, obter_referencia = None)` | `não declarado` | Sem docstring própria na release. |
| `chegar_a_menos_de` | método | `chegar_a_menos_de(nome, leitor, referencia, limite, acao, *, obter = None, obter_referencia = None)` | `não declarado` | Sem docstring própria na release. |
| `tocar` | método | `tocar(nome, leitor, referencia, acao, *, obter = None, obter_referencia = None)` | `não declarado` | Sem docstring própria na release. |
| `intersectar` | método | `intersectar(nome, leitor, referencia, acao, *, obter = None, obter_referencia = None)` | `não declarado` | Sem docstring própria na release. |
| `avaliar` | método | `avaliar(contexto: Any) -> bool` | `bool` | Sem docstring própria na release. |

#### `SequenciaDoisPassos(eventos: Eventos, primeiro: str, segundo: str, acao: AcaoSequencia, janela: float | None = None, nome: str = 'sequencia')`

Entrada pública `SequenciaDoisPassos` da superfície `coral.regras`.

**Implementação:** `coral.sequencias_reativas`

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

#### `Condicao`

Alias público de tipo ou valor.

**Valor declarado:** `Callable[[Any], bool]`

#### `Acao`

Alias público de tipo ou valor.

**Valor declarado:** `Callable[[Any], Any]`

#### `MODOS_REGRA`

Constante pública do módulo.

**Valor declarado:** `frozenset({'ao_ativar', 'sempre', 'uma_vez'})`

<!-- /AUTO:API -->

## Compatibilidade

O motor é genérico e não depende de jogo, RPG ou interface gráfica. Ele pode ser usado em automação, simulação, aplicação de regras e domínios próprios.
