# coral.numerico

## Visão geral

`coral.numerico` é a camada de computação numérica da Coral para vetores, matrizes, estatística e álgebra linear. O módulo foi desenhado para que a linguagem possa oferecer operações científicas sem transformar NumPy em dependência obrigatória de todo programa Coral.

<!-- AUTO:MODULO -->

**Importação:** `coral.numerico`  
**Categoria:** cientifico  

vetores, matrizes, estatística e álgebra numérica

### Superfície pública detectada

`DependenciaNumericaAusente`, `ErroNumerico`, `ResultadoMinimosQuadrados`, `ResultadoRegressaoLinear`, `ResultadoBootstrap`, `ResultadoTestePermutacao`, `numpy_disponivel`, `diagnosticar_numerico`, `vetor`, `matriz`, `zeros`, `uns`, `intervalo`, `espaco_linear`, `identidade`, `remodelar`, `concatenar`, `selecionar_coluna`, `soma`, `media`, `mediana`, `variancia`, `desvio_padrao`, `minimo`, `maximo`, `percentil`, `covariancia`, `correlacao`, `frequencias`, `moda`, `quartis`, `amplitude`, `intervalo_interquartil`, `mediana_desvios_absolutos`, `media_ponderada`, `media_geometrica`, `media_harmonica`, `histograma`, `erro_padrao`, `assimetria`, `curtose`, `matriz_covariancia`, `matriz_correlacao`, `regressao_linear`, `intervalo_bootstrap`, `teste_permutacao`, `norma`, `normalizar`, `produto_vetorial`, `posto`, `minimos_quadrados`, `vetor3`, `distancia_vetores`, `angulo_entre_vetores`, `projecao_vetorial`, `produto_misto3`, `volume_paralelepipedo3`, `rotacionar3`, `transformar_ponto3`, `matriz_rotacao3`, `matriz_translacao3`, `matriz_escala3`, `compor_transformacoes3`, `transformar_vetor3`, `distancia_ponto_plano3`, `projetar_ponto_plano3`, `intersecao_reta_plano3`, `coordenadas_esfericas3`, `ponto_de_esfericas3`, `area_triangulo3`, `volume_tetraedro3`, `transposta`, `produto_escalar`, `multiplicar_matrizes`, `determinante`, `inversa`, `resolver_sistema`, `autovalores`, `forma`

<!-- /AUTO:MODULO -->

## Papel no ecossistema

Use `coral.numerico` quando o problema deixa de ser apenas aritmética escalar e passa a envolver séries, matrizes, medidas estatísticas ou álgebra linear. Para operações matemáticas simples e portáveis, `coral.matematica` costuma ser uma dependência menor.

```text
valores escalares ── coral.matematica
        │
        └── vetores, matrizes, estatística e álgebra ── coral.numerico
                                                        │
                                                        └── experimentos ── coral.laboratorio
```

## Conceitos principais

### NumPy é opcional

Importar a Coral não obriga a instalação de NumPy. As operações deste módulo que dependem da biblioteca científica verificam a capacidade quando usadas. `numpy_disponivel()` e `diagnosticar_numerico()` permitem inspecionar o ambiente antes de escolher um caminho opcional.

### Vetores e matrizes

`vetor`, `matriz`, `zeros`, `uns`, `intervalo` e `espaco_linear` constroem estruturas numéricas. O módulo valida forma e dimensionalidade em vez de deixar erros surgirem muito depois da criação dos dados.

### Estatística

A superfície inclui soma, média, mediana, variância, desvio padrão, mínimo e máximo. Ao trabalhar com variância ou desvio, documente se o cálculo é populacional ou amostral no contexto do projeto.

### Álgebra linear

Transposta, produto escalar, multiplicação matricial, determinante, inversa, solução de sistema e autovalores formam a camada de álgebra linear.

## Quando usar

Use este módulo para análise numérica, processamento de séries, modelos matriciais, simulações, pós processamento de experimentos e algoritmos que realmente dependem de estruturas multidimensionais.

Evite introduzi lo apenas para somar alguns números ou calcular uma raiz: nesses casos `coral.matematica` mantém a dependência menor e a intenção mais clara.

## Começando

A release 1.7.4 usa `coral.numerico` no projeto de laboratório de algoritmos. O trecho abaixo vem de `Exemplos/Projetos_Completos/Vitrine/laboratorio_algoritmos/analise.coral`:

```coral
de coral.json importe ler_json
de coral.numerico importe mediana

crie a função analisar_relatorio com caminho
    defina relatorio como ler_json(caminho)
    defina tempos como [medicao["tempo_segundos"] para cada medicao em relatorio["medicoes"] se medicao["erro"] for igual a nada]
    crie um vetor chamado serie com tempos
    calcule a média de serie como media_serie
    calcule o desvio padrão de serie como desvio_serie
    retorne {"media": media_serie, "mediana": mediana(serie), "desvio": desvio_serie}
fim
```

:::resultado
O trecho define `analisar_relatorio`. Quando a função recebe um relatório compatível, ela devolve um registro com média, mediana e desvio dos tempos válidos.
:::

## API essencial

| Entrada | Papel | Assinatura |
|---|---|---|
| `numpy_disponivel` | descobrir se a capacidade NumPy está disponível | `numpy_disponivel() -> bool` |
| `diagnosticar_numerico` | obter diagnóstico estruturado | `diagnosticar_numerico() -> dict[str, Any]` |
| `vetor` | construir vetor | `vetor(valores: Iterable[Any], tipo: Any \| None = None)` |
| `matriz` | construir matriz | `matriz(linhas: Iterable[Iterable[Any]], tipo: Any \| None = None)` |
| `media` | calcular média | `media(valores)` |
| `mediana` | calcular mediana | `mediana(valores)` |
| `desvio_padrao` | calcular dispersão | `desvio_padrao(valores, populacional = True)` |
| `produto_escalar` | combinar dois vetores | `produto_escalar(a, b)` |
| `determinante` | medir determinante de matriz | `determinante(m)` |
| `resolver_sistema` | resolver sistema linear | `resolver_sistema(coeficientes, termos)` |

## Fluxos comuns

### Preparar uma série

Construa os dados com `vetor` ou com as formas naturais da Coral, valide a disponibilidade da capacidade numérica quando ela for opcional e só então aplique estatística ou álgebra.

### Analisar resultados de laboratório

`coral.laboratorio` produz medições e metadados. `coral.numerico` entra depois para resumir distribuição, tendência e dispersão. Essa separação evita misturar medição com interpretação.

### Criar fallback sem NumPy

Quando NumPy for apenas uma otimização ou recurso complementar, consulte `numpy_disponivel()` e ofereça um caminho mais simples em vez de fazer o programa inteiro falhar na importação.

## Erros e diagnóstico

`DependenciaNumericaAusente` representa a falta da dependência opcional quando uma operação realmente precisa dela. `ErroNumerico` representa entradas ou operações incompatíveis. Use `diagnosticar_numerico()` para diferenciar ambiente incompleto de erro nos dados.

Coleções vazias, formas incompatíveis e matrizes que não satisfazem os requisitos de uma operação devem ser tratadas como erros de domínio, não escondidas com valores artificiais.

## Boas práticas

* Registre a forma dos dados antes de operações matriciais importantes.
* Não confunda ausência de NumPy com programa Coral inválido.
* Em benchmarks, separe custo de preparação dos dados do custo da operação medida.
* Para resultados científicos, preserve semente, parâmetros e ambiente com `coral.laboratorio`.

## Integração com outros módulos

`coral.matematica` cobre matemática geral. `coral.laboratorio` mede experimentos. `coral.json` e `coral.persistencia` ajudam a transportar resultados. `coral.aleatorio` fornece fontes reproduzíveis para simulações.

## Testabilidade e reprodutibilidade

A parte determinística do módulo deve receber dados já preparados. Se a geração da entrada for aleatória, fixe a semente na fonte de aleatoriedade e salve os parâmetros junto do resultado.

## Referência da API

<!-- AUTO:API -->

### Funções

#### `numpy_disponivel`

Descobrir se a capacidade NumPy está disponível.

**Retorno**

Retorna um valor lógico que indica o resultado da verificação.

:::details Detalhes técnicos

**Assinatura:** `numpy_disponivel() -> bool`

**Origem da implementação:** `coral.numerico`

**Arquivo na release:** `coral/numerico.py`

:::

#### `diagnosticar_numerico`

Obter diagnóstico estruturado.

**Retorno**

Retorna um valor declarado como `dict[str, Any]`.

:::details Detalhes técnicos

**Assinatura:** `diagnosticar_numerico() -> dict[str, Any]`

**Origem da implementação:** `coral.numerico`

**Arquivo na release:** `coral/numerico.py`

:::

#### `vetor`

Construir vetor.

**Exemplo**

```coral
de coral.json importe ler_json
de coral.numerico importe mediana

crie a função analisar_relatorio com caminho
    defina relatorio como ler_json(caminho)
    defina tempos como [medicao["tempo_segundos"] para cada medicao em relatorio["medicoes"] se medicao["erro"] for igual a nada]
    crie um vetor chamado serie com tempos
    calcule a média de serie como media_serie
    calcule o desvio padrão de serie como desvio_serie
    retorne {"media": media_serie, "mediana": mediana(serie), "desvio": desvio_serie}
fim
```

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valores` | Coleção de valores processada. | `Iterable[Any]` | obrigatório |
| `tipo` | Tipo solicitado para o resultado, quando o módulo oferece essa escolha. | `Any \| None` | `None` |

**Retorno**

Retorna o vetor criado.

:::details Detalhes técnicos

**Assinatura:** `vetor(valores: Iterable[Any], tipo: Any \| None = None)`

**Origem da implementação:** `coral.numerico`

**Arquivo na release:** `coral/numerico.py`

**Exceções diretamente observáveis no corpo:** `ErroNumerico`

:::

#### `matriz`

Construir matriz.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `linhas` | Linhas usadas para construir ou processar a estrutura. | `Iterable[Iterable[Any]]` | obrigatório |
| `tipo` | Tipo solicitado para o resultado, quando o módulo oferece essa escolha. | `Any \| None` | `None` |

**Retorno**

Retorna a matriz criada.

:::details Detalhes técnicos

**Assinatura:** `matriz(linhas: Iterable[Iterable[Any]], tipo: Any \| None = None)`

**Origem da implementação:** `coral.numerico`

**Arquivo na release:** `coral/numerico.py`

**Exceções diretamente observáveis no corpo:** `ErroNumerico`

:::

#### `zeros`

Cria uma estrutura numérica preenchida com zeros.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `forma` | Forma ou dimensões da estrutura a criar. | `não declarado` | obrigatório |
| `tipo` | Tipo solicitado para o resultado, quando o módulo oferece essa escolha. | `não declarado` | `float` |

**Retorno**

Retorna a estrutura preenchida com zeros.

:::details Detalhes técnicos

**Assinatura:** `zeros(forma, tipo = float)`

**Origem da implementação:** `coral.numerico`

**Arquivo na release:** `coral/numerico.py`

**Exceções diretamente observáveis no corpo:** `ErroNumerico`

:::

#### `uns`

Cria uma estrutura numérica preenchida com uns.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `forma` | Forma ou dimensões da estrutura a criar. | `não declarado` | obrigatório |
| `tipo` | Tipo solicitado para o resultado, quando o módulo oferece essa escolha. | `não declarado` | `float` |

**Retorno**

Retorna a estrutura preenchida com uns.

:::details Detalhes técnicos

**Assinatura:** `uns(forma, tipo = float)`

**Origem da implementação:** `coral.numerico`

**Arquivo na release:** `coral/numerico.py`

**Exceções diretamente observáveis no corpo:** `ErroNumerico`

:::

#### `intervalo`

Cria uma sequência numérica definida por início, fim e passo.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `inicio` | Valor inicial do intervalo ou processo. | `não declarado` | obrigatório |
| `fim` | Valor final do intervalo ou processo. | `não declarado` | `None` |
| `passo` | Incremento aplicado entre valores sucessivos. | `não declarado` | `1` |
| `tipo` | Tipo solicitado para o resultado, quando o módulo oferece essa escolha. | `não declarado` | `None` |

**Retorno**

Retorna a sequência numérica criada.

:::details Detalhes técnicos

**Assinatura:** `intervalo(inicio, fim = None, passo = 1, tipo = None)`

**Origem da implementação:** `coral.numerico`

**Arquivo na release:** `coral/numerico.py`

**Exceções diretamente observáveis no corpo:** `ErroNumerico`

:::

#### `espaco_linear`

Cria valores igualmente espaçados entre dois limites.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `inicio` | Valor inicial do intervalo ou processo. | `não declarado` | obrigatório |
| `fim` | Valor final do intervalo ou processo. | `não declarado` | obrigatório |
| `quantidade` | Quantidade de itens solicitada. | `não declarado` | `50` |

**Retorno**

Retorna a sequência de valores igualmente espaçados.

:::details Detalhes técnicos

**Assinatura:** `espaco_linear(inicio, fim, quantidade = 50)`

**Origem da implementação:** `coral.numerico`

**Arquivo na release:** `coral/numerico.py`

**Exceções diretamente observáveis no corpo:** `ErroNumerico`

:::

#### `identidade`

Executa a operação `identidade` disponibilizada por `coral.numerico`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `ordem` | Valor correspondente a ordem. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `identidade(ordem)`

**Origem da implementação:** `coral.numerico`

**Arquivo na release:** `coral/numerico.py`

:::

#### `remodelar`

Executa a operação `remodelar` disponibilizada por `coral.numerico`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valores` | Coleção de valores processada. | `não declarado` | obrigatório |
| `forma` | Forma ou dimensões da estrutura a criar. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `remodelar(valores, forma)`

**Origem da implementação:** `coral.numerico`

**Arquivo na release:** `coral/numerico.py`

**Exceções diretamente observáveis no corpo:** `ErroNumerico`

:::

#### `concatenar`

Executa a operação `concatenar` disponibilizada por `coral.numerico`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valores` | Coleção de valores processada. | `não declarado` | obrigatório |
| `eixo` | Valor correspondente a eixo. | `não declarado` | `0` |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `concatenar(valores, eixo = 0)`

**Origem da implementação:** `coral.numerico`

**Arquivo na release:** `coral/numerico.py`

**Exceções diretamente observáveis no corpo:** `ErroNumerico`

:::

#### `selecionar_coluna`

Executa a operação `selecionar_coluna` disponibilizada por `coral.numerico`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `registros` | Valor correspondente a registros. | `não declarado` | obrigatório |
| `campo` | Valor correspondente a campo. | `não declarado` | obrigatório |
| `ausentes` | Valor correspondente a ausentes. | `não declarado` | `'erro'` |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `selecionar_coluna(registros, campo, ausentes = 'erro')`

**Origem da implementação:** `coral.numerico`

**Arquivo na release:** `coral/numerico.py`

**Exceções diretamente observáveis no corpo:** `ErroNumerico`

:::

#### `soma`

Calcula a soma dos valores.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valores` | Coleção de valores processada. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado da soma.

:::details Detalhes técnicos

**Assinatura:** `soma(valores)`

**Origem da implementação:** `coral.numerico`

**Arquivo na release:** `coral/numerico.py`

:::

#### `media`

Calcular média.

**Exemplo**

```coral
de coral.json importe ler_json
de coral.numerico importe mediana

crie a função analisar_relatorio com caminho
    defina relatorio como ler_json(caminho)
    defina tempos como [medicao["tempo_segundos"] para cada medicao em relatorio["medicoes"] se medicao["erro"] for igual a nada]
    crie um vetor chamado serie com tempos
    calcule a média de serie como media_serie
    calcule o desvio padrão de serie como desvio_serie
    retorne {"media": media_serie, "mediana": mediana(serie), "desvio": desvio_serie}
fim
```

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valores` | Coleção de valores processada. | `não declarado` | obrigatório |

**Retorno**

Retorna a média calculada.

:::details Detalhes técnicos

**Assinatura:** `media(valores)`

**Origem da implementação:** `coral.numerico`

**Arquivo na release:** `coral/numerico.py`

:::

#### `mediana`

Calcular mediana.

**Exemplo**

```coral
de coral.json importe ler_json
de coral.numerico importe mediana

crie a função analisar_relatorio com caminho
    defina relatorio como ler_json(caminho)
    defina tempos como [medicao["tempo_segundos"] para cada medicao em relatorio["medicoes"] se medicao["erro"] for igual a nada]
    crie um vetor chamado serie com tempos
    calcule a média de serie como media_serie
    calcule o desvio padrão de serie como desvio_serie
    retorne {"media": media_serie, "mediana": mediana(serie), "desvio": desvio_serie}
fim
```

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valores` | Coleção de valores processada. | `não declarado` | obrigatório |

**Retorno**

Retorna a mediana calculada.

:::details Detalhes técnicos

**Assinatura:** `mediana(valores)`

**Origem da implementação:** `coral.numerico`

**Arquivo na release:** `coral/numerico.py`

:::

#### `variancia`

Calcula a variância dos valores.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valores` | Coleção de valores processada. | `não declarado` | obrigatório |
| `populacional` | Valor correspondente a populacional. | `não declarado` | `True` |

**Retorno**

Retorna a variância calculada.

:::details Detalhes técnicos

**Assinatura:** `variancia(valores, populacional = True)`

**Origem da implementação:** `coral.numerico`

**Arquivo na release:** `coral/numerico.py`

**Exceções diretamente observáveis no corpo:** `ErroNumerico`

:::

#### `desvio_padrao`

Calcular dispersão.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valores` | Coleção de valores processada. | `não declarado` | obrigatório |
| `populacional` | Valor correspondente a populacional. | `não declarado` | `True` |

**Retorno**

Retorna o desvio padrão calculado.

:::details Detalhes técnicos

**Assinatura:** `desvio_padrao(valores, populacional = True)`

**Origem da implementação:** `coral.numerico`

**Arquivo na release:** `coral/numerico.py`

**Exceções diretamente observáveis no corpo:** `ErroNumerico`

:::

#### `minimo`

Obtém o menor valor.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valores` | Coleção de valores processada. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `minimo(valores)`

**Origem da implementação:** `coral.numerico`

**Arquivo na release:** `coral/numerico.py`

:::

#### `maximo`

Obtém o maior valor.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valores` | Coleção de valores processada. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `maximo(valores)`

**Origem da implementação:** `coral.numerico`

**Arquivo na release:** `coral/numerico.py`

:::

#### `percentil`

Executa a operação `percentil` disponibilizada por `coral.numerico`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valores` | Coleção de valores processada. | `não declarado` | obrigatório |
| `percentual` | Valor correspondente a percentual. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `percentil(valores, percentual)`

**Origem da implementação:** `coral.numerico`

**Arquivo na release:** `coral/numerico.py`

**Exceções diretamente observáveis no corpo:** `ErroNumerico`

:::

#### `covariancia`

Executa a operação `covariancia` disponibilizada por `coral.numerico`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `a` | Valor correspondente a a. | `não declarado` | obrigatório |
| `b` | Valor correspondente a b. | `não declarado` | obrigatório |
| `populacional` | Valor correspondente a populacional. | `não declarado` | `True` |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `covariancia(a, b, populacional = True)`

**Origem da implementação:** `coral.numerico`

**Arquivo na release:** `coral/numerico.py`

**Exceções diretamente observáveis no corpo:** `ErroNumerico`

:::

#### `correlacao`

Executa a operação `correlacao` disponibilizada por `coral.numerico`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `a` | Valor correspondente a a. | `não declarado` | obrigatório |
| `b` | Valor correspondente a b. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `correlacao(a, b)`

**Origem da implementação:** `coral.numerico`

**Arquivo na release:** `coral/numerico.py`

**Exceções diretamente observáveis no corpo:** `ErroNumerico`

:::

#### `frequencias`

Executa a operação `frequencias` disponibilizada por `coral.numerico`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valores` | Coleção de valores processada. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `frequencias(valores)`

**Origem da implementação:** `coral.numerico`

**Arquivo na release:** `coral/numerico.py`

**Exceções diretamente observáveis no corpo:** `ErroNumerico`

:::

#### `moda`

Executa a operação `moda` disponibilizada por `coral.numerico`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valores` | Coleção de valores processada. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `moda(valores)`

**Origem da implementação:** `coral.numerico`

**Arquivo na release:** `coral/numerico.py`

:::

#### `quartis`

Executa a operação `quartis` disponibilizada por `coral.numerico`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valores` | Coleção de valores processada. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `quartis(valores)`

**Origem da implementação:** `coral.numerico`

**Arquivo na release:** `coral/numerico.py`

:::

#### `amplitude`

Executa a operação `amplitude` disponibilizada por `coral.numerico`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valores` | Coleção de valores processada. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `amplitude(valores)`

**Origem da implementação:** `coral.numerico`

**Arquivo na release:** `coral/numerico.py`

:::

#### `intervalo_interquartil`

Executa a operação `intervalo_interquartil` disponibilizada por `coral.numerico`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valores` | Coleção de valores processada. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `intervalo_interquartil(valores)`

**Origem da implementação:** `coral.numerico`

**Arquivo na release:** `coral/numerico.py`

:::

#### `mediana_desvios_absolutos`

Executa a operação `mediana_desvios_absolutos` disponibilizada por `coral.numerico`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valores` | Coleção de valores processada. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `mediana_desvios_absolutos(valores)`

**Origem da implementação:** `coral.numerico`

**Arquivo na release:** `coral/numerico.py`

:::

#### `media_ponderada`

Executa a operação `media_ponderada` disponibilizada por `coral.numerico`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valores` | Coleção de valores processada. | `não declarado` | obrigatório |
| `pesos` | Pesos associados aos valores usados na escolha. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `media_ponderada(valores, pesos)`

**Origem da implementação:** `coral.numerico`

**Arquivo na release:** `coral/numerico.py`

**Exceções diretamente observáveis no corpo:** `ErroNumerico`

:::

#### `media_geometrica`

Executa a operação `media_geometrica` disponibilizada por `coral.numerico`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valores` | Coleção de valores processada. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `media_geometrica(valores)`

**Origem da implementação:** `coral.numerico`

**Arquivo na release:** `coral/numerico.py`

**Exceções diretamente observáveis no corpo:** `ErroNumerico`

:::

#### `media_harmonica`

Executa a operação `media_harmonica` disponibilizada por `coral.numerico`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valores` | Coleção de valores processada. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `media_harmonica(valores)`

**Origem da implementação:** `coral.numerico`

**Arquivo na release:** `coral/numerico.py`

**Exceções diretamente observáveis no corpo:** `ErroNumerico`

:::

#### `histograma`

Executa a operação `histograma` disponibilizada por `coral.numerico`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valores` | Coleção de valores processada. | `não declarado` | obrigatório |
| `faixas` | Valor correspondente a faixas. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `histograma(valores, faixas)`

**Origem da implementação:** `coral.numerico`

**Arquivo na release:** `coral/numerico.py`

**Exceções diretamente observáveis no corpo:** `ErroNumerico`

:::

#### `erro_padrao`

Calcula o erro padrão da média usando o desvio amostral.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valores` | Coleção de valores processada. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `erro_padrao(valores)`

**Origem da implementação:** `coral.numerico`

**Arquivo na release:** `coral/numerico.py`

:::

#### `assimetria`

Momento padronizado de ordem 3, sem correção de viés amostral.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valores` | Coleção de valores processada. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `assimetria(valores)`

**Origem da implementação:** `coral.numerico`

**Arquivo na release:** `coral/numerico.py`

**Exceções diretamente observáveis no corpo:** `ErroNumerico`

:::

#### `curtose`

Curtose em excesso pelo quarto momento padronizado, isto é, normal = 0.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valores` | Coleção de valores processada. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `curtose(valores)`

**Origem da implementação:** `coral.numerico`

**Arquivo na release:** `coral/numerico.py`

**Exceções diretamente observáveis no corpo:** `ErroNumerico`

:::

#### `matriz_covariancia`

Matriz de covariância com linhas como observações e colunas como variáveis.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `dados` | Dados processados pela operação. | `não declarado` | obrigatório |
| `populacional` | Valor correspondente a populacional. | `não declarado` | `False` |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `matriz_covariancia(dados, populacional = False)`

**Origem da implementação:** `coral.numerico`

**Arquivo na release:** `coral/numerico.py`

**Exceções diretamente observáveis no corpo:** `ErroNumerico`

:::

#### `matriz_correlacao`

Matriz de correlação de Pearson para colunas observadas conjuntamente.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `dados` | Dados processados pela operação. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `matriz_correlacao(dados)`

**Origem da implementação:** `coral.numerico`

**Arquivo na release:** `coral/numerico.py`

**Exceções diretamente observáveis no corpo:** `ErroNumerico`

:::

#### `regressao_linear`

Ajusta ``y = intercepto + inclinacao * x`` por mínimos quadrados simples.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `x` | Coordenada horizontal. | `não declarado` | obrigatório |
| `y` | Coordenada vertical. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `regressao_linear(x, y)`

**Origem da implementação:** `coral.numerico`

**Arquivo na release:** `coral/numerico.py`

**Exceções diretamente observáveis no corpo:** `ErroNumerico`

:::

#### `intervalo_bootstrap`

Intervalo bootstrap percentil reproduzível com gerador aleatório local.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valores` | Coleção de valores processada. | `não declarado` | obrigatório |
| `estatistica` | Valor correspondente a estatistica. | `não declarado` | obrigatório |
| `confianca` | Valor correspondente a confianca. | `não declarado` | obrigatório |
| `repeticoes` | Valor correspondente a repeticoes. | `não declarado` | obrigatório |
| `semente` | Semente usada para tornar a sequência reproduzível. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `intervalo_bootstrap(valores, estatistica, confianca, repeticoes, semente)`

**Origem da implementação:** `coral.numerico`

**Arquivo na release:** `coral/numerico.py`

**Exceções diretamente observáveis no corpo:** `ErroNumerico`

:::

#### `teste_permutacao`

Teste de permutação bilateral para diferença de uma estatística entre grupos.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `a` | Valor correspondente a a. | `não declarado` | obrigatório |
| `b` | Valor correspondente a b. | `não declarado` | obrigatório |
| `estatistica` | Valor correspondente a estatistica. | `não declarado` | obrigatório |
| `repeticoes` | Valor correspondente a repeticoes. | `não declarado` | obrigatório |
| `semente` | Semente usada para tornar a sequência reproduzível. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `teste_permutacao(a, b, estatistica, repeticoes, semente)`

**Origem da implementação:** `coral.numerico`

**Arquivo na release:** `coral/numerico.py`

:::

#### `norma`

Norma euclidiana de um vetor finito e não vazio.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valores` | Coleção de valores processada. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `norma(valores)`

**Origem da implementação:** `coral.numerico`

**Arquivo na release:** `coral/numerico.py`

**Exceções diretamente observáveis no corpo:** `ErroNumerico`

:::

#### `normalizar`

Devolve uma cópia do vetor com norma euclidiana igual a um.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valores` | Coleção de valores processada. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `normalizar(valores)`

**Origem da implementação:** `coral.numerico`

**Arquivo na release:** `coral/numerico.py`

**Exceções diretamente observáveis no corpo:** `ErroNumerico`

:::

#### `produto_vetorial`

Produto vetorial exclusivo de vetores tridimensionais.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `a` | Valor correspondente a a. | `não declarado` | obrigatório |
| `b` | Valor correspondente a b. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `produto_vetorial(a, b)`

**Origem da implementação:** `coral.numerico`

**Arquivo na release:** `coral/numerico.py`

**Exceções diretamente observáveis no corpo:** `ErroNumerico`

:::

#### `posto`

Posto numérico de uma matriz pela tolerância padrão da decomposição SVD do NumPy.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `matriz` | Valor correspondente a matriz. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `posto(matriz)`

**Origem da implementação:** `coral.numerico`

**Arquivo na release:** `coral/numerico.py`

**Exceções diretamente observáveis no corpo:** `ErroNumerico`

:::

#### `minimos_quadrados`

Resolve um ajuste linear por mínimos quadrados sem exigir sistema quadrado.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `coeficientes` | Valor correspondente a coeficientes. | `não declarado` | obrigatório |
| `termos` | Valor correspondente a termos. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `minimos_quadrados(coeficientes, termos)`

**Origem da implementação:** `coral.numerico`

**Arquivo na release:** `coral/numerico.py`

**Exceções diretamente observáveis no corpo:** `ErroNumerico`

:::

#### `vetor3`

Constrói um vetor numérico tridimensional ``(x, y, z)``.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `x` | Coordenada horizontal. | `não declarado` | obrigatório |
| `y` | Coordenada vertical. | `não declarado` | obrigatório |
| `z` | Valor correspondente a z. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `vetor3(x, y, z)`

**Origem da implementação:** `coral.numerico`

**Arquivo na release:** `coral/numerico.py`

:::

#### `distancia_vetores`

Distância euclidiana entre vetores finitos da mesma dimensão.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `a` | Valor correspondente a a. | `não declarado` | obrigatório |
| `b` | Valor correspondente a b. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `distancia_vetores(a, b)`

**Origem da implementação:** `coral.numerico`

**Arquivo na release:** `coral/numerico.py`

**Exceções diretamente observáveis no corpo:** `ErroNumerico`

:::

#### `angulo_entre_vetores`

Ângulo em radianos entre vetores não nulos da mesma dimensão.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `a` | Valor correspondente a a. | `não declarado` | obrigatório |
| `b` | Valor correspondente a b. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `angulo_entre_vetores(a, b)`

**Origem da implementação:** `coral.numerico`

**Arquivo na release:** `coral/numerico.py`

**Exceções diretamente observáveis no corpo:** `ErroNumerico`

:::

#### `projecao_vetorial`

Projeta ``a`` sobre um vetor não nulo, preservando a dimensão.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `a` | Valor correspondente a a. | `não declarado` | obrigatório |
| `sobre` | Valor correspondente a sobre. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `projecao_vetorial(a, sobre)`

**Origem da implementação:** `coral.numerico`

**Arquivo na release:** `coral/numerico.py`

**Exceções diretamente observáveis no corpo:** `ErroNumerico`

:::

#### `produto_misto3`

Produto misto orientado de três vetores tridimensionais.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `a` | Valor correspondente a a. | `não declarado` | obrigatório |
| `b` | Valor correspondente a b. | `não declarado` | obrigatório |
| `c` | Valor correspondente a c. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `produto_misto3(a, b, c)`

**Origem da implementação:** `coral.numerico`

**Arquivo na release:** `coral/numerico.py`

**Exceções diretamente observáveis no corpo:** `ErroNumerico`

:::

#### `volume_paralelepipedo3`

Volume do paralelepípedo gerado por três vetores 3D.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `a` | Valor correspondente a a. | `não declarado` | obrigatório |
| `b` | Valor correspondente a b. | `não declarado` | obrigatório |
| `c` | Valor correspondente a c. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `volume_paralelepipedo3(a, b, c)`

**Origem da implementação:** `coral.numerico`

**Arquivo na release:** `coral/numerico.py`

:::

#### `rotacionar3`

Rotaciona um vetor 3D em torno de um eixo não nulo, em radianos.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `vetor` | Valor correspondente a vetor. | `não declarado` | obrigatório |
| `eixo` | Valor correspondente a eixo. | `não declarado` | obrigatório |
| `angulo` | Valor correspondente a angulo. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `rotacionar3(vetor, eixo, angulo)`

**Origem da implementação:** `coral.numerico`

**Arquivo na release:** `coral/numerico.py`

**Exceções diretamente observáveis no corpo:** `ErroNumerico`

:::

#### `transformar_ponto3`

Aplica uma transformação afim homogênea 4 × 4 a um ponto 3D.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `ponto` | Valor correspondente a ponto. | `não declarado` | obrigatório |
| `transformacao` | Valor correspondente a transformacao. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `transformar_ponto3(ponto, transformacao)`

**Origem da implementação:** `coral.numerico`

**Arquivo na release:** `coral/numerico.py`

**Exceções diretamente observáveis no corpo:** `ErroNumerico`

:::

#### `matriz_rotacao3`

Matriz 3 × 3 de Rodrigues para rotação em torno de um eixo 3D.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `eixo` | Valor correspondente a eixo. | `não declarado` | obrigatório |
| `angulo` | Valor correspondente a angulo. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `matriz_rotacao3(eixo, angulo)`

**Origem da implementação:** `coral.numerico`

**Arquivo na release:** `coral/numerico.py`

**Exceções diretamente observáveis no corpo:** `ErroNumerico`

:::

#### `matriz_translacao3`

Matriz afim 4 × 4 de translação 3D em convenção de vetor coluna.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `dx` | Valor correspondente a dx. | `não declarado` | obrigatório |
| `dy` | Valor correspondente a dy. | `não declarado` | obrigatório |
| `dz` | Valor correspondente a dz. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `matriz_translacao3(dx, dy, dz)`

**Origem da implementação:** `coral.numerico`

**Arquivo na release:** `coral/numerico.py`

:::

#### `matriz_escala3`

Matriz afim 4 × 4 de escala uniforme ou independente por eixo.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `sx` | Valor correspondente a sx. | `não declarado` | obrigatório |
| `sy` | Valor correspondente a sy. | `não declarado` | `None` |
| `sz` | Valor correspondente a sz. | `não declarado` | `None` |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `matriz_escala3(sx, sy = None, sz = None)`

**Origem da implementação:** `coral.numerico`

**Arquivo na release:** `coral/numerico.py`

**Exceções diretamente observáveis no corpo:** `ErroNumerico`

:::

#### `compor_transformacoes3`

Compõe transformações 3D na ordem em que são aplicadas ao ponto.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `*transformacoes` | Valor correspondente a transformacoes. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `compor_transformacoes3(*transformacoes)`

**Origem da implementação:** `coral.numerico`

**Arquivo na release:** `coral/numerico.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `*transformacoes` | variádico |

**Exceções diretamente observáveis no corpo:** `ErroNumerico`

:::

#### `transformar_vetor3`

Aplica a parte linear de uma transformação afim, ignorando translação.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `vetor` | Valor correspondente a vetor. | `não declarado` | obrigatório |
| `transformacao` | Valor correspondente a transformacao. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `transformar_vetor3(vetor, transformacao)`

**Origem da implementação:** `coral.numerico`

**Arquivo na release:** `coral/numerico.py`

**Exceções diretamente observáveis no corpo:** `ErroNumerico`

:::

#### `distancia_ponto_plano3`

Distância euclidiana não negativa entre um ponto e um plano 3D.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `ponto` | Valor correspondente a ponto. | `não declarado` | obrigatório |
| `ponto_plano` | Valor correspondente a ponto plano. | `não declarado` | obrigatório |
| `normal` | Valor correspondente a normal. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `distancia_ponto_plano3(ponto, ponto_plano, normal)`

**Origem da implementação:** `coral.numerico`

**Arquivo na release:** `coral/numerico.py`

**Exceções diretamente observáveis no corpo:** `ErroNumerico`

:::

#### `projetar_ponto_plano3`

Projeção ortogonal de um ponto sobre um plano 3D.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `ponto` | Valor correspondente a ponto. | `não declarado` | obrigatório |
| `ponto_plano` | Valor correspondente a ponto plano. | `não declarado` | obrigatório |
| `normal` | Valor correspondente a normal. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `projetar_ponto_plano3(ponto, ponto_plano, normal)`

**Origem da implementação:** `coral.numerico`

**Arquivo na release:** `coral/numerico.py`

**Exceções diretamente observáveis no corpo:** `ErroNumerico`

:::

#### `intersecao_reta_plano3`

Interseção reta plano; retorna None para paralelas distintas.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `origem` | Origem usada pela operação. | `não declarado` | obrigatório |
| `direcao` | Valor correspondente a direcao. | `não declarado` | obrigatório |
| `ponto_plano` | Valor correspondente a ponto plano. | `não declarado` | obrigatório |
| `normal` | Valor correspondente a normal. | `não declarado` | obrigatório |
| `tolerancia` | Valor correspondente a tolerancia. | `não declarado` | `1e-12` |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `intersecao_reta_plano3(origem, direcao, ponto_plano, normal, *, tolerancia = 1e-12)`

**Origem da implementação:** `coral.numerico`

**Arquivo na release:** `coral/numerico.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `origem` | posicional |
| `direcao` | posicional |
| `ponto_plano` | posicional |
| `normal` | posicional |
| `tolerancia` | nomeado |

**Exceções diretamente observáveis no corpo:** `ErroNumerico`

:::

#### `coordenadas_esfericas3`

Converte (x, y, z) em (raio, azimute, elevação), em radianos.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `ponto` | Valor correspondente a ponto. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `coordenadas_esfericas3(ponto)`

**Origem da implementação:** `coral.numerico`

**Arquivo na release:** `coral/numerico.py`

:::

#### `ponto_de_esfericas3`

Converte (raio, azimute, elevação) para ponto cartesiano 3D.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `raio` | Valor correspondente a raio. | `não declarado` | obrigatório |
| `azimute` | Valor correspondente a azimute. | `não declarado` | obrigatório |
| `elevacao` | Valor correspondente a elevacao. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `ponto_de_esfericas3(raio, azimute, elevacao)`

**Origem da implementação:** `coral.numerico`

**Arquivo na release:** `coral/numerico.py`

**Exceções diretamente observáveis no corpo:** `ErroNumerico`

:::

#### `area_triangulo3`

Área do triângulo definido por três pontos 3D.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `a` | Valor correspondente a a. | `não declarado` | obrigatório |
| `b` | Valor correspondente a b. | `não declarado` | obrigatório |
| `c` | Valor correspondente a c. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `area_triangulo3(a, b, c)`

**Origem da implementação:** `coral.numerico`

**Arquivo na release:** `coral/numerico.py`

**Exceções diretamente observáveis no corpo:** `ErroNumerico`

:::

#### `volume_tetraedro3`

Volume do tetraedro definido por quatro pontos 3D.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `a` | Valor correspondente a a. | `não declarado` | obrigatório |
| `b` | Valor correspondente a b. | `não declarado` | obrigatório |
| `c` | Valor correspondente a c. | `não declarado` | obrigatório |
| `d` | Valor correspondente a d. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `volume_tetraedro3(a, b, c, d)`

**Origem da implementação:** `coral.numerico`

**Arquivo na release:** `coral/numerico.py`

**Exceções diretamente observáveis no corpo:** `ErroNumerico`

:::

#### `transposta`

Obtém a matriz transposta.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valor` | Valor processado pela operação. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `transposta(valor)`

**Origem da implementação:** `coral.numerico`

**Arquivo na release:** `coral/numerico.py`

:::

#### `produto_escalar`

Combinar dois vetores.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `a` | Valor correspondente a a. | `não declarado` | obrigatório |
| `b` | Valor correspondente a b. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `produto_escalar(a, b)`

**Origem da implementação:** `coral.numerico`

**Arquivo na release:** `coral/numerico.py`

**Exceções diretamente observáveis no corpo:** `ErroNumerico`

:::

#### `multiplicar_matrizes`

Multiplica duas matrizes compatíveis.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `a` | Valor correspondente a a. | `não declarado` | obrigatório |
| `b` | Valor correspondente a b. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `multiplicar_matrizes(a, b)`

**Origem da implementação:** `coral.numerico`

**Arquivo na release:** `coral/numerico.py`

**Exceções diretamente observáveis no corpo:** `ErroNumerico`

:::

#### `determinante`

Medir determinante de matriz.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `m` | Valor correspondente a m. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `determinante(m)`

**Origem da implementação:** `coral.numerico`

**Arquivo na release:** `coral/numerico.py`

**Exceções diretamente observáveis no corpo:** `ErroNumerico`

:::

#### `inversa`

Calcula a matriz inversa quando ela existe.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `m` | Valor correspondente a m. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `inversa(m)`

**Origem da implementação:** `coral.numerico`

**Arquivo na release:** `coral/numerico.py`

**Exceções diretamente observáveis no corpo:** `ErroNumerico`

:::

#### `resolver_sistema`

Resolver sistema linear.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `coeficientes` | Valor correspondente a coeficientes. | `não declarado` | obrigatório |
| `termos` | Valor correspondente a termos. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `resolver_sistema(coeficientes, termos)`

**Origem da implementação:** `coral.numerico`

**Arquivo na release:** `coral/numerico.py`

**Exceções diretamente observáveis no corpo:** `ErroNumerico`

:::

#### `autovalores`

Calcula os autovalores da matriz.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `m` | Valor correspondente a m. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `autovalores(m)`

**Origem da implementação:** `coral.numerico`

**Arquivo na release:** `coral/numerico.py`

**Exceções diretamente observáveis no corpo:** `ErroNumerico`

:::

#### `forma`

Obtém forma.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valor` | Valor processado pela operação. | `não declarado` | obrigatório |

**Retorno**

Retorna um valor declarado como `tuple[int, ...]`.

:::details Detalhes técnicos

**Assinatura:** `forma(valor) -> tuple[int, ...]`

**Origem da implementação:** `coral.numerico`

**Arquivo na release:** `coral/numerico.py`

:::

### Classes e protocolos

#### `ResultadoMinimosQuadrados`

Resultado estruturado de :func:`minimos_quadrados`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `solucao` | Valor correspondente a solucao. | `Any` | obrigatório |
| `residuos` | Valor correspondente a residuos. | `Any` | obrigatório |
| `posto` | Valor correspondente a posto. | `int` | obrigatório |
| `valores_singulares` | Valor correspondente a valores singulares. | `Any` | obrigatório |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `solucao` | Valor correspondente a solucao. | `Any` | obrigatório |
| `residuos` | Valor correspondente a residuos. | `Any` | obrigatório |
| `posto` | Valor correspondente a posto. | `int` | obrigatório |
| `valores_singulares` | Valor correspondente a valores singulares. | `Any` | obrigatório |

:::details Detalhes técnicos

**Assinatura:** `ResultadoMinimosQuadrados(solucao: Any, residuos: Any, posto: int, valores_singulares: Any)`

**Origem da implementação:** `coral.numerico`

**Arquivo na release:** `coral/numerico.py`

:::

#### `ResultadoRegressaoLinear`

Ajuste linear simples com resíduos e coeficiente de determinação.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `inclinacao` | Valor correspondente a inclinacao. | `float` | obrigatório |
| `intercepto` | Valor correspondente a intercepto. | `float` | obrigatório |
| `residuos` | Valor correspondente a residuos. | `Any` | obrigatório |
| `r_quadrado` | Valor correspondente a r quadrado. | `float` | obrigatório |
| `quantidade` | Quantidade de itens solicitada. | `int` | obrigatório |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `inclinacao` | Valor correspondente a inclinacao. | `float` | obrigatório |
| `intercepto` | Valor correspondente a intercepto. | `float` | obrigatório |
| `residuos` | Valor correspondente a residuos. | `Any` | obrigatório |
| `r_quadrado` | Valor correspondente a r quadrado. | `float` | obrigatório |
| `quantidade` | Quantidade de itens solicitada. | `int` | obrigatório |

:::details Detalhes técnicos

**Assinatura:** `ResultadoRegressaoLinear(inclinacao: float, intercepto: float, residuos: Any, r_quadrado: float, quantidade: int)`

**Origem da implementação:** `coral.numerico`

**Arquivo na release:** `coral/numerico.py`

:::

#### `ResultadoBootstrap`

Intervalo percentil obtido por reamostragem bootstrap.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `estimativa` | Valor correspondente a estimativa. | `float` | obrigatório |
| `inferior` | Valor correspondente a inferior. | `float` | obrigatório |
| `superior` | Valor correspondente a superior. | `float` | obrigatório |
| `confianca` | Valor correspondente a confianca. | `float` | obrigatório |
| `repeticoes` | Valor correspondente a repeticoes. | `int` | obrigatório |
| `semente` | Semente usada para tornar a sequência reproduzível. | `int` | obrigatório |
| `tamanho_amostra` | Valor correspondente a tamanho amostra. | `int` | obrigatório |
| `custo_estimado` | Valor correspondente a custo estimado. | `int` | obrigatório |
| `metodo` | Valor correspondente a metodo. | `str` | `'bootstrap_percentil'` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `estimativa` | Valor correspondente a estimativa. | `float` | obrigatório |
| `inferior` | Valor correspondente a inferior. | `float` | obrigatório |
| `superior` | Valor correspondente a superior. | `float` | obrigatório |
| `confianca` | Valor correspondente a confianca. | `float` | obrigatório |
| `repeticoes` | Valor correspondente a repeticoes. | `int` | obrigatório |
| `semente` | Semente usada para tornar a sequência reproduzível. | `int` | obrigatório |
| `tamanho_amostra` | Valor correspondente a tamanho amostra. | `int` | obrigatório |
| `custo_estimado` | Valor correspondente a custo estimado. | `int` | obrigatório |
| `metodo` | Valor correspondente a metodo. | `str` | `'bootstrap_percentil'` |

:::details Detalhes técnicos

**Assinatura:** `ResultadoBootstrap(estimativa: float, inferior: float, superior: float, confianca: float, repeticoes: int, semente: int, tamanho_amostra: int, custo_estimado: int, metodo: str = 'bootstrap_percentil')`

**Origem da implementação:** `coral.numerico`

**Arquivo na release:** `coral/numerico.py`

:::

#### `ResultadoTestePermutacao`

Resultado de um teste de permutação bilateral entre duas amostras.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `diferenca_observada` | Valor correspondente a diferenca observada. | `float` | obrigatório |
| `valor_p` | Valor correspondente a valor p. | `float` | obrigatório |
| `repeticoes` | Valor correspondente a repeticoes. | `int` | obrigatório |
| `semente` | Semente usada para tornar a sequência reproduzível. | `int` | obrigatório |
| `tamanho_a` | Valor correspondente a tamanho a. | `int` | obrigatório |
| `tamanho_b` | Valor correspondente a tamanho b. | `int` | obrigatório |
| `custo_estimado` | Valor correspondente a custo estimado. | `int` | obrigatório |
| `metodo` | Valor correspondente a metodo. | `str` | `'permutacao_bilateral'` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `diferenca_observada` | Valor correspondente a diferenca observada. | `float` | obrigatório |
| `valor_p` | Valor correspondente a valor p. | `float` | obrigatório |
| `repeticoes` | Valor correspondente a repeticoes. | `int` | obrigatório |
| `semente` | Semente usada para tornar a sequência reproduzível. | `int` | obrigatório |
| `tamanho_a` | Valor correspondente a tamanho a. | `int` | obrigatório |
| `tamanho_b` | Valor correspondente a tamanho b. | `int` | obrigatório |
| `custo_estimado` | Valor correspondente a custo estimado. | `int` | obrigatório |
| `metodo` | Valor correspondente a metodo. | `str` | `'permutacao_bilateral'` |

:::details Detalhes técnicos

**Assinatura:** `ResultadoTestePermutacao(diferenca_observada: float, valor_p: float, repeticoes: int, semente: int, tamanho_a: int, tamanho_b: int, custo_estimado: int, metodo: str = 'permutacao_bilateral')`

**Origem da implementação:** `coral.numerico`

**Arquivo na release:** `coral/numerico.py`

:::

### Exceções

#### `DependenciaNumericaAusente`

Representa a condição de erro DependenciaNumericaAusente.

:::details Detalhes técnicos

**Assinatura:** `DependenciaNumericaAusente(...)`

**Origem da implementação:** `coral.numerico`

**Arquivo na release:** `coral/numerico.py`

:::

#### `ErroNumerico`

Erro público para entradas numéricas inválidas ou operações incompatíveis.

:::details Detalhes técnicos

**Assinatura:** `ErroNumerico(...)`

**Origem da implementação:** `coral.numerico`

**Arquivo na release:** `coral/numerico.py`

:::

<!-- /AUTO:API -->

## Compatibilidade e dependências

NumPy é opcional. O módulo pode ser importado sem ele, mas operações que dependem da biblioteca científica exigem a capacidade instalada no ambiente de execução.
