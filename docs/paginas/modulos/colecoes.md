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
