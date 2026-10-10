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

## Cabeçalhos de função multilinha

Quando uma função possui muitos parâmetros, o cabeçalho pode colocar cada declaração em sua própria linha. O bloco de parâmetros termina em `fim com`; o corpo continua até o `fim` da função.

```coral
crie a função somar com
    primeiro do tipo inteiro
    segundo do tipo inteiro opcional 2
fim com retornando inteiro
    retorne primeiro mais segundo
fim

mostre somar(3)
```

:::resultado
`segundo` usa o valor padrão `2`, então a chamada mostra `5`.
:::

Tipos, parâmetros opcionais e retorno continuam seguindo os mesmos contratos da forma compacta. A forma multilinha muda a organização visual, não a semântica da função.

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


## Chamadas explícitas multilinha

Quando uma chamada começa a ficar larga ou possui argumentos aninhados, a Coral 1.7.5 permite escrever cada argumento em sua própria linha. `com` no fim da linha abre a chamada e `fim` a encerra.

```coral
crie a função somar com a e b
    retorne a mais b
fim

crie a função calcular com a e b
    retorne a vezes b
fim

defina total como chame somar com
    10
    chame calcular com
        20
        30
    fim
fim

mostre total
```

:::resultado
A chamada interna produz `600`; a chamada externa soma `10` e mostra `610`.
:::

Em uma chamada multilinha, cada linha do bloco representa um argumento completo. Chamadas aninhadas têm o próprio `fim`. Comentários e linhas vazias não viram argumentos, e argumentos nomeados ou expansões continuam disponíveis. Os argumentos são avaliados uma vez, da esquerda para a direita.

Para uma chamada sem argumentos, continue usando `chame funcao`. Um bloco aberto com `com` precisa ter pelo menos um argumento e ser fechado com `fim`.
