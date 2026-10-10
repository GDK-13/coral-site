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

A linguagem cobre programação geral e também domínios especializados: arquivos, JSON, SQLite, matemática, computação numérica, estatística, gráficos 2D e 3D, experimentos, geração procedural, Web, jogos, mundos, regras reativas, RPG, sistema e hardware. A linguagem também oferece tipagem opcional estrutural para coleções e nulidade, herança múltipla com resolução C3, uma entrada opcional `programa principal` e concorrência controlada sobre o modelo assíncrono existente.

A documentação separa **fundamentos da linguagem** de **biblioteca padrão**. Variáveis, operadores, condições, repetições, funções, classes, objetos, tipagem, coleções e tratamento de erros possuem uma seção própria porque fazem parte da linguagem e não de um módulo `coral.*`.

A biblioteca padrão é organizada em módulos `coral.*`. Cada módulo tem uma página própria e pode ser consultado pelo nome ou pelo guia **O que você quer fazer?**.

Se a dúvida for sobre como escrever código Coral, comece por [**Fundamentos da linguagem**](linguagem/index.html). Se a dúvida for sobre uma capacidade pronta da biblioteca, consulte os módulos.

## Português corrente com equivalência determinística

A Coral amplia o português corrente por equivalências explícitas, não por interpretação livre. Formas diferentes que representam a mesma operação convergem para a mesma estrutura semântica, de modo que parser, formatador, LSP e ferramentas continuem concordando sobre o programa.

Além de atribuições, comparações e coleções, a edição corrente permite consultar tipos, converter valores e usar operações básicas de entrada, arquivos, texto, coleções e JSON sem esconder a API equivalente.

```coral
defina entrada como "18"
defina idade como converta entrada para inteiro

se idade for do tipo inteiro então
    mostre o nome do tipo de idade
fim
```

:::resultado
`idade` recebe o inteiro `18`. O teste natural usa o mesmo contrato de `coral.tipos.e_tipo`, e a consulta mostra o nome Coral do tipo.
:::

As chamadas explícitas continuam disponíveis quando você precisa de argumentos opcionais, ordenação reversa, codificação ou outros controles que a forma curta não expressa.

## Escrever Coral com consistência

A Coral 1.8 consolida um guia canônico de escrita. Ele recomenda nomes que expressem intenção, imports públicos explícitos, quatro espaços por nível, uso consciente das formas compacta e multilinha e separação clara entre definições e entrada da aplicação.

Essas recomendações não são uma nova sintaxe e não transformam preferências de estilo em erros. Consulte [**Estilo e legibilidade**](linguagem/estilo_legibilidade.html) para exemplos curtos e regras de uso.

## Arquivo único ou projeto

Um arquivo `.coral` pode ser executado sozinho. Isso é útil para estudar, experimentar uma ideia ou escrever pequenos programas.

Projetos passam a ser interessantes quando você precisa de vários módulos, testes, recursos, caminhos de importação ou configuração compartilhada. Nesse caso, `coral.toml` vira a fonte de configuração do projeto.

> Comece pequeno. A Coral não obriga você a criar um projeto para executar um único arquivo.

## Ferramentas oficiais

A distribuição estável reúne runtime Coral, Coral Language para VS Code, exemplos oficiais e o Livro Oficial. O editor usa a análise da própria Coral para entender o papel de símbolos, assinaturas e imports, com TextMate como fallback quando o documento ainda está incompleto.

O site prioriza o estado atual da linguagem; mudanças entre versões ficam isoladas na página **Notas de versão**.
