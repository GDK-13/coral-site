# Release atual

Esta página resume a release estável publicada e recebe automaticamente o changelog extraído do ZIP oficial.

## O que significa estável

Uma release estável passou pelos gates de congelamento definidos para a linha atual. Durante o desenvolvimento são usados testes focados; no congelamento final entram também as camadas lentas e históricas necessárias.

## Compatibilidade editorial

A versão do runtime, a versão da extensão e a edição do Livro aparecem separadamente porque são artefatos diferentes. Isso evita promover uma nova edição editorial apenas para acompanhar uma alteração técnica.

## Atualização do site

Quando uma nova Coral é publicada, o gerador deste repositório importa o ZIP oficial, compara com o snapshot anterior e atualiza versões, módulos, CLI, exemplos, changelog e páginas mecânicas. Mudanças pedagógicas continuam passando por revisão humana.

## Changelog

O trecho abaixo vem diretamente do changelog da release importada.

<!-- AUTO:CHANGELOG -->

## 1.5.12 — infraestrutura de testes, evidência e redução física

* Reduz a suíte coletável em relação à base física reconstruída da 1.5.11, mantendo a meta de até 1.350 casos no freeze.
* Introduz grafo de impacto estático, estrutural e dinâmico com IDs estáveis e validação própria.
* Adiciona Livro Razão de Evidências com invalidação por conteúdo e versões da infraestrutura.
* Mantém o seletor de impacto em modo sombra, com fallback conservador e recall de falhas de 100% nas campanhas controladas.
* Torna permanente o Harness de Mutação com 12 cenários obrigatórios.
* Adiciona Pulso de dívida temporal, explicabilidade de impacto e controles aditivos.
* Elimina recursão redundante dos gates históricos por orquestração plana baseada em evidência.
* Reforça o pipeline final com compileall, Ruff crítico e reutilização de slow e histórico completos do mesmo freeze.
* Preserva a superfície funcional da Coral 1.5.11, a extensão Coral Language 0.43.0 e o Livro Oficial na edição 1.5.8.

<!-- /AUTO:CHANGELOG -->
