# coral.graficos

## Visão geral

`coral.graficos` cria especificações de visualização a partir de dados comuns da Coral. O módulo cobre gráficos 2D e 3D, estatística visual, painéis e saídas estáticas ou interativas sem obrigar o programa a abrir uma janela.

<!-- AUTO:MODULO -->

**Importação:** `coral.graficos`  
**Categoria:** cientifico  

gráficos científicos 2D e 3D, correlação, incerteza, painéis e exportação SVG, PNG, PDF e HTML interativo

### Superfície pública detectada

`ErroGrafico`, `Serie2D`, `Serie3D`, `Superficie3D`, `SerieCategorias`, `ResumoCaixa`, `SeriesRegistros`, `MatrizCores`, `SerieErro`, `FaixaIncerteza`, `PainelGraficos`, `Grafico`, `linha`, `dispersao`, `dispersao3d`, `trajetoria3d`, `superficie3d`, `barras`, `grafico_histograma`, `grafico_caixa`, `configurar`, `grafico_funcao`, `series_de_registros`, `mapa_calor`, `mapa_correlacao`, `barras_erro`, `faixa_incerteza`, `grafico_experimento`, `painel`, `para_svg`, `para_html`, `salvar_html`, `explorar`, `amostrar_grafico`, `salvar`

<!-- /AUTO:MODULO -->

## Quando usar

Use este módulo quando quiser transformar séries, categorias, matrizes, resultados estatísticos ou experimentos em uma representação visual. Para cálculos estatísticos, use `coral.numerico`; para planejar e registrar experimentos, use `coral.laboratorio`.

## Começando

```coral
de coral.graficos importe linha, configurar, para_svg

defina serie como linha([0, 1, 2, 3], [20.0, 20.8, 21.4, 21.9], nome="temperatura")
defina serie como configurar(serie, titulo="Temperatura", eixos=["tempo", "°C"])
defina svg como para_svg(serie)
mostre "SVG gerado em memória."
```

:::resultado
O gráfico é descrito e convertido para SVG sem abrir interface gráfica.
:::

## Saídas e dependências

`para_svg` usa o renderizador próprio 2D. Exportações como PNG e PDF podem carregar Matplotlib somente quando a saída é solicitada. HTML interativo usa a integração correspondente e continua sendo salvo como arquivo local.

Gráficos 3D preservam as coordenadas fornecidas. Superfícies exigem grade retangular explícita e não inventam pontos ausentes.

## Integração com Laboratório e Web

`grafico_experimento` adapta resultados experimentais sem tornar `coral.graficos` dependente da execução do experimento. `resposta_grafico`, em `coral.web.servidor`, transforma um gráfico em resposta HTML sem iniciar servidor por conta própria.

## Referência da API

<!-- AUTO:API -->

### Funções

#### `linha`

Cria uma série de linha 2D sem abrir interface gráfica.

**Exemplo**

```coral
de coral.graficos importe linha, configurar, para_svg

defina serie como linha([0, 1, 2, 3], [20.0, 20.8, 21.4, 21.9], nome="temperatura")
defina serie como configurar(serie, titulo="Temperatura", eixos=["tempo", "°C"])
defina svg como para_svg(serie)
mostre "SVG gerado em memória."
```

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `x` | Coordenada horizontal. | `Iterable[Any]` | obrigatório |
| `y` | Coordenada vertical. | `Iterable[Any]` | obrigatório |
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str \| None` | `None` |

**Retorno**

Retorna um valor declarado como `Grafico`.

:::details Detalhes técnicos

**Assinatura:** `linha(x: Iterable[Any], y: Iterable[Any], nome: str \| None = None) -> Grafico`

**Origem da implementação:** `coral.graficos`

**Arquivo na release:** `coral/graficos.py`

:::

#### `dispersao`

Cria uma série de pontos 2D sem conectar observações.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `x` | Coordenada horizontal. | `Iterable[Any]` | obrigatório |
| `y` | Coordenada vertical. | `Iterable[Any]` | obrigatório |
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str \| None` | `None` |

**Retorno**

Retorna um valor declarado como `Grafico`.

:::details Detalhes técnicos

**Assinatura:** `dispersao(x: Iterable[Any], y: Iterable[Any], nome: str \| None = None) -> Grafico`

**Origem da implementação:** `coral.graficos`

**Arquivo na release:** `coral/graficos.py`

:::

#### `dispersao3d`

Cria pontos 3D preservando exatamente as coordenadas fornecidas.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `x` | Coordenada horizontal. | `Iterable[Any]` | obrigatório |
| `y` | Coordenada vertical. | `Iterable[Any]` | obrigatório |
| `z` | Valor correspondente a z. | `Iterable[Any]` | obrigatório |
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str \| None` | `None` |

**Retorno**

Retorna um valor declarado como `Grafico`.

:::details Detalhes técnicos

**Assinatura:** `dispersao3d(x: Iterable[Any], y: Iterable[Any], z: Iterable[Any], nome: str \| None = None) -> Grafico`

**Origem da implementação:** `coral.graficos`

**Arquivo na release:** `coral/graficos.py`

:::

#### `trajetoria3d`

Cria uma trajetória 3D na ordem dada, sem reamostrar ou suavizar.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `x` | Coordenada horizontal. | `Iterable[Any]` | obrigatório |
| `y` | Coordenada vertical. | `Iterable[Any]` | obrigatório |
| `z` | Valor correspondente a z. | `Iterable[Any]` | obrigatório |
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str \| None` | `None` |

**Retorno**

Retorna um valor declarado como `Grafico`.

:::details Detalhes técnicos

**Assinatura:** `trajetoria3d(x: Iterable[Any], y: Iterable[Any], z: Iterable[Any], nome: str \| None = None) -> Grafico`

**Origem da implementação:** `coral.graficos`

**Arquivo na release:** `coral/graficos.py`

:::

#### `superficie3d`

Cria uma superfície 3D de grade retangular sem interpolação silenciosa.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `x` | Coordenada horizontal. | `Any` | obrigatório |
| `y` | Coordenada vertical. | `Any` | obrigatório |
| `z` | Valor correspondente a z. | `Any` | obrigatório |
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str \| None` | `None` |

**Retorno**

Retorna um valor declarado como `Grafico`.

:::details Detalhes técnicos

**Assinatura:** `superficie3d(x: Any, y: Any, z: Any, nome: str \| None = None) -> Grafico`

**Origem da implementação:** `coral.graficos`

**Arquivo na release:** `coral/graficos.py`

:::

#### `barras`

Cria barras categóricas; a escala vertical inclui zero por contrato.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `categorias` | Valor correspondente a categorias. | `Iterable[Any]` | obrigatório |
| `valores` | Coleção de valores processada. | `Iterable[Any]` | obrigatório |
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str \| None` | `None` |

**Retorno**

Retorna um valor declarado como `Grafico`.

:::details Detalhes técnicos

**Assinatura:** `barras(categorias: Iterable[Any], valores: Iterable[Any], nome: str \| None = None) -> Grafico`

**Origem da implementação:** `coral.graficos`

**Arquivo na release:** `coral/graficos.py`

**Exceções diretamente observáveis no corpo:** `ErroGrafico`

:::

#### `grafico_histograma`

Cria gráfico a partir do contrato canônico ``numerico.histograma``.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valores` | Coleção de valores processada. | `Iterable[Any]` | obrigatório |
| `faixas` | Valor correspondente a faixas. | `Any` | obrigatório |
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str \| None` | `None` |

**Retorno**

Retorna um valor declarado como `Grafico`.

:::details Detalhes técnicos

**Assinatura:** `grafico_histograma(valores: Iterable[Any], faixas: Any, nome: str \| None = None) -> Grafico`

**Origem da implementação:** `coral.graficos`

**Arquivo na release:** `coral/graficos.py`

**Exceções diretamente observáveis no corpo:** `ErroGrafico`

:::

#### `grafico_caixa`

Cria caixas de Tukey usando quartis do contrato ``coral.numerico``.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `grupos` | Valor correspondente a grupos. | `Any` | obrigatório |

**Retorno**

Retorna um valor declarado como `Grafico`.

:::details Detalhes técnicos

**Assinatura:** `grafico_caixa(grupos: Any) -> Grafico`

**Origem da implementação:** `coral.graficos`

**Arquivo na release:** `coral/graficos.py`

:::

#### `configurar`

Retorna cópia configurada sem alterar dados ou estatísticas do gráfico.

**Exemplo**

```coral
de coral.graficos importe linha, configurar, para_svg

defina serie como linha([0, 1, 2, 3], [20.0, 20.8, 21.4, 21.9], nome="temperatura")
defina serie como configurar(serie, titulo="Temperatura", eixos=["tempo", "°C"])
defina svg como para_svg(serie)
mostre "SVG gerado em memória."
```

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `grafico` | Valor correspondente a grafico. | `Grafico` | obrigatório |
| `titulo` | Valor correspondente a titulo. | `str \| None` | `None` |
| `eixos` | Valor correspondente a eixos. | `Any` | `None` |
| `unidades` | Valor correspondente a unidades. | `Any` | `None` |
| `legenda` | Valor correspondente a legenda. | `bool \| None` | `None` |
| `tema` | Valor correspondente a tema. | `str \| None` | `None` |
| `proveniencia` | Valor correspondente a proveniencia. | `Iterable[Any] \| None` | `None` |
| `texto_alternativo` | Valor correspondente a texto alternativo. | `str \| None` | `None` |

**Retorno**

Retorna um valor declarado como `Grafico`.

:::details Detalhes técnicos

**Assinatura:** `configurar(grafico: Grafico, titulo: str \| None = None, eixos: Any = None, unidades: Any = None, legenda: bool \| None = None, tema: str \| None = None, *, proveniencia: Iterable[Any] \| None = None, texto_alternativo: str \| None = None) -> Grafico`

**Origem da implementação:** `coral.graficos`

**Arquivo na release:** `coral/graficos.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `grafico` | posicional |
| `titulo` | posicional |
| `eixos` | posicional |
| `unidades` | posicional |
| `legenda` | posicional |
| `tema` | posicional |
| `proveniencia` | nomeado |
| `texto_alternativo` | nomeado |

**Exceções diretamente observáveis no corpo:** `ErroGrafico`

:::

#### `grafico_funcao`

Amostra função escalar em intervalo fechado, preservando falhas como lacunas.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `funcao` | Função fornecida para executar a operação. | `Callable[[float], Any]` | obrigatório |
| `inicio` | Valor inicial do intervalo ou processo. | `Any` | obrigatório |
| `fim` | Valor final do intervalo ou processo. | `Any` | obrigatório |
| `amostras` | Valor correspondente a amostras. | `int` | `200` |

**Retorno**

Retorna um valor declarado como `Grafico`.

:::details Detalhes técnicos

**Assinatura:** `grafico_funcao(funcao: Callable[[float], Any], inicio: Any, fim: Any, amostras: int = 200) -> Grafico`

**Origem da implementação:** `coral.graficos`

**Arquivo na release:** `coral/graficos.py`

**Exceções diretamente observáveis no corpo:** `ErroGrafico`

:::

#### `series_de_registros`

Extrai dois campos numéricos alinhados de registros comuns.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `registros` | Valor correspondente a registros. | `Iterable[Any]` | obrigatório |
| `campo_x` | Valor correspondente a campo x. | `str` | obrigatório |
| `campo_y` | Valor correspondente a campo y. | `str` | obrigatório |

**Retorno**

Retorna um valor declarado como `SeriesRegistros`.

:::details Detalhes técnicos

**Assinatura:** `series_de_registros(registros: Iterable[Any], campo_x: str, campo_y: str) -> SeriesRegistros`

**Origem da implementação:** `coral.graficos`

**Arquivo na release:** `coral/graficos.py`

**Exceções diretamente observáveis no corpo:** `ErroGrafico`

:::

#### `mapa_calor`

Representa uma matriz numérica por intensidade de cor, sem recalcular dados.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `matriz` | Valor correspondente a matriz. | `Any` | obrigatório |
| `rotulos_linhas` | Valor correspondente a rotulos linhas. | `Iterable[Any] \| None` | `None` |
| `rotulos_colunas` | Valor correspondente a rotulos colunas. | `Iterable[Any] \| None` | `None` |
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str \| None` | `None` |

**Retorno**

Retorna um valor declarado como `Grafico`.

:::details Detalhes técnicos

**Assinatura:** `mapa_calor(matriz: Any, rotulos_linhas: Iterable[Any] \| None = None, rotulos_colunas: Iterable[Any] \| None = None, nome: str \| None = None) -> Grafico`

**Origem da implementação:** `coral.graficos`

**Arquivo na release:** `coral/graficos.py`

:::

#### `mapa_correlacao`

Calcula Pearson em ``coral.numerico`` e representa a matriz resultante.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `dados` | Dados processados pela operação. | `Any` | obrigatório |
| `rotulos` | Valor correspondente a rotulos. | `Iterable[Any] \| None` | `None` |
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str \| None` | `None` |

**Retorno**

Retorna um valor declarado como `Grafico`.

:::details Detalhes técnicos

**Assinatura:** `mapa_correlacao(dados: Any, rotulos: Iterable[Any] \| None = None, nome: str \| None = None) -> Grafico`

**Origem da implementação:** `coral.graficos`

**Arquivo na release:** `coral/graficos.py`

**Exceções diretamente observáveis no corpo:** `ErroGrafico`

:::

#### `barras_erro`

Cria pontos com barras de erro simétricas ou assimétricas explicitamente fornecidas.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `x` | Coordenada horizontal. | `Iterable[Any]` | obrigatório |
| `y` | Coordenada vertical. | `Iterable[Any]` | obrigatório |
| `erros` | Valor correspondente a erros. | `Iterable[Any]` | obrigatório |
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str \| None` | `None` |

**Retorno**

Retorna um valor declarado como `Grafico`.

:::details Detalhes técnicos

**Assinatura:** `barras_erro(x: Iterable[Any], y: Iterable[Any], erros: Iterable[Any], nome: str \| None = None) -> Grafico`

**Origem da implementação:** `coral.graficos`

**Arquivo na release:** `coral/graficos.py`

:::

#### `faixa_incerteza`

Cria faixa de limites absolutos sem atribuir significado estatístico à faixa.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `x` | Coordenada horizontal. | `Iterable[Any]` | obrigatório |
| `centro` | Valor correspondente a centro. | `Iterable[Any]` | obrigatório |
| `inferior` | Valor correspondente a inferior. | `Iterable[Any]` | obrigatório |
| `superior` | Valor correspondente a superior. | `Iterable[Any]` | obrigatório |
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str \| None` | `None` |

**Retorno**

Retorna um valor declarado como `Grafico`.

:::details Detalhes técnicos

**Assinatura:** `faixa_incerteza(x: Iterable[Any], centro: Iterable[Any], inferior: Iterable[Any], superior: Iterable[Any], nome: str \| None = None) -> Grafico`

**Origem da implementação:** `coral.graficos`

**Arquivo na release:** `coral/graficos.py`

**Exceções diretamente observáveis no corpo:** `ErroGrafico`

:::

#### `grafico_experimento`

Adapta medições bem sucedidas a uma série comum sem dependência no import do módulo.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `resultado` | Valor correspondente a resultado. | `Any` | obrigatório |
| `eixo_x` | Valor correspondente a eixo x. | `str` | obrigatório |
| `metrica` | Valor correspondente a metrica. | `str` | obrigatório |

**Retorno**

Retorna um valor declarado como `Grafico`.

:::details Detalhes técnicos

**Assinatura:** `grafico_experimento(resultado: Any, eixo_x: str, metrica: str) -> Grafico`

**Origem da implementação:** `coral.graficos`

**Arquivo na release:** `coral/graficos.py`

**Exceções diretamente observáveis no corpo:** `ErroGrafico`

:::

#### `painel`

Combina gráficos em grade sem modificar suas escalas ou especificações.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `graficos` | Valor correspondente a graficos. | `Iterable[Grafico]` | obrigatório |
| `colunas` | Valor correspondente a colunas. | `int` | `2` |
| `titulo` | Valor correspondente a titulo. | `str` | `''` |

**Retorno**

Retorna um valor declarado como `PainelGraficos`.

:::details Detalhes técnicos

**Assinatura:** `painel(graficos: Iterable[Grafico], colunas: int = 2, titulo: str = '') -> PainelGraficos`

**Origem da implementação:** `coral.graficos`

**Arquivo na release:** `coral/graficos.py`

**Exceções diretamente observáveis no corpo:** `ErroGrafico`

:::

#### `para_svg`

Renderiza gráficos 2D como SVG autossuficiente em memória.

**Exemplo**

```coral
de coral.graficos importe linha, configurar, para_svg

defina serie como linha([0, 1, 2, 3], [20.0, 20.8, 21.4, 21.9], nome="temperatura")
defina serie como configurar(serie, titulo="Temperatura", eixos=["tempo", "°C"])
defina svg como para_svg(serie)
mostre "SVG gerado em memória."
```

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `grafico` | Valor correspondente a grafico. | `Grafico \| PainelGraficos` | obrigatório |
| `largura` | Largura usada pela operação. | `int` | `800` |
| `altura` | Altura usada pela operação. | `int` | `500` |

**Retorno**

Retorna um valor declarado como `str`.

:::details Detalhes técnicos

**Assinatura:** `para_svg(grafico: Grafico \| PainelGraficos, *, largura: int = 800, altura: int = 500) -> str`

**Origem da implementação:** `coral.graficos`

**Arquivo na release:** `coral/graficos.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `grafico` | posicional |
| `largura` | nomeado |
| `altura` | nomeado |

**Exceções diretamente observáveis no corpo:** `ErroGrafico`

:::

#### `para_html`

Gera documento HTML interativo autossuficiente, sem abrir rede ou janela.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `grafico` | Valor correspondente a grafico. | `Any` | obrigatório |
| `limite_pontos` | Valor correspondente a limite pontos. | `int` | `LIMITE_PONTOS_HTML_PADRAO` |

**Retorno**

Retorna um valor declarado como `str`.

:::details Detalhes técnicos

**Assinatura:** `para_html(grafico: Any, *, limite_pontos: int = LIMITE_PONTOS_HTML_PADRAO) -> str`

**Origem da implementação:** `coral._graficos_interativos`

**Arquivo na release:** `coral/_graficos_interativos.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `grafico` | posicional |
| `limite_pontos` | nomeado |

**Exceções diretamente observáveis no corpo:** `ErroGrafico`

:::

#### `salvar_html`

Salva HTML interativo autossuficiente usando Plotly somente nesta chamada.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `grafico` | Valor correspondente a grafico. | `Any` | obrigatório |
| `caminho` | Caminho do arquivo ou diretório usado pela operação. | `str \| Path` | obrigatório |
| `limite_pontos` | Valor correspondente a limite pontos. | `int` | `LIMITE_PONTOS_HTML_PADRAO` |

**Retorno**

Retorna um valor declarado como `Path`.

:::details Detalhes técnicos

**Assinatura:** `salvar_html(grafico: Any, caminho: str \| Path, *, limite_pontos: int = LIMITE_PONTOS_HTML_PADRAO) -> Path`

**Origem da implementação:** `coral._graficos_interativos`

**Arquivo na release:** `coral/_graficos_interativos.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `grafico` | posicional |
| `caminho` | posicional |
| `limite_pontos` | nomeado |

**Exceções diretamente observáveis no corpo:** `ErroGrafico`

:::

#### `explorar`

Abre uma prévia local apenas quando solicitada explicitamente.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `grafico` | Valor correspondente a grafico. | `Any` | obrigatório |
| `limite_pontos` | Valor correspondente a limite pontos. | `int` | `LIMITE_PONTOS_HTML_PADRAO` |

**Retorno**

Retorna um valor declarado como `Path`.

:::details Detalhes técnicos

**Assinatura:** `explorar(grafico: Any, *, limite_pontos: int = LIMITE_PONTOS_HTML_PADRAO) -> Path`

**Origem da implementação:** `coral._graficos_interativos`

**Arquivo na release:** `coral/_graficos_interativos.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `grafico` | posicional |
| `limite_pontos` | nomeado |

**Exceções diretamente observáveis no corpo:** `ErroGrafico`

:::

#### `amostrar_grafico`

Reduz explicitamente séries simples, registrando a amostragem na especificação.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `grafico` | Valor correspondente a grafico. | `Any` | obrigatório |
| `max_pontos` | Valor correspondente a max pontos. | `int` | obrigatório |

**Retorno**

Retorna um valor declarado como `Any`.

:::details Detalhes técnicos

**Assinatura:** `amostrar_grafico(grafico: Any, max_pontos: int) -> Any`

**Origem da implementação:** `coral._graficos_interativos`

**Arquivo na release:** `coral/_graficos_interativos.py`

**Exceções diretamente observáveis no corpo:** `ErroGrafico`

:::

#### `salvar`

Salva 2D em SVG pelo núcleo; 3D e PNG/PDF usam Matplotlib sob demanda.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `grafico` | Valor correspondente a grafico. | `Grafico \| PainelGraficos` | obrigatório |
| `caminho` | Caminho do arquivo ou diretório usado pela operação. | `str \| Path` | obrigatório |

**Retorno**

Retorna um valor declarado como `Path`.

:::details Detalhes técnicos

**Assinatura:** `salvar(grafico: Grafico \| PainelGraficos, caminho: str \| Path) -> Path`

**Origem da implementação:** `coral.graficos`

**Arquivo na release:** `coral/graficos.py`

**Exceções diretamente observáveis no corpo:** `ErroGrafico`

:::

### Classes e protocolos

#### `Serie2D`

Série cartesiana usada por linhas, dispersão e funções.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `estilo` | Valor correspondente a estilo. | `str` | obrigatório |
| `x` | Coordenada horizontal. | `tuple[float, ...]` | obrigatório |
| `y` | Coordenada vertical. | `tuple[float \| None, ...]` | obrigatório |
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str \| None` | `None` |
| `origem` | Origem usada pela operação. | `str` | `'direta'` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `estilo` | Valor correspondente a estilo. | `str` | obrigatório |
| `x` | Coordenada horizontal. | `tuple[float, ...]` | obrigatório |
| `y` | Coordenada vertical. | `tuple[float \| None, ...]` | obrigatório |
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str \| None` | `None` |
| `origem` | Origem usada pela operação. | `str` | `'direta'` |

:::details Detalhes técnicos

**Assinatura:** `Serie2D(estilo: str, x: tuple[float, ...], y: tuple[float \| None, ...], nome: str \| None = None, origem: str = 'direta')`

**Origem da implementação:** `coral.graficos`

**Arquivo na release:** `coral/graficos.py`

:::

#### `Serie3D`

Série cartesiana tridimensional imutável.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `estilo` | Valor correspondente a estilo. | `str` | obrigatório |
| `x` | Coordenada horizontal. | `tuple[float, ...]` | obrigatório |
| `y` | Coordenada vertical. | `tuple[float, ...]` | obrigatório |
| `z` | Valor correspondente a z. | `tuple[float, ...]` | obrigatório |
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str \| None` | `None` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `estilo` | Valor correspondente a estilo. | `str` | obrigatório |
| `x` | Coordenada horizontal. | `tuple[float, ...]` | obrigatório |
| `y` | Coordenada vertical. | `tuple[float, ...]` | obrigatório |
| `z` | Valor correspondente a z. | `tuple[float, ...]` | obrigatório |
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str \| None` | `None` |

:::details Detalhes técnicos

**Assinatura:** `Serie3D(estilo: str, x: tuple[float, ...], y: tuple[float, ...], z: tuple[float, ...], nome: str \| None = None)`

**Origem da implementação:** `coral.graficos`

**Arquivo na release:** `coral/graficos.py`

:::

#### `Superficie3D`

Grade tridimensional explícita, sem interpolação de pontos ausentes.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `x` | Coordenada horizontal. | `tuple[tuple[float, ...], ...]` | obrigatório |
| `y` | Coordenada vertical. | `tuple[tuple[float, ...], ...]` | obrigatório |
| `z` | Valor correspondente a z. | `tuple[tuple[float, ...], ...]` | obrigatório |
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str \| None` | `None` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `x` | Coordenada horizontal. | `tuple[tuple[float, ...], ...]` | obrigatório |
| `y` | Coordenada vertical. | `tuple[tuple[float, ...], ...]` | obrigatório |
| `z` | Valor correspondente a z. | `tuple[tuple[float, ...], ...]` | obrigatório |
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str \| None` | `None` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `forma` | Obtém forma. | `tuple[int, int]` |

:::details Detalhes técnicos

**Assinatura:** `Superficie3D(x: tuple[tuple[float, ...], ...], y: tuple[tuple[float, ...], ...], z: tuple[tuple[float, ...], ...], nome: str \| None = None)`

**Origem da implementação:** `coral.graficos`

**Arquivo na release:** `coral/graficos.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `forma` | propriedade | `forma() -> tuple[int, int]` |

:::

#### `SerieCategorias`

Série categórica para barras ou histograma.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `estilo` | Valor correspondente a estilo. | `str` | obrigatório |
| `categorias` | Valor correspondente a categorias. | `tuple[str, ...]` | obrigatório |
| `valores` | Coleção de valores processada. | `tuple[float, ...]` | obrigatório |
| `limites` | Valor correspondente a limites. | `tuple[tuple[float, float], ...]` | `()` |
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str \| None` | `None` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `estilo` | Valor correspondente a estilo. | `str` | obrigatório |
| `categorias` | Valor correspondente a categorias. | `tuple[str, ...]` | obrigatório |
| `valores` | Coleção de valores processada. | `tuple[float, ...]` | obrigatório |
| `limites` | Valor correspondente a limites. | `tuple[tuple[float, float], ...]` | `()` |
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str \| None` | `None` |

:::details Detalhes técnicos

**Assinatura:** `SerieCategorias(estilo: str, categorias: tuple[str, ...], valores: tuple[float, ...], limites: tuple[tuple[float, float], ...] = (), nome: str \| None = None)`

**Origem da implementação:** `coral.graficos`

**Arquivo na release:** `coral/graficos.py`

:::

#### `ResumoCaixa`

Resumo estatístico de um grupo para um gráfico de caixa.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | obrigatório |
| `minimo` | Limite mínimo considerado pela operação. | `float` | obrigatório |
| `q1` | Valor correspondente a q1. | `float` | obrigatório |
| `mediana` | Valor correspondente a mediana. | `float` | obrigatório |
| `q3` | Valor correspondente a q3. | `float` | obrigatório |
| `maximo` | Limite máximo considerado pela operação. | `float` | obrigatório |
| `bigode_inferior` | Valor correspondente a bigode inferior. | `float` | obrigatório |
| `bigode_superior` | Valor correspondente a bigode superior. | `float` | obrigatório |
| `extremos` | Valor correspondente a extremos. | `tuple[float, ...]` | obrigatório |
| `quantidade` | Quantidade de itens solicitada. | `int` | obrigatório |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | obrigatório |
| `minimo` | Limite mínimo considerado pela operação. | `float` | obrigatório |
| `q1` | Valor correspondente a q1. | `float` | obrigatório |
| `mediana` | Valor correspondente a mediana. | `float` | obrigatório |
| `q3` | Valor correspondente a q3. | `float` | obrigatório |
| `maximo` | Limite máximo considerado pela operação. | `float` | obrigatório |
| `bigode_inferior` | Valor correspondente a bigode inferior. | `float` | obrigatório |
| `bigode_superior` | Valor correspondente a bigode superior. | `float` | obrigatório |
| `extremos` | Valor correspondente a extremos. | `tuple[float, ...]` | obrigatório |
| `quantidade` | Quantidade de itens solicitada. | `int` | obrigatório |

:::details Detalhes técnicos

**Assinatura:** `ResumoCaixa(nome: str, minimo: float, q1: float, mediana: float, q3: float, maximo: float, bigode_inferior: float, bigode_superior: float, extremos: tuple[float, ...], quantidade: int)`

**Origem da implementação:** `coral.graficos`

**Arquivo na release:** `coral/graficos.py`

:::

#### `SeriesRegistros`

Duas séries alinhadas extraídas de registros comuns.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `x` | Coordenada horizontal. | `tuple[float, ...]` | obrigatório |
| `y` | Coordenada vertical. | `tuple[float, ...]` | obrigatório |
| `campo_x` | Valor correspondente a campo x. | `str` | obrigatório |
| `campo_y` | Valor correspondente a campo y. | `str` | obrigatório |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `x` | Coordenada horizontal. | `tuple[float, ...]` | obrigatório |
| `y` | Coordenada vertical. | `tuple[float, ...]` | obrigatório |
| `campo_x` | Valor correspondente a campo x. | `str` | obrigatório |
| `campo_y` | Valor correspondente a campo y. | `str` | obrigatório |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `quantidade` | Executa a operação `quantidade` disponibilizada por `coral.graficos`. | `int` |

:::details Detalhes técnicos

**Assinatura:** `SeriesRegistros(x: tuple[float, ...], y: tuple[float, ...], campo_x: str, campo_y: str)`

**Origem da implementação:** `coral.graficos`

**Arquivo na release:** `coral/graficos.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `quantidade` | propriedade | `quantidade() -> int` |

:::

#### `MatrizCores`

Matriz numérica e rótulos para mapas de calor e correlação.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valores` | Coleção de valores processada. | `tuple[tuple[float, ...], ...]` | obrigatório |
| `rotulos_linhas` | Valor correspondente a rotulos linhas. | `tuple[str, ...]` | obrigatório |
| `rotulos_colunas` | Valor correspondente a rotulos colunas. | `tuple[str, ...]` | obrigatório |
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str \| None` | `None` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `valores` | Coleção de valores processada. | `tuple[tuple[float, ...], ...]` | obrigatório |
| `rotulos_linhas` | Valor correspondente a rotulos linhas. | `tuple[str, ...]` | obrigatório |
| `rotulos_colunas` | Valor correspondente a rotulos colunas. | `tuple[str, ...]` | obrigatório |
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str \| None` | `None` |

:::details Detalhes técnicos

**Assinatura:** `MatrizCores(valores: tuple[tuple[float, ...], ...], rotulos_linhas: tuple[str, ...], rotulos_colunas: tuple[str, ...], nome: str \| None = None)`

**Origem da implementação:** `coral.graficos`

**Arquivo na release:** `coral/graficos.py`

:::

#### `SerieErro`

Série cartesiana com incerteza inferior e superior por ponto.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `x` | Coordenada horizontal. | `tuple[float, ...]` | obrigatório |
| `y` | Coordenada vertical. | `tuple[float, ...]` | obrigatório |
| `erro_inferior` | Valor correspondente a erro inferior. | `tuple[float, ...]` | obrigatório |
| `erro_superior` | Valor correspondente a erro superior. | `tuple[float, ...]` | obrigatório |
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str \| None` | `None` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `x` | Coordenada horizontal. | `tuple[float, ...]` | obrigatório |
| `y` | Coordenada vertical. | `tuple[float, ...]` | obrigatório |
| `erro_inferior` | Valor correspondente a erro inferior. | `tuple[float, ...]` | obrigatório |
| `erro_superior` | Valor correspondente a erro superior. | `tuple[float, ...]` | obrigatório |
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str \| None` | `None` |

:::details Detalhes técnicos

**Assinatura:** `SerieErro(x: tuple[float, ...], y: tuple[float, ...], erro_inferior: tuple[float, ...], erro_superior: tuple[float, ...], nome: str \| None = None)`

**Origem da implementação:** `coral.graficos`

**Arquivo na release:** `coral/graficos.py`

:::

#### `FaixaIncerteza`

Centro e limites absolutos de uma faixa de incerteza.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `x` | Coordenada horizontal. | `tuple[float, ...]` | obrigatório |
| `centro` | Valor correspondente a centro. | `tuple[float, ...]` | obrigatório |
| `inferior` | Valor correspondente a inferior. | `tuple[float, ...]` | obrigatório |
| `superior` | Valor correspondente a superior. | `tuple[float, ...]` | obrigatório |
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str \| None` | `None` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `x` | Coordenada horizontal. | `tuple[float, ...]` | obrigatório |
| `centro` | Valor correspondente a centro. | `tuple[float, ...]` | obrigatório |
| `inferior` | Valor correspondente a inferior. | `tuple[float, ...]` | obrigatório |
| `superior` | Valor correspondente a superior. | `tuple[float, ...]` | obrigatório |
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str \| None` | `None` |

:::details Detalhes técnicos

**Assinatura:** `FaixaIncerteza(x: tuple[float, ...], centro: tuple[float, ...], inferior: tuple[float, ...], superior: tuple[float, ...], nome: str \| None = None)`

**Origem da implementação:** `coral.graficos`

**Arquivo na release:** `coral/graficos.py`

:::

#### `PainelGraficos`

Composição imutável de gráficos usando uma grade regular.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `graficos` | Valor correspondente a graficos. | `tuple['Grafico', ...]` | obrigatório |
| `colunas` | Valor correspondente a colunas. | `int` | obrigatório |
| `titulo` | Valor correspondente a titulo. | `str` | `''` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `graficos` | Valor correspondente a graficos. | `tuple['Grafico', ...]` | obrigatório |
| `colunas` | Valor correspondente a colunas. | `int` | obrigatório |
| `titulo` | Valor correspondente a titulo. | `str` | `''` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `linhas` | Executa a operação `linhas` disponibilizada por `coral.graficos`. | `int` |

:::details Detalhes técnicos

**Assinatura:** `PainelGraficos(graficos: tuple['Grafico', ...], colunas: int, titulo: str = '')`

**Origem da implementação:** `coral.graficos`

**Arquivo na release:** `coral/graficos.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `linhas` | propriedade | `linhas() -> int` |

:::

#### `Grafico`

Especificação imutável de um gráfico Coral 2D ou 3D.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `tipo` | Tipo solicitado para o resultado, quando o módulo oferece essa escolha. | `str` | obrigatório |
| `elementos` | Valor correspondente a elementos. | `tuple[Any, ...]` | obrigatório |
| `titulo` | Valor correspondente a titulo. | `str` | `''` |
| `rotulo_x` | Valor correspondente a rotulo x. | `str` | `''` |
| `rotulo_y` | Valor correspondente a rotulo y. | `str` | `''` |
| `rotulo_z` | Valor correspondente a rotulo z. | `str` | `''` |
| `unidade_x` | Valor correspondente a unidade x. | `str` | `''` |
| `unidade_y` | Valor correspondente a unidade y. | `str` | `''` |
| `unidade_z` | Valor correspondente a unidade z. | `str` | `''` |
| `legenda` | Valor correspondente a legenda. | `bool` | `True` |
| `tema` | Valor correspondente a tema. | `str` | `'claro'` |
| `proveniencia` | Valor correspondente a proveniencia. | `tuple[str, ...]` | `()` |
| `texto_alternativo` | Valor correspondente a texto alternativo. | `str` | `''` |
| `avisos` | Valor correspondente a avisos. | `tuple[str, ...]` | `()` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `tipo` | Tipo solicitado para o resultado, quando o módulo oferece essa escolha. | `str` | obrigatório |
| `elementos` | Valor correspondente a elementos. | `tuple[Any, ...]` | obrigatório |
| `titulo` | Valor correspondente a titulo. | `str` | `''` |
| `rotulo_x` | Valor correspondente a rotulo x. | `str` | `''` |
| `rotulo_y` | Valor correspondente a rotulo y. | `str` | `''` |
| `rotulo_z` | Valor correspondente a rotulo z. | `str` | `''` |
| `unidade_x` | Valor correspondente a unidade x. | `str` | `''` |
| `unidade_y` | Valor correspondente a unidade y. | `str` | `''` |
| `unidade_z` | Valor correspondente a unidade z. | `str` | `''` |
| `legenda` | Valor correspondente a legenda. | `bool` | `True` |
| `tema` | Valor correspondente a tema. | `str` | `'claro'` |
| `proveniencia` | Valor correspondente a proveniencia. | `tuple[str, ...]` | `()` |
| `texto_alternativo` | Valor correspondente a texto alternativo. | `str` | `''` |
| `avisos` | Valor correspondente a avisos. | `tuple[str, ...]` | `()` |

:::details Detalhes técnicos

**Assinatura:** `Grafico(tipo: str, elementos: tuple[Any, ...], titulo: str = '', rotulo_x: str = '', rotulo_y: str = '', rotulo_z: str = '', unidade_x: str = '', unidade_y: str = '', unidade_z: str = '', legenda: bool = True, tema: str = 'claro', proveniencia: tuple[str, ...] = (), texto_alternativo: str = '', avisos: tuple[str, ...] = ())`

**Origem da implementação:** `coral.graficos`

**Arquivo na release:** `coral/graficos.py`

:::

### Exceções

#### `ErroGrafico`

Erro público para especificações ou dados gráficos inválidos.

:::details Detalhes técnicos

**Assinatura:** `ErroGrafico(...)`

**Origem da implementação:** `coral.graficos`

**Arquivo na release:** `coral/graficos.py`

:::

<!-- /AUTO:API -->
