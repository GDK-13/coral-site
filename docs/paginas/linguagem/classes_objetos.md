# Classes e objetos

Classes descrevem objetos que combinam estado e operações. Cada instância pode manter valores próprios, e classes podem compartilhar comportamento por herança.

## Criar uma classe

```coral
crie a classe Contador
    ao criar uma Contador com inicial
        defina seu valor como inicial
    fim

    método somar com quantidade
        adicione quantidade a seu valor
    fim

    propriedade atual
        retorne seu valor
    fim
fim

crie contador como uma Contador com 10
execute contador.somar(5)
mostre contador.atual
```

:::resultado
O objeto começa com valor `10`, o método soma `5` e a propriedade retorna `15`.
:::

`ao criar` define a inicialização da instância. As formas `seu`, `sua`, `seus` e `suas` acessam atributos do objeto atual.

## Métodos e propriedades

`método nome` declara uma operação de instância. `propriedade nome` permite consultar um valor como atributo. A linguagem também possui formas para método estático, método de classe e definição de propriedade quando esses comportamentos forem necessários.

## Herança simples

```coral
crie a classe Pessoa
    ao criar uma Pessoa com nome
        defina seu nome como nome
    fim
fim

crie a classe Aluno herda de Pessoa
    ao criar uma Aluno com nome e nota
        inicialize a classe pai com nome
        defina sua nota como nota
    fim

    método aprovado
        retorne sua nota for maior ou igual a 7
    fim
fim

crie aluno como uma Aluno com "Ana" e 9
mostre aluno.nome
mostre aluno.aprovado()
```

:::resultado
`Aluno` reaproveita a inicialização de `Pessoa`, guarda a nota e o método `aprovado` retorna verdadeiro.
:::

## Herança múltipla

Uma classe pode declarar mais de uma base em ordem explícita. A Coral usa resolução C3 para determinar a ordem de procura e evitar repetir uma base comum em hierarquias em diamante.

```coral
crie a classe Raiz
    método nomes retornando lista de texto
        retorne ["Raiz"]
    fim
fim

crie a classe A herda de Raiz
    método nomes retornando lista de texto
        retorne ["A"] mais (chame o método pai nomes)
    fim
fim

crie a classe B herda de Raiz
    método nomes retornando lista de texto
        retorne ["B"] mais (chame o método pai nomes)
    fim
fim

crie a classe C herda de A e B
    método nomes retornando lista de texto
        retorne ["C"] mais (chame o método pai nomes)
    fim
fim

crie objeto como uma C
mostre objeto.nomes()
```

:::resultado
A chamada segue a ordem cooperativa da hierarquia e produz `C`, `A`, `B` e `Raiz`, sem visitar `Raiz` duas vezes.
:::

Bases repetidas, ciclos, bases conhecidas que não são classes e ordens de herança comprovadamente inconsistentes recebem diagnóstico antes da execução.

## Cooperação entre classes pai

Dentro de métodos de instância ou de classe, `chame o método pai` continua a cadeia conforme a ordem de resolução. Em construtores, `inicialize a classe pai` faz a mesma cooperação para a inicialização.

A Coral não chama automaticamente todos os construtores das bases. Cada classe participante precisa cooperar explicitamente quando a cadeia de inicialização for necessária.

Use herança quando a relação de especialização fizer sentido. Quando um objeto apenas precisa conter ou usar outro, composição costuma ser mais simples.
