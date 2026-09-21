# coral.replay_reativo

## Visão geral

`coral.replay_reativo` oferece gravação e reprodução determinística de eventos e mudanças. Use para gravar e reproduzir eventos e mudanças de forma determinística.

<!-- AUTO:MODULO -->

**Importação:** `coral.replay_reativo`  
**Categoria:** reativo  

gravação e reprodução determinística de eventos e mudanças

### Superfície pública detectada

`RegistroReplay`, `ResultadoReplay`, `GravadorReplay`, `ReplayReativo`

<!-- /AUTO:MODULO -->

## Papel no ecossistema

Permite registrar entradas relevantes de um fluxo reativo e reaplicá las de forma controlada. O objetivo é reproduzir comportamento sem depender novamente das fontes externas originais.

## Conceitos principais

### Registro

`RegistroReplay` descreve tipo e dados de uma entrada gravada.

### Gravação

`GravadorReplay` coleta registros produzidos durante uma execução.

### Reprodução

`ReplayReativo` consome uma sequência de registros e produz resultados de replay.

### Resultado

`ResultadoReplay` registra tipo, instante e itens processados para inspeção da reprodução.

## Quando usar

Use este módulo quando o problema corresponder diretamente aos conceitos acima. Por ser um módulo complementar, ele normalmente entra em um programa para resolver uma responsabilidade específica e deve permanecer desacoplado da lógica central sempre que possível.

## Começando

```coral
de coral.replay_reativo importe GravadorReplay, ReplayReativo

defina gravador como GravadorReplay()
mostre gravador
defina replay como ReplayReativo([])
mostre replay
```

## API essencial

| Entrada | Papel |
|---|---|
| `GravadorReplay` | gravar entradas |
| `ReplayReativo` | reproduzir registros |
| `RegistroReplay` | registro persistível |
| `ResultadoReplay` | resultado da reprodução |

A seção **Referência da API** no fim desta página contém a superfície pública completa detectada na release, com assinaturas, parâmetros, retornos e docstrings quando presentes.

## Fluxos comuns

1. Defina quais entradas externas precisam ser gravadas.
2. Execute o sistema com fontes determinísticas de tempo e aleatoriedade quando elas influenciam o resultado.
3. Grave os eventos ou mudanças relevantes.
4. Reproduza os registros em ambiente controlado e compare o estado ou resultados obtidos.

## Erros e casos de borda

Replay não consegue reproduzir um efeito que depende de uma fonte externa não registrada, como arquivo mutável, rede, relógio real ou aleatoriedade não controlada.

## Boas práticas

* Grave entradas, não snapshots gigantes de estado a cada passo.
* Use relógio simulado e sementes fixas quando o comportamento depende deles.
* Versione o formato do registro se ele for persistido entre releases.

## Integração com outros módulos

`coral.tempo_eventos` fornece relógio e eventos controláveis; `coral.aleatorio` fornece fontes com semente; `coral.rastreamento_reativo` ajuda a comparar causalidade entre execução e replay.

## Testabilidade e previsibilidade

O teste mais forte é executar uma sequência, gravar, reproduzir e comparar um estado final ou resultados estruturados.

## Compatibilidade e evolução

A documentação desta página descreve a superfície detectada na **Coral 1.5.9**. O gerador do site atualiza automaticamente o inventário e a referência da API quando uma nova release é importada, mas o texto pedagógico desta seção permanece sob revisão humana.

## Referência da API

<!-- AUTO:API -->

### Classes e protocolos

#### `RegistroReplay`

Representa registro persistível.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `tipo` | Tipo solicitado para o resultado, quando o módulo oferece essa escolha. | `str` | obrigatório |
| `dados` | Dados processados pela operação. | `dict[str, Any]` | obrigatório |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `tipo` | Tipo solicitado para o resultado, quando o módulo oferece essa escolha. | `str` | obrigatório |
| `dados` | Dados processados pela operação. | `dict[str, Any]` | obrigatório |

:::details Detalhes técnicos

**Assinatura:** `RegistroReplay(tipo: str, dados: dict[str, Any])`

**Origem da implementação:** `coral.replay_reativo`

**Arquivo na release:** `coral/replay_reativo.py`

:::

#### `ResultadoReplay`

Representa resultado da reprodução.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `tipo` | Tipo solicitado para o resultado, quando o módulo oferece essa escolha. | `str` | obrigatório |
| `instante` | Valor correspondente a instante. | `float` | obrigatório |
| `processados` | Valor correspondente a processados. | `tuple[str, ...]` | `()` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `tipo` | Tipo solicitado para o resultado, quando o módulo oferece essa escolha. | `str` | obrigatório |
| `instante` | Valor correspondente a instante. | `float` | obrigatório |
| `processados` | Valor correspondente a processados. | `tuple[str, ...]` | `()` |

:::details Detalhes técnicos

**Assinatura:** `ResultadoReplay(tipo: str, instante: float, processados: tuple[str, ...] = ())`

**Origem da implementação:** `coral.replay_reativo`

**Arquivo na release:** `coral/replay_reativo.py`

:::

#### `GravadorReplay`

Representa GravadorReplay na API de `coral.replay_reativo`.

**Exemplo**

```coral
de coral.replay_reativo importe GravadorReplay, ReplayReativo

defina gravador como GravadorReplay()
mostre gravador
defina replay como ReplayReativo([])
mostre replay
```

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `registros` | Executa a operação `registros` disponibilizada por `coral.replay_reativo`. | `tuple[RegistroReplay, ...]` |
| `evento` | Executa a operação `evento` disponibilizada por `coral.replay_reativo`. | `RegistroReplay` |
| `mudanca_mapa` | Registra uma mudança aplicada para reconstrução determinística posterior. | `RegistroReplay` |
| `avancar` | Avança o valor solicitado. | `RegistroReplay` |
| `como_json` | Representa o valor como JSON. | `str` |

:::details Detalhes técnicos

**Assinatura:** `GravadorReplay() -> None`

**Origem da implementação:** `coral.replay_reativo`

**Arquivo na release:** `coral/replay_reativo.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `registros` | propriedade | `registros() -> tuple[RegistroReplay, ...]` |
| `evento` | método | `evento(nome: str, *args: Any, origem: str \| None = None, **kwargs: Any) -> RegistroReplay` |
| `mudanca_mapa` | método | `mudanca_mapa(mudanca: Any) -> RegistroReplay` |
| `avancar` | método | `avancar(segundos: Any) -> RegistroReplay` |
| `como_json` | método | `como_json() -> str` |

:::

#### `ReplayReativo`

Representa ReplayReativo na API de `coral.replay_reativo`.

**Exemplo**

```coral
de coral.replay_reativo importe GravadorReplay, ReplayReativo

defina gravador como GravadorReplay()
mostre gravador
defina replay como ReplayReativo([])
mostre replay
```

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `registros` | Valor correspondente a registros. | `Iterable[RegistroReplay \| dict[str, Any]]` | obrigatório |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `reproduzir` | Reproduz o valor solicitado. | `tuple[ResultadoReplay, ...]` |

:::details Detalhes técnicos

**Assinatura:** `ReplayReativo(registros: Iterable[RegistroReplay \| dict[str, Any]]) -> None`

**Origem da implementação:** `coral.replay_reativo`

**Arquivo na release:** `coral/replay_reativo.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `reproduzir` | método | `reproduzir(motor: MotorRegras, relogio: RelogioSimulado, contexto: Any = None) -> tuple[ResultadoReplay, ...]` |

:::

<!-- /AUTO:API -->
