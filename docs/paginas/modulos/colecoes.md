# coral.colecoes

## Visão geral

`coral.colecoes` oferece operações comuns sobre coleções. Use para operações recorrentes sobre listas e outras coleções, como ordenar, remover duplicatas, contar e agrupar pares.

<!-- AUTO:MODULO -->

**Importação:** `coral.colecoes`  
**Categoria:** dados  

operações comuns sobre coleções

### Superfície pública detectada

`ordenar`, `unicos`, `contar`, `primeiro`, `agrupar_pares`

<!-- /AUTO:MODULO -->

## Quando usar

Use para operações recorrentes sobre listas e outras coleções, como ordenar, remover duplicatas, contar e agrupar pares.

Entre as entradas públicas detectadas estão `ordenar`, `unicos`, `contar`, `primeiro`, `agrupar_pares`.

## Começando

Uma importação seletiva começa assim:

```coral
de coral.colecoes importe ordenar, unicos, contar
```

Depois da importação, use o hover e o preenchimento do VS Code para consultar a assinatura exata disponível na release.

## Cuidados

Prefira essas operações quando elas expressarem melhor a intenção do que um laço escrito apenas para manipulação básica.

## Relações com outros módulos

Na mesma área, veja também `coral.persistencia`.

## Referência da API

<!-- AUTO:API -->

### Funções

#### `ordenar(valores, reverso = False)`

Entrada pública `ordenar` da superfície `coral.colecoes`.

**Implementação:** `coral.stdlib.colecoes`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `valores` | `não declarado` | obrigatório | posicional |
| `reverso` | `não declarado` | `False` | posicional |

**Retorno:** `não declarado`

#### `unicos(valores)`

Entrada pública `unicos` da superfície `coral.colecoes`.

**Implementação:** `coral.stdlib.colecoes`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `valores` | `não declarado` | obrigatório | posicional |

**Retorno:** `não declarado`

#### `contar(valores)`

Entrada pública `contar` da superfície `coral.colecoes`.

**Implementação:** `coral.stdlib.colecoes`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `valores` | `não declarado` | obrigatório | posicional |

**Retorno:** `não declarado`

#### `primeiro(valores, padrao = None)`

Entrada pública `primeiro` da superfície `coral.colecoes`.

**Implementação:** `coral.stdlib.colecoes`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `valores` | `não declarado` | obrigatório | posicional |
| `padrao` | `não declarado` | `None` | posicional |

**Retorno:** `não declarado`

#### `agrupar_pares(chaves, valores)`

Entrada pública `agrupar_pares` da superfície `coral.colecoes`.

**Implementação:** `coral.stdlib.colecoes`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `chaves` | `não declarado` | obrigatório | posicional |
| `valores` | `não declarado` | obrigatório | posicional |

**Retorno:** `não declarado`

<!-- /AUTO:API -->
