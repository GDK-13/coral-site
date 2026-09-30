# Introdução

Coral é uma linguagem de programação com sintaxe corrente em português. A proposta é aproximar o código da forma como uma pessoa descreve uma ideia, sem abrir mão de parser, AST, tipos, módulos, testes, depuração e ferramentas reais de linguagem.

## Por onde começar

Se você nunca usou Coral, a sequência mais simples é instalar a distribuição, executar um único arquivo e só depois criar um projeto com `coral.toml`.

1. Instale a distribuição estável.
2. Abra **Seu primeiro programa**.
3. Execute um arquivo `.coral` diretamente.
4. Quando precisar de módulos e testes, crie um projeto.
5. Instale Coral Language no VS Code para ter navegação, diagnósticos, testes e depuração integrados.

## O que a Coral oferece

A linguagem cobre programação geral e também domínios especializados: arquivos, JSON, matemática, computação numérica, estatística, gráficos 2D e 3D, experimentos, geração procedural, Web, jogos, mundos, regras reativas, RPG, sistema e hardware.

A biblioteca padrão é organizada em módulos `coral.*`. Cada módulo tem uma página própria nesta documentação e pode ser consultado pelo nome ou pelo guia **O que você quer fazer?**.

## Português corrente com equivalência determinística

A Coral amplia o português corrente por equivalências explícitas, não por interpretação livre. Formas diferentes que representam a mesma operação convergem para a mesma estrutura semântica, de modo que parser, formatador, LSP e ferramentas continuem concordando sobre o programa.

O vocabulário corrente inclui atribuições e mutações naturais, comparações com `é`, pertencimento com `está em`, consultas de vazio e faixa, operações de coleção, conversões e chamadas naturais.

```coral
defina idade como 18
aumente idade em 1

se idade é maior que 18
    mostre "maior de idade"
fim
```

:::resultado
A variável `idade` passa a valer `19` e o programa mostra `maior de idade`.
:::

## Arquivo único ou projeto

Um arquivo `.coral` pode ser executado sozinho. Isso é útil para estudar, experimentar uma ideia ou escrever pequenos programas.

Projetos passam a ser interessantes quando você precisa de vários módulos, testes, recursos, caminhos de importação ou configuração compartilhada. Nesse caso, `coral.toml` vira a fonte de configuração do projeto.

> Comece pequeno. A Coral não obriga você a criar um projeto para executar um único arquivo.

## Ferramentas oficiais

A distribuição estável reúne runtime Coral, Coral Language para VS Code, exemplos oficiais e o Livro Oficial. O site prioriza o estado atual da linguagem; mudanças entre versões ficam isoladas na página **Notas de versão**.
