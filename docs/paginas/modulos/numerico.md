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

A release 1.6.0 usa `coral.numerico` no projeto de laboratório de algoritmos. O trecho abaixo vem de `Exemplos/Projetos_Completos/Vitrine/laboratorio_algoritmos/analise.coral`:

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
defina relatorio como ler_json(caminho)
    defina tempos como [medicao["tempo_segundos"] para cada medicao em relatorio["medicoes"] se medicao["erro"] for igual a nada]
    crie um vetor chamado serie com tempos
    calcule a média de serie como media_serie
    calcule o desvio padrão de serie como desvio_serie
    retorne {"media": media_serie, "mediana": mediana(serie), "desvio": desvio_serie}
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
