# Valores e variáveis

Variáveis ligam nomes a valores. Elas permitem guardar estado, reutilizar resultados e alterar informações ao longo da execução.

## Criar e alterar uma variável

```coral
defina pontos como 10
adicione 5 a pontos
subtraia 2 de pontos
mostre pontos
```

:::resultado
`pontos` começa com `10`, passa por `15` e termina em `13`.
:::

`defina nome como expressão` cria ou atribui um nome. A forma `nome recebe expressão` também faz atribuição.

```coral
defina vidas como 3
vidas recebe 5
mostre vidas
```

:::resultado
A saída é `5`.
:::

## Valores básicos

A Coral possui literais para inteiros, decimais, textos, booleanos, ausência e coleções.

```coral
defina idade como 19
defina altura como 1.75
defina nome como "Ana"
defina ativo como verdadeiro
defina ausente como nulo
defina notas como [7, 8, 9]
defina perfil como {"nome": "Ana", "nivel": 2}
```

Inteiros não possuem parte fracionária. Decimais usam ponto no código. Textos aceitam aspas simples ou duplas. `verdadeiro` e `falso` representam valores lógicos. `nulo` representa ausência de valor.

## Textos multilinha

Quando um texto precisa ocupar várias linhas, a Coral 1.7.9 aceita três aspas duplas ou três aspas simples como delimitador. O resultado continua sendo um valor do tipo texto.

```coral
defina mensagem como """
    Olá!
    Este texto ocupa mais de uma linha.
    O recuo comum é removido.
"""

mostre mensagem
```

:::resultado
`mensagem` contém três linhas de texto sem o recuo usado apenas para organizar o código.
:::

Se o conteúdo começar logo depois das aspas, essa posição é preservada. Quando o conteúdo começa na linha seguinte, a primeira quebra é estrutural e não entra no valor. O mesmo vale para a última quebra quando o delimitador final está sozinho em sua própria linha.

O literal não interpola variáveis nem interpreta SQL, HTML, Markdown ou outro formato. Esses conteúdos continuam sendo apenas texto até que o programa os entregue a uma API específica.

## Atualizações em português corrente

Além de `adicione` e `subtraia`, a linguagem aceita formas correntes equivalentes para certas atualizações.

```coral
defina contador como 1
aumente contador em 4
diminua contador em 2
mostre contador
```

:::resultado
O valor final de `contador` é `3`.
:::

## Nomes e ordem de execução

Um nome deve existir antes de ser consultado, exceto quando é introduzido pelo próprio contexto, como um parâmetro de função. A ordem das instruções importa: uma linha posterior observa o estado produzido pelas anteriores.

Para consultar tipos ou anotar uma variável, continue em **Tipos e tipagem**.
