# Tipos e tipagem

A Coral é dinamicamente tipada e permite anotações opcionais. As anotações documentam intenção, ajudam o analisador e o editor e podem revelar incompatibilidades comprovadas, mas não convertem valores automaticamente nem tornam toda execução estaticamente tipada.

## Consultar o tipo de um valor

As consultas naturais servem para os descritores básicos da linguagem.

```coral
defina valor como 42

se valor for do tipo inteiro então
    mostre o nome do tipo de valor
fim

defina tipo como o tipo de valor
mostre tipo
```

:::resultado
O teste reconhece `valor` como inteiro. As consultas usam o mesmo contrato oferecido por `coral.tipos`.
:::

Booleano não é tratado como inteiro. Para tipos definidos pelo programa, use a API explícita de `coral.tipos` quando precisar de uma consulta dinâmica.

## Anotar variáveis e parâmetros

```coral
defina idade do tipo inteiro como 19

crie a função dobro com numero do tipo inteiro retornando inteiro
    retorne numero vezes 2
fim

mostre dobro(idade)
```

:::resultado
A anotação informa a intenção de tipo e a função retorna `38`.
:::

## Coleções tipadas

A edição corrente permite descrever a estrutura interna das coleções, não apenas o nome genérico do contêiner.

```coral
defina notas do tipo lista de decimal como [8, 9.5]
defina tags do tipo conjunto de texto como {"coral", "linguagem"}
defina idades do tipo dicionário de texto para inteiro como {"Ana": 19}
defina pessoa do tipo tupla de (texto, inteiro) como ("Ana", 19)

mostre notas
mostre pessoa[1]
```

:::resultado
`notas`, `tags`, `idades` e `pessoa` preservam o comportamento normal das coleções, enquanto a anotação fornece informação estrutural ao analisador e ao editor.
:::

Tipos podem ser compostos. Por exemplo, `dicionário de texto para lista de inteiro` representa um dicionário cujos valores conhecidos são listas de inteiros.

## Valores que também podem ser nulos

A forma `T ou nulo` informa que o valor pode ter o tipo descrito ou ser nulo.

```coral
defina apelido do tipo texto ou nulo como nulo
defina medidas do tipo lista de (inteiro ou nulo) como [10, nulo, 30]

mostre apelido
mostre medidas
```

:::resultado
`apelido` aceita texto ou `nulo`. Em `medidas`, a lista existe e cada elemento pode ser inteiro ou nulo.
:::

A posição dos parênteses importa. `lista de inteiro ou nulo` descreve uma lista que também pode ser nula. `lista de (inteiro ou nulo)` descreve uma lista existente cujos elementos podem ser nulos.

A nulidade é a união estrutural suportada por esta edição. Formas gerais como `inteiro ou texto` não pertencem ao contrato atual.

## Verificação conservadora

A Coral não inventa certeza quando o tipo de um valor não pode ser provado. Coleções mutáveis também são tratadas de forma conservadora: uma `lista de inteiro` não é assumida como `lista de decimal` apenas por existir relação útil entre valores numéricos individuais.

Uma anotação também não é uma conversão. Se o dado chega como texto, converta explicitamente.

```coral
defina entrada como "12"
defina idade como converta entrada para inteiro
mostre idade mais 1
```

:::resultado
A conversão produz o inteiro `12`; a soma então produz `13`.
:::

Tipos simples continuam incluindo `inteiro`, `decimal`, `texto`, `booleano`, `lista`, `dicionário`, `conjunto`, `tupla`, `qualquer`, `nulo` e nomes de classes.

Para operações detalhadas de inspeção de tipo, consulte [`coral.tipos`](../modulos/tipos.html). Para conversões explícitas, consulte [`coral.conversoes`](../modulos/conversoes.html).
