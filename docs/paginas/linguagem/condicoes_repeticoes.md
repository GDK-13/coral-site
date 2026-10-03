# Condições e repetições

Controle de fluxo decide quais instruções executam e quantas vezes elas se repetem.

## Decisões com `se`

```coral
defina media como 7

se media for maior ou igual a 7 então
    mostre "Aprovado"
senão se media for maior ou igual a 5 então
    mostre "Recuperação"
senão
    mostre "Reprovado"
fim
```

:::resultado
Com média `7`, apenas o primeiro ramo é executado.
:::

`senão se` e `senão` são opcionais. `fim` encerra a decisão.

## Repetir por intervalo

```coral
defina total como 0

para numero de 1 até 4 faça
    adicione numero a total
fim

mostre total
```

:::resultado
O limite final é incluído e o total resulta em `10`.
:::

Use `até antes de` quando o limite final não deve participar.

## Percorrer uma coleção

```coral
defina nomes como ["Ana", "Bia", "Caio"]

para cada nome em nomes faça
    mostre nome
fim
```

:::resultado
Cada nome é processado uma vez, na ordem da lista.
:::

## Repetir enquanto uma condição for verdadeira

```coral
defina restante como 3

 enquanto restante for maior que 0 faça
    mostre restante
    subtraia 1 de restante
fim
```

:::resultado
O laço mostra `3`, `2` e `1`, então termina quando `restante` chega a zero.
:::

## Interromper ou pular uma passagem

```coral
para n de 0 até antes de 5 faça
    se n for igual a 1 então
        continue
    fim
    se n for igual a 3 então
        pare
    fim
    mostre n
fim
```

:::resultado
São mostrados `0` e `2`. `continue` pula a passagem atual e `pare` encerra o laço mais próximo.
:::

`repita quantidade vezes` também pode ser usado quando você precisa repetir um bloco sem manter o contador manualmente.
