# coral.laboratorio

## Visão geral

`coral.laboratorio` organiza experimentos reproduzíveis, repetições, varredura de parâmetros, métricas, medição de tempo e memória e exportação de resultados. Ele serve para estudar comportamento do programa sem fingir que uma única execução é uma conclusão universal.

<!-- AUTO:MODULO -->

**Importação:** `coral.laboratorio`  
**Categoria:** cientifico  

experimentos reproduzíveis, medições e grades de parâmetros

### Superfície pública detectada

`Medicao`, `ResultadoExperimento`, `grade_parametros`, `executar_experimento`, `diagnosticar_laboratorio`, `protocolo_medicao`

<!-- /AUTO:MODULO -->

## Papel no ecossistema

O laboratório coordena a execução; ele não substitui a análise. Uma estrutura comum é medir com `coral.laboratorio`, persistir os relatórios e analisar depois com `coral.numerico`.

## Conceitos principais

### Experimento

`executar_experimento` recebe um nome, uma função e parâmetros de execução. Cada repetição gera uma `Medicao` com parâmetros, semente, duração, memória, retorno, erro e métricas adicionais.

### Grade de parâmetros

`grade_parametros` produz combinações de parâmetros para uma varredura sistemática. Isso ajuda a deixar explícito o espaço de experimentação em vez de esconder variações dentro da função medida.

### Resultado

`ResultadoExperimento` reúne medições e metadados. Ele pode resumir o experimento e salvar JSON, CSV ou Markdown.

### Protocolo de medição

`protocolo_medicao()` descreve o protocolo usado pelo runtime. A própria API evita prometer que uma medição local é um benchmark universal.

## Quando usar

Use para comparar algoritmos, testar impacto de parâmetros, registrar resultados repetíveis e produzir artefatos de análise. Não use o laboratório como substituto de testes funcionais: primeiro prove correção, depois meça desempenho.

## Começando

A release inclui uma vitrine completa em `Exemplos/Projetos_Completos/Vitrine/laboratorio_algoritmos/`. O trecho abaixo usa a sintaxe de experimento da linguagem:

```coral
experimento "inserção / aleatórios" como insercao_aleatorios repetindo 5 vezes usando a semente 20260909
    retorne ordenacao_insercao(dados_aleatorios)
fim

salve o experimento insercao_aleatorios em "resultados/insercao_aleatorios.json"
salve o experimento insercao_aleatorios em "resultados/insercao_aleatorios.csv"
salve o experimento insercao_aleatorios em "resultados/insercao_aleatorios.md"
```

## API essencial

| Entrada | Papel | Assinatura |
|---|---|---|
| `Medicao` | registro de uma repetição | `Medicao(repeticao: int, parametros: dict[str, Any], semente: int \| None, tempo_segundos: float, memoria_atual_bytes: int, memoria_pico_bytes: int, retorno: Any = None, erro: str \| None = None, metricas: dict[str, Any] = field(default_factory=dict))` |
| `ResultadoExperimento` | agregado do experimento | `ResultadoExperimento(nome: str, medicoes: list[Medicao], metadados: dict[str, Any])` |
| `grade_parametros` | gerar combinações de parâmetros | `grade_parametros(parametros: Mapping[str, Iterable[Any]] \| None) -> list[dict[str, Any]]` |
| `executar_experimento` | executar e medir | `executar_experimento(nome: str, funcao: Callable[..., Any], *, repeticoes: int = 1, parametros: Mapping[str, Iterable[Any]] \| None = None, semente: int \| None = None, metricas: Callable[[Any], Mapping[str, Any]] \| None = None, continuar_em_erro: bool = True, relogio: FonteTempo \| None = None) -> ResultadoExperimento` |
| `diagnosticar_laboratorio` | diagnosticar capacidade | `diagnosticar_laboratorio() -> dict[str, Any]` |
| `protocolo_medicao` | descrever protocolo | `protocolo_medicao(relogio: FonteTempo \| None = None) -> dict[str, Any]` |

## Fluxo recomendado

1. Valide a correção lógica do algoritmo fora do experimento.
2. Defina entradas e sementes de referência.
3. Defina o que muda entre execuções.
4. Execute repetições suficientes para o objetivo local.
5. Salve metadados e ambiente.
6. Faça a análise estatística em uma etapa separada.

## Métricas personalizadas

O parâmetro `metricas` de `executar_experimento` pode derivar métricas a partir do retorno. Use isso para medidas de domínio que não são simplesmente tempo e memória.

## Erros e casos de borda

Quando `continuar_em_erro` está habilitado, uma repetição com falha pode ser registrada em vez de encerrar toda a campanha. Isso é útil para estudar fronteiras de parâmetros, mas não transforma uma falha em sucesso: consulte `ResultadoExperimento.passou()` e as medições.

Resultados de tempo variam com máquina, carga, sistema operacional, temperatura e outras condições. Preserve contexto suficiente para que o leitor saiba o que foi realmente medido.

## Boas práticas

* Fixe sementes quando houver aleatoriedade.
* Separe aquecimento, preparação de dados e trecho que realmente deseja medir.
* Não compare tempos de máquinas diferentes como se fossem equivalentes sem metodologia.
* Salve o ambiente e os parâmetros junto dos resultados.
* Use `coral.numerico` para estatística posterior em vez de misturar análise com medição.

## Integração com outros módulos

`coral.numerico` analisa séries. `coral.sistema` registra ambiente. `coral.json` e `coral.persistencia` transportam relatórios. `coral.aleatorio` fornece sementes e fontes reproduzíveis.

## Referência da API

<!-- AUTO:API -->

### Funções

#### `grade_parametros(parametros: Mapping[str, Iterable[Any]] | None) -> list[dict[str, Any]]`

Entrada pública `grade_parametros` da superfície `coral.laboratorio`.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `parametros` | `Mapping[str, Iterable[Any]] \| None` | obrigatório | posicional |

**Retorno:** `list[dict[str, Any]]`

**Exceções observáveis no corpo:** `ValueError`

#### `executar_experimento(nome: str, funcao: Callable[..., Any], *, repeticoes: int = 1, parametros: Mapping[str, Iterable[Any]] | None = None, semente: int | None = None, metricas: Callable[[Any], Mapping[str, Any]] | None = None, continuar_em_erro: bool = True, relogio: FonteTempo | None = None) -> ResultadoExperimento`

Entrada pública `executar_experimento` da superfície `coral.laboratorio`.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `nome` | `str` | obrigatório | posicional |
| `funcao` | `Callable[..., Any]` | obrigatório | posicional |
| `repeticoes` | `int` | `1` | nomeado |
| `parametros` | `Mapping[str, Iterable[Any]] \| None` | `None` | nomeado |
| `semente` | `int \| None` | `None` | nomeado |
| `metricas` | `Callable[[Any], Mapping[str, Any]] \| None` | `None` | nomeado |
| `continuar_em_erro` | `bool` | `True` | nomeado |
| `relogio` | `FonteTempo \| None` | `None` | nomeado |

**Retorno:** `ResultadoExperimento`

**Exceções observáveis no corpo:** `ValueError`, `propagar`

#### `diagnosticar_laboratorio() -> dict[str, Any]`

Entrada pública `diagnosticar_laboratorio` da superfície `coral.laboratorio`.

**Retorno:** `dict[str, Any]`

#### `protocolo_medicao(relogio: FonteTempo | None = None) -> dict[str, Any]`

Descreve o protocolo usado pelo runtime sem prometer estabilidade de benchmark.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `relogio` | `FonteTempo \| None` | `None` | posicional |

**Retorno:** `dict[str, Any]`

### Classes e protocolos

#### `Medicao(repeticao: int, parametros: dict[str, Any], semente: int | None, tempo_segundos: float, memoria_atual_bytes: int, memoria_pico_bytes: int, retorno: Any = None, erro: str | None = None, metricas: dict[str, Any] = field(default_factory=dict))`

Entrada pública `Medicao` da superfície `coral.laboratorio`.

**Atributos declarados**

| Nome | Tipo | Padrão |
|---|---|---|
| `repeticao` | `int` | obrigatório |
| `parametros` | `dict[str, Any]` | obrigatório |
| `semente` | `int \| None` | obrigatório |
| `tempo_segundos` | `float` | obrigatório |
| `memoria_atual_bytes` | `int` | obrigatório |
| `memoria_pico_bytes` | `int` | obrigatório |
| `retorno` | `Any` | `None` |
| `erro` | `str \| None` | `None` |
| `metricas` | `dict[str, Any]` | `field(default_factory=dict)` |

#### `ResultadoExperimento(nome: str, medicoes: list[Medicao], metadados: dict[str, Any])`

Entrada pública `ResultadoExperimento` da superfície `coral.laboratorio`.

**Atributos declarados**

| Nome | Tipo | Padrão |
|---|---|---|
| `nome` | `str` | obrigatório |
| `medicoes` | `list[Medicao]` | obrigatório |
| `metadados` | `dict[str, Any]` | obrigatório |

**Métodos e propriedades públicas**

| Nome | Tipo | Assinatura | Retorno | Descrição |
|---|---|---|---|---|
| `passou` | propriedade | `passou() -> bool` | `bool` | Sem docstring própria na release. |
| `adicionar_metadados` | método | `adicionar_metadados(nome: str, valor: Any) -> None` | `None` | Sem docstring própria na release. |
| `retornos` | método | `retornos(*, incluir_falhas: bool = False) -> list[Any]` | `list[Any]` | Sem docstring própria na release. |
| `resumo` | método | `resumo() -> dict[str, Any]` | `dict[str, Any]` | Sem docstring própria na release. |
| `para_dict` | método | `para_dict() -> dict[str, Any]` | `dict[str, Any]` | Sem docstring própria na release. |
| `resultado_operacao` | método | `resultado_operacao() -> ResultadoOperacao` | `ResultadoOperacao` | Sem docstring própria na release. |
| `salvar_json` | método | `salvar_json(caminho: str \| Path) -> Path` | `Path` | Sem docstring própria na release. |
| `salvar_csv` | método | `salvar_csv(caminho: str \| Path) -> Path` | `Path` | Sem docstring própria na release. |
| `salvar` | método | `salvar(caminho: str \| Path) -> Path` | `Path` | Sem docstring própria na release. |
| `salvar_markdown` | método | `salvar_markdown(caminho: str \| Path) -> Path` | `Path` | Sem docstring própria na release. |

<!-- /AUTO:API -->

## Compatibilidade

O protocolo é portátil, mas medidas de desempenho são dependentes do ambiente. A API documenta o que o runtime mede; ela não garante equivalência de benchmark entre hosts diferentes.
