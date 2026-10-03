# Operadores e expressões

Expressões produzem valores. Elas podem combinar números, textos, comparações, chamadas, índices e outros resultados.

## Aritmética

```coral
defina a como 12
defina b como 5
mostre a mais b
mostre a menos b
mostre a vezes b
mostre a dividido por b
mostre a % b
```

:::resultado
As expressões calculam soma, subtração, multiplicação, divisão e resto, nessa ordem.
:::

As formas simbólicas equivalentes continuam disponíveis quando forem mais claras para o problema.

## Comparações

```coral
defina idade como 19
mostre idade for igual a 19
mostre idade for diferente de 20
mostre idade for maior que 18
mostre idade for menor ou igual a 19
```

:::resultado
As quatro comparações produzem valores lógicos verdadeiros.
:::

Não use `=` como comparação. Para igualdade, use `for igual a` ou a forma simbólica correspondente.

## Lógica

`e`, `ou` e `não` combinam condições.

```coral
defina idade como 19
defina possui_documento como verdadeiro

se idade for maior ou igual a 18 e possui_documento então
    mostre "entrada permitida"
fim
```

:::resultado
A mensagem é exibida porque as duas condições são verdadeiras.
:::

Quando uma expressão ficar ambígua para leitura humana, use parênteses para deixar a intenção explícita.

## Acesso, chamada e índice

Chamadas de função, acesso a membros e índices também são expressões.

```coral
defina dados como {"nome": "Lia", "notas": [8, 9]}
mostre dados["nome"]
mostre dados["notas"][0]
```

:::resultado
A primeira consulta mostra `Lia` e a segunda acessa a primeira nota.
:::
