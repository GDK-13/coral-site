# Estilo e legibilidade

A Coral 1.8 possui um guia canônico de escrita. Ele não cria uma segunda linguagem nem transforma preferências de estilo em erros de compilação. O objetivo é tornar programas mais fáceis de ler, revisar e manter.

## Ideia central

Prefira a forma que deixa a intenção mais clara. Uma construção curta pode continuar compacta; quando muitos argumentos, imports ou bases tornam a linha difícil de conferir, use a forma multilinha explícita já oferecida pela linguagem.

Quatro espaços por nível e cada `fim` alinhado com a construção que ele encerra formam a base visual recomendada.

## Organize definição e execução

`programa principal` é útil quando um arquivo reúne definições e também representa uma aplicação. Assim, importar o módulo não inicia o programa.

```coral
crie a função dobro com valor do tipo inteiro retornando inteiro
    retorne valor vezes 2
fim

programa principal
    mostre dobro(3)
fim
```

:::resultado
Ao executar o arquivo diretamente, a saída é `6`. Ao importar o módulo, o bloco principal não é iniciado.
:::

Scripts pequenos podem permanecer lineares quando isso for mais simples.

## Nomes e imports

Escolha nomes que indiquem o papel do valor, como `validar_item`, `processar_arquivo` ou `relatorio`. Mantenha o mesmo vocabulário no código e na documentação do projeto.

Importe explicitamente os símbolos usados de módulos públicos `coral.*`. Evite depender de helpers internos da implementação.

## Forma compacta e forma multilinha

Chamadas curtas ficam mais fáceis de ler em uma linha. Chamadas extensas podem usar um argumento por linha.

```coral
crie a função soma com a e b
    retorne a mais b
fim

defina total como chame soma com
    2,
    3
fim

mostre total
```

:::resultado
A chamada produz `5`. O `fim` depois dos argumentos pertence à chamada multilinha.
:::

A mesma ideia vale para cabeçalhos de função, imports e herança multilinha. Não suponha continuação automática apenas pela indentação: use os fechamentos previstos pela sintaxe.

## Tipos ajudam a explicar intenção

Anotações de parâmetros, retornos e coleções ajudam o editor e o leitor, mas não convertem valores nem substituem validação de dados externos.

```coral
de coral.conversoes importe inteiro

defina quantidade do tipo inteiro como inteiro("12")
mostre quantidade
```

:::resultado
`quantidade` recebe o inteiro `12` porque a conversão foi feita explicitamente.
:::

Declare `T ou nulo` quando a ausência fizer parte do contrato em vez de esconder essa possibilidade.

## Recursos e efeitos externos

Use contexto quando a API o oferecer e deixe efeitos externos visíveis no código. Quem abre uma conexão decide quando confirmar ou reverter uma transação. Valores SQL devem ser enviados por parâmetros separados da consulta.

Leitura gradual reduz materialização desnecessária, mas não torna toda aplicação de memória constante. Se o programa acumular os dados lidos para estatística, gráfico ou relatório, documente esse ponto.

## Concorrência controlada

Ao usar `FilaTarefas`, declare conscientemente o limite de simultaneidade, a política de falha e, quando necessário, timeouts e progresso. Cancelamento é cooperativo: uma função síncrona que já começou em uma thread auxiliar não é interrompida à força.

## Formatação

O formatador deve preservar a intenção do código e o conteúdo de textos multilinha. Aplicar a formatação novamente deve produzir o mesmo resultado.

O guia de estilo orienta escrita e manutenção. A referência normativa continua nas páginas da linguagem, dos módulos e no Volume II do Livro Oficial.
