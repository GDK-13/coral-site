# coral.aleatorio

## Visão geral

`coral.aleatorio` oferece aleatoriedade reproduzível e simulação. Use quando um programa precisa de sorteios, amostras ou simulações reproduzíveis. Uma fonte com semente fixa é especialmente útil em testes.

<!-- AUTO:MODULO -->

**Importação:** `coral.aleatorio`  
**Categoria:** simulacao  

aleatoriedade reproduzível e simulação

> Aviso: Não usar para senhas, chaves, tokens ou outros segredos.

### Superfície pública detectada

`FonteAleatoria`, `fonte`, `inteiro`, `decimal`, `escolher`, `amostra`, `escolha_ponderada`, `embaralhar`

<!-- /AUTO:MODULO -->

## Quando usar

Use quando um programa precisa de sorteios, amostras ou simulações reproduzíveis. Uma fonte com semente fixa é especialmente útil em testes.

Entre as entradas públicas detectadas estão `FonteAleatoria`, `fonte`, `inteiro`, `decimal`, `escolher`, `amostra`.

## Começando

A release inclui um exemplo real em `Exemplos/Dados/03_aleatorio_e_persistencia.coral`:

```coral
# Aleatoriedade reproduzível e persistência portátil.
de coral.aleatorio importe fonte
de coral.persistencia importe salvar, carregar

defina gerador_a como fonte(42)
defina gerador_b como fonte(42)
defina primeiro como gerador_a.inteiro(1, 100)
defina segundo como gerador_b.inteiro(1, 100)
garanta que primeiro for igual a segundo

defina dados como {"ponto": (3, 4), "tags": {"a", "b"}}
```

## Cuidados

Não use aleatoriedade comum para segredos. Para tokens e bytes seguros, use `coral.criptografia`.

## Relações com outros módulos

Consulte a navegação lateral para módulos que fornecem dados, sistema, texto ou runtime complementar.

## Referência da API

<!-- AUTO:API -->

### Funções

#### `fonte(semente = None) -> FonteAleatoria`

Entrada pública `fonte` da superfície `coral.aleatorio`.

**Implementação:** `coral.stdlib.aleatorio`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `semente` | `não declarado` | `None` | posicional |

**Retorno:** `FonteAleatoria`

#### `inteiro(minimo, maximo, *, fonte: FonteAleatoria | None = None)`

Entrada pública `inteiro` da superfície `coral.aleatorio`.

**Implementação:** `coral.stdlib.aleatorio`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `minimo` | `não declarado` | obrigatório | posicional |
| `maximo` | `não declarado` | obrigatório | posicional |
| `fonte` | `FonteAleatoria \| None` | `None` | nomeado |

**Retorno:** `não declarado`

#### `decimal(minimo = 0.0, maximo = 1.0, *, fonte: FonteAleatoria | None = None)`

Entrada pública `decimal` da superfície `coral.aleatorio`.

**Implementação:** `coral.stdlib.aleatorio`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `minimo` | `não declarado` | `0.0` | posicional |
| `maximo` | `não declarado` | `1.0` | posicional |
| `fonte` | `FonteAleatoria \| None` | `None` | nomeado |

**Retorno:** `não declarado`

#### `escolher(valores, *, fonte: FonteAleatoria | None = None)`

Entrada pública `escolher` da superfície `coral.aleatorio`.

**Implementação:** `coral.stdlib.aleatorio`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `valores` | `não declarado` | obrigatório | posicional |
| `fonte` | `FonteAleatoria \| None` | `None` | nomeado |

**Retorno:** `não declarado`

#### `amostra(valores, quantidade, *, fonte: FonteAleatoria | None = None)`

Entrada pública `amostra` da superfície `coral.aleatorio`.

**Implementação:** `coral.stdlib.aleatorio`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `valores` | `não declarado` | obrigatório | posicional |
| `quantidade` | `não declarado` | obrigatório | posicional |
| `fonte` | `FonteAleatoria \| None` | `None` | nomeado |

**Retorno:** `não declarado`

#### `escolha_ponderada(valores, pesos, *, fonte: FonteAleatoria | None = None)`

Entrada pública `escolha_ponderada` da superfície `coral.aleatorio`.

**Implementação:** `coral.stdlib.aleatorio`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `valores` | `não declarado` | obrigatório | posicional |
| `pesos` | `não declarado` | obrigatório | posicional |
| `fonte` | `FonteAleatoria \| None` | `None` | nomeado |

**Retorno:** `não declarado`

**Exceções observáveis no corpo:** `ValueError`

#### `embaralhar(valores, *, fonte: FonteAleatoria | None = None)`

Entrada pública `embaralhar` da superfície `coral.aleatorio`.

**Implementação:** `coral.stdlib.aleatorio`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `valores` | `não declarado` | obrigatório | posicional |
| `fonte` | `FonteAleatoria \| None` | `None` | nomeado |

**Retorno:** `não declarado`

### Classes e protocolos

#### `FonteAleatoria(semente: Any = None)`

Fonte reproduzível quando criada com semente explícita.

**Implementação:** `coral.stdlib.aleatorio`

**Atributos declarados**

| Nome | Tipo | Padrão |
|---|---|---|
| `semente` | `Any` | `None` |

**Métodos e propriedades públicas**

| Nome | Tipo | Assinatura | Retorno | Descrição |
|---|---|---|---|---|
| `inteiro` | método | `inteiro(minimo, maximo)` | `não declarado` | Sem docstring própria na release. |
| `decimal` | método | `decimal(minimo = 0.0, maximo = 1.0)` | `não declarado` | Sem docstring própria na release. |
| `escolher` | método | `escolher(valores)` | `não declarado` | Sem docstring própria na release. |
| `amostra` | método | `amostra(valores, quantidade)` | `não declarado` | Sem docstring própria na release. |
| `escolha_ponderada` | método | `escolha_ponderada(valores, pesos)` | `não declarado` | Sem docstring própria na release. |
| `embaralhar` | método | `embaralhar(valores)` | `não declarado` | Sem docstring própria na release. |

<!-- /AUTO:API -->
