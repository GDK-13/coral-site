# Funções e escopo

Funções agrupam comportamento reutilizável. Elas podem receber parâmetros, devolver valores e manter regras claras de escopo.

## Declarar e chamar uma função

```coral
crie a função dobro com numero
    retorne numero vezes 2
fim

mostre dobro(21)
```

:::resultado
A chamada retorna `42`.
:::

## Parâmetros opcionais

```coral
crie a função saudar com nome e prefixo opcional "Olá"
    retorne prefixo mais ", " mais nome
fim

mostre saudar("Ana")
mostre saudar(nome="Bia", prefixo="Oi")
```

:::resultado
A primeira chamada usa o valor opcional. A segunda fornece argumentos nomeados explicitamente.
:::

## Quantidade variável de argumentos

```coral
crie a função contar com vários valores
    retorne quantidade de valores
fim

mostre contar(10, 20, 30)
```

:::resultado
A função recebe três valores e retorna `3`.
:::

## Escopo léxico

Nomes criados dentro de uma função pertencem ao escopo daquela função. Uma função interna pode declarar que pretende alterar um nome do escopo externo.

```coral
crie a função criar_contador
    defina valor como 0

    crie a função proximo
        use valor do escopo externo
        adicione 1 a valor
        retorne valor
    fim

    retorne proximo
fim

defina contador como criar_contador()
mostre contador()
mostre contador()
```

:::resultado
As chamadas mostram `1` e `2`. A função interna preserva acesso ao estado criado pela função externa.
:::

## Chamadas naturais

Uma função pode declarar uma forma natural explícita. Isso não é interpretação livre de português: o padrão faz parte da declaração.

```coral
crie a função dobro com numero chamada como "dobre {numero}"
    retorne numero vezes 2
fim

mostre dobre 21
```

:::resultado
A forma natural chama a mesma função e produz `42`.
:::
