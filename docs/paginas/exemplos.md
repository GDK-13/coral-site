# Exemplos oficiais

A biblioteca de exemplos serve para aprender recursos reais da linguagem sem misturar demonstrações pedagógicas com fixtures internas de aceitação.

## Organização

Os exemplos são agrupados por assunto, como fundamentos, dados, jogos, mundo, regras, simulações e projetos completos. Exemplos muito pequenos ou quase idênticos são condensados para reduzir repetição.

## Como usar

Abra um exemplo próximo do assunto que você quer estudar e execute o arquivo com o runtime da release. Projetos completos possuem sua própria estrutura e podem incluir `coral.toml`, módulos auxiliares e testes.

## Português corrente na Coral 1.5.19

O exemplo `Exemplos/Fundamentos/14_portugues_corrente_1_5_19.coral` concentra as formas naturais adicionadas na 1.5.19. Ele demonstra consultas de vazio, iteração com `de`, faixa inclusiva, prefixo e sufixo, mutações de coleção, conversão e alteração numérica.

```coral
defina idades como [17, 22, 35]
defina nome como "Coral"

se idades não está vazia
    mostre quantidade de itens em idades
fim

para cada idade de idades faça
    se idade está entre 18 e 60
        mostre idade
    fim
fim

se nome começa com "Cor" e nome termina com "al"
    mostre "nome reconhecido"
fim
```

## Coral 1.6.0: coesão sem inflar a biblioteca de exemplos

O inventário importado não registra exemplos novos entre a base 1.5.20 e a 1.6.0. A 1.5.21 e a 1.6.0 concentram mudanças de coesão, fronteiras internas, runtime, stdlib e sustentabilidade sem introduzir uma nova camada sintática ou domínio público que exija outra leva de exemplos pedagógicos. Os exemplos existentes continuam sendo a referência para a superfície funcional preservada.

## Apresentação 2D introduzida na Coral 1.5.13

Três exemplos de Jogos continuam como referência para a camada 2D introduzida na 1.5.13:

* `Exemplos/Jogos/09_camera_enquadramento_1_5_13.coral`: seguimento, zona morta, antecipação, limites, enquadramento, zoom, rotação e efeitos determinísticos de câmera.
* `Exemplos/Jogos/10_animacao_tempo_eventos_1_5_13.coral`: animação por quadros, quadros chave, clipes, estados, eventos e composição temporal headless.
* `Exemplos/Jogos/11_camadas_hud_transicao_1_5_13.coral`: camadas, paralaxe, HUD, texto 2D, animação de propriedades, composição e transição de cena.

## Exemplos citados pelo Livro

Os códigos citados no Livro também são sincronizados em `Livro/Exemplos/Citados`. Essa cópia existe para tornar o material autocontido, mas os caminhos canônicos continuam na biblioteca geral de exemplos.

## Fixtures de aceitação

Fixtures usadas para provar comportamento do compilador não ficam misturadas com os exemplos pedagógicos. Elas pertencem à área de testes da distribuição.

## Inventário da release

O quadro abaixo é atualizado automaticamente a partir do ZIP oficial.

<!-- AUTO:EXEMPLOS -->

**Total detectado na release:** 62 arquivos `.coral`.

| Área | Arquivos |
|---|---:|
| Agentes | 2 |
| Dados | 5 |
| Espaco | 1 |
| Fundamentos | 5 |
| Jogos | 11 |
| Mundo | 4 |
| Projetos_Completos | 16 |
| Regras | 3 |
| SimulacaoTemporal | 13 |
| Simulacoes | 2 |

<!-- /AUTO:EXEMPLOS -->
