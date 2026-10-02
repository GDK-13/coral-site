# Exemplos oficiais

A biblioteca de exemplos serve para aprender recursos reais da linguagem sem misturar demonstrações pedagógicas com fixtures internas de aceitação.

## Organização

Os exemplos são agrupados por assunto, como fundamentos, dados, gráficos, Web, jogos, mundo, regras, simulações, sistema e projetos completos.

## Como usar

Abra um exemplo próximo do assunto que você quer estudar e execute o arquivo com o runtime da distribuição. Projetos completos possuem sua própria estrutura e podem incluir `coral.toml`, módulos auxiliares e testes.

## Português corrente

O conjunto de fundamentos inclui exemplos de consultas de vazio, iteração, faixas, prefixos e sufixos, mutações de coleção, conversões e alterações numéricas.

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
```

## Biblioteca base 1.7.2

A 1.7.2 inclui três exemplos curtos dedicados às formas naturais da biblioteca base. Eles são um bom ponto de partida para consultar entrada, tipos, conversões, texto, coleções e JSON sem precisar abrir um projeto maior.

* `Exemplos/Basica_1_7_2/entrada.coral`: leitura natural de linha e conversão tolerante com valor padrão;
* `Exemplos/Basica_1_7_2/tipos_conversoes.coral`: consulta de tipo, teste natural de tipo e conversões;
* `Exemplos/Basica_1_7_2/texto_colecoes_json.coral`: texto, frequência, valores únicos, ordenação e JSON.

A distribuição também inclui um exemplo de projeto dividido em módulos em `Exemplos/Projetos_Completos/Vitrine/nucleo_modular/`. `principal.coral` coordena o programa, enquanto `calculos.coral` e `apresentacao.coral` separam cálculo e apresentação.

## Ciência e dados

A biblioteca inclui exemplos para matemática escalar, estatística descritiva, álgebra linear, transformações 3D, planejamento de experimentos e integração entre geração procedural e Laboratório.

Caminhos úteis:

* `Exemplos/Dados/06_matematica_escalar.coral`
* `Exemplos/Dados/07_estatistica_descritiva.coral`
* `Exemplos/Dados/08_laboratorio_experimentos.coral`
* `Exemplos/Dados/09_experimento_procedural.coral`
* `Exemplos/Espaco/02_algebra_linear_e_transformacoes3d.coral`
* `Exemplos/Espaco/03_visualizacao_cientifica_3d.coral`

## Gráficos

Os exemplos de gráficos cobrem séries 2D, SVG local, estatística com incerteza, painéis e HTML interativo.

* `Exemplos/Graficos/01_series_e_svg.coral`
* `Exemplos/Graficos/02_estatistica_incerteza_e_painel.coral`
* `Exemplos/Graficos/03_html_interativo.coral`

## Web

A área Web separa composição local de HTML e URL, cliente HTTP, servidor local e integração com gráficos interativos.

* `Exemplos/Web/01_html_e_url.coral`
* `Exemplos/Web/02_cliente_http_loopback.coral`
* `Exemplos/Web/03_servidor_http_local.coral`
* `Exemplos/Web/04_grafico_interativo_local.coral`

## Jogos e apresentação

A área Jogos cobre câmera, animação temporal, camadas, HUD, transições, mapas, depuração visual e integração com procedural.

## Exemplos citados pelo Livro

Os códigos citados no Livro também são sincronizados em `Livro/Exemplos/Citados`. Essa cópia torna o material autocontido, enquanto a biblioteca geral continua organizada em `Exemplos/`.

## Inventário da distribuição

O quadro abaixo é atualizado automaticamente a partir do ZIP oficial.

<!-- AUTO:EXEMPLOS -->

**Total detectado na release:** 88 arquivos `.coral`.

| Área | Arquivos |
|---|---:|
| Agentes | 2 |
| Basica_1_7_2 | 3 |
| Dados | 9 |
| Espaco | 3 |
| Fundamentos | 5 |
| Graficos | 3 |
| Integracao | 4 |
| Jogos | 12 |
| Mundo | 4 |
| Projetos_Completos | 19 |
| Regras | 3 |
| SimulacaoTemporal | 14 |
| Simulacoes | 2 |
| Sistema | 1 |
| Web | 4 |

<!-- /AUTO:EXEMPLOS -->
