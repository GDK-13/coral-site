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

## 1.5.9 — integração oficial com VS Code e refinamento da distribuição

* Promove Coral Language 0.41.0 como extensão oficial da Coral 1.5.9.
* Amplia IntelliSense próprio, navegação, hovers, signature help, auto import, semantic tokens e diagnóstico contextual pelo LSP.
* Corrige o reconhecimento de formas naturais importadas tanto na execução direta quanto nos diagnósticos do editor.
* Consolida execução, Test Explorer, REPL, DAP/F5, restart, informações de ambiente e recuperação de falhas do servidor.
* Evolui Project Explorer, suporte a `coral.toml`, projetos aninhados, multiroot, criação guiada de arquivos e Biblioteca Coral.
* Refina a coloração em duas camadas, com TextMate como fallback e semantic tokens contextuais respeitando o tema do usuário.
* Atualiza o limite de linha para 150 caracteres e mantém a sugestão segura de quebra com prévia fantasma no VS Code.
* Reestrutura a biblioteca de exemplos, remove demonstrações redundantes ou excessivamente nichadas e separa fixtures de aceitação dos exemplos pedagógicos.
* Faz `Livro/Exemplos` conter também cópias sincronizadas dos códigos citados no Livro, sem recompilação redundante nas validações.
* Mantém o Livro Oficial na edição 1.5.8, desacoplando a edição editorial da versão técnica do runtime.
* Incorpora a nova guideline oficial de identidade visual da Coral à documentação e ao gerador do Livro.
* Preserva a política anti acúmulo: validações focadas durante o desenvolvimento e uma única bateria completa no congelamento da release.

<!-- /AUTO:CHANGELOG -->
