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


## Tipagem e herança 1.7.3

A pasta `Exemplos/Tipagem_1_7_3/` reúne cinco programas executáveis dedicados às construções de linguagem desta edição.

* `01_anotacoes_compostas.coral` mostra listas, conjuntos, dicionários, tuplas e nulidade nas anotações.
* `02_heranca_cooperativa.coral` demonstra herança múltipla, resolução C3 e `chame o método pai`.
* `03_programa_principal.coral` mostra a entrada opcional de aplicação e a possibilidade de declarar funções abaixo dela.
* `04_cadastro_tipado.coral` combina coleções tipadas, retorno nulo, duas bases e entrada principal.
* `05_composicao_completa.coral` reúne tipos estruturais, hierarquia em diamante e chamada cooperativa.

Os exemplos são validados pelo gate do site contra o runtime publicado antes de entrarem na documentação.

## Análise entre módulos 1.7.4

`Exemplos/Analise_1_7_4/Cadastro/` é um projeto completo pequeno para estudar classes, parâmetros tipados, fachada de módulo, aliases, testes e `programa principal`.

* `modelos.coral` declara `Autor` e `Livro` e mostra parâmetros tipados no construtor.
* `fachada.coral` concentra os nomes públicos usados pelo consumidor.
* `principal.coral` executa o cadastro pela fachada sem iniciar a aplicação quando o módulo é apenas importado.
* `testes/cadastro.coral` verifica a mesma API pelo runner nativo.

O exemplo também serve para observar no VS Code como parâmetros, propriedades, classes e símbolos importados recebem papéis semânticos diferentes.

## Classes e chamadas 1.7.5

`Exemplos/Analise_1_7_5/Ecossistema/` é um projeto curto para estudar as duas construções centrais da versão.

* `modelos.coral` define `Animal`, subclasses com herança múltipla e `Celula`, cujos métodos consultam pertencimento a classes com `for do tipo`.
* `principal.coral` importa as classes e cria uma célula com uma chamada explícita multilinha.
* `testes/ecossistema.coral` confere o mesmo comportamento pelo runner nativo.

O projeto **Ecossistema** também é útil para observar no VS Code conclusão de classes depois de `do tipo`, navegação entre arquivos e ajuda de assinatura em chamadas multilinha.

## Cabeçalhos e ambientes 1.7.6

A pasta `Exemplos/Citados/Cabecalhos_1_7_6/` possui três exemplos mínimos para parâmetros multilinha, imports multilinha e herança multilinha. Eles são úteis para comparar a forma compacta com a organização vertical sem misturar o conceito com um projeto maior.

`Exemplos/Projetos/Ambiente_Reproduzivel/` demonstra resolução de dependências, `coral.lock`, preparação de ambiente e execução offline com uma wheel didática produzida localmente.

## Arquivos graduais 1.7.7

`Exemplos/Projetos/Importador_Gradual/` processa um CSV em lotes de dois registros, filtra entradas e escreve outro CSV. O exemplo evidencia passagem única, ownership do leitor e memória controlada pelo tamanho do lote.

Use esse projeto junto da página [`coral.arquivos`](modulos/arquivos.html) para estudar `ler_linhas`, `ler_csv`, `ler_lotes_csv`, `escrever_linhas` e `escrever_csv`.

## Esquemas e validação 1.7.8

`Exemplos/Projetos/Importador_Validado/` adiciona validação declarativa ao fluxo gradual. Quantidade e preço são convertidos explicitamente antes de `coral.esquemas`; erros de conversão permanecem responsabilidade da aplicação e erros de validação recebem campo, regra, registro e origem.

O projeto é uma referência útil para distinguir texto CSV vazio, chave ausente e `nulo`, além de mostrar como interromper a coleta por limite de erros sem carregar todos os registros em memória.

## SQLite e textos multilinha 1.7.9

`Exemplos/Projetos/Catalogo_SQLite/` mostra persistência local com `coral.sqlite`. O projeto cria um banco em arquivo, prepara a tabela com SQL multilinha, insere valores por parâmetros, confirma a alteração, consulta os registros e fecha a conexão explicitamente.

O exemplo também é uma referência compacta para os textos multilinha gerais da linguagem: o SQL permanece legível no código sem receber interpretação especial da Coral.

## Aplicações de referência 1.8.0

A Coral 1.8 reúne três projetos de referência que combinam recursos públicos em programas completos. Eles são mais úteis quando você já conhece os exemplos menores e quer observar validação, arquivos, persistência, concorrência e relatórios trabalhando juntos.

* `Exemplos/Projetos/Catalogo_SQLite/` lê CSV, converte e valida registros, persiste em SQLite com parâmetros e demonstra confirmação, reversão e reabertura do banco.
* `Exemplos/Projetos/Analise_CSV/` percorre CSV gradualmente, valida a coluna numérica, calcula estatística dos valores aceitos e pode exportar um gráfico quando o componente necessário está disponível.
* `Exemplos/Projetos/Automacao_Arquivos/` usa `FilaTarefas` para limitar simultaneidade, preservar sucesso parcial, acompanhar progresso e demonstrar cancelamento cooperativo antes de operações bloqueantes.

Os três projetos mantêm a entrada da aplicação separada do núcleo reutilizável e permitem direcionar resultados para outra pasta. Leia o `README.md` de cada projeto antes de executar com seus próprios dados.

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

**Total detectado na release:** 114 arquivos `.coral`.

| Área | Arquivos |
|---|---:|
| Agentes | 2 |
| Analise_1_7_4 | 4 |
| Analise_1_7_5 | 3 |
| Basica_1_7_2 | 3 |
| Citados | 3 |
| Dados | 9 |
| Espaco | 3 |
| Fundamentos | 5 |
| Graficos | 3 |
| Integracao | 4 |
| Jogos | 12 |
| Mundo | 4 |
| Projetos | 11 |
| Projetos_Completos | 19 |
| Regras | 3 |
| SimulacaoTemporal | 14 |
| Simulacoes | 2 |
| Sistema | 1 |
| Tipagem_1_7_3 | 5 |
| Web | 4 |

<!-- /AUTO:EXEMPLOS -->
