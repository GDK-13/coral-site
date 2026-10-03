# Programa principal

`programa principal` é uma entrada opcional para organizar aplicações sem obrigar todo arquivo Coral a seguir esse formato. Scripts lineares continuam válidos.

## Entrada explícita da aplicação

```coral
programa principal
    mostre "Olá, Coral!"
    chame apresentar com "Ana"
fim

crie a função apresentar com nome
    mostre "Olá, " mais nome
fim
```

:::resultado
Ao executar o arquivo diretamente, o módulo é inicializado e o bloco principal roda uma única vez. A função declarada abaixo já está disponível quando a entrada começa.
:::

O bloco não recebe parâmetros, não declara tipo de retorno e não cria uma função pública chamada `principal`.

## Arquivo importado como módulo

Um arquivo que contém `programa principal` ainda pode ser importado. Nesse caso, seus símbolos públicos ficam disponíveis, mas a entrada principal não é executada. Isso evita efeitos inesperados em testes e bibliotecas.

## `chame`, `execute` e retorno

Use `chame nome com argumentos` quando a intenção for invocar uma função pelo nome e ignorar seu retorno. Use `execute EXPRESSAO` para executar por efeito uma chamada escrita como expressão, como `execute objeto.metodo()`.

`programa principal` não precisa de nenhuma dessas formas para começar: a execução direta do arquivo inicia o bloco automaticamente.

Um `retorne` vazio pode encerrar a entrada antecipadamente, mas a entrada principal não devolve um valor.

## Limites

Só pode existir uma entrada principal válida por módulo, e ela precisa estar no nível do módulo. Não coloque `programa principal` dentro de condição, repetição, função, classe, tratamento de erro ou seleção por padrão.

REPL e execução interativa de trechos não iniciam esse bloco porque não representam a execução completa do módulo.
