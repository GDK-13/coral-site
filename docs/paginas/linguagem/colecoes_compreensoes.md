# Coleções e compreensões

Listas, dicionários, tuplas e conjuntos são valores da própria linguagem. O módulo `coral.colecoes` complementa esses valores com operações prontas, mas os literais e o acesso básico não dependem dele.

## Listas

```coral
defina notas como [7, 8, 9]
coloque 10 em notas
mostre quantidade de notas
mostre notas[0]
mostre notas[1:3]
```

:::resultado
A lista passa a ter quatro elementos. O primeiro índice é zero e a fatia de `1` até antes de `3` contém `8` e `9`.
:::

## Dicionários

```coral
defina aluno como {"nome": "Ana", "nota": 8}
defina a chave "cidade" de aluno como "Timon"
mostre aluno["nome"]
mostre aluno["cidade"]
```

:::resultado
O dicionário relaciona chaves a valores e a nova chave `cidade` fica disponível imediatamente.
:::

## Tuplas e conjuntos

Tuplas representam sequências que não são alteradas como listas. Conjuntos representam elementos únicos. `{}` representa um dicionário vazio; use a forma própria de conjunto vazio quando precisar de um conjunto sem elementos.

```coral
defina coordenada como (10, 20)
defina unicos como {1, 1, 2}
mostre coordenada[0]
mostre quantidade de unicos
```

:::resultado
A primeira consulta retorna `10`. O conjunto possui dois valores únicos.
:::

## Compreensões

```coral
defina numeros como [1, 2, 3, 4]
defina pares_dobrados como [n vezes 2 para cada n em numeros se n % 2 for igual a 0]
mostre pares_dobrados
```

:::resultado
A compreensão filtra `2` e `4` e produz `[4, 8]`.
:::

## Desempacotamento

```coral
defina x e y como (10, 20)
mostre x
mostre y
```

:::resultado
`x` recebe `10` e `y` recebe `20`.
:::

Para ordenar, obter valores únicos, contar ocorrências e outras operações prontas, consulte [`coral.colecoes`](../modulos/colecoes.html).
