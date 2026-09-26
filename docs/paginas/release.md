# Release atual

Esta página resume a release estável publicada e recebe automaticamente o changelog extraído do ZIP oficial.

## O que significa estável

Uma release estável passou pelos gates de congelamento definidos para a linha atual. Durante o desenvolvimento são usados testes focados; no congelamento final entram também as camadas lentas e históricas necessárias.

## Compatibilidade editorial

A versão do runtime, a versão da extensão e a edição do Livro aparecem separadamente porque são artefatos diferentes. Isso evita promover uma nova edição editorial apenas para acompanhar uma alteração técnica.

## Atualização do site

Quando uma nova Coral é publicada, o gerador deste repositório importa o ZIP oficial, compara com o snapshot anterior e atualiza versões, módulos, CLI, exemplos, changelog e páginas mecânicas. Mudanças pedagógicas continuam passando por revisão humana.

## Resumo da Coral 1.6.0

A 1.6.0 é a release de **Coesão Interna**. Ela parte da candidata 1.5.21 e preserva a superfície pública da linha 1.5 enquanto fecha fronteiras entre parser, AST, backend, runtime, biblioteca padrão e serviços internos.

* **Fronteiras arquiteturais:** `coral.release.arquitetura/1` declara camadas, contratos, autoridades, grafo de dependências e orçamentos estruturais.
* **Parser, AST e backend:** o núcleo semântico recebe AST, o backend estrutural deixa de reabrir parsing e a normalização de chamadas naturais acontece antes do backend.
* **Equivalência estrutural:** a AST ganha assinatura e comparação estrutural para provar a convergência de formas superficiais equivalentes do português corrente.
* **Runtime mínimo:** `coral.runtime_minimo` concentra o núcleo sem dependências opcionais; `coral.runtime` permanece como fachada compatível e os serviços internos são resolvidos de forma preguiçosa.
* **Stdlib e persistência:** fachadas públicas ficam separadas das implementações canônicas. `coral.persistencia` passa a expor `VERSOES_LEITURA`, `VERSAO_ESCRITA` e `politica_persistencia()` para tornar executável a política do formato persistente.
* **Fechamento arquitetural:** o gate final exige zero ciclos, zero violações de camada e zero exceções transitórias, mantendo hotspots centrais sob orçamento explícito.
* **Suíte específica de release:** casos históricos redundantes foram consolidados em testes orientados a contrato, sem criar um novo teste CP24 específico da versão para permanecer na suíte ativa.

### Ponte da 1.5.21

A 1.5.21 funcionou como **Candidata de Coesão** entre a sustentabilidade da 1.5.20 e a arquitetura 1.6.0. Ela reduziu acoplamento em CLI, LSP e Setup, extraiu responsabilidades visuais e de catálogo, e convergiu autoridades internas usadas pelo fluxo de release.

### O que muda para quem programa em Coral

Para a maior parte dos programas, a atualização é deliberadamente pouco disruptiva: o importador do site não detectou módulos novos ou removidos, mudança de sintaxe, comandos novos de CLI nem alteração na biblioteca de exemplos. A principal ampliação pública detectada está em `coral.persistencia`, que agora expõe a política de compatibilidade do formato como dados consultáveis.

Isso significa que a 1.6.0 deve ser lida principalmente como uma mudança de **como a linguagem é organizada e verificada por dentro**, e não como uma troca do vocabulário que o usuário já aprendeu na linha 1.5.

### Estado do congelamento

A entrega final declara a Coral 1.6.0 **congelada, publicável e promovida**, com Coral Language `0.53.0` e Livro Oficial `1.5.8`. O fechamento registra 1467 testes rápidos aprovados, 88 desmarcados, 30 subtests aprovados, 38 de 38 arquivos slow aprovados, ciclo real de instalação aprovado, auditoria estrita de versões aprovada, sustentabilidade 6 de 6, higiene final sem candidatos e equivalência aprovada para o ZIP completo e os patches.

O trecho de `CHANGELOG.md` importado abaixo preserva literalmente o cabeçalho **“em desenvolvimento”** presente no arquivo fonte da distribuição. O estado oficial desta página segue a entrega final congelada.

## Changelog importado

O trecho abaixo vem diretamente do changelog da release importada.

<!-- AUTO:CHANGELOG -->

## Coral 1.6.0 — em desenvolvimento

## CP24 — Congelamento

* Torna o fechamento arquitetural parte obrigatória do congelamento 1.6.0.
* Reconhece `coesao_1_6_0.json` como autoridade corrente, preservando fallback apenas para árvores históricas.
* Evita criar um teste CP24 específico da versão na suíte ativa.
* Reserva promoção para depois de rápida, slow, instalação, auditorias, sincronização e equivalência.

## CP18 a CP23 — Fechamento da arquitetura

* Exige zero ciclos, violações de camada e exceções transitórias.
* Migra a autoridade corrente de coesão para `coesao_1_6_0.json`, ancorada em 1.5.21.
* Preserva fachadas públicas sem tratá las como compatibilidade interna descartável.
* Mantém quatro hotspots sob orçamento explícito de tamanho e acoplamento.
* Consolida os testes específicos de release de 52 funções históricas para 8 funções orientadas a contrato.
* Integra `coral.release.fechamento_arquitetura/1` ao gate de coesão.

## CP12 a CP17 — Runtime, stdlib e serviços

* Extrai `coral.runtime_minimo` e mantém `coral.runtime` como fachada compatível.
* Formaliza cinco serviços internos com resolução preguiçosa e sem carregar extras no núcleo.
* Distingue fachadas públicas da stdlib de suas implementações canônicas.
* Expõe a política executável da persistência e a compara com a matriz de sustentabilidade.
* Unifica diagnósticos operacionais e de código em um envelope estrutural comum.
* Integra `coral.release.runtime_stdlib/1` ao gate de coesão com testes orientados a contratos.

## CP6 a CP11 — Parser, AST e backend

* Separa o núcleo semântico da fachada pública que aceita código fonte.
* Torna o backend estrutural consumidor de AST e move parsing para a orquestração.
* Move normalização de chamadas naturais para antes do backend.
* Classifica emissão de expressões como serviço da AST.
* Adiciona equivalência estrutural para provar convergência das formas de português corrente.
* Fecha as seis exceções transitórias com zero exceções ativas, zero ciclos e zero violações de camada.

## CP0 a CP5 — Fronteiras fundamentais

* Abre a linha 1.6.0 sobre a Coral 1.5.21 com âncora explícita da linha anterior.
* Introduz `coral.release.arquitetura/1` com mapa de camadas, contratos, autoridades, grafo e orçamentos.
* Integra o gate arquitetural ao comando `coral_release coesao`.
* Registra seis exceções transitórias herdadas para remoção no CP6 a CP11, sem escondê las como dependências permitidas.

## 1.5.21

### CP24 — congelamento

* Torna coesão um gate formal do congelamento, junto de sustentabilidade e higiene.
* Exige 3/3 metas de acoplamento, 2/2 extrações controladas e 5/5 autoridades internas antes da promoção.
* Reserva rápida completa, slow isolada, ciclo de instalação, equivalência e patches para o pipeline amplo final.

### CP18 a CP23 — convergência de autoridades

* `release.util_arquivos` vira a autoridade única de SHA256 de arquivo e digest JSON estável do fluxo de release.
* Sete consumidores deixam de reimplementar hashing de arquivos.
* A auditoria de coesão passa a bloquear divergência de autoridades internas declaradas.


### CP12 a CP17 — decomposição controlada

* A GUI do Setup passa a viver em `coral.setup_visual`, mantendo fachada pública preguiçosa.
* Catálogo e templates leves do LSP passam a `coral.lsp_catalogo_editor`.
* Extrações possuem orçamento bloqueante de tamanho, acoplamento e fronteiras.


### CP6 a CP11 — redução de acoplamento

* LSP e Setup adotam fronteiras de carregamento menores e metas bloqueantes de coesão.

<!-- /AUTO:CHANGELOG -->
