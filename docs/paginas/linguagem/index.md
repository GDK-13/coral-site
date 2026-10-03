# Fundamentos da linguagem

A documentação da Coral é dividida em duas camadas. **Linguagem** explica as construções que existem no próprio código, como variáveis, expressões, funções, classes e controle de fluxo. **Módulos** documentam a biblioteca padrão `coral.*`, como arquivos, JSON, matemática, gráficos e jogos.

Você não precisa importar um módulo para criar uma variável, escrever uma condição, declarar uma função, definir uma classe, anotar tipos estruturais ou usar `programa principal`. Esses recursos pertencem à linguagem.

## Percurso recomendado

Se você está começando, siga esta ordem:

1. **Valores e variáveis** para entender estado e atribuição.
2. **Operadores e expressões** para combinar valores.
3. **Condições e repetições** para controlar o fluxo.
4. **Funções e escopo** para organizar comportamento reutilizável.
5. **Programa principal** para declarar uma entrada explícita quando o arquivo representar uma aplicação.
6. **Classes e objetos** para combinar estado, operações e herança.
7. **Tipos e tipagem** para anotações simples, coleções tipadas e nulidade.
8. **Coleções e compreensões** para trabalhar com grupos de valores.
9. **Erros e padrões** para tratar falhas e selecionar estruturas.
10. **Geradores e assíncrono** quando precisar de execução sob demanda ou concorrência cooperativa.

## Um exemplo que combina os fundamentos

```coral
defina notas como [7, 8, 9]
defina total como 0

para cada nota em notas faça
    adicione nota a total
fim

defina media como total dividido por quantidade de notas

se media for maior ou igual a 7 então
    mostre "Aprovado"
senão
    mostre "Revisar conteúdo"
fim
```

:::resultado
A lista guarda as notas, o laço acumula o total, a expressão calcula a média e a condição escolhe a mensagem final.
:::

## Linguagem e biblioteca padrão

Uma mesma tarefa pode combinar as duas camadas. `defina`, `se`, `para`, `crie a função` e `crie a classe` pertencem à linguagem. Já operações como ler arquivos, interpretar JSON ou criar gráficos são oferecidas por módulos da biblioteca padrão.

Quando a dúvida for **como escrever o programa**, comece nesta seção. Quando a dúvida for **qual recurso pronto usar**, consulte os módulos ou o guia **O que você quer fazer?**.
