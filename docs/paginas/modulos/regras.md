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

#### `regra`

Helper de criação.

**Exemplo**

```coral
defina estado como "normal"

regra "ferido" quando vida for menor ou igual a 5 então
    defina estado como "ferido"
fim
```

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | obrigatório |
| `quando` | Valor correspondente a quando. | `Condicao` | obrigatório |
| `entao` | Valor correspondente a entao. | `Acao` | obrigatório |
| `modo` | Valor correspondente a modo. | `str` | `'ao_ativar'` |
| `prioridade` | Valor correspondente a prioridade. | `str \| int` | `'normal'` |
| `max_execucoes` | Valor correspondente a max execucoes. | `int \| None` | `None` |
| `cooldown` | Valor correspondente a cooldown. | `float` | `0.0` |

**Retorno**

Retorna um valor declarado como `Regra`.

:::details Detalhes técnicos

**Assinatura:** `regra(nome: str, quando: Condicao, entao: Acao, *, modo: str = 'ao_ativar', prioridade: str \| int = 'normal', max_execucoes: int \| None = None, cooldown: float = 0.0) -> Regra`

**Origem da implementação:** `coral.regras`

**Arquivo na release:** `coral/regras.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `nome` | posicional |
| `quando` | posicional |
| `entao` | posicional |
| `modo` | nomeado |
| `prioridade` | nomeado |
| `max_execucoes` | nomeado |
| `cooldown` | nomeado |

:::

### Classes e protocolos

#### `Regra`

Representa condição e ação.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | obrigatório |
| `condicao` | Valor correspondente a condicao. | `Condicao` | obrigatório |
| `acao` | Valor correspondente a acao. | `Acao` | obrigatório |
| `modo` | Valor correspondente a modo. | `str` | `'ao_ativar'` |
| `habilitada` | Valor correspondente a habilitada. | `bool` | `True` |
| `ativa` | Valor correspondente a ativa. | `bool` | `False` |
| `execucoes` | Valor correspondente a execucoes. | `int` | `0` |
| `prioridade` | Valor correspondente a prioridade. | `str \| int` | `'normal'` |
| `max_execucoes` | Valor correspondente a max execucoes. | `int \| None` | `None` |
| `cooldown` | Valor correspondente a cooldown. | `float` | `0.0` |
| `ultimo_disparo` | Valor correspondente a ultimo disparo. | `float \| None` | `None` |
| `motivo_ultima_supressao` | Valor correspondente a motivo ultima supressao. | `str \| None` | `None` |
| `ultima_condicao` | Valor correspondente a ultima condicao. | `bool \| None` | `None` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | obrigatório |
| `condicao` | Valor correspondente a condicao. | `Condicao` | obrigatório |
| `acao` | Valor correspondente a acao. | `Acao` | obrigatório |
| `modo` | Valor correspondente a modo. | `str` | `'ao_ativar'` |
| `habilitada` | Valor correspondente a habilitada. | `bool` | `True` |
| `ativa` | Valor correspondente a ativa. | `bool` | `False` |
| `execucoes` | Valor correspondente a execucoes. | `int` | `0` |
| `prioridade` | Valor correspondente a prioridade. | `str \| int` | `'normal'` |
| `max_execucoes` | Valor correspondente a max execucoes. | `int \| None` | `None` |
| `cooldown` | Valor correspondente a cooldown. | `float` | `0.0` |
| `ultimo_disparo` | Valor correspondente a ultimo disparo. | `float \| None` | `None` |
| `motivo_ultima_supressao` | Valor correspondente a motivo ultima supressao. | `str \| None` | `None` |
| `ultima_condicao` | Valor correspondente a ultima condicao. | `bool \| None` | `None` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `avaliar` | Executa a operação `avaliar` disponibilizada por `coral.regras`. | `bool` |

:::details Detalhes técnicos

**Assinatura:** `Regra(nome: str, condicao: Condicao, acao: Acao, modo: str = 'ao_ativar', habilitada: bool = True, ativa: bool = False, execucoes: int = 0, prioridade: str \| int = 'normal', max_execucoes: int \| None = None, cooldown: float = 0.0, ultimo_disparo: float \| None = None, motivo_ultima_supressao: str \| None = None, ultima_condicao: bool \| None = None)`

**Origem da implementação:** `coral.regras`

**Arquivo na release:** `coral/regras.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `avaliar` | método | `avaliar(contexto: Any, *, instante: float \| None = None) -> bool` |

:::

#### `GrupoRegras`

Representa GrupoRegras na API de `coral.regras`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | obrigatório |
| `regras` | Valor correspondente a regras. | `tuple[Regra, ...]` | obrigatório |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | obrigatório |
| `regras` | Valor correspondente a regras. | `tuple[Regra, ...]` | obrigatório |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `habilitar` | Executa a operação `habilitar` disponibilizada por `coral.regras`. | `None` |
| `desabilitar` | Executa a operação `desabilitar` disponibilizada por `coral.regras`. | `None` |

:::details Detalhes técnicos

**Assinatura:** `GrupoRegras(nome: str, regras: tuple[Regra, ...])`

**Origem da implementação:** `coral.regras`

**Arquivo na release:** `coral/regras.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `habilitar` | método | `habilitar() -> None` |
| `desabilitar` | método | `desabilitar() -> None` |

:::

#### `Debounce`

Representa Debounce na API de `coral.regras`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `intervalo` | Valor correspondente a intervalo. | `float` | obrigatório |
| `acao` | Valor correspondente a acao. | `Acao` | obrigatório |
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | `'debounce'` |
| `restante` | Valor correspondente a restante. | `float \| None` | `None` |
| `pendente` | Valor correspondente a pendente. | `bool` | `False` |
| `contexto_mais_recente` | Valor correspondente a contexto mais recente. | `Any` | `None` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `intervalo` | Valor correspondente a intervalo. | `float` | obrigatório |
| `acao` | Valor correspondente a acao. | `Acao` | obrigatório |
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | `'debounce'` |
| `restante` | Valor correspondente a restante. | `float \| None` | `None` |
| `pendente` | Valor correspondente a pendente. | `bool` | `False` |
| `contexto_mais_recente` | Valor correspondente a contexto mais recente. | `Any` | `None` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `notificar` | Executa a operação `notificar` disponibilizada por `coral.regras`. | `None` |
| `atualizar` | Atualiza o valor solicitado. | `bool` |

:::details Detalhes técnicos

**Assinatura:** `Debounce(intervalo: float, acao: Acao, nome: str = 'debounce', restante: float \| None = None, pendente: bool = False, contexto_mais_recente: Any = None)`

**Origem da implementação:** `coral.regras`

**Arquivo na release:** `coral/regras.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `notificar` | método | `notificar(contexto: Any = None) -> None` |
| `atualizar` | método | `atualizar(dt: float) -> bool` |

:::

#### `Temporizador`

Representa Temporizador na API de `coral.regras`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `intervalo` | Valor correspondente a intervalo. | `float` | obrigatório |
| `acao` | Valor correspondente a acao. | `Acao` | obrigatório |
| `repetir` | Valor correspondente a repetir. | `bool` | `False` |
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | `'temporizador'` |
| `restante` | Valor correspondente a restante. | `float \| None` | `None` |
| `ativo` | Valor correspondente a ativo. | `bool` | `True` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `intervalo` | Valor correspondente a intervalo. | `float` | obrigatório |
| `acao` | Valor correspondente a acao. | `Acao` | obrigatório |
| `repetir` | Valor correspondente a repetir. | `bool` | `False` |
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | `'temporizador'` |
| `restante` | Valor correspondente a restante. | `float \| None` | `None` |
| `ativo` | Valor correspondente a ativo. | `bool` | `True` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `atualizar` | Atualiza o valor solicitado. | `int` |

:::details Detalhes técnicos

**Assinatura:** `Temporizador(intervalo: float, acao: Acao, repetir: bool = False, nome: str = 'temporizador', restante: float \| None = None, ativo: bool = True)`

**Origem da implementação:** `coral.regras`

**Arquivo na release:** `coral/regras.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `atualizar` | método | `atualizar(contexto: Any, dt: float) -> int` |

:::

#### `Eventos`

Barramento local compatível com ``coral.regras.Eventos``.

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
| `quando` | Executa a operação `quando` disponibilizada por `coral.regras`. | `não declarado` |
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

#### `MotorRegras`

Representa MotorRegras na API de `coral.regras`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `relogio` | Relógio usado para controlar tempo ou atualização. | `FonteTempo \| None` | `None` |
| `eventos` | Fonte ou conjunto de eventos associado à operação. | `Eventos \| None` | `None` |
| `rastreamento` | Valor correspondente a rastreamento. | `RastreamentoReativo \| str \| None` | `None` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `adicionar` | Adiciona o valor solicitado. | `Regra` |
| `regra` | Helper de criação. | `Regra` |
| `obter_regra` | Obtém regra. | `Regra` |
| `habilitar_regra` | Executa a operação `habilitar_regra` disponibilizada por `coral.regras`. | `Regra` |
| `desabilitar_regra` | Executa a operação `desabilitar_regra` disponibilizada por `coral.regras`. | `Regra` |
| `criar_grupo` | Cria grupo. | `GrupoRegras` |
| `obter_grupo` | Obtém grupo. | `GrupoRegras` |
| `habilitar_grupo` | Executa a operação `habilitar_grupo` disponibilizada por `coral.regras`. | `GrupoRegras` |
| `desabilitar_grupo` | Executa a operação `desabilitar_grupo` disponibilizada por `coral.regras`. | `GrupoRegras` |
| `observar_mudanca` | Observa mudanca. | `ObservadorMudanca` |
| `observar_passar_de` | Observa passar de. | `ObservadorMudanca` |
| `observar_cair_abaixo_de` | Observa cair abaixo de. | `ObservadorMudanca` |
| `observar_entrada_regiao` | Observa entrada regiao. | `ObservadorEspacial` |
| `observar_saida_regiao` | Observa saida regiao. | `ObservadorEspacial` |
| `observar_proximidade` | Observa proximidade. | `ObservadorEspacial` |
| `observar_toque` | Observa toque. | `ObservadorEspacial` |
| `observar_intersecao` | Observa intersecao. | `ObservadorEspacial` |
| `observar_regioes_mapa` | Observa transições discretas usando o mesmo barramento do motor. | `não declarado` |
| `sequencia` | Executa a operação `sequencia` disponibilizada por `coral.regras`. | `SequenciaDoisPassos` |
| `debounce` | Executa a operação `debounce` disponibilizada por `coral.regras`. | `Debounce` |
| `ativar_regra_durante` | Executa a operação `ativar_regra_durante` disponibilizada por `coral.regras`. | `Regra` |
| `ativar_regra_ate` | Executa a operação `ativar_regra_ate` disponibilizada por `coral.regras`. | `Regra` |
| `depois_de` | Executa a operação `depois_de` disponibilizada por `coral.regras`. | `Temporizador` |
| `a_cada` | Executa a operação `a_cada` disponibilizada por `coral.regras`. | `Temporizador` |
| `instante_atual` | Executa a operação `instante_atual` disponibilizada por `coral.regras`. | `float` |
| `avaliar` | Executa a operação `avaliar` disponibilizada por `coral.regras`. | `tuple[str, ...]` |
| `atualizar` | Atualiza o valor solicitado. | `tuple[str, ...]` |
| `processar_ciclo` | Processa ciclo. | `tuple[Evento, ...]` |
| `emitir_evento` | Emite um evento de regra pelo barramento compartilhado, sem conhecer consumidores. | `int` |
| `atualizar_por_relogio` | Atualiza por relogio. | `tuple[str, ...]` |

:::details Detalhes técnicos

**Assinatura:** `MotorRegras(*, relogio: FonteTempo \| None = None, eventos: Eventos \| None = None, rastreamento: RastreamentoReativo \| str \| None = None)`

**Origem da implementação:** `coral.regras`

**Arquivo na release:** `coral/regras.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `relogio` | nomeado |
| `eventos` | nomeado |
| `rastreamento` | nomeado |

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `adicionar` | método | `adicionar(regra: Regra) -> Regra` |
| `regra` | método | `regra(nome: str, condicao: Condicao, acao: Acao, *, modo: str = 'ao_ativar', prioridade: str \| int = 'normal', max_execucoes: int \| None = None, cooldown: float = 0.0) -> Regra` |
| `obter_regra` | método | `obter_regra(nome: str) -> Regra` |
| `habilitar_regra` | método | `habilitar_regra(nome: str) -> Regra` |
| `desabilitar_regra` | método | `desabilitar_regra(nome: str) -> Regra` |
| `criar_grupo` | método | `criar_grupo(nome: str, regras: list[str] \| tuple[str, ...]) -> GrupoRegras` |
| `obter_grupo` | método | `obter_grupo(nome: str) -> GrupoRegras` |
| `habilitar_grupo` | método | `habilitar_grupo(nome: str) -> GrupoRegras` |
| `desabilitar_grupo` | método | `desabilitar_grupo(nome: str) -> GrupoRegras` |
| `observar_mudanca` | método | `observar_mudanca(nome: str, leitor, acao) -> ObservadorMudanca` |
| `observar_passar_de` | método | `observar_passar_de(nome: str, leitor, limite, acao) -> ObservadorMudanca` |
| `observar_cair_abaixo_de` | método | `observar_cair_abaixo_de(nome: str, leitor, limite, acao) -> ObservadorMudanca` |
| `observar_entrada_regiao` | método | `observar_entrada_regiao(nome: str, leitor, regiao_alvo, acao, **opcoes) -> ObservadorEspacial` |
| `observar_saida_regiao` | método | `observar_saida_regiao(nome: str, leitor, regiao_alvo, acao, **opcoes) -> ObservadorEspacial` |
| `observar_proximidade` | método | `observar_proximidade(nome: str, leitor, referencia, limite, acao, **opcoes) -> ObservadorEspacial` |
| `observar_toque` | método | `observar_toque(nome: str, leitor, referencia, acao, **opcoes) -> ObservadorEspacial` |
| `observar_intersecao` | método | `observar_intersecao(nome: str, leitor, referencia, acao, **opcoes) -> ObservadorEspacial` |
| `observar_regioes_mapa` | método | `observar_regioes_mapa(nome: str, alvo: Any, mapa, regioes, resolvedor, *, identificador_alvo: Any = None)` |
| `sequencia` | método | `sequencia(nome: str, primeiro: str, segundo: str, acao, *, janela: float \| None = None) -> SequenciaDoisPassos` |
| `debounce` | método | `debounce(segundos: float, acao: Acao, *, nome: str = 'debounce') -> Debounce` |
| `ativar_regra_durante` | método | `ativar_regra_durante(nome: str, segundos: float) -> Regra` |
| `ativar_regra_ate` | método | `ativar_regra_ate(nome: str, condicao: Condicao) -> Regra` |
| `depois_de` | método | `depois_de(segundos: float, acao: Acao, *, nome: str = 'depois') -> Temporizador` |
| `a_cada` | método | `a_cada(segundos: float, acao: Acao, *, nome: str = 'intervalo') -> Temporizador` |
| `instante_atual` | método | `instante_atual() -> float` |
| `avaliar` | método | `avaliar(contexto: Any) -> tuple[str, ...]` |
| `atualizar` | método | `atualizar(contexto: Any, dt: float \| None = None) -> tuple[str, ...]` |
| `processar_ciclo` | método | `processar_ciclo(contexto: Any = None, *, limite_reacoes: int = 1000) -> tuple[Evento, ...]` |
| `emitir_evento` | método | `emitir_evento(nome: str, *args, **kwargs) -> int` |
| `atualizar_por_relogio` | método | `atualizar_por_relogio(contexto: Any) -> tuple[str, ...]` |

:::

#### `ObservadorMudanca`

Representa ObservadorMudanca na API de `coral.regras`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | obrigatório |
| `leitor` | Valor correspondente a leitor. | `LeitorValor` | obrigatório |
| `acao` | Valor correspondente a acao. | `AcaoMudanca` | obrigatório |
| `modo` | Valor correspondente a modo. | `str` | `'mudanca'` |
| `limite` | Valor correspondente a limite. | `Any` | `None` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | obrigatório |
| `leitor` | Valor correspondente a leitor. | `LeitorValor` | obrigatório |
| `acao` | Valor correspondente a acao. | `AcaoMudanca` | obrigatório |
| `modo` | Valor correspondente a modo. | `str` | `'mudanca'` |
| `limite` | Valor correspondente a limite. | `Any` | `None` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `passar_de` | Executa a operação `passar_de` disponibilizada por `coral.regras`. | `'ObservadorMudanca'` |
| `cair_abaixo_de` | Executa a operação `cair_abaixo_de` disponibilizada por `coral.regras`. | `'ObservadorMudanca'` |
| `inicializado` | Indica o estado de inicializado. | `bool` |
| `valor_anterior` | Obtém valor anterior. | `Any` |
| `avaliar` | Executa a operação `avaliar` disponibilizada por `coral.regras`. | `bool` |

:::details Detalhes técnicos

**Assinatura:** `ObservadorMudanca(nome: str, leitor: LeitorValor, acao: AcaoMudanca, modo: str = 'mudanca', limite: Any = None)`

**Origem da implementação:** `coral.observadores_reativos`

**Arquivo na release:** `coral/observadores_reativos.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `passar_de` | método | `passar_de(nome: str, leitor: LeitorValor, limite: Any, acao: AcaoMudanca) -> 'ObservadorMudanca'` |
| `cair_abaixo_de` | método | `cair_abaixo_de(nome: str, leitor: LeitorValor, limite: Any, acao: AcaoMudanca) -> 'ObservadorMudanca'` |
| `inicializado` | propriedade | `inicializado() -> bool` |
| `valor_anterior` | propriedade | `valor_anterior() -> Any` |
| `avaliar` | método | `avaliar(contexto: Any) -> bool` |

:::

#### `ObservadorEspacial`

Representa ObservadorEspacial na API de `coral.regras`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | obrigatório |
| `leitor` | Valor correspondente a leitor. | `LeitorValor` | obrigatório |
| `referencia` | Valor correspondente a referencia. | `Any` | obrigatório |
| `acao` | Valor correspondente a acao. | `Callable[[Any, Any, Any], Any]` | obrigatório |
| `relacao` | Valor correspondente a relacao. | `str` | obrigatório |
| `transicao` | Valor correspondente a transicao. | `str` | `'entrar'` |
| `limite` | Valor correspondente a limite. | `Any` | `None` |
| `obter` | Valor correspondente a obter. | `Callable[[Any], Any] \| None` | `None` |
| `obter_referencia` | Valor correspondente a obter referencia. | `Callable[[Any], Any] \| None` | `None` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | obrigatório |
| `leitor` | Valor correspondente a leitor. | `LeitorValor` | obrigatório |
| `referencia` | Valor correspondente a referencia. | `Any` | obrigatório |
| `acao` | Valor correspondente a acao. | `Callable[[Any, Any, Any], Any]` | obrigatório |
| `relacao` | Valor correspondente a relacao. | `str` | obrigatório |
| `transicao` | Valor correspondente a transicao. | `str` | `'entrar'` |
| `limite` | Valor correspondente a limite. | `Any` | `None` |
| `obter` | Valor correspondente a obter. | `Callable[[Any], Any] \| None` | `None` |
| `obter_referencia` | Valor correspondente a obter referencia. | `Callable[[Any], Any] \| None` | `None` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `entrar_em_regiao` | Executa a operação `entrar_em_regiao` disponibilizada por `coral.regras`. | `não declarado` |
| `sair_de_regiao` | Executa a operação `sair_de_regiao` disponibilizada por `coral.regras`. | `não declarado` |
| `chegar_a_menos_de` | Executa a operação `chegar_a_menos_de` disponibilizada por `coral.regras`. | `não declarado` |
| `tocar` | Executa o valor solicitado. | `não declarado` |
| `intersectar` | Verifica a interseção de o valor solicitado. | `não declarado` |
| `avaliar` | Executa a operação `avaliar` disponibilizada por `coral.regras`. | `bool` |

:::details Detalhes técnicos

**Assinatura:** `ObservadorEspacial(nome: str, leitor: LeitorValor, referencia: Any, acao: Callable[[Any, Any, Any], Any], relacao: str, transicao: str = 'entrar', limite: Any = None, obter: Callable[[Any], Any] \| None = None, obter_referencia: Callable[[Any], Any] \| None = None)`

**Origem da implementação:** `coral.observadores_reativos`

**Arquivo na release:** `coral/observadores_reativos.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `entrar_em_regiao` | método | `entrar_em_regiao(nome, leitor, regiao_alvo, acao, *, obter = None, obter_referencia = None)` |
| `sair_de_regiao` | método | `sair_de_regiao(nome, leitor, regiao_alvo, acao, *, obter = None, obter_referencia = None)` |
| `chegar_a_menos_de` | método | `chegar_a_menos_de(nome, leitor, referencia, limite, acao, *, obter = None, obter_referencia = None)` |
| `tocar` | método | `tocar(nome, leitor, referencia, acao, *, obter = None, obter_referencia = None)` |
| `intersectar` | método | `intersectar(nome, leitor, referencia, acao, *, obter = None, obter_referencia = None)` |
| `avaliar` | método | `avaliar(contexto: Any) -> bool` |

:::

#### `SequenciaDoisPassos`

Representa SequenciaDoisPassos na API de `coral.regras`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `eventos` | Fonte ou conjunto de eventos associado à operação. | `Eventos` | obrigatório |
| `primeiro` | Valor correspondente a primeiro. | `str` | obrigatório |
| `segundo` | Valor correspondente a segundo. | `str` | obrigatório |
| `acao` | Valor correspondente a acao. | `AcaoSequencia` | obrigatório |
| `janela` | Valor correspondente a janela. | `float \| None` | `None` |
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | `'sequencia'` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `eventos` | Fonte ou conjunto de eventos associado à operação. | `Eventos` | obrigatório |
| `primeiro` | Valor correspondente a primeiro. | `str` | obrigatório |
| `segundo` | Valor correspondente a segundo. | `str` | obrigatório |
| `acao` | Valor correspondente a acao. | `AcaoSequencia` | obrigatório |
| `janela` | Valor correspondente a janela. | `float \| None` | `None` |
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | `'sequencia'` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `resetar` | Executa a operação `resetar` disponibilizada por `coral.regras`. | `None` |

:::details Detalhes técnicos

**Assinatura:** `SequenciaDoisPassos(eventos: Eventos, primeiro: str, segundo: str, acao: AcaoSequencia, janela: float \| None = None, nome: str = 'sequencia')`

**Origem da implementação:** `coral.sequencias_reativas`

**Arquivo na release:** `coral/sequencias_reativas.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `resetar` | método | `resetar() -> None` |

:::

### Constantes e aliases

#### `Condicao`

Expõe `Condicao` como parte da API pública do módulo.

:::details Detalhes técnicos

**Assinatura:** `Condicao`

**Origem da implementação:** `coral.regras`

**Arquivo na release:** `coral/regras.py`

**Valor declarado:** `Callable[[Any], bool]`

:::

#### `Acao`

Expõe `Acao` como parte da API pública do módulo.

:::details Detalhes técnicos

**Assinatura:** `Acao`

**Origem da implementação:** `coral.regras`

**Arquivo na release:** `coral/regras.py`

**Valor declarado:** `Callable[[Any], Any]`

:::

#### `MODOS_REGRA`

Expõe a constante pública `MODOS_REGRA`.

:::details Detalhes técnicos

**Assinatura:** `MODOS_REGRA`

**Origem da implementação:** `coral.regras`

**Arquivo na release:** `coral/regras.py`

**Valor declarado:** `frozenset({'ao_ativar', 'sempre', 'uma_vez'})`

:::

<!-- /AUTO:API -->

## Compatibilidade

O motor é genérico e não depende de jogo, RPG ou interface gráfica. Ele pode ser usado em automação, simulação, aplicação de regras e domínios próprios.
