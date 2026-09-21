# Testes

A Coral trata testes como parte da linguagem e do fluxo de projeto. O objetivo é permitir validação rápida durante o desenvolvimento sem transformar a suíte em uma sequência cada vez mais lenta.

## Teste básico

Um projeto pode manter seus casos em uma pasta de testes declarada no `coral.toml`. O runner descobre esses casos e o VS Code os apresenta no Test Explorer.

## Executar pela CLI

A CLI expõe o runner por comandos próprios. Para descobrir as opções disponíveis na release atual, consulte a página **REPL e CLI** ou execute a ajuda do runtime.

## Test Explorer

No VS Code, testes podem ser executados, repetidos e depurados sem abrir um terminal separado. Casos parametrizados, grupos e skips são representados quando o runner fornece essa informação.

## Política anti acúmulo

A Coral separa validações rápidas, verificações lentas e contratos históricos. Durante o desenvolvimento, cada correção roda apenas o conjunto afetado. A bateria completa fica reservada ao congelamento da release.

Isso evita repetir continuamente centenas de verificações que já estavam verdes e não foram afetadas pela mudança atual.

> Testes que dependem de janela, áudio, entrada física ou ambiente gráfico pertencem aos gates de campo e não ao loop rápido cotidiano.
