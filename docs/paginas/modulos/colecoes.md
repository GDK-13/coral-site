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

## Papel no ecossistema

Reúne operações pequenas e frequentes sobre coleções, deixando explícitas intenções que de outro modo exigiriam laços utilitários repetidos.

## Conceitos principais

### Ordenação

`ordenar` devolve uma coleção ordenada, com opção de ordem reversa.

### Unicidade

`unicos` remove repetições preservando a finalidade de produzir valores únicos.

### Contagem e primeiro valor

`contar` resume a quantidade e `primeiro` permite um valor padrão quando não há elemento.

### Pareamento

`agrupar_pares` transforma chaves e valores correspondentes em uma estrutura associativa.

## Quando usar

Use este módulo quando o problema corresponder diretamente aos conceitos acima. Por ser um módulo complementar, ele normalmente entra em um programa para resolver uma responsabilidade específica e deve permanecer desacoplado da lógica central sempre que possível.

## Começando

```coral
de coral.colecoes importe ordenar, unicos, primeiro

defina valores como [3, 1, 3, 2]
defina ordenados como ordenar(valores)
defina sem_repeticao como unicos(valores)
mostre ordenados
mostre sem_repeticao
mostre primeiro(ordenados, nulo)
```

## API essencial

| Entrada | Papel |
|---|---|
| `ordenar` | ordenar valores |
| `unicos` | obter valores únicos |
| `contar` | contar elementos |
| `primeiro` | obter primeiro ou padrão |
| `agrupar_pares` | associar chaves e valores |

A seção **Referência da API** no fim desta página contém a superfície pública completa detectada na release, com assinaturas, parâmetros, retornos e docstrings quando presentes.

## Fluxos comuns

1. Escolha a operação que descreve diretamente a intenção do passo.
2. Converta dados externos antes de ordenar ou agrupar quando os tipos ainda não estiverem coerentes.
3. Ao usar `primeiro`, escolha conscientemente se ausência deve virar um padrão ou ser tratada antes.

## Erros e casos de borda

Coleções heterogêneas podem não possuir uma ordem natural comparável. Pareamentos com tamanhos incompatíveis devem ser tratados conforme o contrato da função em vez de presumir preenchimento automático.

## Boas práticas

* Prefira estas operações a laços escritos apenas para uma transformação trivial.
* Não esconda uma regra de domínio importante em uma cadeia longa de utilitários.
* Use `unicos` quando unicidade é parte da intenção, não apenas como correção tardia de dados duplicados.

## Integração com outros módulos

`coral.texto` cuida de sequências textuais; `coral.persistencia` cuida de representação portátil; `coral.conversoes` ajuda a normalizar entradas antes de operar sobre coleções.

## Testabilidade e previsibilidade

Funções de coleção são boas candidatas a testes com entradas vazias, um único elemento, duplicatas e dados já ordenados.

## Compatibilidade e evolução

A documentação desta página descreve a superfície detectada na **Coral 1.5.9**. O gerador do site atualiza automaticamente o inventário e a referência da API quando uma nova release é importada, mas o texto pedagógico desta seção permanece sob revisão humana.

## Referência da API

<!-- AUTO:API -->

### Funções

#### `ordenar`

Ordenar valores.

**Exemplo**

```coral
de coral.colecoes importe ordenar, unicos, primeiro

defina valores como [3, 1, 3, 2]
defina ordenados como ordenar(valores)
defina sem_repeticao como unicos(valores)
mostre ordenados
mostre sem_repeticao
mostre primeiro(ordenados, nulo)
```

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valores` | Coleção de valores processada. | `não declarado` | obrigatório |
| `reverso` | Valor correspondente a reverso. | `não declarado` | `False` |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `ordenar(valores, reverso = False)`

**Origem da implementação:** `coral.stdlib.colecoes`

**Arquivo na release:** `coral/stdlib/colecoes.py`

:::

#### `unicos`

Obter valores únicos.

**Exemplo**

```coral
de coral.colecoes importe ordenar, unicos, primeiro

defina valores como [3, 1, 3, 2]
defina ordenados como ordenar(valores)
defina sem_repeticao como unicos(valores)
mostre ordenados
mostre sem_repeticao
mostre primeiro(ordenados, nulo)
```

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valores` | Coleção de valores processada. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `unicos(valores)`

**Origem da implementação:** `coral.stdlib.colecoes`

**Arquivo na release:** `coral/stdlib/colecoes.py`

:::

#### `contar`

Contar elementos.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valores` | Coleção de valores processada. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `contar(valores)`

**Origem da implementação:** `coral.stdlib.colecoes`

**Arquivo na release:** `coral/stdlib/colecoes.py`

:::

#### `primeiro`

Obter primeiro ou padrão.

**Exemplo**

```coral
de coral.colecoes importe ordenar, unicos, primeiro

defina valores como [3, 1, 3, 2]
defina ordenados como ordenar(valores)
defina sem_repeticao como unicos(valores)
mostre ordenados
mostre sem_repeticao
mostre primeiro(ordenados, nulo)
```

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valores` | Coleção de valores processada. | `não declarado` | obrigatório |
| `padrao` | Valor usado quando não há resultado específico disponível. | `não declarado` | `None` |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `primeiro(valores, padrao = None)`

**Origem da implementação:** `coral.stdlib.colecoes`

**Arquivo na release:** `coral/stdlib/colecoes.py`

:::

#### `agrupar_pares`

Associar chaves e valores.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `chaves` | Valor correspondente a chaves. | `não declarado` | obrigatório |
| `valores` | Coleção de valores processada. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `agrupar_pares(chaves, valores)`

**Origem da implementação:** `coral.stdlib.colecoes`

**Arquivo na release:** `coral/stdlib/colecoes.py`

:::

<!-- /AUTO:API -->
