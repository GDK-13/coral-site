# coral.matematica

## Visão geral

`coral.matematica` oferece operações matemáticas fundamentais recorrentes. Use para operações matemáticas fundamentais que aparecem em programas comuns sem exigir a camada numérica mais ampla.

<!-- AUTO:MODULO -->

**Importação:** `coral.matematica`  
**Categoria:** matematica  

operações matemáticas fundamentais recorrentes

### Superfície pública detectada

`raiz`, `potencia`, `absoluto`, `arredondar`, `minimo`, `maximo`, `soma`, `media`, `seno`, `cosseno`, `tangente`, `piso`, `teto`, `truncar`, `log`, `exp`, `graus`, `radianos`, `limitar`, `finito`, `mdc`, `mmc`, `pi`, `e`

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

A documentação desta página descreve a superfície detectada na **Coral 1.5.9**. O gerador do site atualiza automaticamente o inventário e a referência da API quando uma nova release é importada, mas o texto pedagógico desta seção permanece sob revisão humana.

## Referência da API

<!-- AUTO:API -->

### Funções

#### `raiz(valor)`

Entrada pública `raiz` da superfície `coral.matematica`.

**Implementação:** `coral.stdlib.matematica`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `valor` | `não declarado` | obrigatório | posicional |

**Retorno:** `não declarado`

#### `potencia(base, expoente)`

Entrada pública `potencia` da superfície `coral.matematica`.

**Implementação:** `coral.stdlib.matematica`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `base` | `não declarado` | obrigatório | posicional |
| `expoente` | `não declarado` | obrigatório | posicional |

**Retorno:** `não declarado`

#### `absoluto(valor)`

Entrada pública `absoluto` da superfície `coral.matematica`.

**Implementação:** `coral.stdlib.matematica`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `valor` | `não declarado` | obrigatório | posicional |

**Retorno:** `não declarado`

#### `arredondar(valor, casas = 0)`

Entrada pública `arredondar` da superfície `coral.matematica`.

**Implementação:** `coral.stdlib.matematica`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `valor` | `não declarado` | obrigatório | posicional |
| `casas` | `não declarado` | `0` | posicional |

**Retorno:** `não declarado`

#### `minimo(valores)`

Entrada pública `minimo` da superfície `coral.matematica`.

**Implementação:** `coral.stdlib.matematica`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `valores` | `não declarado` | obrigatório | posicional |

**Retorno:** `não declarado`

#### `maximo(valores)`

Entrada pública `maximo` da superfície `coral.matematica`.

**Implementação:** `coral.stdlib.matematica`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `valores` | `não declarado` | obrigatório | posicional |

**Retorno:** `não declarado`

#### `soma(valores)`

Entrada pública `soma` da superfície `coral.matematica`.

**Implementação:** `coral.stdlib.matematica`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `valores` | `não declarado` | obrigatório | posicional |

**Retorno:** `não declarado`

#### `media(valores)`

Entrada pública `media` da superfície `coral.matematica`.

**Implementação:** `coral.stdlib.matematica`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `valores` | `não declarado` | obrigatório | posicional |

**Retorno:** `não declarado`

**Exceções observáveis no corpo:** `ValueError`

#### `seno(valor)`

Entrada pública `seno` da superfície `coral.matematica`.

**Implementação:** `coral.stdlib.matematica`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `valor` | `não declarado` | obrigatório | posicional |

**Retorno:** `não declarado`

#### `cosseno(valor)`

Entrada pública `cosseno` da superfície `coral.matematica`.

**Implementação:** `coral.stdlib.matematica`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `valor` | `não declarado` | obrigatório | posicional |

**Retorno:** `não declarado`

#### `tangente(valor)`

Entrada pública `tangente` da superfície `coral.matematica`.

**Implementação:** `coral.stdlib.matematica`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `valor` | `não declarado` | obrigatório | posicional |

**Retorno:** `não declarado`

#### `piso(valor)`

Entrada pública `piso` da superfície `coral.matematica`.

**Implementação:** `coral.stdlib.matematica`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `valor` | `não declarado` | obrigatório | posicional |

**Retorno:** `não declarado`

#### `teto(valor)`

Entrada pública `teto` da superfície `coral.matematica`.

**Implementação:** `coral.stdlib.matematica`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `valor` | `não declarado` | obrigatório | posicional |

**Retorno:** `não declarado`

#### `truncar(valor)`

Entrada pública `truncar` da superfície `coral.matematica`.

**Implementação:** `coral.stdlib.matematica`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `valor` | `não declarado` | obrigatório | posicional |

**Retorno:** `não declarado`

#### `log(valor, base = None)`

Entrada pública `log` da superfície `coral.matematica`.

**Implementação:** `coral.stdlib.matematica`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `valor` | `não declarado` | obrigatório | posicional |
| `base` | `não declarado` | `None` | posicional |

**Retorno:** `não declarado`

#### `exp(valor)`

Entrada pública `exp` da superfície `coral.matematica`.

**Implementação:** `coral.stdlib.matematica`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `valor` | `não declarado` | obrigatório | posicional |

**Retorno:** `não declarado`

#### `graus(valor)`

Entrada pública `graus` da superfície `coral.matematica`.

**Implementação:** `coral.stdlib.matematica`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `valor` | `não declarado` | obrigatório | posicional |

**Retorno:** `não declarado`

#### `radianos(valor)`

Entrada pública `radianos` da superfície `coral.matematica`.

**Implementação:** `coral.stdlib.matematica`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `valor` | `não declarado` | obrigatório | posicional |

**Retorno:** `não declarado`

#### `limitar(valor, minimo, maximo)`

Entrada pública `limitar` da superfície `coral.matematica`.

**Implementação:** `coral.stdlib.matematica`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `valor` | `não declarado` | obrigatório | posicional |
| `minimo` | `não declarado` | obrigatório | posicional |
| `maximo` | `não declarado` | obrigatório | posicional |

**Retorno:** `não declarado`

**Exceções observáveis no corpo:** `ValueError`

#### `finito(valor)`

Entrada pública `finito` da superfície `coral.matematica`.

**Implementação:** `coral.stdlib.matematica`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `valor` | `não declarado` | obrigatório | posicional |

**Retorno:** `não declarado`

#### `mdc(*valores)`

Entrada pública `mdc` da superfície `coral.matematica`.

**Implementação:** `coral.stdlib.matematica`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `*valores` | `não declarado` | obrigatório | variádico |

**Retorno:** `não declarado`

#### `mmc(*valores)`

Entrada pública `mmc` da superfície `coral.matematica`.

**Implementação:** `coral.stdlib.matematica`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `*valores` | `não declarado` | obrigatório | variádico |

**Retorno:** `não declarado`

### Constantes e aliases

#### `pi`

Alias público de tipo ou valor.

**Implementação:** `coral.stdlib.matematica`

**Valor declarado:** `math.pi`

#### `e`

Alias público de tipo ou valor.

**Implementação:** `coral.stdlib.matematica`

**Valor declarado:** `math.e`

<!-- /AUTO:API -->
