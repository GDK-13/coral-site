# Introdução

Coral é uma linguagem de programação com sintaxe corrente em português. A proposta é aproximar o código da forma como uma pessoa descreve uma ideia, sem abrir mão de parser, AST, tipos, módulos, ferramentas e contratos reais de linguagem.

## Por onde começar

Se você nunca usou Coral, a sequência mais simples é instalar a distribuição, executar um único arquivo e só depois criar um projeto com `coral.toml`.

1. Instale a release estável.
2. Abra a página **Seu primeiro programa**.
3. Execute um arquivo `.coral` diretamente.
4. Quando precisar de módulos e testes, crie um projeto.
5. Instale a extensão Coral Language no VS Code para ter LSP, debug, testes e navegação integrados.

## O que a Coral oferece

A linguagem cobre programação geral e também domínios que costumam exigir bastante infraestrutura: arquivos, JSON, matemática, aleatoriedade, jogos, mundos, regras reativas, RPG, experimentos, hardware e integração com o sistema.

A biblioteca padrão é organizada em módulos `coral.*`. Cada módulo tem uma página própria nesta documentação.

## Português corrente com equivalência determinística

A Coral amplia o português corrente por equivalências explícitas, não por interpretação livre. Formas diferentes que significam a mesma operação convergem para a mesma estrutura semântica, de modo que parser, formatador, LSP e ferramentas continuem concordando sobre o programa.

A linha 1.5.19 ampliou esse vocabulário com formas como `passa a ser`, `aumente`, `diminua`, `devolva`, comparações com `é`, pertencimento com `está em`, condições sem `então`, laços sem `faça`, consultas de vazio e faixa, operações de coleção e conversões naturais. As formas anteriores continuam válidas.

```coral
defina idade como 18
aumente idade em 1

se idade é maior que 18
    mostre "maior de idade"
fim
```

A Coral 1.6.0 preserva essa superfície pública e reorganiza o interior da linguagem em fronteiras explícitas entre parser, AST, backend, runtime e biblioteca padrão. A equivalência estrutural da AST passa a ser usada para provar que formas superficiais equivalentes do português corrente convergem para a mesma estrutura semântica.

## Arquivo único ou projeto

Um arquivo `.coral` pode ser executado sozinho. Isso é útil para estudar, experimentar uma ideia ou escrever pequenos programas.

Projetos passam a ser interessantes quando você precisa de vários módulos, testes, recursos, caminhos de importação ou configuração compartilhada. Nesse caso, `coral.toml` vira a fonte de configuração do projeto.

> Comece pequeno. A Coral não obriga você a criar um projeto para executar um único arquivo.

## Ferramentas oficiais

A distribuição estável reúne o runtime Coral, a extensão Coral Language para VS Code, exemplos oficiais e o Livro Oficial. A versão técnica do runtime e a edição do Livro podem evoluir separadamente.
