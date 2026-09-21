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

## Quando usar

Use para operações matemáticas fundamentais que aparecem em programas comuns sem exigir a camada numérica mais ampla.

Entre as entradas públicas detectadas estão `raiz`, `potencia`, `absoluto`, `arredondar`, `minimo`, `maximo`.

## Começando

Uma importação seletiva começa assim:

```coral
de coral.matematica importe raiz, potencia, absoluto
```

Depois da importação, use o hover e o preenchimento do VS Code para consultar a assinatura exata disponível na release.

## Cuidados

Para vetores, matrizes e estatística, consulte também `coral.numerico`.

## Relações com outros módulos

Consulte a navegação lateral para módulos que fornecem dados, sistema, texto ou runtime complementar.

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
