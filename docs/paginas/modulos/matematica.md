# coral.matematica

## Visão geral

`coral.matematica` oferece operações matemáticas fundamentais recorrentes. Use para operações matemáticas fundamentais que aparecem em programas comuns sem exigir a camada numérica mais ampla.

<!-- AUTO:MODULO -->

**Importação:** `coral.matematica`  
**Categoria:** matematica  

operações matemáticas fundamentais recorrentes

### Superfície pública detectada

`raiz`, `potencia`, `absoluto`, `arredondar`, `minimo`, `maximo`, `soma`, `media`, `fatorial`, `combinacoes`, `arranjos`, `hipotenusa`, `aproximadamente_igual`, `interpolar_linear`, `seno`, `cosseno`, `tangente`, `arco_seno`, `arco_cosseno`, `arco_tangente`, `piso`, `teto`, `truncar`, `log`, `log10`, `log2`, `exp`, `graus`, `radianos`, `raiz_nesima`, `produto`, `sinal`, `volume_bola3`, `limitar`, `finito`, `mdc`, `mmc`, `pi`, `e`

<!-- /AUTO:MODULO -->

## Papel no ecossistema

Reúne operações matemáticas fundamentais recorrentes para código geral. É complementar a `coral.numerico`, que concentra estruturas e recursos numéricos mais amplos.

## Conceitos principais

### Aritmética e agregação

`raiz`, `potencia`, `absoluto`, `arredondar`, `soma`, `media`, `minimo` e `maximo` cobrem operações comuns.

### Trigonometria

`seno`, `cosseno`, `tangente`, `graus` e `radianos` permitem trabalhar explicitamente com ângulos.

### Arredondamento e limites

`piso`, `teto`, `truncar` e `limitar` controlam transformação de faixa e discretização.

### Exponenciais

`log` e `exp` cobrem transformações exponenciais e logarítmicas.

### Inteiros

`mdc` e `mmc` tratam relações entre inteiros; `finito` ajuda a verificar valores numéricos.

### Constantes

`pi` e `e` ficam disponíveis como constantes públicas.

## Quando usar

Use este módulo quando o problema corresponder diretamente aos conceitos acima. Por ser um módulo complementar, ele normalmente entra em um programa para resolver uma responsabilidade específica e deve permanecer desacoplado da lógica central sempre que possível.

## Começando

```coral
de coral.matematica importe raiz, media, seno, pi

mostre raiz(81)
mostre media([2, 4, 6, 8])
mostre seno(pi / 2)
```

## API essencial

| Entrada | Papel |
|---|---|
| `raiz` / `potencia` | potências e raízes |
| `soma` / `media` | agregação |
| `seno` / `cosseno` / `tangente` | trigonometria |
| `piso` / `teto` / `truncar` | arredondamento direcional |
| `log` / `exp` | exponenciais |
| `limitar` | restringir faixa |
| `mdc` / `mmc` | inteiros |
| `pi` / `e` | constantes |

A seção **Referência da API** no fim desta página contém a superfície pública completa detectada na release, com assinaturas, parâmetros, retornos e docstrings quando presentes.

## Fluxos comuns

1. Escolha a operação com unidade e domínio corretos.
2. Converta graus para radianos quando a API trigonométrica exigir radianos.
3. Valide domínio antes de raiz ou log quando a entrada puder ser inválida.
4. Use `coral.numerico` quando o problema evoluir para vetores, estatística, séries ou outros recursos de laboratório numérico.

## Erros e casos de borda

Raiz de valor fora do domínio real, log inválido, divisão implícita por condições inadequadas ou valores não finitos são casos que devem ser considerados pelo chamador.

## Boas práticas

* Documente a unidade de ângulos.
* Evite números mágicos para constantes já fornecidas.
* Teste tolerância numérica quando o resultado envolve ponto flutuante.

## Integração com outros módulos

`coral.numerico` amplia o domínio numérico; `coral.laboratorio` usa operações matemáticas em experimentos; `coral.jogos` aproveita funções periódicas em animações.

## Testabilidade e previsibilidade

Para ponto flutuante, compare com tolerância quando a igualdade exata não for matematicamente garantida. Casos de borda de domínio merecem testes separados.

## Compatibilidade e evolução

A documentação desta página descreve a superfície detectada na **Coral 1.7.4**. O gerador do site atualiza automaticamente o inventário e a referência da API quando uma nova release é importada, mas o texto pedagógico desta seção permanece sob revisão humana.

## Referência da API

<!-- AUTO:API -->

### Funções

#### `raiz`

Calcula uma raiz do valor informado.

**Exemplo**

```coral
de coral.matematica importe raiz, media, seno, pi

mostre raiz(81)
mostre media([2, 4, 6, 8])
mostre seno(pi / 2)
```

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valor` | Valor processado pela operação. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `raiz(valor)`

**Origem da implementação:** `coral.stdlib.matematica`

**Arquivo na release:** `coral/stdlib/matematica.py`

:::

#### `potencia`

Eleva um valor à potência informada.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `base` | Base usada pela conversão ou cálculo. | `não declarado` | obrigatório |
| `expoente` | Valor correspondente a expoente. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `potencia(base, expoente)`

**Origem da implementação:** `coral.stdlib.matematica`

**Arquivo na release:** `coral/stdlib/matematica.py`

:::

#### `absoluto`

Calcula o valor absoluto.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valor` | Valor processado pela operação. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `absoluto(valor)`

**Origem da implementação:** `coral.stdlib.matematica`

**Arquivo na release:** `coral/stdlib/matematica.py`

:::

#### `arredondar`

Arredonda o valor segundo a precisão solicitada.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valor` | Valor processado pela operação. | `não declarado` | obrigatório |
| `casas` | Valor correspondente a casas. | `não declarado` | `0` |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `arredondar(valor, casas = 0)`

**Origem da implementação:** `coral.stdlib.matematica`

**Arquivo na release:** `coral/stdlib/matematica.py`

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

**Origem da implementação:** `coral.stdlib.matematica`

**Arquivo na release:** `coral/stdlib/matematica.py`

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

**Origem da implementação:** `coral.stdlib.matematica`

**Arquivo na release:** `coral/stdlib/matematica.py`

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

**Origem da implementação:** `coral.stdlib.matematica`

**Arquivo na release:** `coral/stdlib/matematica.py`

:::

#### `media`

Calcula a média dos valores.

**Exemplo**

```coral
de coral.matematica importe raiz, media, seno, pi

mostre raiz(81)
mostre media([2, 4, 6, 8])
mostre seno(pi / 2)
```

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valores` | Coleção de valores processada. | `não declarado` | obrigatório |

**Retorno**

Retorna a média calculada.

:::details Detalhes técnicos

**Assinatura:** `media(valores)`

**Origem da implementação:** `coral.stdlib.matematica`

**Arquivo na release:** `coral/stdlib/matematica.py`

**Exceções diretamente observáveis no corpo:** `ValueError`

:::

#### `fatorial`

Fatorial de um inteiro não negativo.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `n` | Valor correspondente a n. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `fatorial(n)`

**Origem da implementação:** `coral.stdlib.matematica`

**Arquivo na release:** `coral/stdlib/matematica.py`

**Exceções diretamente observáveis no corpo:** `ValueError`

:::

#### `combinacoes`

Quantidade de escolhas de k elementos sem considerar ordem.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `n` | Valor correspondente a n. | `não declarado` | obrigatório |
| `k` | Valor correspondente a k. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `combinacoes(n, k)`

**Origem da implementação:** `coral.stdlib.matematica`

**Arquivo na release:** `coral/stdlib/matematica.py`

**Exceções diretamente observáveis no corpo:** `ValueError`

:::

#### `arranjos`

Quantidade de escolhas ordenadas de k elementos sem repetição.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `n` | Valor correspondente a n. | `não declarado` | obrigatório |
| `k` | Valor correspondente a k. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `arranjos(n, k)`

**Origem da implementação:** `coral.stdlib.matematica`

**Arquivo na release:** `coral/stdlib/matematica.py`

**Exceções diretamente observáveis no corpo:** `ValueError`

:::

#### `hipotenusa`

Comprimento euclidiano dos catetos a e b, calculado de forma estável.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `a` | Valor correspondente a a. | `não declarado` | obrigatório |
| `b` | Valor correspondente a b. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `hipotenusa(a, b)`

**Origem da implementação:** `coral.stdlib.matematica`

**Arquivo na release:** `coral/stdlib/matematica.py`

:::

#### `aproximadamente_igual`

Compara números reais com tolerâncias explícitas.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `a` | Valor correspondente a a. | `não declarado` | obrigatório |
| `b` | Valor correspondente a b. | `não declarado` | obrigatório |
| `tolerancia_relativa` | Valor correspondente a tolerancia relativa. | `não declarado` | `1e-09` |
| `tolerancia_absoluta` | Valor correspondente a tolerancia absoluta. | `não declarado` | `0.0` |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `aproximadamente_igual(a, b, tolerancia_relativa = 1e-09, tolerancia_absoluta = 0.0)`

**Origem da implementação:** `coral.stdlib.matematica`

**Arquivo na release:** `coral/stdlib/matematica.py`

**Exceções diretamente observáveis no corpo:** `ValueError`

:::

#### `interpolar_linear`

Interpola ou extrapola linearmente entre dois valores reais finitos.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `inicio` | Valor inicial do intervalo ou processo. | `não declarado` | obrigatório |
| `fim` | Valor final do intervalo ou processo. | `não declarado` | obrigatório |
| `fracao` | Valor correspondente a fracao. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `interpolar_linear(inicio, fim, fracao)`

**Origem da implementação:** `coral.stdlib.matematica`

**Arquivo na release:** `coral/stdlib/matematica.py`

:::

#### `seno`

Calcula o seno do ângulo.

**Exemplo**

```coral
de coral.matematica importe raiz, media, seno, pi

mostre raiz(81)
mostre media([2, 4, 6, 8])
mostre seno(pi / 2)
```

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valor` | Valor processado pela operação. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `seno(valor)`

**Origem da implementação:** `coral.stdlib.matematica`

**Arquivo na release:** `coral/stdlib/matematica.py`

:::

#### `cosseno`

Calcula o cosseno do ângulo.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valor` | Valor processado pela operação. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `cosseno(valor)`

**Origem da implementação:** `coral.stdlib.matematica`

**Arquivo na release:** `coral/stdlib/matematica.py`

:::

#### `tangente`

Calcula a tangente do ângulo.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valor` | Valor processado pela operação. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `tangente(valor)`

**Origem da implementação:** `coral.stdlib.matematica`

**Arquivo na release:** `coral/stdlib/matematica.py`

:::

#### `arco_seno`

Executa a operação `arco_seno` disponibilizada por `coral.matematica`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valor` | Valor processado pela operação. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `arco_seno(valor)`

**Origem da implementação:** `coral.stdlib.matematica`

**Arquivo na release:** `coral/stdlib/matematica.py`

**Exceções diretamente observáveis no corpo:** `ValueError`

:::

#### `arco_cosseno`

Executa a operação `arco_cosseno` disponibilizada por `coral.matematica`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valor` | Valor processado pela operação. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `arco_cosseno(valor)`

**Origem da implementação:** `coral.stdlib.matematica`

**Arquivo na release:** `coral/stdlib/matematica.py`

**Exceções diretamente observáveis no corpo:** `ValueError`

:::

#### `arco_tangente`

Executa a operação `arco_tangente` disponibilizada por `coral.matematica`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valor` | Valor processado pela operação. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `arco_tangente(valor)`

**Origem da implementação:** `coral.stdlib.matematica`

**Arquivo na release:** `coral/stdlib/matematica.py`

:::

#### `piso`

Obtém o maior inteiro que não ultrapassa o valor.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valor` | Valor processado pela operação. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `piso(valor)`

**Origem da implementação:** `coral.stdlib.matematica`

**Arquivo na release:** `coral/stdlib/matematica.py`

:::

#### `teto`

Obtém o menor inteiro que não é inferior ao valor.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valor` | Valor processado pela operação. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `teto(valor)`

**Origem da implementação:** `coral.stdlib.matematica`

**Arquivo na release:** `coral/stdlib/matematica.py`

:::

#### `truncar`

Remove a parte fracionária do valor segundo a operação suportada pela release.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valor` | Valor processado pela operação. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `truncar(valor)`

**Origem da implementação:** `coral.stdlib.matematica`

**Arquivo na release:** `coral/stdlib/matematica.py`

:::

#### `log`

Calcula o logaritmo do valor na base informada.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valor` | Valor processado pela operação. | `não declarado` | obrigatório |
| `base` | Base usada pela conversão ou cálculo. | `não declarado` | `None` |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `log(valor, base = None)`

**Origem da implementação:** `coral.stdlib.matematica`

**Arquivo na release:** `coral/stdlib/matematica.py`

:::

#### `log10`

Executa a operação `log10` disponibilizada por `coral.matematica`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valor` | Valor processado pela operação. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `log10(valor)`

**Origem da implementação:** `coral.stdlib.matematica`

**Arquivo na release:** `coral/stdlib/matematica.py`

**Exceções diretamente observáveis no corpo:** `ValueError`

:::

#### `log2`

Executa a operação `log2` disponibilizada por `coral.matematica`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valor` | Valor processado pela operação. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `log2(valor)`

**Origem da implementação:** `coral.stdlib.matematica`

**Arquivo na release:** `coral/stdlib/matematica.py`

**Exceções diretamente observáveis no corpo:** `ValueError`

:::

#### `exp`

Calcula a função exponencial do valor.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valor` | Valor processado pela operação. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `exp(valor)`

**Origem da implementação:** `coral.stdlib.matematica`

**Arquivo na release:** `coral/stdlib/matematica.py`

:::

#### `graus`

Converte um ângulo em radianos para graus.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valor` | Valor processado pela operação. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `graus(valor)`

**Origem da implementação:** `coral.stdlib.matematica`

**Arquivo na release:** `coral/stdlib/matematica.py`

:::

#### `radianos`

Converte um ângulo em graus para radianos.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valor` | Valor processado pela operação. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `radianos(valor)`

**Origem da implementação:** `coral.stdlib.matematica`

**Arquivo na release:** `coral/stdlib/matematica.py`

:::

#### `raiz_nesima`

Raiz real de índice inteiro positivo.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valor` | Valor processado pela operação. | `não declarado` | obrigatório |
| `indice` | Valor correspondente a indice. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `raiz_nesima(valor, indice)`

**Origem da implementação:** `coral.stdlib.matematica`

**Arquivo na release:** `coral/stdlib/matematica.py`

**Exceções diretamente observáveis no corpo:** `ValueError`

:::

#### `produto`

Multiplica os itens de uma coleção; a coleção vazia tem produto 1.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valores` | Coleção de valores processada. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `produto(valores)`

**Origem da implementação:** `coral.stdlib.matematica`

**Arquivo na release:** `coral/stdlib/matematica.py`

:::

#### `sinal`

Devolve -1, 0 ou 1 para um número real finito.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valor` | Valor processado pela operação. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `sinal(valor)`

**Origem da implementação:** `coral.stdlib.matematica`

**Arquivo na release:** `coral/stdlib/matematica.py`

:::

#### `volume_bola3`

Volume de uma bola euclidiana tridimensional de raio não negativo.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `raio` | Valor correspondente a raio. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `volume_bola3(raio)`

**Origem da implementação:** `coral.stdlib.matematica`

**Arquivo na release:** `coral/stdlib/matematica.py`

**Exceções diretamente observáveis no corpo:** `ValueError`

:::

#### `limitar`

Restringir faixa.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valor` | Valor processado pela operação. | `não declarado` | obrigatório |
| `minimo` | Limite mínimo considerado pela operação. | `não declarado` | obrigatório |
| `maximo` | Limite máximo considerado pela operação. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `limitar(valor, minimo, maximo)`

**Origem da implementação:** `coral.stdlib.matematica`

**Arquivo na release:** `coral/stdlib/matematica.py`

**Exceções diretamente observáveis no corpo:** `ValueError`

:::

#### `finito`

Indica se o valor numérico é finito.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valor` | Valor processado pela operação. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `finito(valor)`

**Origem da implementação:** `coral.stdlib.matematica`

**Arquivo na release:** `coral/stdlib/matematica.py`

:::

#### `mdc`

Calcula o máximo divisor comum.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `*valores` | Coleção de valores processada. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `mdc(*valores)`

**Origem da implementação:** `coral.stdlib.matematica`

**Arquivo na release:** `coral/stdlib/matematica.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `*valores` | variádico |

:::

#### `mmc`

Calcula o mínimo múltiplo comum.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `*valores` | Coleção de valores processada. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `mmc(*valores)`

**Origem da implementação:** `coral.stdlib.matematica`

**Arquivo na release:** `coral/stdlib/matematica.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `*valores` | variádico |

:::

### Constantes e aliases

#### `pi`

Expõe `pi` como parte da API pública do módulo.

**Exemplo**

```coral
de coral.matematica importe raiz, media, seno, pi

mostre raiz(81)
mostre media([2, 4, 6, 8])
mostre seno(pi / 2)
```

:::details Detalhes técnicos

**Assinatura:** `pi`

**Origem da implementação:** `coral.stdlib.matematica`

**Arquivo na release:** `coral/stdlib/matematica.py`

**Valor declarado:** `math.pi`

:::

#### `e`

Expõe `e` como parte da API pública do módulo.

:::details Detalhes técnicos

**Assinatura:** `e`

**Origem da implementação:** `coral.stdlib.matematica`

**Arquivo na release:** `coral/stdlib/matematica.py`

**Valor declarado:** `math.e`

:::

<!-- /AUTO:API -->
