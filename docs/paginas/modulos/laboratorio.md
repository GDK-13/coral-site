# coral.laboratorio

## Visão geral

`coral.laboratorio` organiza experimentos reproduzíveis, repetições, varredura de parâmetros, métricas, medição de tempo e memória e exportação de resultados. Ele serve para estudar comportamento do programa sem fingir que uma única execução é uma conclusão universal.

<!-- AUTO:MODULO -->

**Importação:** `coral.laboratorio`  
**Categoria:** cientifico  

planejamento, execução, análise e recuperação de experimentos reproduzíveis

### Superfície pública detectada

`CONTRATO_RESULTADO_JSON`, `VERSAO_RESULTADO_JSON`, `Medicao`, `ResultadoExperimento`, `grade_parametros`, `planejar_experimento`, `selecionar_medicoes`, `resumir_por_parametro`, `validar_resultado`, `carregar_resultado_json`, `comparar_experimentos`, `executar_experimento`, `planejar_experimento_procedural`, `executar_experimento_procedural`, `diagnosticar_laboratorio`, `protocolo_medicao`

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

:::resultado
O experimento é configurado para cinco repetições com semente fixa e os resultados são salvos em JSON, CSV e Markdown nos caminhos indicados.
:::

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

#### `grade_parametros`

Gerar combinações de parâmetros.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `parametros` | Valor correspondente a parametros. | `Mapping[str, Iterable[Any]] \| None` | obrigatório |

**Retorno**

Retorna um valor declarado como `list[dict[str, Any]]`.

:::details Detalhes técnicos

**Assinatura:** `grade_parametros(parametros: Mapping[str, Iterable[Any]] \| None) -> list[dict[str, Any]]`

**Origem da implementação:** `coral.laboratorio`

**Arquivo na release:** `coral/laboratorio.py`

**Exceções diretamente observáveis no corpo:** `ValueError`

:::

#### `planejar_experimento`

Calcula o tamanho de uma execução experimental sem materializar a grade completa.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `parametros` | Valor correspondente a parametros. | `Mapping[str, Iterable[Any]] \| None` | obrigatório |
| `repeticoes` | Valor correspondente a repeticoes. | `int` | `1` |
| `limite` | Valor correspondente a limite. | `int \| None` | `None` |

**Retorno**

Retorna um valor declarado como `dict[str, Any]`.

:::details Detalhes técnicos

**Assinatura:** `planejar_experimento(parametros: Mapping[str, Iterable[Any]] \| None, repeticoes: int = 1, limite: int \| None = None) -> dict[str, Any]`

**Origem da implementação:** `coral.laboratorio`

**Arquivo na release:** `coral/laboratorio.py`

**Exceções diretamente observáveis no corpo:** `ValueError`

:::

#### `selecionar_medicoes`

Seleciona medições preservando ordem e sem modificar o resultado original.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `resultado` | Valor correspondente a resultado. | `ResultadoExperimento` | obrigatório |
| `criterio` | Valor correspondente a criterio. | `Callable[[Medicao], bool] \| Mapping[str, Any]` | obrigatório |

**Retorno**

Retorna um valor declarado como `list[Medicao]`.

:::details Detalhes técnicos

**Assinatura:** `selecionar_medicoes(resultado: ResultadoExperimento, criterio: Callable[[Medicao], bool] \| Mapping[str, Any]) -> list[Medicao]`

**Origem da implementação:** `coral.laboratorio`

**Arquivo na release:** `coral/laboratorio.py`

**Exceções diretamente observáveis no corpo:** `TypeError`, `ValueError`

:::

#### `resumir_por_parametro`

Agrupa medições pelo valor de um parâmetro, preservando a ordem de aparição.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `resultado` | Valor correspondente a resultado. | `ResultadoExperimento` | obrigatório |
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | obrigatório |

**Retorno**

Retorna um valor declarado como `dict[str, Any]`.

:::details Detalhes técnicos

**Assinatura:** `resumir_por_parametro(resultado: ResultadoExperimento, nome: str) -> dict[str, Any]`

**Origem da implementação:** `coral.laboratorio`

**Arquivo na release:** `coral/laboratorio.py`

**Exceções diretamente observáveis no corpo:** `TypeError`, `ValueError`

:::

#### `validar_resultado`

Valida a estrutura e a portabilidade de um resultado sem modificá lo.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `resultado` | Valor correspondente a resultado. | `Any` | obrigatório |

**Retorno**

Retorna um valor declarado como `dict[str, Any]`.

:::details Detalhes técnicos

**Assinatura:** `validar_resultado(resultado: Any) -> dict[str, Any]`

**Origem da implementação:** `coral.laboratorio`

**Arquivo na release:** `coral/laboratorio.py`

:::

#### `carregar_resultado_json`

Carrega relatório JSON do laboratório e recusa contratos ou esquemas desconhecidos.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `caminho` | Caminho do arquivo ou diretório usado pela operação. | `str \| Path` | obrigatório |

**Retorno**

Retorna um valor declarado como `ResultadoExperimento`.

:::details Detalhes técnicos

**Assinatura:** `carregar_resultado_json(caminho: str \| Path) -> ResultadoExperimento`

**Origem da implementação:** `coral.laboratorio`

**Arquivo na release:** `coral/laboratorio.py`

**Exceções diretamente observáveis no corpo:** `ValueError`

:::

#### `comparar_experimentos`

Compara dois experimentos de forma estritamente descritiva.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `a` | Valor correspondente a a. | `ResultadoExperimento` | obrigatório |
| `b` | Valor correspondente a b. | `ResultadoExperimento` | obrigatório |

**Retorno**

Retorna um valor declarado como `dict[str, Any]`.

:::details Detalhes técnicos

**Assinatura:** `comparar_experimentos(a: ResultadoExperimento, b: ResultadoExperimento) -> dict[str, Any]`

**Origem da implementação:** `coral.laboratorio`

**Arquivo na release:** `coral/laboratorio.py`

**Exceções diretamente observáveis no corpo:** `TypeError`, `ValueError`

:::

#### `executar_experimento`

Executar e medir.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | obrigatório |
| `funcao` | Função fornecida para executar a operação. | `Callable[..., Any]` | obrigatório |
| `repeticoes` | Valor correspondente a repeticoes. | `int` | `1` |
| `parametros` | Valor correspondente a parametros. | `Mapping[str, Iterable[Any]] \| None` | `None` |
| `semente` | Semente usada para tornar a sequência reproduzível. | `int \| None` | `None` |
| `metricas` | Valor correspondente a metricas. | `Callable[[Any], Mapping[str, Any]] \| None` | `None` |
| `continuar_em_erro` | Valor correspondente a continuar em erro. | `bool` | `True` |
| `relogio` | Relógio usado para controlar tempo ou atualização. | `FonteTempo \| None` | `None` |

**Retorno**

Retorna um valor declarado como `ResultadoExperimento`.

:::details Detalhes técnicos

**Assinatura:** `executar_experimento(nome: str, funcao: Callable[..., Any], *, repeticoes: int = 1, parametros: Mapping[str, Iterable[Any]] \| None = None, semente: int \| None = None, metricas: Callable[[Any], Mapping[str, Any]] \| None = None, continuar_em_erro: bool = True, relogio: FonteTempo \| None = None) -> ResultadoExperimento`

**Origem da implementação:** `coral.laboratorio`

**Arquivo na release:** `coral/laboratorio.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `nome` | posicional |
| `funcao` | posicional |
| `repeticoes` | nomeado |
| `parametros` | nomeado |
| `semente` | nomeado |
| `metricas` | nomeado |
| `continuar_em_erro` | nomeado |
| `relogio` | nomeado |

**Exceções diretamente observáveis no corpo:** `ValueError`, `propagar`

:::

#### `planejar_experimento_procedural`

Planeja um estudo procedural sem reconstruir nem executar a receita.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `receita` | Valor correspondente a receita. | `Any` | obrigatório |
| `sementes` | Valor correspondente a sementes. | `Iterable[Any] \| None` | `None` |
| `parametros` | Valor correspondente a parametros. | `Mapping[str, Iterable[Any]] \| None` | `None` |
| `repeticoes` | Valor correspondente a repeticoes. | `int` | `1` |
| `limite_execucoes` | Valor correspondente a limite execucoes. | `int \| None` | `None` |
| `limite_custo_total` | Valor correspondente a limite custo total. | `int \| None` | `None` |

**Retorno**

Retorna um valor declarado como `dict[str, Any]`.

:::details Detalhes técnicos

**Assinatura:** `planejar_experimento_procedural(receita: Any, *, sementes: Iterable[Any] \| None = None, parametros: Mapping[str, Iterable[Any]] \| None = None, repeticoes: int = 1, limite_execucoes: int \| None = None, limite_custo_total: int \| None = None) -> dict[str, Any]`

**Origem da implementação:** `coral.laboratorio`

**Arquivo na release:** `coral/laboratorio.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `receita` | posicional |
| `sementes` | nomeado |
| `parametros` | nomeado |
| `repeticoes` | nomeado |
| `limite_execucoes` | nomeado |
| `limite_custo_total` | nomeado |

**Exceções diretamente observáveis no corpo:** `ValueError`

:::

#### `executar_experimento_procedural`

Executa uma receita procedural como fator explícito de um experimento.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | obrigatório |
| `receita` | Valor correspondente a receita. | `Any` | obrigatório |
| `funcao` | Função fornecida para executar a operação. | `Callable[..., Any]` | obrigatório |
| `sementes` | Valor correspondente a sementes. | `Iterable[Any] \| None` | `None` |
| `parametros` | Valor correspondente a parametros. | `Mapping[str, Iterable[Any]] \| None` | `None` |
| `repeticoes` | Valor correspondente a repeticoes. | `int` | `1` |
| `semente_laboratorio` | Valor correspondente a semente laboratorio. | `int \| None` | `None` |
| `metricas` | Valor correspondente a metricas. | `Callable[[Any], Mapping[str, Any]] \| None` | `None` |
| `continuar_em_erro` | Valor correspondente a continuar em erro. | `bool` | `True` |
| `relogio` | Relógio usado para controlar tempo ou atualização. | `FonteTempo \| None` | `None` |
| `limite_custo_receita` | Valor correspondente a limite custo receita. | `int` | `1000000` |
| `limite_execucoes` | Valor correspondente a limite execucoes. | `int \| None` | `None` |
| `limite_custo_total` | Valor correspondente a limite custo total. | `int \| None` | `None` |

**Retorno**

Retorna um valor declarado como `ResultadoExperimento`.

:::details Detalhes técnicos

**Assinatura:** `executar_experimento_procedural(nome: str, receita: Any, funcao: Callable[..., Any], *, sementes: Iterable[Any] \| None = None, parametros: Mapping[str, Iterable[Any]] \| None = None, repeticoes: int = 1, semente_laboratorio: int \| None = None, metricas: Callable[[Any], Mapping[str, Any]] \| None = None, continuar_em_erro: bool = True, relogio: FonteTempo \| None = None, limite_custo_receita: int = 1000000, limite_execucoes: int \| None = None, limite_custo_total: int \| None = None) -> ResultadoExperimento`

**Origem da implementação:** `coral.laboratorio`

**Arquivo na release:** `coral/laboratorio.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `nome` | posicional |
| `receita` | posicional |
| `funcao` | posicional |
| `sementes` | nomeado |
| `parametros` | nomeado |
| `repeticoes` | nomeado |
| `semente_laboratorio` | nomeado |
| `metricas` | nomeado |
| `continuar_em_erro` | nomeado |
| `relogio` | nomeado |
| `limite_custo_receita` | nomeado |
| `limite_execucoes` | nomeado |
| `limite_custo_total` | nomeado |

**Exceções diretamente observáveis no corpo:** `TypeError`, `ValueError`

:::

#### `diagnosticar_laboratorio`

Diagnosticar capacidade.

**Retorno**

Retorna um valor declarado como `dict[str, Any]`.

:::details Detalhes técnicos

**Assinatura:** `diagnosticar_laboratorio() -> dict[str, Any]`

**Origem da implementação:** `coral.laboratorio`

**Arquivo na release:** `coral/laboratorio.py`

:::

#### `protocolo_medicao`

Descreve o protocolo usado pelo runtime sem prometer estabilidade de benchmark.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `relogio` | Relógio usado para controlar tempo ou atualização. | `FonteTempo \| None` | `None` |

**Retorno**

Retorna um valor declarado como `dict[str, Any]`.

:::details Detalhes técnicos

**Assinatura:** `protocolo_medicao(relogio: FonteTempo \| None = None) -> dict[str, Any]`

**Origem da implementação:** `coral.laboratorio`

**Arquivo na release:** `coral/laboratorio.py`

:::

### Classes e protocolos

#### `Medicao`

Representa registro de uma repetição.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `repeticao` | Valor correspondente a repeticao. | `int` | obrigatório |
| `parametros` | Valor correspondente a parametros. | `dict[str, Any]` | obrigatório |
| `semente` | Semente usada para tornar a sequência reproduzível. | `int \| None` | obrigatório |
| `tempo_segundos` | Valor correspondente a tempo segundos. | `float` | obrigatório |
| `memoria_atual_bytes` | Valor correspondente a memoria atual bytes. | `int` | obrigatório |
| `memoria_pico_bytes` | Valor correspondente a memoria pico bytes. | `int` | obrigatório |
| `retorno` | Valor correspondente a retorno. | `Any` | `None` |
| `erro` | Valor correspondente a erro. | `str \| None` | `None` |
| `metricas` | Valor correspondente a metricas. | `dict[str, Any]` | `field(default_factory=dict)` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `repeticao` | Valor correspondente a repeticao. | `int` | obrigatório |
| `parametros` | Valor correspondente a parametros. | `dict[str, Any]` | obrigatório |
| `semente` | Semente usada para tornar a sequência reproduzível. | `int \| None` | obrigatório |
| `tempo_segundos` | Valor correspondente a tempo segundos. | `float` | obrigatório |
| `memoria_atual_bytes` | Valor correspondente a memoria atual bytes. | `int` | obrigatório |
| `memoria_pico_bytes` | Valor correspondente a memoria pico bytes. | `int` | obrigatório |
| `retorno` | Valor correspondente a retorno. | `Any` | `None` |
| `erro` | Valor correspondente a erro. | `str \| None` | `None` |
| `metricas` | Valor correspondente a metricas. | `dict[str, Any]` | `field(default_factory=dict)` |

:::details Detalhes técnicos

**Assinatura:** `Medicao(repeticao: int, parametros: dict[str, Any], semente: int \| None, tempo_segundos: float, memoria_atual_bytes: int, memoria_pico_bytes: int, retorno: Any = None, erro: str \| None = None, metricas: dict[str, Any] = field(default_factory=dict))`

**Origem da implementação:** `coral.laboratorio`

**Arquivo na release:** `coral/laboratorio.py`

:::

#### `ResultadoExperimento`

Representa agregado do experimento.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | obrigatório |
| `medicoes` | Valor correspondente a medicoes. | `list[Medicao]` | obrigatório |
| `metadados` | Valor correspondente a metadados. | `dict[str, Any]` | obrigatório |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | obrigatório |
| `medicoes` | Valor correspondente a medicoes. | `list[Medicao]` | obrigatório |
| `metadados` | Valor correspondente a metadados. | `dict[str, Any]` | obrigatório |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `passou` | Executa a operação `passou` disponibilizada por `coral.laboratorio`. | `bool` |
| `adicionar_metadados` | Adiciona metadados. | `None` |
| `retornos` | Obtém retornos. | `list[Any]` |
| `resumo` | Executa a operação `resumo` disponibilizada por `coral.laboratorio`. | `dict[str, Any]` |
| `para_dict` | Converte o valor para dict. | `dict[str, Any]` |
| `resultado_operacao` | Executa a operação `resultado_operacao` disponibilizada por `coral.laboratorio`. | `ResultadoOperacao` |
| `salvar_json` | Salva JSON. | `Path` |
| `salvar_csv` | Salva csv. | `Path` |
| `salvar` | Salva o valor solicitado. | `Path` |
| `salvar_markdown` | Salva markdown. | `Path` |

:::details Detalhes técnicos

**Assinatura:** `ResultadoExperimento(nome: str, medicoes: list[Medicao], metadados: dict[str, Any])`

**Origem da implementação:** `coral.laboratorio`

**Arquivo na release:** `coral/laboratorio.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `passou` | propriedade | `passou() -> bool` |
| `adicionar_metadados` | método | `adicionar_metadados(nome: str, valor: Any) -> None` |
| `retornos` | método | `retornos(*, incluir_falhas: bool = False) -> list[Any]` |
| `resumo` | método | `resumo() -> dict[str, Any]` |
| `para_dict` | método | `para_dict() -> dict[str, Any]` |
| `resultado_operacao` | método | `resultado_operacao() -> ResultadoOperacao` |
| `salvar_json` | método | `salvar_json(caminho: str \| Path) -> Path` |
| `salvar_csv` | método | `salvar_csv(caminho: str \| Path) -> Path` |
| `salvar` | método | `salvar(caminho: str \| Path) -> Path` |
| `salvar_markdown` | método | `salvar_markdown(caminho: str \| Path) -> Path` |

:::

### Constantes e aliases

#### `CONTRATO_RESULTADO_JSON`

Expõe a constante pública `CONTRATO_RESULTADO_JSON`.

:::details Detalhes técnicos

**Assinatura:** `CONTRATO_RESULTADO_JSON`

**Origem da implementação:** `coral.laboratorio`

**Arquivo na release:** `coral/laboratorio.py`

**Valor declarado:** `'coral.laboratorio.resultado/1'`

:::

#### `VERSAO_RESULTADO_JSON`

Expõe a constante pública `VERSAO_RESULTADO_JSON`.

:::details Detalhes técnicos

**Assinatura:** `VERSAO_RESULTADO_JSON`

**Origem da implementação:** `coral.laboratorio`

**Arquivo na release:** `coral/laboratorio.py`

**Valor declarado:** `1`

:::

<!-- /AUTO:API -->

## Compatibilidade

O protocolo é portátil, mas medidas de desempenho são dependentes do ambiente. A API documenta o que o runtime mede; ela não garante equivalência de benchmark entre hosts diferentes.
