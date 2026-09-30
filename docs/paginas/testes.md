# Testes

A Coral trata testes como parte do fluxo normal de um projeto. O objetivo é executar casos rapidamente pela CLI ou pelo VS Code e manter testes próximos do código que eles verificam.

## Teste básico

Um projeto pode manter seus casos em uma pasta de testes declarada no `coral.toml`. O runner descobre esses casos e o VS Code os apresenta no Test Explorer.

## Executar pela CLI

A CLI expõe o runner por comandos próprios. Para descobrir as opções disponíveis na edição atual, consulte **REPL e CLI** ou execute a ajuda do runtime.

## Test Explorer

No VS Code, testes podem ser executados, repetidos e depurados sem abrir um terminal separado. Casos parametrizados, grupos e skips são representados quando o runner fornece essa informação.

## Testes rápidos e testes de ambiente

Casos puramente lógicos devem permanecer rápidos e reproduzíveis. Testes que dependem de janela, áudio, entrada física, GPU, rede local ou hardware devem declarar essa dependência de ambiente em vez de mascará la como falha lógica.

## Boa prática

Mantenha cada teste focado em um comportamento observável. Quando um recurso depende de tempo, aleatoriedade ou entrada, prefira as fontes controláveis oferecidas pelos módulos correspondentes para tornar o caso repetível.
