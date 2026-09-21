# coral.numerico

## Visão geral

`coral.numerico` é a camada de computação numérica da Coral para vetores, matrizes, estatística e álgebra linear. O módulo foi desenhado para que a linguagem possa oferecer operações científicas sem transformar NumPy em dependência obrigatória de todo programa Coral.

<!-- AUTO:MODULO -->

**Importação:** `coral.numerico`  
**Categoria:** cientifico  

vetores, matrizes, estatística e álgebra numérica

### Superfície pública detectada

`DependenciaNumericaAusente`, `ErroNumerico`, `numpy_disponivel`, `diagnosticar_numerico`, `vetor`, `matriz`, `zeros`, `uns`, `intervalo`, `espaco_linear`, `soma`, `media`, `mediana`, `variancia`, `desvio_padrao`, `minimo`, `maximo`, `transposta`, `produto_escalar`, `multiplicar_matrizes`, `determinante`, `inversa`, `resolver_sistema`, `autovalores`, `forma`

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

A release 1.5.9 usa `coral.numerico` no projeto de laboratório de algoritmos. O trecho abaixo vem de `Exemplos/Projetos_Completos/Vitrine/laboratorio_algoritmos/analise.coral`:

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

#### `numpy_disponivel() -> bool`

Entrada pública `numpy_disponivel` da superfície `coral.numerico`.

**Retorno:** `bool`

#### `diagnosticar_numerico() -> dict[str, Any]`

Entrada pública `diagnosticar_numerico` da superfície `coral.numerico`.

**Retorno:** `dict[str, Any]`

#### `vetor(valores: Iterable[Any], tipo: Any | None = None)`

Entrada pública `vetor` da superfície `coral.numerico`.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `valores` | `Iterable[Any]` | obrigatório | posicional |
| `tipo` | `Any \| None` | `None` | posicional |

**Retorno:** `não declarado`

**Exceções observáveis no corpo:** `ErroNumerico`

#### `matriz(linhas: Iterable[Iterable[Any]], tipo: Any | None = None)`

Entrada pública `matriz` da superfície `coral.numerico`.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `linhas` | `Iterable[Iterable[Any]]` | obrigatório | posicional |
| `tipo` | `Any \| None` | `None` | posicional |

**Retorno:** `não declarado`

**Exceções observáveis no corpo:** `ErroNumerico`

#### `zeros(forma, tipo = float)`

Entrada pública `zeros` da superfície `coral.numerico`.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `forma` | `não declarado` | obrigatório | posicional |
| `tipo` | `não declarado` | `float` | posicional |

**Retorno:** `não declarado`

**Exceções observáveis no corpo:** `ErroNumerico`

#### `uns(forma, tipo = float)`

Entrada pública `uns` da superfície `coral.numerico`.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `forma` | `não declarado` | obrigatório | posicional |
| `tipo` | `não declarado` | `float` | posicional |

**Retorno:** `não declarado`

**Exceções observáveis no corpo:** `ErroNumerico`

#### `intervalo(inicio, fim = None, passo = 1, tipo = None)`

Entrada pública `intervalo` da superfície `coral.numerico`.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `inicio` | `não declarado` | obrigatório | posicional |
| `fim` | `não declarado` | `None` | posicional |
| `passo` | `não declarado` | `1` | posicional |
| `tipo` | `não declarado` | `None` | posicional |

**Retorno:** `não declarado`

**Exceções observáveis no corpo:** `ErroNumerico`

#### `espaco_linear(inicio, fim, quantidade = 50)`

Entrada pública `espaco_linear` da superfície `coral.numerico`.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `inicio` | `não declarado` | obrigatório | posicional |
| `fim` | `não declarado` | obrigatório | posicional |
| `quantidade` | `não declarado` | `50` | posicional |

**Retorno:** `não declarado`

**Exceções observáveis no corpo:** `ErroNumerico`

#### `soma(valores)`

Entrada pública `soma` da superfície `coral.numerico`.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `valores` | `não declarado` | obrigatório | posicional |

**Retorno:** `não declarado`

#### `media(valores)`

Entrada pública `media` da superfície `coral.numerico`.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `valores` | `não declarado` | obrigatório | posicional |

**Retorno:** `não declarado`

#### `mediana(valores)`

Entrada pública `mediana` da superfície `coral.numerico`.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `valores` | `não declarado` | obrigatório | posicional |

**Retorno:** `não declarado`

#### `variancia(valores, populacional = True)`

Entrada pública `variancia` da superfície `coral.numerico`.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `valores` | `não declarado` | obrigatório | posicional |
| `populacional` | `não declarado` | `True` | posicional |

**Retorno:** `não declarado`

**Exceções observáveis no corpo:** `ErroNumerico`

#### `desvio_padrao(valores, populacional = True)`

Entrada pública `desvio_padrao` da superfície `coral.numerico`.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `valores` | `não declarado` | obrigatório | posicional |
| `populacional` | `não declarado` | `True` | posicional |

**Retorno:** `não declarado`

**Exceções observáveis no corpo:** `ErroNumerico`

#### `minimo(valores)`

Entrada pública `minimo` da superfície `coral.numerico`.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `valores` | `não declarado` | obrigatório | posicional |

**Retorno:** `não declarado`

#### `maximo(valores)`

Entrada pública `maximo` da superfície `coral.numerico`.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `valores` | `não declarado` | obrigatório | posicional |

**Retorno:** `não declarado`

#### `transposta(valor)`

Entrada pública `transposta` da superfície `coral.numerico`.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `valor` | `não declarado` | obrigatório | posicional |

**Retorno:** `não declarado`

#### `produto_escalar(a, b)`

Entrada pública `produto_escalar` da superfície `coral.numerico`.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `a` | `não declarado` | obrigatório | posicional |
| `b` | `não declarado` | obrigatório | posicional |

**Retorno:** `não declarado`

**Exceções observáveis no corpo:** `ErroNumerico`

#### `multiplicar_matrizes(a, b)`

Entrada pública `multiplicar_matrizes` da superfície `coral.numerico`.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `a` | `não declarado` | obrigatório | posicional |
| `b` | `não declarado` | obrigatório | posicional |

**Retorno:** `não declarado`

**Exceções observáveis no corpo:** `ErroNumerico`

#### `determinante(m)`

Entrada pública `determinante` da superfície `coral.numerico`.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `m` | `não declarado` | obrigatório | posicional |

**Retorno:** `não declarado`

**Exceções observáveis no corpo:** `ErroNumerico`

#### `inversa(m)`

Entrada pública `inversa` da superfície `coral.numerico`.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `m` | `não declarado` | obrigatório | posicional |

**Retorno:** `não declarado`

**Exceções observáveis no corpo:** `ErroNumerico`

#### `resolver_sistema(coeficientes, termos)`

Entrada pública `resolver_sistema` da superfície `coral.numerico`.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `coeficientes` | `não declarado` | obrigatório | posicional |
| `termos` | `não declarado` | obrigatório | posicional |

**Retorno:** `não declarado`

**Exceções observáveis no corpo:** `ErroNumerico`

#### `autovalores(m)`

Entrada pública `autovalores` da superfície `coral.numerico`.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `m` | `não declarado` | obrigatório | posicional |

**Retorno:** `não declarado`

**Exceções observáveis no corpo:** `ErroNumerico`

#### `forma(valor) -> tuple[int, ...]`

Entrada pública `forma` da superfície `coral.numerico`.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `valor` | `não declarado` | obrigatório | posicional |

**Retorno:** `tuple[int, ...]`

### Exceções

#### `DependenciaNumericaAusente(...)`

Entrada pública `DependenciaNumericaAusente` da superfície `coral.numerico`.

#### `ErroNumerico(...)`

Erro público para entradas numéricas inválidas ou operações incompatíveis.

<!-- /AUTO:API -->

## Compatibilidade e dependências

NumPy é opcional. O módulo pode ser importado sem ele, mas operações que dependem da biblioteca científica exigem a capacidade instalada no ambiente de execução.
