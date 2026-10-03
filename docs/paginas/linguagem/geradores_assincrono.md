# Geradores e assíncrono

Geradores produzem valores sob demanda. Funções assíncronas permitem esperar operações sem transformar toda a linguagem em execução concorrente implícita.

## Geradores

```coral
crie a função numeros com limite
    para n de 0 até antes de limite faça
        produza n
    fim
fim

para cada n em numeros(3) faça
    mostre n
fim
```

:::resultado
O gerador entrega `0`, `1` e `2` conforme o laço solicita novos valores.
:::

`produza` suspende a função e entrega um valor. Uma solicitação posterior continua a execução a partir daquele ponto.

## Funções assíncronas

```coral
crie a função assíncrona dobro_assincrono com numero
    espere 0 segundos
    retorne numero vezes 2
fim

crie a função assíncrona principal
    defina resultado como aguarde dobro_assincrono(21)
    mostre resultado
fim

execute assincronamente principal()
```

:::resultado
A função principal aguarda o resultado assíncrono e mostra `42`.
:::

Use assíncrono quando existir uma operação que realmente precise esperar ou cooperar com outra tarefa. Para temporizadores, eventos e recursos especializados, consulte os módulos correspondentes da biblioteca padrão.
