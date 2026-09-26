# coral.jogos

## Visão geral

`coral.jogos` é a camada de apresentação interativa da Coral. Ela reúne loop de jogo, entrada, desenho, sprites, cenas, animação, câmera, colisão e renderização de mapas sem obrigar o modelo de mundo a conhecer a biblioteca gráfica.

<!-- AUTO:MODULO -->

**Importação:** `coral.jogos`  
**Categoria:** jogos  

janela, desenho, sprites, animação, câmera, apresentação, cenas, mapas e eventos de jogo

### Superfície pública detectada

`Jogo`, `TransicaoCena`, `MetricasJogo`, `Cor`, `Retangulo`, `BackendNulo`, `ErroJogosCoral`, `DependenciaJogosAusente`, `PRETO`, `BRANCO`, `VERMELHO`, `VERDE`, `AZUL`, `AMARELO`, `criar_jogo`, `pygame_disponivel`, `diagnosticar_jogos`, `Assets`, `Sprite`, `Cena`, `CamadaApresentacao`, `TextoApresentacao`, `RepresentacaoEntidade`, `ErroAssetCoral`, `Animacao`, `AnimacoesDirecionais`, `VinculoAnimacaoMovimento`, `EstadosAnimacao`, `VinculoEstadosAnimacaoMovimento`, `TransicaoEstadoAnimacao`, `CondicaoTransicaoAnimacao`, `TransicoesEstadosAnimacao`, `VinculoTransicoesEstadosMovimento`, `VinculoTransicoesEventos`, `EfeitoCamera`, `Camera`, `VinculoClipe`, `ligar_clipe`, `registrar_propriedade_animavel`, `QuadroSprite`, `Spritesheet`, `carregar_spritesheet`, `FormaTransformada`, `formas_colidem`, `CanalAnimado`, `AnimacaoTransformacao`, `onda_seno`, `onda_cosseno`, `onda_triangular`, `onda_serra`, `onda_pulso`, `normalizar_progresso`, `curva_linear`, `curva_entrada_suave`, `curva_saida_suave`, `curva_entrada_saida_suave`, `curva_quadratica`, `curva_cubica`, `curva_degrau`, `resolver_curva_temporal`, `avaliar_curva_temporal`, `interpolar`, `QuadroChave`, `FaixaAnimacao`, `ClipeAnimacao`, `AcaoApresentacao`, `EsperaApresentacao`, `EsperaConclusao`, `SequenciaApresentacao`, `ParaleloApresentacao`, `ComposicaoTemporal`, `VinculoTempoApresentacao`, `VinculoComposicaoEventos`, `ComandoComposicao`, `GravadorComposicao`, `executar`, `esperar`, `esperar_conclusao`, `sequencia`, `paralelo`, `usar_fonte_tempo`, `ligar_evento`, `forma_espacial_sprite`, `posicao_espacial_sprite`, `sprites_colidem`, `AdaptadorEventosJogo`, `adaptar_eventos`, `Viewport`, `CONTRATO_OVERLAY_DEBUG`, `PrimitivaDebug`, `OverlayDebug`, `EstiloOverlayDebug`, `ConfiguracaoDebugJogo`, `normalizar_categorias_debug`, `gerar_overlay_debug`, `gerar_overlay_metricas_debug`, `desenhar_overlay_debug`, `EstiloCelula`, `RenderizadorMapa2D`, `celula_para_tela`, `mundo_para_tela`, `tela_para_celula`, `tela_para_mundo`, `animar_propriedade`, `reproduzir_ao_contrario`

<!-- /AUTO:MODULO -->

## Papel no ecossistema

O módulo apresenta e controla interação. Estado persistente e semântica do domínio pertencem a `coral.mundo`, `coral.rpg`, `coral.simulacao` ou outro módulo apropriado. `RepresentacaoEntidade` liga uma entidade a um `Sprite` sem transformar o objeto visual na fonte de verdade do sistema.

Na 1.5.13 essa separação também vale para câmera, efeitos, HUD, transições e composição temporal. A apresentação pode reagir ao domínio, mas não assume sua autoridade.

## Conceitos principais

### Jogo e backend

`Jogo` organiza ciclo de vida, atualização, desenho, entrada, cena e eventos. `criar_jogo` é o helper funcional. `BackendNulo` executa a mesma camada de controle sem abrir janela e continua sendo o caminho preferido para testes automatizados.

### Sprites, cenas e camadas

`Sprite` reúne posição, dimensão, imagem, cor, velocidade, visibilidade e transformações. `Cena` organiza o ciclo visual e, na 1.5.13, pode conter `CamadaApresentacao` ordenadas. Uma camada pode usar espaço de mundo ou espaço de tela, além de opacidade e paralaxe próprios.

### Transformações

Sprites suportam escala, rotação, opacidade e espelhamento. Colisão pode acompanhar escala e rotação de maneira configurável, evitando que apresentação e hitbox precisem ser sempre idênticas.

### Animação por quadros e por propriedades

`Animacao`, `AnimacoesDirecionais`, `EstadosAnimacao` e transições de estado cuidam da animação baseada em quadros. A 1.5.13 acrescenta `QuadroChave`, `FaixaAnimacao` e `ClipeAnimacao` para dirigir propriedades numéricas ao longo do tempo com curvas explícitas. `animar_propriedade` simplifica o caso comum de mover, escalar, girar ou alterar outra propriedade suportada até um valor.

### Câmera e efeitos temporários

`Camera` faz a transformação inversível entre mundo e tela com zoom e rotação, além de culling conservador. Ela pode seguir alvos com suavização independente da taxa de quadros, usar zona morta, antecipação, enquadramento, limites e travas de eixo. Efeitos como tremor, impulso de deslocamento, zoom ou rotação são temporários e não precisam alterar o estado lógico da câmera.

### Composição temporal

`ComposicaoTemporal` coordena ações de apresentação usando tempo explícito. `sequencia`, `paralelo`, `esperar`, `esperar_conclusao` e `executar` permitem montar pequenas linhas temporais sem depender de temporizadores espalhados pelo loop principal. A composição pode ser pausada, retomada, cancelada, reiniciada e controlada por uma fonte de tempo escolhida pelo programa.

### Texto, HUD e transições

`TextoApresentacao` fornece texto 2D reutilizável para o mundo ou para a tela. Camadas presas à tela atendem HUDs e interfaces que não devem acompanhar a câmera. `TransicaoCena` e `Jogo.mudar_cena_com_transicao` coordenam a passagem visual entre cenas sem transferir a posse do jogo para o efeito.

### Replay e reconstrução

A 1.5.13 persiste apenas estado visual que pode ser reconstruído com segurança. `GravadorComposicao` registra comandos explícitos de uma composição para replay determinístico, em vez de tentar serializar callbacks ou recursos gráficos opacos.

## Quando usar

Use para jogos 2D, protótipos interativos, visualizações e interfaces que precisam de entrada ou apresentação em tempo real. Se você só precisa modelar um mapa, regras ou uma simulação sem interface, os módulos de domínio podem operar sem `coral.jogos`.

## Começando sem janela

Trecho oficial de `Exemplos/Jogos/01_jogo_e_entrada_sem_janela.coral`:

```coral
de coral.jogos importe VERMELHO, AZUL

crie um jogo chamado jogo sem janela
execute jogo.backend.definir_teclas("direita")
execute jogo.backend.definir_mouse(posicao=[12, 34], pressionados=["esquerdo"])

garanta que jogo.tecla_pressionada("direita") for igual a verdadeiro
garanta que jogo.botao_mouse_pressionado("esquerdo") for igual a verdadeiro
```

:::resultado
As duas garantias devem passar sem abrir uma janela real. O `BackendNulo` mantém o estado de teclado e mouse necessário para o teste.
:::

## Câmera com enquadramento

A câmera da 1.5.13 pode seguir um alvo, limitar sua área, antecipar movimento e enquadrar vários objetos. Trecho de `Exemplos/Jogos/09_camera_enquadramento_1_5_13.coral`:

```coral
de coral.jogos importe Camera, Sprite, Retangulo

defina camera como Camera(0, 0, 320, 180)
defina heroi como Sprite(100, 80, 16, 16, velocidade_x=40)
defina aliado como Sprite(260, 120, 16, 16)

execute camera.definir_zona_morta(20, 12)
execute camera.seguir(heroi, constante_tempo=0.25, antecipacao=0.2)
execute camera.definir_limites(Retangulo(0, 0, 1000, 600))
execute camera.enquadrar_alvos([heroi, aliado], margem=20, ajustar_zoom=True)
execute camera.definir_rotacao(15)
```

Quando usar tremor ou outro efeito temporário, forneça uma semente quando precisar repetir exatamente o mesmo resultado em teste ou replay.

## Quadros chave e composição temporal

Trecho inspirado no exemplo oficial `10_animacao_tempo_eventos_1_5_13.coral`:

```coral
de coral.jogos importe QuadroChave, FaixaAnimacao, ClipeAnimacao, Sprite

defina faixa_x como FaixaAnimacao("x", (
    QuadroChave(0.0, 0.0, "entrada_saida_suave"),
    QuadroChave(1.0, 100.0)
))

defina clipe como ClipeAnimacao((faixa_x,), modo="ida_volta")
defina heroi como Sprite(0, 0, 16, 16)
execute heroi.animar_com_clipe(clipe, {"x": "x"})
execute heroi.atualizar(0.5)
```

O avanço depende do tempo informado. Isso evita que a animação mude de velocidade apenas porque a taxa de quadros variou.

## Camadas, HUD e transições

Trecho de `Exemplos/Jogos/11_camadas_hud_transicao_1_5_13.coral`:

```coral
de coral.jogos importe Cena, Sprite, TextoApresentacao

defina origem como Cena("origem")
defina fundo como origem.criar_camada("fundo", ordem=-10, paralaxe=0.5)
defina hud como origem.criar_camada("hud", ordem=10, espaco="tela")

defina montanhas como Sprite(40, 20, 100, 40)
defina titulo como TextoApresentacao("Apresentação Coral", tamanho=12, ancora_viewport="topo")

execute origem.adicionar_em_camada(montanhas, fundo)
execute origem.adicionar_em_camada(titulo, hud)
```

Elementos no espaço de mundo podem usar paralaxe. Elementos no espaço de tela permanecem adequados para HUD e interface.

## Mapas, câmera e viewport

`RenderizadorMapa2D` continua consumindo mapas genéricos de `coral.mundo`. `Viewport` separa a resolução lógica da resolução física e deve ser combinado com a câmera quando a janela for redimensionada ou tiver escala própria.

## API essencial

| Entrada | Papel |
|---|---|
| `Jogo` | ciclo principal, entrada, cenas e transições |
| `BackendNulo` | execução determinística sem janela |
| `Sprite` | objeto visual transformável |
| `Cena` | organização do ciclo visual e de camadas |
| `CamadaApresentacao` | ordem, espaço de mundo ou tela, opacidade e paralaxe |
| `TextoApresentacao` | texto 2D para mundo ou HUD |
| `Camera` | transformação mundo tela, zoom, rotação, seguimento, enquadramento e efeitos |
| `EfeitoCamera` | efeito visual temporário separado do estado lógico |
| `QuadroChave` | valor de uma propriedade em um instante |
| `FaixaAnimacao` | sequência temporal de quadros chave para uma propriedade |
| `ClipeAnimacao` | reprodução de uma ou mais faixas |
| `animar_propriedade` | animação direta de uma propriedade suportada |
| `ComposicaoTemporal` | sequência e paralelismo de ações com tempo explícito |
| `TransicaoCena` | apresentação temporal entre cenas |
| `GravadorComposicao` | comandos de replay determinístico da composição |
| `Viewport` | resolução lógica, área física e conversões de tela |
| `RenderizadorMapa2D` | apresentação de mapas de `coral.mundo` |

As assinaturas completas, parâmetros e operações públicas ficam na referência automática abaixo e são extraídas diretamente da release.

## Sprites, escala e colisão

`Sprite.definir_escala`, `aumentar`, `diminuir`, `definir_rotacao`, `girar` e os controles de espelhamento alteram a apresentação. `colisao_acompanha_escala` e `colisao_acompanha_rotacao` permitem decidir se a geometria de colisão acompanha a transformação.

## Automação matemática

`CanalAnimado` e `AnimacaoTransformacao` continuam úteis para movimentos periódicos por seno, cosseno, onda triangular, serra ou pulso. Para animações com começo, fim e duração definidos, prefira os quadros chave e clipes da 1.5.13.

## Estados e eventos

Estados e transições visuais podem responder a movimento ou ao barramento de `coral.tempo_eventos`. O vínculo é opcional: o domínio emite o evento, enquanto a apresentação escolhe como essa informação será representada.

## Janela, tela cheia e redimensionamento

`Jogo` pode iniciar em tela cheia, alternar esse estado em execução e atualizar o tamanho físico quando a janela é redimensionada. O `Viewport` mantém conversões entre coordenadas físicas e lógicas, evitando que a lógica do jogo dependa diretamente da resolução real da janela.

## Erros e diagnóstico

`DependenciaJogosAusente` representa ausência do backend gráfico real quando ele é necessário. `pygame_disponivel()` permite detectar a capacidade. Para lógica e apresentação determinística, prove primeiro o comportamento com `BackendNulo` antes de depender de uma janela real.

Assets inválidos usam `ErroAssetCoral`. Separar assets, sprites e domínio ajuda a localizar se a falha está no arquivo, na transformação, na composição ou na lógica do mundo.

## Boas práticas

* Teste entrada, câmera, animação e composição com `BackendNulo` sempre que o comportamento não exigir pixels reais.
* Mantenha o modelo de mundo fora do sprite e fora da cena.
* Use `Camera.mundo_para_tela` e `Camera.tela_para_mundo` em vez de reconstruir transformações manualmente.
* Use camadas de tela para HUD e camadas de mundo para conteúdo que deve reagir à câmera.
* Avance animações e composições com tempo explícito.
* Use semente em efeitos aleatórios quando precisar de reprodução determinística.
* Persista estado reconstruível e registre comandos quando o objetivo for replay.

## Integração com outros módulos

`coral.mundo` fornece mapas e entidades. `coral.tempo_eventos` fornece o barramento usado por vínculos opcionais. `coral.rpg` fornece personagens. `coral.procedural` cuida de geração determinística e `coral.simulacao` pode evoluir o estado temporal sem depender da janela. A apresentação consome essas informações por pontes, sem inverter a direção das dependências.

## Testabilidade e ambientes

O backend nulo permite validar transformação de câmera, avanço temporal, transições de estado, composição e entrada simulada sem abrir janela. Gates gráficos reais continuam necessários para janela, driver, renderização, áudio, teclado, mouse e GPU.

## Compatibilidade e evolução

A **Coral 1.6.0** mantém a superfície pública de Jogos detectada nas releases anteriores. Os recursos de apresentação introduzidos na 1.5.13 seguem disponíveis; a 1.6.0 concentra mudanças em coesão interna e fronteiras arquiteturais sem remover essa API. O Livro Oficial permanece na edição 1.5.8.

## Referência da API

<!-- AUTO:API -->

### Funções

#### `criar_jogo`

Cria uma instância de jogo com janela, entrada e backend configuráveis.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `titulo` | Valor correspondente a titulo. | `str` | obrigatório |
| `largura` | Largura usada pela operação. | `int` | `800` |
| `altura` | Altura usada pela operação. | `int` | `450` |
| `fps` | Quantidade alvo de quadros por segundo. | `int` | `60` |
| `backend` | Backend usado para executar a operação. | `não declarado` | `None` |
| `mundo` | Mundo associado à operação. | `não declarado` | `None` |
| `relogio` | Relógio usado para controlar tempo ou atualização. | `não declarado` | `None` |
| `eventos` | Fonte ou conjunto de eventos associado à operação. | `não declarado` | `None` |
| `tela_cheia` | Define se a janela deve usar tela cheia. | `bool` | `False` |

**Retorno**

Retorna um valor declarado como `Jogo`.

:::details Detalhes técnicos

**Assinatura:** `criar_jogo(titulo: str, largura: int = 800, altura: int = 450, fps: int = 60, *, backend = None, mundo = None, relogio = None, eventos = None, tela_cheia: bool = False) -> Jogo`

**Origem da implementação:** `coral.jogos`

**Arquivo na release:** `coral/jogos/__init__.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `titulo` | posicional |
| `largura` | posicional |
| `altura` | posicional |
| `fps` | posicional |
| `backend` | nomeado |
| `mundo` | nomeado |
| `relogio` | nomeado |
| `eventos` | nomeado |
| `tela_cheia` | nomeado |

:::

#### `pygame_disponivel`

Indica se pygame está disponível ou atende à condição esperada.

**Retorno**

Retorna um valor lógico que indica o resultado da verificação.

:::details Detalhes técnicos

**Assinatura:** `pygame_disponivel() -> bool`

**Origem da implementação:** `coral.jogos`

**Arquivo na release:** `coral/jogos/__init__.py`

:::

#### `diagnosticar_jogos`

Produz informações de diagnóstico para jogos.

**Retorno**

Retorna um valor declarado como `dict[str, object]`.

:::details Detalhes técnicos

**Assinatura:** `diagnosticar_jogos() -> dict[str, object]`

**Origem da implementação:** `coral.jogos`

**Arquivo na release:** `coral/jogos/__init__.py`

:::

#### `ligar_clipe`

Liga clipe.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `alvo` | Valor correspondente a alvo. | `Any` | obrigatório |
| `clipe` | Valor correspondente a clipe. | `ClipeAnimacao` | obrigatório |
| `mapeamento` | Valor correspondente a mapeamento. | `dict[str, str]` | obrigatório |
| `modo` | Valor correspondente a modo. | `str` | `'absoluto'` |
| `restaurar_ao_final` | Valor correspondente a restaurar ao final. | `bool` | `False` |
| `composicao` | Valor correspondente a composicao. | `str` | `'substituir'` |
| `permitir_conflito` | Controla se deve permitir conflito. | `bool` | `False` |

**Retorno**

Retorna um valor declarado como `VinculoClipe`.

:::details Detalhes técnicos

**Assinatura:** `ligar_clipe(alvo: Any, clipe: ClipeAnimacao, mapeamento: dict[str, str], *, modo: str = 'absoluto', restaurar_ao_final: bool = False, composicao: str = 'substituir', permitir_conflito: bool = False) -> VinculoClipe`

**Origem da implementação:** `coral.jogos.objetos`

**Arquivo na release:** `coral/jogos/objetos.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `alvo` | posicional |
| `clipe` | posicional |
| `mapeamento` | posicional |
| `modo` | nomeado |
| `restaurar_ao_final` | nomeado |
| `composicao` | nomeado |
| `permitir_conflito` | nomeado |

**Exceções diretamente observáveis no corpo:** `ValueError`, `TypeError`

:::

#### `registrar_propriedade_animavel`

Registra propriedade animavel.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `tipo` | Tipo solicitado para o resultado, quando o módulo oferece essa escolha. | `type` | obrigatório |
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | obrigatório |
| `obter` | Valor correspondente a obter. | `Callable[[Any], float]` | obrigatório |
| `definir` | Valor correspondente a definir. | `Callable[[Any, float], None]` | obrigatório |

**Retorno**

Não produz um valor de retorno útil; o efeito ocorre no estado ou recurso alvo.

:::details Detalhes técnicos

**Assinatura:** `registrar_propriedade_animavel(tipo: type, nome: str, obter: Callable[[Any], float], definir: Callable[[Any, float], None]) -> None`

**Origem da implementação:** `coral.jogos.objetos`

**Arquivo na release:** `coral/jogos/objetos.py`

**Exceções diretamente observáveis no corpo:** `TypeError`, `ValueError`

:::

#### `carregar_spritesheet`

Atalho funcional para criar uma spritesheet em grade uniforme.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `caminho` | Caminho do arquivo ou diretório usado pela operação. | `str \| Path` | obrigatório |
| `largura_imagem` | Largura de imagem. | `int` | obrigatório |
| `altura_imagem` | Altura de imagem. | `int` | obrigatório |
| `largura_quadro` | Largura de quadro. | `int` | obrigatório |
| `altura_quadro` | Altura de quadro. | `int` | obrigatório |
| `margem` | Valor correspondente a margem. | `int` | `0` |
| `espacamento` | Valor correspondente a espacamento. | `int` | `0` |

**Retorno**

Retorna um valor declarado como `Spritesheet`.

:::details Detalhes técnicos

**Assinatura:** `carregar_spritesheet(caminho: str \| Path, largura_imagem: int, altura_imagem: int, largura_quadro: int, altura_quadro: int, *, margem: int = 0, espacamento: int = 0) -> Spritesheet`

**Origem da implementação:** `coral.jogos.spritesheet`

**Arquivo na release:** `coral/jogos/spritesheet.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `caminho` | posicional |
| `largura_imagem` | posicional |
| `altura_imagem` | posicional |
| `largura_quadro` | posicional |
| `altura_quadro` | posicional |
| `margem` | nomeado |
| `espacamento` | nomeado |

:::

#### `formas_colidem`

Colisão convexa por SAT. Toque de borda não conta como colisão.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `a` | Valor correspondente a a. | `FormaTransformada` | obrigatório |
| `b` | Valor correspondente a b. | `FormaTransformada` | obrigatório |

**Retorno**

Retorna um valor lógico que indica o resultado da verificação.

:::details Detalhes técnicos

**Assinatura:** `formas_colidem(a: FormaTransformada, b: FormaTransformada) -> bool`

**Origem da implementação:** `coral.jogos.transformacoes`

**Arquivo na release:** `coral/jogos/transformacoes.py`

:::

#### `onda_seno`

Calcula uma onda de seno.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `fase` | Valor correspondente a fase. | `float` | obrigatório |

**Retorno**

Retorna um valor declarado como `float`.

:::details Detalhes técnicos

**Assinatura:** `onda_seno(fase: float) -> float`

**Origem da implementação:** `coral.jogos.transformacoes`

**Arquivo na release:** `coral/jogos/transformacoes.py`

:::

#### `onda_cosseno`

Calcula uma onda de cosseno.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `fase` | Valor correspondente a fase. | `float` | obrigatório |

**Retorno**

Retorna um valor declarado como `float`.

:::details Detalhes técnicos

**Assinatura:** `onda_cosseno(fase: float) -> float`

**Origem da implementação:** `coral.jogos.transformacoes`

**Arquivo na release:** `coral/jogos/transformacoes.py`

:::

#### `onda_triangular`

Calcula uma onda de triangular.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `fase` | Valor correspondente a fase. | `float` | obrigatório |

**Retorno**

Retorna um valor declarado como `float`.

:::details Detalhes técnicos

**Assinatura:** `onda_triangular(fase: float) -> float`

**Origem da implementação:** `coral.jogos.transformacoes`

**Arquivo na release:** `coral/jogos/transformacoes.py`

:::

#### `onda_serra`

Calcula uma onda de serra.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `fase` | Valor correspondente a fase. | `float` | obrigatório |

**Retorno**

Retorna um valor declarado como `float`.

:::details Detalhes técnicos

**Assinatura:** `onda_serra(fase: float) -> float`

**Origem da implementação:** `coral.jogos.transformacoes`

**Arquivo na release:** `coral/jogos/transformacoes.py`

:::

#### `onda_pulso`

Calcula uma onda de pulso.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `fase` | Valor correspondente a fase. | `float` | obrigatório |

**Retorno**

Retorna um valor declarado como `float`.

:::details Detalhes técnicos

**Assinatura:** `onda_pulso(fase: float) -> float`

**Origem da implementação:** `coral.jogos.transformacoes`

**Arquivo na release:** `coral/jogos/transformacoes.py`

:::

#### `normalizar_progresso`

Normaliza progresso temporal; extrapolação só ocorre quando explícita.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `progresso` | Valor correspondente a progresso. | `float` | obrigatório |
| `extrapolar` | Valor correspondente a extrapolar. | `bool` | `False` |

**Retorno**

Retorna um valor declarado como `float`.

:::details Detalhes técnicos

**Assinatura:** `normalizar_progresso(progresso: float, *, extrapolar: bool = False) -> float`

**Origem da implementação:** `coral.jogos.transformacoes`

**Arquivo na release:** `coral/jogos/transformacoes.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `progresso` | posicional |
| `extrapolar` | nomeado |

:::

#### `curva_linear`

Executa a operação `curva_linear` disponibilizada por `coral.jogos`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `progresso` | Valor correspondente a progresso. | `float` | obrigatório |

**Retorno**

Retorna um valor declarado como `float`.

:::details Detalhes técnicos

**Assinatura:** `curva_linear(progresso: float) -> float`

**Origem da implementação:** `coral.jogos.transformacoes`

**Arquivo na release:** `coral/jogos/transformacoes.py`

:::

#### `curva_entrada_suave`

Executa a operação `curva_entrada_suave` disponibilizada por `coral.jogos`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `progresso` | Valor correspondente a progresso. | `float` | obrigatório |

**Retorno**

Retorna um valor declarado como `float`.

:::details Detalhes técnicos

**Assinatura:** `curva_entrada_suave(progresso: float) -> float`

**Origem da implementação:** `coral.jogos.transformacoes`

**Arquivo na release:** `coral/jogos/transformacoes.py`

:::

#### `curva_saida_suave`

Executa a operação `curva_saida_suave` disponibilizada por `coral.jogos`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `progresso` | Valor correspondente a progresso. | `float` | obrigatório |

**Retorno**

Retorna um valor declarado como `float`.

:::details Detalhes técnicos

**Assinatura:** `curva_saida_suave(progresso: float) -> float`

**Origem da implementação:** `coral.jogos.transformacoes`

**Arquivo na release:** `coral/jogos/transformacoes.py`

:::

#### `curva_entrada_saida_suave`

Executa a operação `curva_entrada_saida_suave` disponibilizada por `coral.jogos`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `progresso` | Valor correspondente a progresso. | `float` | obrigatório |

**Retorno**

Retorna um valor declarado como `float`.

:::details Detalhes técnicos

**Assinatura:** `curva_entrada_saida_suave(progresso: float) -> float`

**Origem da implementação:** `coral.jogos.transformacoes`

**Arquivo na release:** `coral/jogos/transformacoes.py`

:::

#### `curva_quadratica`

Executa a operação `curva_quadratica` disponibilizada por `coral.jogos`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `progresso` | Valor correspondente a progresso. | `float` | obrigatório |

**Retorno**

Retorna um valor declarado como `float`.

:::details Detalhes técnicos

**Assinatura:** `curva_quadratica(progresso: float) -> float`

**Origem da implementação:** `coral.jogos.transformacoes`

**Arquivo na release:** `coral/jogos/transformacoes.py`

:::

#### `curva_cubica`

Executa a operação `curva_cubica` disponibilizada por `coral.jogos`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `progresso` | Valor correspondente a progresso. | `float` | obrigatório |

**Retorno**

Retorna um valor declarado como `float`.

:::details Detalhes técnicos

**Assinatura:** `curva_cubica(progresso: float) -> float`

**Origem da implementação:** `coral.jogos.transformacoes`

**Arquivo na release:** `coral/jogos/transformacoes.py`

:::

#### `curva_degrau`

Executa a operação `curva_degrau` disponibilizada por `coral.jogos`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `progresso` | Valor correspondente a progresso. | `float` | obrigatório |

**Retorno**

Retorna um valor declarado como `float`.

:::details Detalhes técnicos

**Assinatura:** `curva_degrau(progresso: float) -> float`

**Origem da implementação:** `coral.jogos.transformacoes`

**Arquivo na release:** `coral/jogos/transformacoes.py`

:::

#### `resolver_curva_temporal`

Resolve curva temporal.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `curva` | Valor correspondente a curva. | `str \| Callable[[float], float]` | obrigatório |

**Retorno**

Retorna um valor declarado como `Callable[[float], float]`.

:::details Detalhes técnicos

**Assinatura:** `resolver_curva_temporal(curva: str \| Callable[[float], float]) -> Callable[[float], float]`

**Origem da implementação:** `coral.jogos.transformacoes`

**Arquivo na release:** `coral/jogos/transformacoes.py`

**Exceções diretamente observáveis no corpo:** `ValueError`

:::

#### `avaliar_curva_temporal`

Executa a operação `avaliar_curva_temporal` disponibilizada por `coral.jogos`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `curva` | Valor correspondente a curva. | `str \| Callable[[float], float]` | obrigatório |
| `progresso` | Valor correspondente a progresso. | `float` | obrigatório |
| `extrapolar` | Valor correspondente a extrapolar. | `bool` | `False` |

**Retorno**

Retorna um valor declarado como `float`.

:::details Detalhes técnicos

**Assinatura:** `avaliar_curva_temporal(curva: str \| Callable[[float], float], progresso: float, *, extrapolar: bool = False) -> float`

**Origem da implementação:** `coral.jogos.transformacoes`

**Arquivo na release:** `coral/jogos/transformacoes.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `curva` | posicional |
| `progresso` | posicional |
| `extrapolar` | nomeado |

:::

#### `interpolar`

Executa a operação `interpolar` disponibilizada por `coral.jogos`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `inicio` | Valor inicial do intervalo ou processo. | `float` | obrigatório |
| `fim` | Valor final do intervalo ou processo. | `float` | obrigatório |
| `progresso` | Valor correspondente a progresso. | `float` | obrigatório |
| `curva` | Valor correspondente a curva. | `str \| Callable[[float], float]` | `'linear'` |
| `extrapolar` | Valor correspondente a extrapolar. | `bool` | `False` |

**Retorno**

Retorna um valor declarado como `float`.

:::details Detalhes técnicos

**Assinatura:** `interpolar(inicio: float, fim: float, progresso: float, *, curva: str \| Callable[[float], float] = 'linear', extrapolar: bool = False) -> float`

**Origem da implementação:** `coral.jogos.transformacoes`

**Arquivo na release:** `coral/jogos/transformacoes.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `inicio` | posicional |
| `fim` | posicional |
| `progresso` | posicional |
| `curva` | nomeado |
| `extrapolar` | nomeado |

:::

#### `executar`

Executa o valor solicitado.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `acao` | Valor correspondente a acao. | `Callable[[], Any]` | obrigatório |
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str \| None` | `None` |

**Retorno**

Retorna um valor declarado como `AcaoApresentacao`.

:::details Detalhes técnicos

**Assinatura:** `executar(acao: Callable[[], Any], *, nome: str \| None = None) -> AcaoApresentacao`

**Origem da implementação:** `coral.jogos.composicao`

**Arquivo na release:** `coral/jogos/composicao.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `acao` | posicional |
| `nome` | nomeado |

:::

#### `esperar`

Executa a operação `esperar` disponibilizada por `coral.jogos`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `duracao` | Valor correspondente a duracao. | `float` | obrigatório |
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str \| None` | `None` |

**Retorno**

Retorna um valor declarado como `EsperaApresentacao`.

:::details Detalhes técnicos

**Assinatura:** `esperar(duracao: float, *, nome: str \| None = None) -> EsperaApresentacao`

**Origem da implementação:** `coral.jogos.composicao`

**Arquivo na release:** `coral/jogos/composicao.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `duracao` | posicional |
| `nome` | nomeado |

:::

#### `esperar_conclusao`

Executa a operação `esperar_conclusao` disponibilizada por `coral.jogos`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `alvo` | Valor correspondente a alvo. | `Any` | obrigatório |
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str \| None` | `None` |

**Retorno**

Retorna um valor declarado como `EsperaConclusao`.

:::details Detalhes técnicos

**Assinatura:** `esperar_conclusao(alvo: Any, *, nome: str \| None = None) -> EsperaConclusao`

**Origem da implementação:** `coral.jogos.composicao`

**Arquivo na release:** `coral/jogos/composicao.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `alvo` | posicional |
| `nome` | nomeado |

:::

#### `sequencia`

Executa a operação `sequencia` disponibilizada por `coral.jogos`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `*etapas` | Valor correspondente a etapas. | `NoApresentacao` | obrigatório |
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str \| None` | `None` |

**Retorno**

Retorna um valor declarado como `SequenciaApresentacao`.

:::details Detalhes técnicos

**Assinatura:** `sequencia(*etapas: NoApresentacao, nome: str \| None = None) -> SequenciaApresentacao`

**Origem da implementação:** `coral.jogos.composicao`

**Arquivo na release:** `coral/jogos/composicao.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `*etapas` | variádico |
| `nome` | nomeado |

:::

#### `paralelo`

Executa a operação `paralelo` disponibilizada por `coral.jogos`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `*etapas` | Valor correspondente a etapas. | `NoApresentacao` | obrigatório |
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str \| None` | `None` |

**Retorno**

Retorna um valor declarado como `ParaleloApresentacao`.

:::details Detalhes técnicos

**Assinatura:** `paralelo(*etapas: NoApresentacao, nome: str \| None = None) -> ParaleloApresentacao`

**Origem da implementação:** `coral.jogos.composicao`

**Arquivo na release:** `coral/jogos/composicao.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `*etapas` | variádico |
| `nome` | nomeado |

:::

#### `usar_fonte_tempo`

Seleciona fonte tempo.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `composicao` | Valor correspondente a composicao. | `ComposicaoTemporal` | obrigatório |
| `fonte` | Fonte explícita usada pela operação; quando omitida, vale o comportamento padrão do módulo. | `Any` | obrigatório |

**Retorno**

Retorna um valor declarado como `VinculoTempoApresentacao`.

:::details Detalhes técnicos

**Assinatura:** `usar_fonte_tempo(composicao: ComposicaoTemporal, fonte: Any) -> VinculoTempoApresentacao`

**Origem da implementação:** `coral.jogos.composicao`

**Arquivo na release:** `coral/jogos/composicao.py`

:::

#### `ligar_evento`

Liga evento.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `composicao` | Valor correspondente a composicao. | `ComposicaoTemporal` | obrigatório |
| `eventos` | Fonte ou conjunto de eventos associado à operação. | `Any` | obrigatório |
| `evento` | Valor correspondente a evento. | `str` | obrigatório |
| `modo` | Valor correspondente a modo. | `str` | `'reiniciar'` |

**Retorno**

Retorna um valor declarado como `VinculoComposicaoEventos`.

:::details Detalhes técnicos

**Assinatura:** `ligar_evento(composicao: ComposicaoTemporal, eventos: Any, evento: str, *, modo: str = 'reiniciar') -> VinculoComposicaoEventos`

**Origem da implementação:** `coral.jogos.composicao`

**Arquivo na release:** `coral/jogos/composicao.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `composicao` | posicional |
| `eventos` | posicional |
| `evento` | posicional |
| `modo` | nomeado |

:::

#### `forma_espacial_sprite`

Converte a geometria de um sprite para uma forma espacial usada em consultas e colisões.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `sprite` | Valor correspondente a sprite. | `Any` | obrigatório |

**Retorno**

Retorna um valor declarado como `Poligono`.

:::details Detalhes técnicos

**Assinatura:** `forma_espacial_sprite(sprite: Any) -> Poligono`

**Origem da implementação:** `coral.jogos.espacial`

**Arquivo na release:** `coral/jogos/espacial.py`

**Exceções diretamente observáveis no corpo:** `TypeError`

:::

#### `posicao_espacial_sprite`

Obtém a posição espacial correspondente ao sprite.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `sprite` | Valor correspondente a sprite. | `Any` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `posicao_espacial_sprite(sprite: Any)`

**Origem da implementação:** `coral.jogos.espacial`

**Arquivo na release:** `coral/jogos/espacial.py`

:::

#### `sprites_colidem`

Colisão 2D de Jogos usando sobreposição interior da baseline.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `a` | Valor correspondente a a. | `Any` | obrigatório |
| `b` | Valor correspondente a b. | `Any` | obrigatório |

**Retorno**

Retorna um valor lógico que indica o resultado da verificação.

:::details Detalhes técnicos

**Assinatura:** `sprites_colidem(a: Any, b: Any) -> bool`

**Origem da implementação:** `coral.jogos.espacial`

**Arquivo na release:** `coral/jogos/espacial.py`

:::

#### `adaptar_eventos`

Adapta eventos.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `jogo` | Valor correspondente a jogo. | `Jogo` | obrigatório |
| `teclas` | Valor correspondente a teclas. | `Iterable[str]` | `()` |
| `botoes_mouse` | Valor correspondente a botoes mouse. | `Iterable[str]` | `()` |
| `observar_mouse` | Valor correspondente a observar mouse. | `bool` | `False` |

**Retorno**

Retorna um valor declarado como `AdaptadorEventosJogo`.

:::details Detalhes técnicos

**Assinatura:** `adaptar_eventos(jogo: Jogo, *, teclas: Iterable[str] = (), botoes_mouse: Iterable[str] = (), observar_mouse: bool = False) -> AdaptadorEventosJogo`

**Origem da implementação:** `coral.jogos.eventos`

**Arquivo na release:** `coral/jogos/eventos.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `jogo` | posicional |
| `teclas` | nomeado |
| `botoes_mouse` | nomeado |
| `observar_mouse` | nomeado |

:::

#### `normalizar_categorias_debug`

Normaliza categorias públicas do modo de debug persistente.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `categorias` | Valor correspondente a categorias. | `Any` | `None` |

**Retorno**

Retorna um valor declarado como `frozenset[str]`.

:::details Detalhes técnicos

**Assinatura:** `normalizar_categorias_debug(categorias: Any = None) -> frozenset[str]`

**Origem da implementação:** `coral.jogos.debug`

**Arquivo na release:** `coral/jogos/debug.py`

**Exceções diretamente observáveis no corpo:** `ValueError`

:::

#### `gerar_overlay_debug`

Gera primitivas de debug sem desenhar e sem depender de backend gráfico.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `objeto` | Objeto processado pela operação. | `Any` | obrigatório |
| `limites` | Valor correspondente a limites. | `bool` | `True` |
| `colisores` | Valor correspondente a colisores. | `bool` | `True` |
| `camera` | Valor correspondente a camera. | `bool` | `True` |
| `pivos` | Valor correspondente a pivos. | `bool` | `True` |
| `rotulos` | Valor correspondente a rotulos. | `bool` | `False` |
| `incluir_invisiveis` | Controla se deve incluir invisiveis. | `bool` | `False` |

**Retorno**

Retorna um valor declarado como `OverlayDebug`.

:::details Detalhes técnicos

**Assinatura:** `gerar_overlay_debug(objeto: Any, *, limites: bool = True, colisores: bool = True, camera: bool = True, pivos: bool = True, rotulos: bool = False, incluir_invisiveis: bool = False) -> OverlayDebug`

**Origem da implementação:** `coral.jogos.debug`

**Arquivo na release:** `coral/jogos/debug.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `objeto` | posicional |
| `limites` | nomeado |
| `colisores` | nomeado |
| `camera` | nomeado |
| `pivos` | nomeado |
| `rotulos` | nomeado |
| `incluir_invisiveis` | nomeado |

:::

#### `gerar_overlay_metricas_debug`

Converte métricas operacionais em texto de tela, sem backend gráfico.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `metricas` | Valor correspondente a metricas. | `Any` | obrigatório |
| `x` | Coordenada horizontal. | `float` | `8.0` |
| `y` | Coordenada vertical. | `float` | `8.0` |
| `espacamento` | Valor correspondente a espacamento. | `float` | `18.0` |

**Retorno**

Retorna um valor declarado como `OverlayDebug`.

:::details Detalhes técnicos

**Assinatura:** `gerar_overlay_metricas_debug(metricas: Any, *, x: float = 8.0, y: float = 8.0, espacamento: float = 18.0) -> OverlayDebug`

**Origem da implementação:** `coral.jogos.debug`

**Arquivo na release:** `coral/jogos/debug.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `metricas` | posicional |
| `x` | nomeado |
| `y` | nomeado |
| `espacamento` | nomeado |

**Exceções diretamente observáveis no corpo:** `TypeError`

:::

#### `desenhar_overlay_debug`

Renderiza primitivas de debug pela API pública de desenho.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `alvo` | Valor correspondente a alvo. | `Any` | obrigatório |
| `overlay_ou_objeto` | Valor correspondente a overlay ou objeto. | `Any` | obrigatório |
| `camera` | Valor correspondente a camera. | `Any \| None` | `None` |
| `estilo` | Valor correspondente a estilo. | `EstiloOverlayDebug \| None` | `None` |
| `limites` | Valor correspondente a limites. | `bool` | `True` |
| `colisores` | Valor correspondente a colisores. | `bool` | `True` |
| `pivos` | Valor correspondente a pivos. | `bool` | `True` |
| `rotulos` | Valor correspondente a rotulos. | `bool` | `False` |
| `incluir_invisiveis` | Controla se deve incluir invisiveis. | `bool` | `False` |
| `mostrar_camera` | Valor correspondente a mostrar camera. | `bool` | `True` |

**Retorno**

Retorna um valor declarado como `OverlayDebug`.

:::details Detalhes técnicos

**Assinatura:** `desenhar_overlay_debug(alvo: Any, overlay_ou_objeto: Any, *, camera: Any \| None = None, estilo: EstiloOverlayDebug \| None = None, limites: bool = True, colisores: bool = True, pivos: bool = True, rotulos: bool = False, incluir_invisiveis: bool = False, mostrar_camera: bool = True) -> OverlayDebug`

**Origem da implementação:** `coral.jogos.debug`

**Arquivo na release:** `coral/jogos/debug.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `alvo` | posicional |
| `overlay_ou_objeto` | posicional |
| `camera` | nomeado |
| `estilo` | nomeado |
| `limites` | nomeado |
| `colisores` | nomeado |
| `pivos` | nomeado |
| `rotulos` | nomeado |
| `incluir_invisiveis` | nomeado |
| `mostrar_camera` | nomeado |

**Exceções diretamente observáveis no corpo:** `TypeError`

:::

#### `celula_para_tela`

Converte coordenadas de celula para tela.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `mapa` | Valor correspondente a mapa. | `Mapa` | obrigatório |
| `camera` | Valor correspondente a camera. | `Camera \| None` | obrigatório |
| `celula` | Valor correspondente a celula. | `Any` | obrigatório |
| `ancora` | Valor correspondente a ancora. | `str` | `'centro'` |
| `viewport` | Valor correspondente a viewport. | `Viewport \| None` | `None` |

**Retorno**

Retorna um valor declarado como `tuple[float, float]`.

:::details Detalhes técnicos

**Assinatura:** `celula_para_tela(mapa: Mapa, camera: Camera \| None, celula: Any, *, ancora: str = 'centro', viewport: Viewport \| None = None) -> tuple[float, float]`

**Origem da implementação:** `coral.jogos.mapas`

**Arquivo na release:** `coral/jogos/mapas.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `mapa` | posicional |
| `camera` | posicional |
| `celula` | posicional |
| `ancora` | nomeado |
| `viewport` | nomeado |

:::

#### `mundo_para_tela`

Converte coordenadas de mundo para tela.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `camera` | Valor correspondente a camera. | `Camera \| None` | obrigatório |
| `coordenada` | Valor correspondente a coordenada. | `Any` | obrigatório |
| `viewport` | Valor correspondente a viewport. | `Viewport \| None` | `None` |

**Retorno**

Retorna um valor declarado como `tuple[float, float]`.

:::details Detalhes técnicos

**Assinatura:** `mundo_para_tela(camera: Camera \| None, coordenada: Any, *, viewport: Viewport \| None = None) -> tuple[float, float]`

**Origem da implementação:** `coral.jogos.mapas`

**Arquivo na release:** `coral/jogos/mapas.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `camera` | posicional |
| `coordenada` | posicional |
| `viewport` | nomeado |

**Exceções diretamente observáveis no corpo:** `ErroMapaCoral`

:::

#### `tela_para_celula`

Converte coordenadas de tela para celula.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `mapa` | Valor correspondente a mapa. | `Mapa` | obrigatório |
| `camera` | Valor correspondente a camera. | `Camera \| None` | obrigatório |
| `x` | Coordenada horizontal. | `float` | obrigatório |
| `y` | Coordenada vertical. | `float` | obrigatório |
| `viewport` | Valor correspondente a viewport. | `Viewport \| None` | `None` |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `tela_para_celula(mapa: Mapa, camera: Camera \| None, x: float, y: float, *, viewport: Viewport \| None = None)`

**Origem da implementação:** `coral.jogos.mapas`

**Arquivo na release:** `coral/jogos/mapas.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `mapa` | posicional |
| `camera` | posicional |
| `x` | posicional |
| `y` | posicional |
| `viewport` | nomeado |

:::

#### `tela_para_mundo`

Converte coordenadas de tela para mundo.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `camera` | Valor correspondente a camera. | `Camera \| None` | obrigatório |
| `x` | Coordenada horizontal. | `float` | obrigatório |
| `y` | Coordenada vertical. | `float` | obrigatório |
| `viewport` | Valor correspondente a viewport. | `Viewport \| None` | `None` |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `tela_para_mundo(camera: Camera \| None, x: float, y: float, *, viewport: Viewport \| None = None)`

**Origem da implementação:** `coral.jogos.mapas`

**Arquivo na release:** `coral/jogos/mapas.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `camera` | posicional |
| `x` | posicional |
| `y` | posicional |
| `viewport` | nomeado |

**Exceções diretamente observáveis no corpo:** `ErroMapaCoral`

:::

#### `animar_propriedade`

Anime uma propriedade pública suportada até um valor em tempo explícito.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `alvo` | Valor correspondente a alvo. | `Any` | obrigatório |
| `propriedade` | Valor correspondente a propriedade. | `str` | obrigatório |
| `valor` | Valor processado pela operação. | `float` | obrigatório |
| `duracao` | Valor correspondente a duracao. | `float` | obrigatório |
| `curva` | Valor correspondente a curva. | `str \| Callable[[float], float]` | `'suave'` |
| `modo` | Valor correspondente a modo. | `str` | `'normal'` |

**Retorno**

Retorna um valor declarado como `'VinculoClipe'`.

:::details Detalhes técnicos

**Assinatura:** `animar_propriedade(alvo: Any, propriedade: str, valor: float, duracao: float, *, curva: str \| Callable[[float], float] = 'suave', modo: str = 'normal') -> 'VinculoClipe'`

**Origem da implementação:** `coral.jogos.objetos`

**Arquivo na release:** `coral/jogos/objetos.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `alvo` | posicional |
| `propriedade` | posicional |
| `valor` | posicional |
| `duracao` | posicional |
| `curva` | nomeado |
| `modo` | nomeado |

**Exceções diretamente observáveis no corpo:** `ValueError`

:::

#### `reproduzir_ao_contrario`

Reinicie uma animação ou clipe no modo reverso, quando suportado.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `animacao` | Valor correspondente a animacao. | `Any` | obrigatório |

**Retorno**

Retorna um valor declarado como `Any`.

:::details Detalhes técnicos

**Assinatura:** `reproduzir_ao_contrario(animacao: Any) -> Any`

**Origem da implementação:** `coral.jogos.objetos`

**Arquivo na release:** `coral/jogos/objetos.py`

**Exceções diretamente observáveis no corpo:** `TypeError`

:::

### Classes e protocolos

#### `Jogo`

Representa ciclo principal, entrada, cenas e transições.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `titulo` | Valor correspondente a titulo. | `str` | obrigatório |
| `largura` | Largura usada pela operação. | `int` | `800` |
| `altura` | Altura usada pela operação. | `int` | `450` |
| `fps` | Quantidade alvo de quadros por segundo. | `int` | `60` |
| `backend` | Backend usado para executar a operação. | `BackendJogos` | obrigatório |
| `mundo` | Mundo associado à operação. | `não declarado` | `None` |
| `relogio` | Relógio usado para controlar tempo ou atualização. | `FonteTempo \| None` | `None` |
| `eventos` | Fonte ou conjunto de eventos associado à operação. | `Eventos \| None` | `None` |
| `tela_cheia` | Define se a janela deve usar tela cheia. | `bool` | `False` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `estado_inspecao` | Executa a operação `estado_inspecao` disponibilizada por `coral.jogos`. | `dict[str, Any]` |
| `estado_debug` | Executa a operação `estado_debug` disponibilizada por `coral.jogos`. | `dict[str, Any]` |
| `observabilidade_ativa` | Indica se há trabalho opcional de inspeção ou overlay por quadro. | `bool` |
| `debug_ativo` | Executa a operação `debug_ativo` disponibilizada por `coral.jogos`. | `bool` |
| `configurar_debug` | Configura debug. | `não declarado` |
| `ativar_debug` | Executa a operação `ativar_debug` disponibilizada por `coral.jogos`. | `não declarado` |
| `desativar_debug` | Executa a operação `desativar_debug` disponibilizada por `coral.jogos`. | `não declarado` |
| `alternar_debug` | Alterna debug. | `bool` |
| `desenhar_debug` | Desenha o modo persistente atual e devolve o overlay combinado. | `não declarado` |
| `monitorar_inspecao` | Ativa histórico curto de observabilidade no próprio laço do jogo. | `não declarado` |
| `parar_monitoramento_inspecao` | Interrompe monitoramento inspecao. | `não declarado` |
| `historico_inspecao` | Executa a operação `historico_inspecao` disponibilizada por `coral.jogos`. | `não declarado` |
| `quando_iniciar` | Registra uma ação para quando ocorrer iniciar. | `não declarado` |
| `quando_atualizar` | Registra uma ação para quando ocorrer atualizar. | `não declarado` |
| `quando_desenhar` | Registra uma ação para quando ocorrer desenhar. | `não declarado` |
| `quando_encerrar` | Registra uma ação para quando ocorrer encerrar. | `não declarado` |
| `parar` | Interrompe o valor solicitado. | `None` |
| `remover_mundo` | Desassocia o Mundo atual e remove somente a propagação criada pelo Jogo. | `não declarado` |
| `usar_mundo` | Associa um Mundo ao jogo e propaga eventos do Mundo para o Jogo. | `não declarado` |
| `tecla_pressionada` | Executa a operação `tecla_pressionada` disponibilizada por `coral.jogos`. | `bool` |
| `posicao_mouse` | Executa a operação `posicao_mouse` disponibilizada por `coral.jogos`. | `tuple[int, int]` |
| `tamanho_logico` | Executa a operação `tamanho_logico` disponibilizada por `coral.jogos`. | `tuple[int, int]` |
| `tamanho_fisico` | Executa a operação `tamanho_fisico` disponibilizada por `coral.jogos`. | `tuple[int, int]` |
| `viewport` | Executa a operação `viewport` disponibilizada por `coral.jogos`. | `Viewport` |
| `posicao_mouse_logica` | Executa a operação `posicao_mouse_logica` disponibilizada por `coral.jogos`. | `tuple[float, float]` |
| `redimensionar_janela` | Executa a operação `redimensionar_janela` disponibilizada por `coral.jogos`. | `tuple[int, int]` |
| `botao_mouse_pressionado` | Executa a operação `botao_mouse_pressionado` disponibilizada por `coral.jogos`. | `bool` |
| `mouse_clicado` | Executa a operação `mouse_clicado` disponibilizada por `coral.jogos`. | `bool` |
| `mouse_solto` | Executa a operação `mouse_solto` disponibilizada por `coral.jogos`. | `bool` |
| `roda_mouse` | Executa a operação `roda_mouse` disponibilizada por `coral.jogos`. | `tuple[int, int]` |
| `em_tela_cheia` | Indica o estado de em tela cheia. | `bool` |
| `definir_tela_cheia` | Define tela cheia. | `None` |
| `alternar_tela_cheia` | Alterna tela cheia. | `bool` |
| `limpar` | Limpa o valor solicitado. | `None` |
| `desenhar_retangulo` | Desenha retangulo. | `Retangulo` |
| `desenhar_circulo` | Desenha circulo. | `None` |
| `desenhar_linha` | Desenha linha. | `None` |
| `desenhar_poligono` | Desenha poligono. | `None` |
| `desenhar_overlay_debug` | Desenha um overlay de debug usando somente a API pública de Jogos. | `não declarado` |
| `desenhar_ponto` | Desenha ponto. | `None` |
| `desenhar_texto` | Desenha texto. | `None` |
| `medir_texto` | Executa a operação `medir_texto` disponibilizada por `coral.jogos`. | `tuple[float, float]` |
| `desenhar_imagem` | Desenha imagem. | `None` |
| `tocar_som` | Executa som. | `None` |
| `mudar_cena` | Executa a operação `mudar_cena` disponibilizada por `coral.jogos`. | `None` |
| `transicao_cena` | Executa a operação `transicao_cena` disponibilizada por `coral.jogos`. | `TransicaoCena \| None` |
| `entrada_bloqueada_por_transicao` | Executa a operação `entrada_bloqueada_por_transicao` disponibilizada por `coral.jogos`. | `bool` |
| `mudar_cena_com_transicao` | Executa a operação `mudar_cena_com_transicao` disponibilizada por `coral.jogos`. | `TransicaoCena` |
| `cancelar_transicao_cena` | Cancela transicao cena. | `bool` |
| `executar` | Executa o valor solicitado. | `None` |

:::details Detalhes técnicos

**Assinatura:** `Jogo(titulo: str, largura: int = 800, altura: int = 450, fps: int = 60, *, backend: BackendJogos, mundo = None, relogio: FonteTempo \| None = None, eventos: Eventos \| None = None, tela_cheia: bool = False)`

**Origem da implementação:** `coral.jogos.base`

**Arquivo na release:** `coral/jogos/base.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `titulo` | posicional |
| `largura` | posicional |
| `altura` | posicional |
| `fps` | posicional |
| `backend` | nomeado |
| `mundo` | nomeado |
| `relogio` | nomeado |
| `eventos` | nomeado |
| `tela_cheia` | nomeado |

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `estado_inspecao` | método | `estado_inspecao() -> dict[str, Any]` |
| `estado_debug` | método | `estado_debug() -> dict[str, Any]` |
| `observabilidade_ativa` | método | `observabilidade_ativa() -> bool` |
| `debug_ativo` | método | `debug_ativo() -> bool` |
| `configurar_debug` | método | `configurar_debug(*, ativo: bool \| None = None, categorias = None, incluir_invisiveis: bool \| None = None, estilo = None)` |
| `ativar_debug` | método | `ativar_debug(*categorias: str, incluir_invisiveis: bool \| None = None, estilo = None)` |
| `desativar_debug` | método | `desativar_debug()` |
| `alternar_debug` | método | `alternar_debug(*categorias: str) -> bool` |
| `desenhar_debug` | método | `desenhar_debug()` |
| `monitorar_inspecao` | método | `monitorar_inspecao(*, max_amostras: int = 120, intervalo: float = 0.1, somente_mudancas: bool = True)` |
| `parar_monitoramento_inspecao` | método | `parar_monitoramento_inspecao()` |
| `historico_inspecao` | método | `historico_inspecao()` |
| `quando_iniciar` | método | `quando_iniciar(funcao: Callable[['Jogo'], Any])` |
| `quando_atualizar` | método | `quando_atualizar(funcao: Callable[['Jogo', float], Any])` |
| `quando_desenhar` | método | `quando_desenhar(funcao: Callable[['Jogo'], Any])` |
| `quando_encerrar` | método | `quando_encerrar(funcao: Callable[['Jogo'], Any])` |
| `parar` | método | `parar() -> None` |
| `remover_mundo` | método | `remover_mundo()` |
| `usar_mundo` | método | `usar_mundo(mundo)` |
| `tecla_pressionada` | método | `tecla_pressionada(tecla: str) -> bool` |
| `posicao_mouse` | método | `posicao_mouse() -> tuple[int, int]` |
| `tamanho_logico` | método | `tamanho_logico() -> tuple[int, int]` |
| `tamanho_fisico` | método | `tamanho_fisico() -> tuple[int, int]` |
| `viewport` | método | `viewport(*, modo: str = 'ajustar') -> Viewport` |
| `posicao_mouse_logica` | método | `posicao_mouse_logica(*, limitar: bool = False, modo: str = 'ajustar') -> tuple[float, float]` |
| `redimensionar_janela` | método | `redimensionar_janela(largura: int, altura: int) -> tuple[int, int]` |
| `botao_mouse_pressionado` | método | `botao_mouse_pressionado(botao: str = 'esquerdo') -> bool` |
| `mouse_clicado` | método | `mouse_clicado(botao: str = 'esquerdo') -> bool` |
| `mouse_solto` | método | `mouse_solto(botao: str = 'esquerdo') -> bool` |
| `roda_mouse` | método | `roda_mouse() -> tuple[int, int]` |
| `em_tela_cheia` | método | `em_tela_cheia() -> bool` |
| `definir_tela_cheia` | método | `definir_tela_cheia(ativa: bool) -> None` |
| `alternar_tela_cheia` | método | `alternar_tela_cheia() -> bool` |
| `limpar` | método | `limpar(cor: Cor = PRETO) -> None` |
| `desenhar_retangulo` | método | `desenhar_retangulo(x: float, y: float, largura: float, altura: float, cor: Cor = BRANCO, *, contorno: int = 0, opacidade: float = 1.0) -> Retangulo` |
| `desenhar_circulo` | método | `desenhar_circulo(x: float, y: float, raio: float, cor: Cor = BRANCO, *, contorno: int = 0, opacidade: float = 1.0) -> None` |
| `desenhar_linha` | método | `desenhar_linha(x1: float, y1: float, x2: float, y2: float, cor: Cor = BRANCO, *, espessura: int = 1, opacidade: float = 1.0) -> None` |
| `desenhar_poligono` | método | `desenhar_poligono(vertices, cor: Cor = BRANCO, *, contorno: int = 1, opacidade: float = 1.0) -> None` |
| `desenhar_overlay_debug` | método | `desenhar_overlay_debug(objeto = None, **opcoes)` |
| `desenhar_ponto` | método | `desenhar_ponto(x: float, y: float, cor: Cor = BRANCO, *, tamanho: int = 1, opacidade: float = 1.0) -> None` |
| `desenhar_texto` | método | `desenhar_texto(texto: str, x: float, y: float, tamanho: int = 24, cor: Cor = BRANCO, *, origem: str = 'topo_esquerdo', opacidade: float = 1.0) -> None` |
| `medir_texto` | método | `medir_texto(texto: str, tamanho: int = 24) -> tuple[float, float]` |
| `desenhar_imagem` | método | `desenhar_imagem(caminho: str \| QuadroSprite, x: float, y: float, largura: float \| None = None, altura: float \| None = None, *, escala: float = 1.0, rotacao: float = 0.0, espelhar_horizontalmente: bool = False, espelhar_verticalmente: bool = False, origem: str = 'topo_esquerdo', pivo: tuple[float, float] \| None = None, opacidade: float = 1.0) -> None` |
| `tocar_som` | método | `tocar_som(caminho: str, volume: float = 1.0) -> None` |
| `mudar_cena` | método | `mudar_cena(cena) -> None` |
| `transicao_cena` | propriedade | `transicao_cena() -> TransicaoCena \| None` |
| `entrada_bloqueada_por_transicao` | método | `entrada_bloqueada_por_transicao() -> bool` |
| `mudar_cena_com_transicao` | método | `mudar_cena_com_transicao(cena, *, tipo: str = 'desaparecer', duracao: float = 0.4, curva: str \| Callable[[float], float] = 'suave', bloquear_entrada: bool = True, atualizar_anterior: bool = True, atualizar_proxima: bool = True, direcao: str = 'direita') -> TransicaoCena` |
| `cancelar_transicao_cena` | método | `cancelar_transicao_cena() -> bool` |
| `executar` | método | `executar(*, max_quadros: int \| None = None) -> None` |

:::

#### `TransicaoCena`

Coordena apresentação temporal entre duas cenas sem possuir o jogo.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `origem` | Origem usada pela operação. | `Any` | obrigatório |
| `destino` | Destino que receberá o resultado da operação. | `Any` | obrigatório |
| `tipo` | Tipo solicitado para o resultado, quando o módulo oferece essa escolha. | `str` | `'desaparecer'` |
| `duracao` | Valor correspondente a duracao. | `float` | `0.4` |
| `curva` | Valor correspondente a curva. | `str \| Callable[[float], float]` | `'suave'` |
| `bloquear_entrada` | Valor correspondente a bloquear entrada. | `bool` | `True` |
| `atualizar_anterior` | Valor correspondente a atualizar anterior. | `bool` | `True` |
| `atualizar_proxima` | Valor correspondente a atualizar proxima. | `bool` | `True` |
| `direcao` | Valor correspondente a direcao. | `str` | `'direita'` |
| `tempo` | Valor correspondente a tempo. | `float` | `0.0` |
| `estado` | Estado usado ou atualizado pela operação. | `str` | `'ativo'` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `origem` | Origem usada pela operação. | `Any` | obrigatório |
| `destino` | Destino que receberá o resultado da operação. | `Any` | obrigatório |
| `tipo` | Tipo solicitado para o resultado, quando o módulo oferece essa escolha. | `str` | `'desaparecer'` |
| `duracao` | Valor correspondente a duracao. | `float` | `0.4` |
| `curva` | Valor correspondente a curva. | `str \| Callable[[float], float]` | `'suave'` |
| `bloquear_entrada` | Valor correspondente a bloquear entrada. | `bool` | `True` |
| `atualizar_anterior` | Valor correspondente a atualizar anterior. | `bool` | `True` |
| `atualizar_proxima` | Valor correspondente a atualizar proxima. | `bool` | `True` |
| `direcao` | Valor correspondente a direcao. | `str` | `'direita'` |
| `tempo` | Valor correspondente a tempo. | `float` | `0.0` |
| `estado` | Estado usado ou atualizado pela operação. | `str` | `'ativo'` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `progresso` | Executa a operação `progresso` disponibilizada por `coral.jogos`. | `float` |
| `progresso_curvo` | Executa a operação `progresso_curvo` disponibilizada por `coral.jogos`. | `float` |
| `ativa` | Executa a operação `ativa` disponibilizada por `coral.jogos`. | `bool` |
| `finalizada` | Indica o estado de finalizada. | `bool` |
| `fase` | Executa a operação `fase` disponibilizada por `coral.jogos`. | `str` |
| `entrada_bloqueada` | Executa a operação `entrada_bloqueada` disponibilizada por `coral.jogos`. | `bool` |
| `ao_concluir` | Executa a operação `ao_concluir` disponibilizada por `coral.jogos`. | `Callable` |
| `pausar` | Pausa o valor solicitado. | `'TransicaoCena'` |
| `retomar` | Retoma o valor solicitado. | `'TransicaoCena'` |
| `cancelar` | Cancela o valor solicitado. | `'TransicaoCena'` |
| `avancar` | Avança e informa se a troca de cena deve ocorrer neste passo. | `bool` |
| `amostra` | Estado visual independente de backend para renderers e testes. | `dict[str, Any]` |

:::details Detalhes técnicos

**Assinatura:** `TransicaoCena(origem: Any, destino: Any, tipo: str = 'desaparecer', duracao: float = 0.4, curva: str \| Callable[[float], float] = 'suave', bloquear_entrada: bool = True, atualizar_anterior: bool = True, atualizar_proxima: bool = True, direcao: str = 'direita', tempo: float = 0.0, estado: str = 'ativo')`

**Origem da implementação:** `coral.jogos.base`

**Arquivo na release:** `coral/jogos/base.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `progresso` | propriedade | `progresso() -> float` |
| `progresso_curvo` | propriedade | `progresso_curvo() -> float` |
| `ativa` | propriedade | `ativa() -> bool` |
| `finalizada` | propriedade | `finalizada() -> bool` |
| `fase` | propriedade | `fase() -> str` |
| `entrada_bloqueada` | propriedade | `entrada_bloqueada() -> bool` |
| `ao_concluir` | método | `ao_concluir(callback: Callable) -> Callable` |
| `pausar` | método | `pausar() -> 'TransicaoCena'` |
| `retomar` | método | `retomar() -> 'TransicaoCena'` |
| `cancelar` | método | `cancelar() -> 'TransicaoCena'` |
| `avancar` | método | `avancar(dt: float) -> bool` |
| `amostra` | método | `amostra() -> dict[str, Any]` |

:::

#### `MetricasJogo`

Métricas operacionais leves e determinísticas do laço principal.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `quadros` | Valor correspondente a quadros. | `int` | `0` |
| `delta_logico` | Valor correspondente a delta logico. | `float` | `0.0` |
| `tempo_quadro` | Valor correspondente a tempo quadro. | `float` | `0.0` |
| `fps_instantaneo` | Valor correspondente a FPS instantaneo. | `float` | `0.0` |
| `fps_medio` | Valor correspondente a FPS medio. | `float` | `0.0` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `quadros` | Valor correspondente a quadros. | `int` | `0` |
| `delta_logico` | Valor correspondente a delta logico. | `float` | `0.0` |
| `tempo_quadro` | Valor correspondente a tempo quadro. | `float` | `0.0` |
| `fps_instantaneo` | Valor correspondente a FPS instantaneo. | `float` | `0.0` |
| `fps_medio` | Valor correspondente a FPS medio. | `float` | `0.0` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `tempo_quadro_ms` | Executa a operação `tempo_quadro_ms` disponibilizada por `coral.jogos`. | `float` |
| `registrar` | Registra o valor solicitado. | `None` |
| `estado_inspecao` | Executa a operação `estado_inspecao` disponibilizada por `coral.jogos`. | `dict[str, Any]` |

:::details Detalhes técnicos

**Assinatura:** `MetricasJogo(quadros: int = 0, delta_logico: float = 0.0, tempo_quadro: float = 0.0, fps_instantaneo: float = 0.0, fps_medio: float = 0.0)`

**Origem da implementação:** `coral.jogos.base`

**Arquivo na release:** `coral/jogos/base.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `tempo_quadro_ms` | propriedade | `tempo_quadro_ms() -> float` |
| `registrar` | método | `registrar(delta_logico: float, tempo_quadro: float) -> None` |
| `estado_inspecao` | método | `estado_inspecao() -> dict[str, Any]` |

:::

#### `Cor`

Representa Cor na API de `coral.jogos`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `vermelho` | Valor correspondente a vermelho. | `int` | obrigatório |
| `verde` | Valor correspondente a verde. | `int` | obrigatório |
| `azul` | Valor correspondente a azul. | `int` | obrigatório |
| `alfa` | Valor correspondente a alfa. | `int` | `255` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `vermelho` | Valor correspondente a vermelho. | `int` | obrigatório |
| `verde` | Valor correspondente a verde. | `int` | obrigatório |
| `azul` | Valor correspondente a azul. | `int` | obrigatório |
| `alfa` | Valor correspondente a alfa. | `int` | `255` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `rgb` | Cria uma cor a partir de componentes RGB. | `tuple[int, int, int]` |

:::details Detalhes técnicos

**Assinatura:** `Cor(vermelho: int, verde: int, azul: int, alfa: int = 255)`

**Origem da implementação:** `coral.jogos.base`

**Arquivo na release:** `coral/jogos/base.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `rgb` | método | `rgb() -> tuple[int, int, int]` |

:::

#### `Retangulo`

Representa Retangulo na API de `coral.jogos`.

**Exemplo**

```coral
execute camera.definir_zona_morta(20, 12)
execute camera.seguir(heroi, constante_tempo=0.25, antecipacao=0.2)
execute camera.definir_limites(Retangulo(0, 0, 1000, 600))
execute camera.enquadrar_alvos([heroi, aliado], margem=20, ajustar_zoom=True)
execute camera.definir_rotacao(15)
```

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `x` | Coordenada horizontal. | `float` | obrigatório |
| `y` | Coordenada vertical. | `float` | obrigatório |
| `largura` | Largura usada pela operação. | `float` | obrigatório |
| `altura` | Altura usada pela operação. | `float` | obrigatório |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `x` | Coordenada horizontal. | `float` | obrigatório |
| `y` | Coordenada vertical. | `float` | obrigatório |
| `largura` | Largura usada pela operação. | `float` | obrigatório |
| `altura` | Altura usada pela operação. | `float` | obrigatório |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `colide_com` | Executa a operação `colide_com` disponibilizada por `coral.jogos`. | `bool` |

:::details Detalhes técnicos

**Assinatura:** `Retangulo(x: float, y: float, largura: float, altura: float)`

**Origem da implementação:** `coral.jogos.base`

**Arquivo na release:** `coral/jogos/base.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `colide_com` | método | `colide_com(outro: 'Retangulo') -> bool` |

:::

#### `BackendNulo`

Backend determinístico para testes, servidores e execução sem interface gráfica.

**Exemplo**

```coral
defina camera como Camera(0, 0, 64, 64)
defina backend como BackendNulo()
defina renderizador como RenderizadorMapa2D(sala, camera=camera)
defina desenhadas como renderizador.desenhar(backend)
```

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `dt_fixo` | Valor correspondente a dt fixo. | `float \| None` | `None` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `definir_teclas` | Substitui o estado atual de teclado do backend sem janela. | `None` |
| `programar_teclas` | Programa estados de teclado por quadro para testes determinísticos. | `None` |
| `definir_mouse` | Define mouse. | `None` |
| `programar_mouse` | Programa mouse. | `None` |
| `iniciar` | Inicia o valor solicitado. | `None` |
| `processar_eventos` | Processa eventos. | `bool` |
| `tecla_pressionada` | Executa a operação `tecla_pressionada` disponibilizada por `coral.jogos`. | `bool` |
| `posicao_mouse` | Executa a operação `posicao_mouse` disponibilizada por `coral.jogos`. | `tuple[int, int]` |
| `botao_mouse_pressionado` | Executa a operação `botao_mouse_pressionado` disponibilizada por `coral.jogos`. | `bool` |
| `mouse_clicado` | Executa a operação `mouse_clicado` disponibilizada por `coral.jogos`. | `bool` |
| `mouse_solto` | Executa a operação `mouse_solto` disponibilizada por `coral.jogos`. | `bool` |
| `roda_mouse` | Executa a operação `roda_mouse` disponibilizada por `coral.jogos`. | `tuple[int, int]` |
| `definir_tela_cheia` | Define tela cheia. | `None` |
| `definir_tamanho_janela` | Define tamanho janela. | `None` |
| `tamanho_fisico` | Executa a operação `tamanho_fisico` disponibilizada por `coral.jogos`. | `tuple[int, int]` |
| `definir_recorte` | Define recorte. | `None` |
| `limpar` | Limpa o valor solicitado. | `None` |
| `desenhar_retangulo` | Desenha retangulo. | `None` |
| `desenhar_circulo` | Desenha circulo. | `None` |
| `desenhar_linha` | Desenha linha. | `None` |
| `desenhar_poligono` | Desenha poligono. | `None` |
| `desenhar_ponto` | Desenha ponto. | `None` |
| `desenhar_texto` | Desenha texto. | `None` |
| `medir_texto` | Executa a operação `medir_texto` disponibilizada por `coral.jogos`. | `tuple[float, float]` |
| `desenhar_imagem` | Desenha imagem. | `None` |
| `apresentar` | Executa a operação `apresentar` disponibilizada por `coral.jogos`. | `None` |
| `tocar_som` | Executa som. | `None` |
| `limitar_fps` | Executa a operação `limitar_fps` disponibilizada por `coral.jogos`. | `float` |
| `encerrar` | Encerra o valor solicitado. | `None` |

:::details Detalhes técnicos

**Assinatura:** `BackendNulo(*, dt_fixo: float \| None = None)`

**Origem da implementação:** `coral.jogos.base`

**Arquivo na release:** `coral/jogos/base.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `dt_fixo` | nomeado |

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `definir_teclas` | método | `definir_teclas(*teclas: str) -> None` |
| `programar_teclas` | método | `programar_teclas(*quadros) -> None` |
| `definir_mouse` | método | `definir_mouse(*, posicao: tuple[int, int] = (0, 0), pressionados = (), clicados = (), soltos = (), roda: tuple[int, int] = (0, 0)) -> None` |
| `programar_mouse` | método | `programar_mouse(*quadros: dict[str, Any]) -> None` |
| `iniciar` | método | `iniciar(titulo: str, largura: int, altura: int, *, tela_cheia: bool = False) -> None` |
| `processar_eventos` | método | `processar_eventos() -> bool` |
| `tecla_pressionada` | método | `tecla_pressionada(tecla: str) -> bool` |
| `posicao_mouse` | método | `posicao_mouse() -> tuple[int, int]` |
| `botao_mouse_pressionado` | método | `botao_mouse_pressionado(botao: str) -> bool` |
| `mouse_clicado` | método | `mouse_clicado(botao: str) -> bool` |
| `mouse_solto` | método | `mouse_solto(botao: str) -> bool` |
| `roda_mouse` | método | `roda_mouse() -> tuple[int, int]` |
| `definir_tela_cheia` | método | `definir_tela_cheia(ativa: bool) -> None` |
| `definir_tamanho_janela` | método | `definir_tamanho_janela(largura: int, altura: int) -> None` |
| `tamanho_fisico` | método | `tamanho_fisico() -> tuple[int, int]` |
| `definir_recorte` | método | `definir_recorte(recorte: Retangulo \| None) -> None` |
| `limpar` | método | `limpar(cor: Cor) -> None` |
| `desenhar_retangulo` | método | `desenhar_retangulo(retangulo: Retangulo, cor: Cor, *, contorno: int = 0, opacidade: float = 1.0) -> None` |
| `desenhar_circulo` | método | `desenhar_circulo(x: float, y: float, raio: float, cor: Cor, *, contorno: int = 0, opacidade: float = 1.0) -> None` |
| `desenhar_linha` | método | `desenhar_linha(x1: float, y1: float, x2: float, y2: float, cor: Cor, *, espessura: int = 1, opacidade: float = 1.0) -> None` |
| `desenhar_poligono` | método | `desenhar_poligono(vertices, cor: Cor, *, contorno: int = 1, opacidade: float = 1.0) -> None` |
| `desenhar_ponto` | método | `desenhar_ponto(x: float, y: float, cor: Cor, *, tamanho: int = 1, opacidade: float = 1.0) -> None` |
| `desenhar_texto` | método | `desenhar_texto(texto: str, x: float, y: float, tamanho: int, cor: Cor, *, origem: str = 'topo_esquerdo', opacidade: float = 1.0) -> None` |
| `medir_texto` | método | `medir_texto(texto: str, tamanho: int) -> tuple[float, float]` |
| `desenhar_imagem` | método | `desenhar_imagem(caminho: str \| QuadroSprite, x: float, y: float, largura: float \| None = None, altura: float \| None = None, *, escala: float = 1.0, rotacao: float = 0.0, espelhar_horizontalmente: bool = False, espelhar_verticalmente: bool = False, origem: str = 'topo_esquerdo', pivo: tuple[float, float] \| None = None, opacidade: float = 1.0) -> None` |
| `apresentar` | método | `apresentar() -> None` |
| `tocar_som` | método | `tocar_som(caminho: str, *, volume: float = 1.0) -> None` |
| `limitar_fps` | método | `limitar_fps(fps: int) -> float` |
| `encerrar` | método | `encerrar() -> None` |

:::

#### `Assets`

Representa Assets na API de `coral.jogos`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `raiz` | Valor correspondente a raiz. | `str \| Path` | `'assets'` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `imagem` | Obtém imagem. | `Path` |
| `som` | Obtém som. | `Path` |
| `spritesheet` | Obtém spritesheet. | `Spritesheet` |

:::details Detalhes técnicos

**Assinatura:** `Assets(raiz: str \| Path = 'assets')`

**Origem da implementação:** `coral.jogos.objetos`

**Arquivo na release:** `coral/jogos/objetos.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `imagem` | método | `imagem(nome: str \| Path) -> Path` |
| `som` | método | `som(nome: str \| Path) -> Path` |
| `spritesheet` | método | `spritesheet(nome: str \| Path, *, largura_imagem: int, altura_imagem: int, largura_quadro: int, altura_quadro: int, margem: int = 0, espacamento: int = 0) -> Spritesheet` |

:::

#### `Sprite`

Representa objeto visual transformável.

**Exemplo**

```coral
defina camera como Camera(0, 0, 320, 180)
defina heroi como Sprite(100, 80, 16, 16, velocidade_x=40)
defina aliado como Sprite(260, 120, 16, 16)

execute camera.definir_zona_morta(20, 12)
```

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `x` | Coordenada horizontal. | `float` | obrigatório |
| `y` | Coordenada vertical. | `float` | obrigatório |
| `largura` | Largura usada pela operação. | `float` | obrigatório |
| `altura` | Altura usada pela operação. | `float` | obrigatório |
| `imagem` | Valor correspondente a imagem. | `str \| Path \| QuadroSprite \| None` | `None` |
| `cor` | Valor correspondente a cor. | `Cor` | `BRANCO` |
| `velocidade_x` | Valor correspondente a velocidade x. | `float` | `0.0` |
| `velocidade_y` | Valor correspondente a velocidade y. | `float` | `0.0` |
| `visivel` | Valor correspondente a visivel. | `bool` | `True` |
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | `'sprite'` |
| `dados` | Dados processados pela operação. | `dict[str, Any]` | `field(default_factory=dict)` |
| `animacao` | Valor correspondente a animacao. | `Any` | `None` |
| `escala` | Valor correspondente a escala. | `float` | `1.0` |
| `rotacao` | Valor correspondente a rotacao. | `float` | `0.0` |
| `espelhado_horizontalmente` | Valor correspondente a espelhado horizontalmente. | `bool` | `False` |
| `espelhado_verticalmente` | Valor correspondente a espelhado verticalmente. | `bool` | `False` |
| `origem` | Origem usada pela operação. | `str` | `'topo_esquerdo'` |
| `pivo` | Valor correspondente a pivo. | `tuple[float, float] \| None` | `None` |
| `opacidade` | Valor correspondente a opacidade. | `float` | `1.0` |
| `colisao_acompanha_escala` | Valor correspondente a colisao acompanha escala. | `bool` | `False` |
| `colisao_acompanha_rotacao` | Valor correspondente a colisao acompanha rotacao. | `bool` | `False` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `x` | Coordenada horizontal. | `float` | obrigatório |
| `y` | Coordenada vertical. | `float` | obrigatório |
| `largura` | Largura usada pela operação. | `float` | obrigatório |
| `altura` | Altura usada pela operação. | `float` | obrigatório |
| `imagem` | Valor correspondente a imagem. | `str \| Path \| QuadroSprite \| None` | `None` |
| `cor` | Valor correspondente a cor. | `Cor` | `BRANCO` |
| `velocidade_x` | Valor correspondente a velocidade x. | `float` | `0.0` |
| `velocidade_y` | Valor correspondente a velocidade y. | `float` | `0.0` |
| `visivel` | Valor correspondente a visivel. | `bool` | `True` |
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | `'sprite'` |
| `dados` | Dados processados pela operação. | `dict[str, Any]` | `field(default_factory=dict)` |
| `animacao` | Valor correspondente a animacao. | `Any` | `None` |
| `escala` | Valor correspondente a escala. | `float` | `1.0` |
| `rotacao` | Valor correspondente a rotacao. | `float` | `0.0` |
| `espelhado_horizontalmente` | Valor correspondente a espelhado horizontalmente. | `bool` | `False` |
| `espelhado_verticalmente` | Valor correspondente a espelhado verticalmente. | `bool` | `False` |
| `origem` | Origem usada pela operação. | `str` | `'topo_esquerdo'` |
| `pivo` | Valor correspondente a pivo. | `tuple[float, float] \| None` | `None` |
| `opacidade` | Valor correspondente a opacidade. | `float` | `1.0` |
| `colisao_acompanha_escala` | Valor correspondente a colisao acompanha escala. | `bool` | `False` |
| `colisao_acompanha_rotacao` | Valor correspondente a colisao acompanha rotacao. | `bool` | `False` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `estado_inspecao` | Executa a operação `estado_inspecao` disponibilizada por `coral.jogos`. | `dict[str, Any]` |
| `retangulo` | Obtém retangulo. | `Retangulo` |
| `limites_visuais` | Retângulo conservador da imagem após escala, espelho e rotação. | `Retangulo` |
| `forma_colisao` | Executa a operação `forma_colisao` disponibilizada por `coral.jogos`. | `não declarado` |
| `mover` | Move o valor solicitado. | `None` |
| `definir_escala` | Define escala. | `não declarado` |
| `aumentar` | Aumenta o valor solicitado. | `não declarado` |
| `diminuir` | Diminui o valor solicitado. | `não declarado` |
| `definir_rotacao` | Define rotacao. | `não declarado` |
| `girar` | Gira o valor solicitado. | `não declarado` |
| `definir_opacidade` | Define opacidade. | `não declarado` |
| `alternar_espelhamento` | Alterna espelhamento. | `não declarado` |
| `remover_espelhamento` | Remove espelhamento. | `não declarado` |
| `restaurar_transformacoes` | Restaura transformacoes. | `não declarado` |
| `configurar_colisao` | Configura colisao. | `não declarado` |
| `manter_colisao_fixa` | Executa a operação `manter_colisao_fixa` disponibilizada por `coral.jogos`. | `não declarado` |
| `animar_transformacoes` | Executa a operação `animar_transformacoes` disponibilizada por `coral.jogos`. | `não declarado` |
| `pausar_automacao` | Pausa automacao. | `não declarado` |
| `retomar_automacao` | Retoma automacao. | `não declarado` |
| `reiniciar_automacao` | Reinicia automacao. | `não declarado` |
| `remover_automacao` | Remove automacao. | `não declarado` |
| `animar_com_clipe` | Executa a operação `animar_com_clipe` disponibilizada por `coral.jogos`. | `não declarado` |
| `atualizar` | Atualiza o valor solicitado. | `None` |
| `colide_com` | Executa a operação `colide_com` disponibilizada por `coral.jogos`. | `bool` |

:::details Detalhes técnicos

**Assinatura:** `Sprite(x: float, y: float, largura: float, altura: float, imagem: str \| Path \| QuadroSprite \| None = None, cor: Cor = BRANCO, velocidade_x: float = 0.0, velocidade_y: float = 0.0, visivel: bool = True, nome: str = 'sprite', dados: dict[str, Any] = field(default_factory=dict), animacao: Any = None, escala: float = 1.0, rotacao: float = 0.0, espelhado_horizontalmente: bool = False, espelhado_verticalmente: bool = False, origem: str = 'topo_esquerdo', pivo: tuple[float, float] \| None = None, opacidade: float = 1.0, colisao_acompanha_escala: bool = False, colisao_acompanha_rotacao: bool = False)`

**Origem da implementação:** `coral.jogos.objetos`

**Arquivo na release:** `coral/jogos/objetos.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `estado_inspecao` | método | `estado_inspecao() -> dict[str, Any]` |
| `retangulo` | propriedade | `retangulo() -> Retangulo` |
| `limites_visuais` | propriedade | `limites_visuais() -> Retangulo` |
| `forma_colisao` | propriedade | `forma_colisao()` |
| `mover` | método | `mover(dx: float, dy: float) -> None` |
| `definir_escala` | método | `definir_escala(escala: float)` |
| `aumentar` | método | `aumentar(percentual: float)` |
| `diminuir` | método | `diminuir(percentual: float)` |
| `definir_rotacao` | método | `definir_rotacao(graus: float)` |
| `girar` | método | `girar(graus: float)` |
| `definir_opacidade` | método | `definir_opacidade(opacidade: float)` |
| `alternar_espelhamento` | método | `alternar_espelhamento(eixo: str)` |
| `remover_espelhamento` | método | `remover_espelhamento(eixo: str)` |
| `restaurar_transformacoes` | método | `restaurar_transformacoes()` |
| `configurar_colisao` | método | `configurar_colisao(*, acompanhar_escala: bool \| None = None, acompanhar_rotacao: bool \| None = None)` |
| `manter_colisao_fixa` | método | `manter_colisao_fixa()` |
| `animar_transformacoes` | método | `animar_transformacoes(**canais)` |
| `pausar_automacao` | método | `pausar_automacao(automacao = None)` |
| `retomar_automacao` | método | `retomar_automacao(automacao = None)` |
| `reiniciar_automacao` | método | `reiniciar_automacao(automacao = None)` |
| `remover_automacao` | método | `remover_automacao(automacao, *, restaurar_base: bool = False)` |
| `animar_com_clipe` | método | `animar_com_clipe(clipe: ClipeAnimacao, mapeamento: dict[str, str], *, modo: str = 'absoluto', restaurar_ao_final: bool = False, composicao: str = 'substituir', permitir_conflito: bool = False)` |
| `atualizar` | método | `atualizar(dt: float) -> None` |
| `colide_com` | método | `colide_com(outro: 'Sprite') -> bool` |

:::

#### `Cena`

Representa organização do ciclo visual e de camadas.

**Exemplo**

```coral
de coral.jogos importe Cena, Sprite, TextoApresentacao

defina origem como Cena("origem")
defina fundo como origem.criar_camada("fundo", ordem=-10, paralaxe=0.5)
defina hud como origem.criar_camada("hud", ordem=10, espaco="tela")
```

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | obrigatório |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `estado_inspecao` | Executa a operação `estado_inspecao` disponibilizada por `coral.jogos`. | `dict[str, Any]` |
| `representacoes` | Obtém representacoes. | `tuple[RepresentacaoEntidade, ...]` |
| `camadas` | Obtém camadas. | `tuple[CamadaApresentacao, ...]` |
| `criar_camada` | Cria camada. | `CamadaApresentacao` |
| `camada` | Executa a operação `camada` disponibilizada por `coral.jogos`. | `CamadaApresentacao` |
| `adicionar` | Adiciona o valor solicitado. | `Sprite` |
| `adicionar_em_camada` | Adiciona em camada. | `Any` |
| `remover_de_camada` | Remove de camada. | `bool` |
| `representar` | Cria uma representação de o valor solicitado. | `RepresentacaoEntidade` |
| `remover` | Remove o valor solicitado. | `None` |
| `quando_entrar` | Registra uma ação para quando ocorrer entrar. | `não declarado` |
| `quando_sair` | Registra uma ação para quando ocorrer sair. | `não declarado` |
| `quando_atualizar` | Registra uma ação para quando ocorrer atualizar. | `não declarado` |
| `quando_desenhar` | Registra uma ação para quando ocorrer desenhar. | `não declarado` |
| `entrar` | Executa a operação `entrar` disponibilizada por `coral.jogos`. | `não declarado` |
| `sair` | Executa a operação `sair` disponibilizada por `coral.jogos`. | `não declarado` |
| `atualizar` | Atualiza o valor solicitado. | `não declarado` |
| `desenhar` | Executa a operação `desenhar` disponibilizada por `coral.jogos`. | `não declarado` |

:::details Detalhes técnicos

**Assinatura:** `Cena(nome: str)`

**Origem da implementação:** `coral.jogos.objetos`

**Arquivo na release:** `coral/jogos/objetos.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `estado_inspecao` | método | `estado_inspecao() -> dict[str, Any]` |
| `representacoes` | propriedade | `representacoes() -> tuple[RepresentacaoEntidade, ...]` |
| `camadas` | propriedade | `camadas() -> tuple[CamadaApresentacao, ...]` |
| `criar_camada` | método | `criar_camada(nome: str, *, ordem: int = 0, visivel: bool = True, opacidade: float = 1.0, espaco: str = 'mundo', paralaxe: float \| tuple[float, float] = 1.0) -> CamadaApresentacao` |
| `camada` | método | `camada(nome: str) -> CamadaApresentacao` |
| `adicionar` | método | `adicionar(sprite: Sprite, *, camada: str \| CamadaApresentacao \| None = None) -> Sprite` |
| `adicionar_em_camada` | método | `adicionar_em_camada(elemento: Any, camada: str \| CamadaApresentacao) -> Any` |
| `remover_de_camada` | método | `remover_de_camada(elemento: Any, camada: str \| CamadaApresentacao \| None = None) -> bool` |
| `representar` | método | `representar(entidade: Any, sprite: Any, *, atributo_x: str = 'x', atributo_y: str = 'y') -> RepresentacaoEntidade` |
| `remover` | método | `remover(sprite: Sprite) -> None` |
| `quando_entrar` | método | `quando_entrar(f)` |
| `quando_sair` | método | `quando_sair(f)` |
| `quando_atualizar` | método | `quando_atualizar(f)` |
| `quando_desenhar` | método | `quando_desenhar(f)` |
| `entrar` | método | `entrar(jogo)` |
| `sair` | método | `sair(jogo)` |
| `atualizar` | método | `atualizar(jogo, dt: float)` |
| `desenhar` | método | `desenhar(jogo)` |

:::

#### `CamadaApresentacao`

Camada 2D ordenada que pode pertencer ao mundo ou à tela.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | obrigatório |
| `ordem` | Valor correspondente a ordem. | `int` | `0` |
| `visivel` | Valor correspondente a visivel. | `bool` | `True` |
| `opacidade` | Valor correspondente a opacidade. | `float` | `1.0` |
| `espaco` | Valor correspondente a espaco. | `str` | `'mundo'` |
| `paralaxe_x` | Valor correspondente a paralaxe x. | `float` | `1.0` |
| `paralaxe_y` | Valor correspondente a paralaxe y. | `float` | `1.0` |
| `elementos` | Valor correspondente a elementos. | `list[Any]` | `field(default_factory=list)` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | obrigatório |
| `ordem` | Valor correspondente a ordem. | `int` | `0` |
| `visivel` | Valor correspondente a visivel. | `bool` | `True` |
| `opacidade` | Valor correspondente a opacidade. | `float` | `1.0` |
| `espaco` | Valor correspondente a espaco. | `str` | `'mundo'` |
| `paralaxe_x` | Valor correspondente a paralaxe x. | `float` | `1.0` |
| `paralaxe_y` | Valor correspondente a paralaxe y. | `float` | `1.0` |
| `elementos` | Valor correspondente a elementos. | `list[Any]` | `field(default_factory=list)` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `estado_inspecao` | Executa a operação `estado_inspecao` disponibilizada por `coral.jogos`. | `dict[str, Any]` |
| `presa_a_tela` | Executa a operação `presa_a_tela` disponibilizada por `coral.jogos`. | `bool` |
| `adicionar` | Adiciona o valor solicitado. | `Any` |
| `remover` | Remove o valor solicitado. | `bool` |
| `definir_visibilidade` | Define visibilidade. | `'CamadaApresentacao'` |
| `definir_opacidade` | Define opacidade. | `'CamadaApresentacao'` |
| `definir_paralaxe` | Define paralaxe. | `'CamadaApresentacao'` |

:::details Detalhes técnicos

**Assinatura:** `CamadaApresentacao(nome: str, ordem: int = 0, visivel: bool = True, opacidade: float = 1.0, espaco: str = 'mundo', paralaxe_x: float = 1.0, paralaxe_y: float = 1.0, elementos: list[Any] = field(default_factory=list))`

**Origem da implementação:** `coral.jogos.objetos`

**Arquivo na release:** `coral/jogos/objetos.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `estado_inspecao` | método | `estado_inspecao() -> dict[str, Any]` |
| `presa_a_tela` | propriedade | `presa_a_tela() -> bool` |
| `adicionar` | método | `adicionar(elemento: Any) -> Any` |
| `remover` | método | `remover(elemento: Any) -> bool` |
| `definir_visibilidade` | método | `definir_visibilidade(visivel: bool) -> 'CamadaApresentacao'` |
| `definir_opacidade` | método | `definir_opacidade(opacidade: float) -> 'CamadaApresentacao'` |
| `definir_paralaxe` | método | `definir_paralaxe(x: float = 1.0, y: float \| None = None) -> 'CamadaApresentacao'` |

:::

#### `TextoApresentacao`

Texto 2D reutilizável para camadas de mundo ou de tela.

**Exemplo**

```coral
defina montanhas como Sprite(40, 20, 100, 40)
defina titulo como TextoApresentacao("Apresentação Coral", tamanho=12, ancora_viewport="topo")

execute origem.adicionar_em_camada(montanhas, fundo)
execute origem.adicionar_em_camada(titulo, hud)
```

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `texto` | Texto processado pela operação. | `str` | obrigatório |
| `x` | Coordenada horizontal. | `float` | `0.0` |
| `y` | Coordenada vertical. | `float` | `0.0` |
| `tamanho` | Valor correspondente a tamanho. | `int` | `24` |
| `cor` | Valor correspondente a cor. | `Cor` | `BRANCO` |
| `largura_maxima` | Largura de maxima. | `float \| None` | `None` |
| `alinhamento_horizontal` | Valor correspondente a alinhamento horizontal. | `str` | `'esquerda'` |
| `alinhamento_vertical` | Valor correspondente a alinhamento vertical. | `str` | `'topo'` |
| `espacamento_linhas` | Valor correspondente a espacamento linhas. | `float` | `1.0` |
| `sombra` | Valor correspondente a sombra. | `Cor \| None` | `None` |
| `deslocamento_sombra` | Valor correspondente a deslocamento sombra. | `tuple[float, float]` | `(2.0, 2.0)` |
| `contorno` | Valor correspondente a contorno. | `Cor \| None` | `None` |
| `espessura_contorno` | Valor correspondente a espessura contorno. | `int` | `1` |
| `opacidade` | Valor correspondente a opacidade. | `float` | `1.0` |
| `origem` | Origem usada pela operação. | `str \| None` | `None` |
| `pivo` | Valor correspondente a pivo. | `tuple[float, float] \| None` | `None` |
| `ancora_viewport` | Valor correspondente a ancora viewport. | `str \| None` | `None` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `texto` | Texto processado pela operação. | `str` | obrigatório |
| `x` | Coordenada horizontal. | `float` | `0.0` |
| `y` | Coordenada vertical. | `float` | `0.0` |
| `tamanho` | Valor correspondente a tamanho. | `int` | `24` |
| `cor` | Valor correspondente a cor. | `Cor` | `BRANCO` |
| `largura_maxima` | Largura de maxima. | `float \| None` | `None` |
| `alinhamento_horizontal` | Valor correspondente a alinhamento horizontal. | `str` | `'esquerda'` |
| `alinhamento_vertical` | Valor correspondente a alinhamento vertical. | `str` | `'topo'` |
| `espacamento_linhas` | Valor correspondente a espacamento linhas. | `float` | `1.0` |
| `sombra` | Valor correspondente a sombra. | `Cor \| None` | `None` |
| `deslocamento_sombra` | Valor correspondente a deslocamento sombra. | `tuple[float, float]` | `(2.0, 2.0)` |
| `contorno` | Valor correspondente a contorno. | `Cor \| None` | `None` |
| `espessura_contorno` | Valor correspondente a espessura contorno. | `int` | `1` |
| `opacidade` | Valor correspondente a opacidade. | `float` | `1.0` |
| `origem` | Origem usada pela operação. | `str \| None` | `None` |
| `pivo` | Valor correspondente a pivo. | `tuple[float, float] \| None` | `None` |
| `ancora_viewport` | Valor correspondente a ancora viewport. | `str \| None` | `None` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `linhas` | Executa a operação `linhas` disponibilizada por `coral.jogos`. | `tuple[str, ...]` |
| `medir` | Executa a operação `medir` disponibilizada por `coral.jogos`. | `tuple[float, float]` |
| `desenhar` | Executa a operação `desenhar` disponibilizada por `coral.jogos`. | `None` |

:::details Detalhes técnicos

**Assinatura:** `TextoApresentacao(texto: str, x: float = 0.0, y: float = 0.0, tamanho: int = 24, cor: Cor = BRANCO, largura_maxima: float \| None = None, alinhamento_horizontal: str = 'esquerda', alinhamento_vertical: str = 'topo', espacamento_linhas: float = 1.0, sombra: Cor \| None = None, deslocamento_sombra: tuple[float, float] = (2.0, 2.0), contorno: Cor \| None = None, espessura_contorno: int = 1, opacidade: float = 1.0, origem: str \| None = None, pivo: tuple[float, float] \| None = None, ancora_viewport: str \| None = None)`

**Origem da implementação:** `coral.jogos.objetos`

**Arquivo na release:** `coral/jogos/objetos.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `linhas` | método | `linhas(jogo) -> tuple[str, ...]` |
| `medir` | método | `medir(jogo) -> tuple[float, float]` |
| `desenhar` | método | `desenhar(jogo, cena: 'Cena', camada: CamadaApresentacao) -> None` |

:::

#### `RepresentacaoEntidade`

Liga uma entidade de mundo a um Sprite sem acoplar coral.mundo a jogos.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `entidade` | Valor correspondente a entidade. | `Any` | obrigatório |
| `sprite` | Valor correspondente a sprite. | `Sprite` | obrigatório |
| `atributo_x` | Nome do atributo usado como x. | `str` | `'x'` |
| `atributo_y` | Nome do atributo usado como y. | `str` | `'y'` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `entidade` | Valor correspondente a entidade. | `Any` | obrigatório |
| `sprite` | Valor correspondente a sprite. | `Sprite` | obrigatório |
| `atributo_x` | Nome do atributo usado como x. | `str` | `'x'` |
| `atributo_y` | Nome do atributo usado como y. | `str` | `'y'` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `x` | Executa a operação `x` disponibilizada por `coral.jogos`. | `float` |
| `y` | Executa a operação `y` disponibilizada por `coral.jogos`. | `float` |
| `largura` | Executa a operação `largura` disponibilizada por `coral.jogos`. | `float` |
| `altura` | Executa a operação `altura` disponibilizada por `coral.jogos`. | `float` |
| `velocidade_x` | Executa a operação `velocidade_x` disponibilizada por `coral.jogos`. | `float` |
| `velocidade_y` | Executa a operação `velocidade_y` disponibilizada por `coral.jogos`. | `float` |
| `sincronizar` | Sincroniza o valor solicitado. | `Sprite` |

:::details Detalhes técnicos

**Assinatura:** `RepresentacaoEntidade(entidade: Any, sprite: Sprite, atributo_x: str = 'x', atributo_y: str = 'y')`

**Origem da implementação:** `coral.jogos.objetos`

**Arquivo na release:** `coral/jogos/objetos.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `x` | propriedade | `x() -> float` |
| `y` | propriedade | `y() -> float` |
| `largura` | propriedade | `largura() -> float` |
| `altura` | propriedade | `altura() -> float` |
| `velocidade_x` | propriedade | `velocidade_x() -> float` |
| `velocidade_y` | propriedade | `velocidade_y() -> float` |
| `sincronizar` | método | `sincronizar() -> Sprite` |

:::

#### `Animacao`

Representa Animacao na API de `coral.jogos`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `quadros` | Valor correspondente a quadros. | `tuple[str \| Path \| QuadroSprite, ...]` | obrigatório |
| `fps` | Quantidade alvo de quadros por segundo. | `float` | `10.0` |
| `repetir` | Valor correspondente a repetir. | `bool` | `True` |
| `finalizada` | Valor correspondente a finalizada. | `bool` | `False` |
| `duracoes` | Valor correspondente a duracoes. | `tuple[float, ...] \| None` | `None` |
| `velocidade` | Valor correspondente a velocidade. | `float` | `1.0` |
| `modo` | Valor correspondente a modo. | `str` | `'normal'` |
| `indice_inicial` | Valor correspondente a indice inicial. | `int \| None` | `None` |
| `marcadores` | Valor correspondente a marcadores. | `dict[str, int]` | `field(default_factory=dict)` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `quadros` | Valor correspondente a quadros. | `tuple[str \| Path \| QuadroSprite, ...]` | obrigatório |
| `fps` | Quantidade alvo de quadros por segundo. | `float` | `10.0` |
| `repetir` | Valor correspondente a repetir. | `bool` | `True` |
| `finalizada` | Valor correspondente a finalizada. | `bool` | `False` |
| `duracoes` | Valor correspondente a duracoes. | `tuple[float, ...] \| None` | `None` |
| `velocidade` | Valor correspondente a velocidade. | `float` | `1.0` |
| `modo` | Valor correspondente a modo. | `str` | `'normal'` |
| `indice_inicial` | Valor correspondente a indice inicial. | `int \| None` | `None` |
| `marcadores` | Valor correspondente a marcadores. | `dict[str, int]` | `field(default_factory=dict)` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `estado_inspecao` | Executa a operação `estado_inspecao` disponibilizada por `coral.jogos`. | `dict[str, Any]` |
| `quadro_atual` | Obtém quadro atual. | `não declarado` |
| `indice_atual` | Executa a operação `indice_atual` disponibilizada por `coral.jogos`. | `int` |
| `ciclos` | Executa a operação `ciclos` disponibilizada por `coral.jogos`. | `int` |
| `duracao` | Executa a operação `duracao` disponibilizada por `coral.jogos`. | `float` |
| `tempo_atual` | Executa a operação `tempo_atual` disponibilizada por `coral.jogos`. | `float` |
| `marcar` | Executa a operação `marcar` disponibilizada por `coral.jogos`. | `'Animacao'` |
| `ao_marcador` | Executa a operação `ao_marcador` disponibilizada por `coral.jogos`. | `Callable` |
| `ao_completar_ciclo` | Executa a operação `ao_completar_ciclo` disponibilizada por `coral.jogos`. | `Callable` |
| `ao_finalizar` | Executa a operação `ao_finalizar` disponibilizada por `coral.jogos`. | `Callable` |
| `reiniciar` | Reinicia o valor solicitado. | `não declarado` |
| `buscar_quadro` | Procura quadro e devolve o resultado quando encontrado. | `'Animacao'` |
| `buscar_tempo` | Procura tempo e devolve o resultado quando encontrado. | `'Animacao'` |
| `duplicar` | Executa a operação `duplicar` disponibilizada por `coral.jogos`. | `'Animacao'` |
| `atualizar` | Atualiza o valor solicitado. | `não declarado` |

:::details Detalhes técnicos

**Assinatura:** `Animacao(quadros: tuple[str \| Path \| QuadroSprite, ...], fps: float = 10.0, repetir: bool = True, finalizada: bool = False, duracoes: tuple[float, ...] \| None = None, velocidade: float = 1.0, modo: str = 'normal', indice_inicial: int \| None = None, marcadores: dict[str, int] = field(default_factory=dict))`

**Origem da implementação:** `coral.jogos.objetos`

**Arquivo na release:** `coral/jogos/objetos.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `estado_inspecao` | método | `estado_inspecao() -> dict[str, Any]` |
| `quadro_atual` | propriedade | `quadro_atual()` |
| `indice_atual` | propriedade | `indice_atual() -> int` |
| `ciclos` | propriedade | `ciclos() -> int` |
| `duracao` | propriedade | `duracao() -> float` |
| `tempo_atual` | propriedade | `tempo_atual() -> float` |
| `marcar` | método | `marcar(nome: str, quadro: int) -> 'Animacao'` |
| `ao_marcador` | método | `ao_marcador(nome: str, callback: Callable) -> Callable` |
| `ao_completar_ciclo` | método | `ao_completar_ciclo(callback: Callable) -> Callable` |
| `ao_finalizar` | método | `ao_finalizar(callback: Callable) -> Callable` |
| `reiniciar` | método | `reiniciar()` |
| `buscar_quadro` | método | `buscar_quadro(indice: int) -> 'Animacao'` |
| `buscar_tempo` | método | `buscar_tempo(segundos: float) -> 'Animacao'` |
| `duplicar` | método | `duplicar() -> 'Animacao'` |
| `atualizar` | método | `atualizar(dt: float)` |

:::

#### `AnimacoesDirecionais`

Conjunto nomeado de animações para direções de movimento.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `animacoes` | Valor correspondente a animacoes. | `dict[str, Animacao]` | obrigatório |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `animacoes` | Valor correspondente a animacoes. | `dict[str, Animacao]` | obrigatório |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `direcoes` | Obtém direcoes. | `tuple[str, ...]` |
| `para` | Executa a operação `para` disponibilizada por `coral.jogos`. | `Animacao` |
| `usar` | Seleciona o valor solicitado. | `Animacao` |
| `ligar` | Liga o valor solicitado. | `VinculoAnimacaoMovimento` |

:::details Detalhes técnicos

**Assinatura:** `AnimacoesDirecionais(animacoes: dict[str, Animacao])`

**Origem da implementação:** `coral.jogos.objetos`

**Arquivo na release:** `coral/jogos/objetos.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `direcoes` | propriedade | `direcoes() -> tuple[str, ...]` |
| `para` | método | `para(direcao: str) -> Animacao` |
| `usar` | método | `usar(sprite: Sprite, direcao: str, *, reiniciar: bool = True) -> Animacao` |
| `ligar` | método | `ligar(movimento: MovimentoDirecional, sprite: Sprite) -> VinculoAnimacaoMovimento` |

:::

#### `VinculoAnimacaoMovimento`

Representa VinculoAnimacaoMovimento na API de `coral.jogos`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `grupo` | Valor correspondente a grupo. | `'AnimacoesDirecionais'` | obrigatório |
| `movimento` | Valor correspondente a movimento. | `MovimentoDirecional` | obrigatório |
| `sprite` | Valor correspondente a sprite. | `Sprite` | obrigatório |
| `direcoes_compativeis` | Valor correspondente a direcoes compativeis. | `tuple[str, ...]` | obrigatório |
| `direcao_visual` | Valor correspondente a direcao visual. | `str \| None` | `None` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `grupo` | Valor correspondente a grupo. | `'AnimacoesDirecionais'` | obrigatório |
| `movimento` | Valor correspondente a movimento. | `MovimentoDirecional` | obrigatório |
| `sprite` | Valor correspondente a sprite. | `Sprite` | obrigatório |
| `direcoes_compativeis` | Valor correspondente a direcoes compativeis. | `tuple[str, ...]` | obrigatório |
| `direcao_visual` | Valor correspondente a direcao visual. | `str \| None` | `None` |

:::details Detalhes técnicos

**Assinatura:** `VinculoAnimacaoMovimento(grupo: 'AnimacoesDirecionais', movimento: MovimentoDirecional, sprite: Sprite, direcoes_compativeis: tuple[str, ...], direcao_visual: str \| None = None)`

**Origem da implementação:** `coral.jogos.objetos`

**Arquivo na release:** `coral/jogos/objetos.py`

:::

#### `EstadosAnimacao`

Agrupa estados visuais sem assumir autoridade sobre estado lógico.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `estados` | Valor correspondente a estados. | `dict[str, Animacao \| AnimacoesDirecionais]` | obrigatório |
| `estado_inicial` | Valor correspondente a estado inicial. | `str \| None` | `None` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `estados` | Obtém estados. | `tuple[str, ...]` |
| `para` | Executa a operação `para` disponibilizada por `coral.jogos`. | `Animacao \| AnimacoesDirecionais` |
| `ao_entrar` | Executa a operação `ao_entrar` disponibilizada por `coral.jogos`. | `Callable` |
| `ao_sair` | Executa a operação `ao_sair` disponibilizada por `coral.jogos`. | `Callable` |
| `ligar` | Liga o valor solicitado. | `VinculoEstadosAnimacaoMovimento` |
| `usar` | Seleciona o valor solicitado. | `Animacao` |

:::details Detalhes técnicos

**Assinatura:** `EstadosAnimacao(estados: dict[str, Animacao \| AnimacoesDirecionais], *, estado_inicial: str \| None = None)`

**Origem da implementação:** `coral.jogos.objetos`

**Arquivo na release:** `coral/jogos/objetos.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `estados` | posicional |
| `estado_inicial` | nomeado |

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `estados` | propriedade | `estados() -> tuple[str, ...]` |
| `para` | método | `para(estado: str) -> Animacao \| AnimacoesDirecionais` |
| `ao_entrar` | método | `ao_entrar(estado: str, callback: Callable) -> Callable` |
| `ao_sair` | método | `ao_sair(estado: str, callback: Callable) -> Callable` |
| `ligar` | método | `ligar(movimento: MovimentoDirecional, sprite: Sprite, *, estado_inicial: str \| None = None, direcao_inicial: str \| None = None) -> VinculoEstadosAnimacaoMovimento` |
| `usar` | método | `usar(sprite: Sprite, estado: str, *, direcao: str \| None = None, reiniciar: bool = True) -> Animacao` |

:::

#### `VinculoEstadosAnimacaoMovimento`

Mantém estado visual e direção como dimensões independentes.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `grupo` | Valor correspondente a grupo. | `'EstadosAnimacao'` | obrigatório |
| `movimento` | Valor correspondente a movimento. | `MovimentoDirecional` | obrigatório |
| `sprite` | Valor correspondente a sprite. | `Sprite` | obrigatório |
| `estado_atual` | Valor correspondente a estado atual. | `str \| None` | `None` |
| `estado_anterior` | Valor correspondente a estado anterior. | `str \| None` | `None` |
| `direcao_visual` | Valor correspondente a direcao visual. | `str \| None` | `None` |
| `ultima_direcao_visual` | Valor correspondente a ultima direcao visual. | `str \| None` | `None` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `grupo` | Valor correspondente a grupo. | `'EstadosAnimacao'` | obrigatório |
| `movimento` | Valor correspondente a movimento. | `MovimentoDirecional` | obrigatório |
| `sprite` | Valor correspondente a sprite. | `Sprite` | obrigatório |
| `estado_atual` | Valor correspondente a estado atual. | `str \| None` | `None` |
| `estado_anterior` | Valor correspondente a estado anterior. | `str \| None` | `None` |
| `direcao_visual` | Valor correspondente a direcao visual. | `str \| None` | `None` |
| `ultima_direcao_visual` | Valor correspondente a ultima direcao visual. | `str \| None` | `None` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `usar` | Seleciona o valor solicitado. | `Animacao` |

:::details Detalhes técnicos

**Assinatura:** `VinculoEstadosAnimacaoMovimento(grupo: 'EstadosAnimacao', movimento: MovimentoDirecional, sprite: Sprite, estado_atual: str \| None = None, estado_anterior: str \| None = None, direcao_visual: str \| None = None, ultima_direcao_visual: str \| None = None)`

**Origem da implementação:** `coral.jogos.objetos`

**Arquivo na release:** `coral/jogos/objetos.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `usar` | método | `usar(estado: str, *, direcao: str \| None = None, reiniciar: bool = True) -> Animacao` |

:::

#### `TransicaoEstadoAnimacao`

Política declarativa para uma transição visual.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `estado` | Estado usado ou atualizado pela operação. | `str` | obrigatório |
| `prioridade` | Valor correspondente a prioridade. | `int` | `0` |
| `tempo_minimo` | Valor correspondente a tempo minimo. | `float` | `0.0` |
| `bloquear_interrupcao` | Valor correspondente a bloquear interrupcao. | `float` | `0.0` |
| `retorno_automatico` | Valor correspondente a retorno automatico. | `str \| None` | `None` |
| `reiniciar` | Valor correspondente a reiniciar. | `bool` | `True` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `estado` | Estado usado ou atualizado pela operação. | `str` | obrigatório |
| `prioridade` | Valor correspondente a prioridade. | `int` | `0` |
| `tempo_minimo` | Valor correspondente a tempo minimo. | `float` | `0.0` |
| `bloquear_interrupcao` | Valor correspondente a bloquear interrupcao. | `float` | `0.0` |
| `retorno_automatico` | Valor correspondente a retorno automatico. | `str \| None` | `None` |
| `reiniciar` | Valor correspondente a reiniciar. | `bool` | `True` |

:::details Detalhes técnicos

**Assinatura:** `TransicaoEstadoAnimacao(estado: str, prioridade: int = 0, tempo_minimo: float = 0.0, bloquear_interrupcao: float = 0.0, retorno_automatico: str \| None = None, reiniciar: bool = True)`

**Origem da implementação:** `coral.jogos.objetos`

**Arquivo na release:** `coral/jogos/objetos.py`

:::

#### `CondicaoTransicaoAnimacao`

Representa CondicaoTransicaoAnimacao na API de `coral.jogos`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `condicao` | Valor correspondente a condicao. | `Callable[[Sprite], bool]` | obrigatório |
| `transicao` | Valor correspondente a transicao. | `TransicaoEstadoAnimacao` | obrigatório |
| `ordem` | Valor correspondente a ordem. | `int` | `0` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `condicao` | Valor correspondente a condicao. | `Callable[[Sprite], bool]` | obrigatório |
| `transicao` | Valor correspondente a transicao. | `TransicaoEstadoAnimacao` | obrigatório |
| `ordem` | Valor correspondente a ordem. | `int` | `0` |

:::details Detalhes técnicos

**Assinatura:** `CondicaoTransicaoAnimacao(condicao: Callable[[Sprite], bool], transicao: TransicaoEstadoAnimacao, ordem: int = 0)`

**Origem da implementação:** `coral.jogos.objetos`

**Arquivo na release:** `coral/jogos/objetos.py`

:::

#### `TransicoesEstadosAnimacao`

Transições visuais por evento, condição ou chamada manual.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `estados` | Valor correspondente a estados. | `EstadosAnimacao` | obrigatório |
| `transicoes` | Valor correspondente a transicoes. | `dict[str, str \| TransicaoEstadoAnimacao \| dict[str, Any]]` | obrigatório |
| `reiniciar_ao_retornar` | Valor correspondente a reiniciar ao retornar. | `bool` | `True` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `eventos` | Obtém eventos. | `tuple[str, ...]` |
| `para` | Executa a operação `para` disponibilizada por `coral.jogos`. | `str` |
| `para_transicao` | Converte o valor para transicao. | `TransicaoEstadoAnimacao` |
| `quando` | Executa a operação `quando` disponibilizada por `coral.jogos`. | `CondicaoTransicaoAnimacao` |
| `ligar` | Liga o valor solicitado. | `VinculoTransicoesEstadosMovimento` |
| `ligar_eventos` | Liga eventos. | `VinculoTransicoesEventos` |
| `acionar` | Aciona o valor solicitado. | `Animacao \| None` |
| `transicionar` | Executa a operação `transicionar` disponibilizada por `coral.jogos`. | `Animacao \| None` |

:::details Detalhes técnicos

**Assinatura:** `TransicoesEstadosAnimacao(estados: EstadosAnimacao, transicoes: dict[str, str \| TransicaoEstadoAnimacao \| dict[str, Any]], *, reiniciar_ao_retornar: bool = True)`

**Origem da implementação:** `coral.jogos.objetos`

**Arquivo na release:** `coral/jogos/objetos.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `estados` | posicional |
| `transicoes` | posicional |
| `reiniciar_ao_retornar` | nomeado |

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `eventos` | propriedade | `eventos() -> tuple[str, ...]` |
| `para` | método | `para(evento: str) -> str` |
| `para_transicao` | método | `para_transicao(evento: str) -> TransicaoEstadoAnimacao` |
| `quando` | método | `quando(condicao: Callable[[Sprite], bool], estado: str, *, prioridade: int = 0, tempo_minimo: float = 0.0, bloquear_interrupcao: float = 0.0, retorno_automatico: str \| None = None, reiniciar: bool = True) -> CondicaoTransicaoAnimacao` |
| `ligar` | método | `ligar(movimento: MovimentoDirecional, sprite: Sprite) -> VinculoTransicoesEstadosMovimento` |
| `ligar_eventos` | método | `ligar_eventos(eventos: Any, sprite: Sprite) -> VinculoTransicoesEventos` |
| `acionar` | método | `acionar(sprite: Sprite, evento: str) -> Animacao \| None` |
| `transicionar` | método | `transicionar(sprite: Sprite, estado: str, **kwargs) -> Animacao \| None` |

:::

#### `VinculoTransicoesEstadosMovimento`

Executa a máquina visual opt in de um Sprite.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `grupo` | Valor correspondente a grupo. | `'TransicoesEstadosAnimacao'` | obrigatório |
| `movimento` | Valor correspondente a movimento. | `MovimentoDirecional` | obrigatório |
| `sprite` | Valor correspondente a sprite. | `Sprite` | obrigatório |
| `vinculo_estados` | Valor correspondente a vinculo estados. | `VinculoEstadosAnimacaoMovimento` | obrigatório |
| `ultimo_evento` | Valor correspondente a ultimo evento. | `str \| None` | `None` |
| `tempo_no_estado` | Valor correspondente a tempo no estado. | `float` | `0.0` |
| `bloqueio_restante` | Valor correspondente a bloqueio restante. | `float` | `0.0` |
| `prioridade_atual` | Valor correspondente a prioridade atual. | `int` | `0` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `grupo` | Valor correspondente a grupo. | `'TransicoesEstadosAnimacao'` | obrigatório |
| `movimento` | Valor correspondente a movimento. | `MovimentoDirecional` | obrigatório |
| `sprite` | Valor correspondente a sprite. | `Sprite` | obrigatório |
| `vinculo_estados` | Valor correspondente a vinculo estados. | `VinculoEstadosAnimacaoMovimento` | obrigatório |
| `ultimo_evento` | Valor correspondente a ultimo evento. | `str \| None` | `None` |
| `tempo_no_estado` | Valor correspondente a tempo no estado. | `float` | `0.0` |
| `bloqueio_restante` | Valor correspondente a bloqueio restante. | `float` | `0.0` |
| `prioridade_atual` | Valor correspondente a prioridade atual. | `int` | `0` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `estado_atual` | Executa a operação `estado_atual` disponibilizada por `coral.jogos`. | `str \| None` |
| `estado_anterior` | Executa a operação `estado_anterior` disponibilizada por `coral.jogos`. | `str \| None` |
| `pode_ser_interrompido` | Executa a operação `pode_ser_interrompido` disponibilizada por `coral.jogos`. | `bool` |
| `transicionar` | Executa a operação `transicionar` disponibilizada por `coral.jogos`. | `Animacao \| None` |
| `acionar` | Aciona o valor solicitado. | `Animacao \| None` |
| `atualizar` | Atualiza o valor solicitado. | `None` |

:::details Detalhes técnicos

**Assinatura:** `VinculoTransicoesEstadosMovimento(grupo: 'TransicoesEstadosAnimacao', movimento: MovimentoDirecional, sprite: Sprite, vinculo_estados: VinculoEstadosAnimacaoMovimento, ultimo_evento: str \| None = None, tempo_no_estado: float = 0.0, bloqueio_restante: float = 0.0, prioridade_atual: int = 0)`

**Origem da implementação:** `coral.jogos.objetos`

**Arquivo na release:** `coral/jogos/objetos.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `estado_atual` | propriedade | `estado_atual() -> str \| None` |
| `estado_anterior` | propriedade | `estado_anterior() -> str \| None` |
| `pode_ser_interrompido` | propriedade | `pode_ser_interrompido() -> bool` |
| `transicionar` | método | `transicionar(estado: str, *, prioridade: int = 0, tempo_minimo: float = 0.0, bloquear_interrupcao: float = 0.0, retorno_automatico: str \| None = None, reiniciar: bool = True) -> Animacao \| None` |
| `acionar` | método | `acionar(evento: str) -> Animacao \| None` |
| `atualizar` | método | `atualizar(dt: float) -> None` |

:::

#### `VinculoTransicoesEventos`

Escuta um barramento genérico e encaminha eventos declarados para transições visuais.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `grupo` | Valor correspondente a grupo. | `'TransicoesEstadosAnimacao'` | obrigatório |
| `eventos` | Fonte ou conjunto de eventos associado à operação. | `Any` | obrigatório |
| `sprite` | Valor correspondente a sprite. | `Sprite` | obrigatório |
| `vinculo_movimento` | Valor correspondente a vinculo movimento. | `VinculoTransicoesEstadosMovimento` | obrigatório |
| `ativo` | Valor correspondente a ativo. | `bool` | `field(default=True, init=False)` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `grupo` | Valor correspondente a grupo. | `'TransicoesEstadosAnimacao'` | obrigatório |
| `eventos` | Fonte ou conjunto de eventos associado à operação. | `Any` | obrigatório |
| `sprite` | Valor correspondente a sprite. | `Sprite` | obrigatório |
| `vinculo_movimento` | Valor correspondente a vinculo movimento. | `VinculoTransicoesEstadosMovimento` | obrigatório |
| `ativo` | Valor correspondente a ativo. | `bool` | `field(default=True, init=False)` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `desligar` | Desliga o valor solicitado. | `None` |

:::details Detalhes técnicos

**Assinatura:** `VinculoTransicoesEventos(grupo: 'TransicoesEstadosAnimacao', eventos: Any, sprite: Sprite, vinculo_movimento: VinculoTransicoesEstadosMovimento, ativo: bool = field(default=True, init=False))`

**Origem da implementação:** `coral.jogos.objetos`

**Arquivo na release:** `coral/jogos/objetos.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `desligar` | método | `desligar() -> None` |

:::

#### `EfeitoCamera`

Efeito visual temporal que não altera o estado lógico da câmera.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `tipo` | Tipo solicitado para o resultado, quando o módulo oferece essa escolha. | `str` | obrigatório |
| `duracao` | Valor correspondente a duracao. | `float` | obrigatório |
| `intensidade` | Valor correspondente a intensidade. | `float` | `1.0` |
| `x` | Coordenada horizontal. | `float` | `0.0` |
| `y` | Coordenada vertical. | `float` | `0.0` |
| `zoom` | Valor correspondente a zoom. | `float` | `0.0` |
| `rotacao` | Valor correspondente a rotacao. | `float` | `0.0` |
| `semente` | Semente usada para tornar a sequência reproduzível. | `int` | `0` |
| `frequencia` | Valor correspondente a frequencia. | `float` | `24.0` |
| `curva` | Valor correspondente a curva. | `str \| Callable[[float], float]` | `'linear'` |
| `tempo` | Valor correspondente a tempo. | `float` | `0.0` |
| `estado` | Estado usado ou atualizado pela operação. | `str` | `'ativo'` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `tipo` | Tipo solicitado para o resultado, quando o módulo oferece essa escolha. | `str` | obrigatório |
| `duracao` | Valor correspondente a duracao. | `float` | obrigatório |
| `intensidade` | Valor correspondente a intensidade. | `float` | `1.0` |
| `x` | Coordenada horizontal. | `float` | `0.0` |
| `y` | Coordenada vertical. | `float` | `0.0` |
| `zoom` | Valor correspondente a zoom. | `float` | `0.0` |
| `rotacao` | Valor correspondente a rotacao. | `float` | `0.0` |
| `semente` | Semente usada para tornar a sequência reproduzível. | `int` | `0` |
| `frequencia` | Valor correspondente a frequencia. | `float` | `24.0` |
| `curva` | Valor correspondente a curva. | `str \| Callable[[float], float]` | `'linear'` |
| `tempo` | Valor correspondente a tempo. | `float` | `0.0` |
| `estado` | Estado usado ou atualizado pela operação. | `str` | `'ativo'` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `progresso` | Executa a operação `progresso` disponibilizada por `coral.jogos`. | `float` |
| `ativo` | Indica o estado de ativo. | `bool` |
| `amostra` | Seleciona uma amostra de valores da coleção fornecida. | `tuple[float, float, float, float]` |
| `avancar` | Avança o valor solicitado. | `None` |
| `pausar` | Pausa o valor solicitado. | `'EfeitoCamera'` |
| `retomar` | Retoma o valor solicitado. | `'EfeitoCamera'` |
| `cancelar` | Cancela o valor solicitado. | `'EfeitoCamera'` |

:::details Detalhes técnicos

**Assinatura:** `EfeitoCamera(tipo: str, duracao: float, intensidade: float = 1.0, x: float = 0.0, y: float = 0.0, zoom: float = 0.0, rotacao: float = 0.0, semente: int = 0, frequencia: float = 24.0, curva: str \| Callable[[float], float] = 'linear', tempo: float = 0.0, estado: str = 'ativo')`

**Origem da implementação:** `coral.jogos.objetos`

**Arquivo na release:** `coral/jogos/objetos.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `progresso` | propriedade | `progresso() -> float` |
| `ativo` | propriedade | `ativo() -> bool` |
| `amostra` | método | `amostra() -> tuple[float, float, float, float]` |
| `avancar` | método | `avancar(dt: float) -> None` |
| `pausar` | método | `pausar() -> 'EfeitoCamera'` |
| `retomar` | método | `retomar() -> 'EfeitoCamera'` |
| `cancelar` | método | `cancelar() -> 'EfeitoCamera'` |

:::

#### `Camera`

Câmera 2D headless com transformação inversível de mundo e tela.

**Exemplo**

```coral
de coral.jogos importe Camera, Sprite, Retangulo

defina camera como Camera(0, 0, 320, 180)
defina heroi como Sprite(100, 80, 16, 16, velocidade_x=40)
defina aliado como Sprite(260, 120, 16, 16)
```

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `x` | Coordenada horizontal. | `float` | `0.0` |
| `y` | Coordenada vertical. | `float` | `0.0` |
| `largura` | Largura usada pela operação. | `float` | `800.0` |
| `altura` | Altura usada pela operação. | `float` | `450.0` |
| `alvo` | Valor correspondente a alvo. | `Any \| None` | `None` |
| `suavidade` | Valor correspondente a suavidade. | `float` | `1.0` |
| `zoom` | Valor correspondente a zoom. | `float` | `1.0` |
| `rotacao` | Valor correspondente a rotacao. | `float` | `0.0` |
| `zoom_minimo` | Valor correspondente a zoom minimo. | `float \| None` | `None` |
| `zoom_maximo` | Valor correspondente a zoom maximo. | `float \| None` | `None` |
| `deslocamento_visual_x` | Valor correspondente a deslocamento visual x. | `float` | `0.0` |
| `deslocamento_visual_y` | Valor correspondente a deslocamento visual y. | `float` | `0.0` |
| `constante_tempo` | Valor correspondente a constante tempo. | `float \| None` | `None` |
| `zona_morta` | Valor correspondente a zona morta. | `tuple[float, float] \| None` | `None` |
| `enquadramento_x` | Valor correspondente a enquadramento x. | `float` | `0.0` |
| `enquadramento_y` | Valor correspondente a enquadramento y. | `float` | `0.0` |
| `antecipacao` | Valor correspondente a antecipacao. | `float` | `0.0` |
| `limites` | Valor correspondente a limites. | `Retangulo \| None` | `None` |
| `travar_x` | Valor correspondente a travar x. | `bool` | `False` |
| `travar_y` | Valor correspondente a travar y. | `bool` | `False` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `x` | Coordenada horizontal. | `float` | `0.0` |
| `y` | Coordenada vertical. | `float` | `0.0` |
| `largura` | Largura usada pela operação. | `float` | `800.0` |
| `altura` | Altura usada pela operação. | `float` | `450.0` |
| `alvo` | Valor correspondente a alvo. | `Any \| None` | `None` |
| `suavidade` | Valor correspondente a suavidade. | `float` | `1.0` |
| `zoom` | Valor correspondente a zoom. | `float` | `1.0` |
| `rotacao` | Valor correspondente a rotacao. | `float` | `0.0` |
| `zoom_minimo` | Valor correspondente a zoom minimo. | `float \| None` | `None` |
| `zoom_maximo` | Valor correspondente a zoom maximo. | `float \| None` | `None` |
| `deslocamento_visual_x` | Valor correspondente a deslocamento visual x. | `float` | `0.0` |
| `deslocamento_visual_y` | Valor correspondente a deslocamento visual y. | `float` | `0.0` |
| `constante_tempo` | Valor correspondente a constante tempo. | `float \| None` | `None` |
| `zona_morta` | Valor correspondente a zona morta. | `tuple[float, float] \| None` | `None` |
| `enquadramento_x` | Valor correspondente a enquadramento x. | `float` | `0.0` |
| `enquadramento_y` | Valor correspondente a enquadramento y. | `float` | `0.0` |
| `antecipacao` | Valor correspondente a antecipacao. | `float` | `0.0` |
| `limites` | Valor correspondente a limites. | `Retangulo \| None` | `None` |
| `travar_x` | Valor correspondente a travar x. | `bool` | `False` |
| `travar_y` | Valor correspondente a travar y. | `bool` | `False` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `estado_inspecao` | Executa a operação `estado_inspecao` disponibilizada por `coral.jogos`. | `dict[str, Any]` |
| `centro` | Executa a operação `centro` disponibilizada por `coral.jogos`. | `tuple[float, float]` |
| `definir_centro` | Define centro. | `'Camera'` |
| `definir_limites_zoom` | Define limites zoom. | `'Camera'` |
| `definir_zoom` | Define zoom. | `'Camera'` |
| `definir_rotacao` | Define rotacao. | `'Camera'` |
| `girar` | Gira o valor solicitado. | `'Camera'` |
| `definir_deslocamento_visual` | Define deslocamento visual. | `'Camera'` |
| `limpar_deslocamento_visual` | Limpa deslocamento visual. | `'Camera'` |
| `animar_com_clipe` | Executa a operação `animar_com_clipe` disponibilizada por `coral.jogos`. | `não declarado` |
| `efeitos` | Executa a operação `efeitos` disponibilizada por `coral.jogos`. | `tuple[EfeitoCamera, ...]` |
| `adicionar_efeito` | Adiciona efeito. | `EfeitoCamera` |
| `tremer` | Executa a operação `tremer` disponibilizada por `coral.jogos`. | `EfeitoCamera` |
| `impulsionar_deslocamento` | Executa a operação `impulsionar_deslocamento` disponibilizada por `coral.jogos`. | `EfeitoCamera` |
| `impulsionar_zoom` | Executa a operação `impulsionar_zoom` disponibilizada por `coral.jogos`. | `EfeitoCamera` |
| `impulsionar_rotacao` | Executa a operação `impulsionar_rotacao` disponibilizada por `coral.jogos`. | `EfeitoCamera` |
| `aproximar_temporariamente` | Executa a operação `aproximar_temporariamente` disponibilizada por `coral.jogos`. | `EfeitoCamera` |
| `pausar_efeitos` | Pausa efeitos. | `None` |
| `retomar_efeitos` | Retoma efeitos. | `None` |
| `cancelar_efeitos` | Cancela efeitos. | `None` |
| `definir_constante_tempo` | Define constante tempo. | `'Camera'` |
| `definir_zona_morta` | Define zona morta. | `'Camera'` |
| `definir_enquadramento` | Define enquadramento. | `'Camera'` |
| `definir_antecipacao` | Define antecipacao. | `'Camera'` |
| `definir_limites` | Define limites. | `'Camera'` |
| `travar_eixos` | Executa a operação `travar_eixos` disponibilizada por `coral.jogos`. | `'Camera'` |
| `seguir` | Passa a seguir o valor solicitado. | `não declarado` |
| `seguir_representacao` | Passa a seguir representacao. | `'Camera'` |
| `centralizar_no_alvo` | Executa a operação `centralizar_no_alvo` disponibilizada por `coral.jogos`. | `'Camera'` |
| `enquadrar_alvos` | Executa a operação `enquadrar_alvos` disponibilizada por `coral.jogos`. | `'Camera'` |
| `atualizar` | Atualiza o valor solicitado. | `não declarado` |
| `mundo_para_tela` | Converte coordenadas de mundo para tela. | `tuple[float, float]` |
| `mundo_para_tela_paralaxe` | Projeta um ponto usando uma fração do deslocamento da câmera. | `tuple[float, float]` |
| `tela_para_mundo` | Converte coordenadas de tela para mundo. | `tuple[float, float]` |
| `area_visivel` | Executa a operação `area_visivel` disponibilizada por `coral.jogos`. | `Retangulo` |
| `visivel` | Executa a operação `visivel` disponibilizada por `coral.jogos`. | `bool` |
| `tela` | Compatibilidade histórica: converte coordenadas de mundo para tela. | `tuple[float, float]` |

:::details Detalhes técnicos

**Assinatura:** `Camera(x: float = 0.0, y: float = 0.0, largura: float = 800.0, altura: float = 450.0, alvo: Any \| None = None, suavidade: float = 1.0, zoom: float = 1.0, rotacao: float = 0.0, zoom_minimo: float \| None = None, zoom_maximo: float \| None = None, deslocamento_visual_x: float = 0.0, deslocamento_visual_y: float = 0.0, constante_tempo: float \| None = None, zona_morta: tuple[float, float] \| None = None, enquadramento_x: float = 0.0, enquadramento_y: float = 0.0, antecipacao: float = 0.0, limites: Retangulo \| None = None, travar_x: bool = False, travar_y: bool = False)`

**Origem da implementação:** `coral.jogos.objetos`

**Arquivo na release:** `coral/jogos/objetos.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `estado_inspecao` | método | `estado_inspecao() -> dict[str, Any]` |
| `centro` | propriedade | `centro() -> tuple[float, float]` |
| `definir_centro` | método | `definir_centro(x: float, y: float) -> 'Camera'` |
| `definir_limites_zoom` | método | `definir_limites_zoom(minimo: float \| None = None, maximo: float \| None = None) -> 'Camera'` |
| `definir_zoom` | método | `definir_zoom(valor: float) -> 'Camera'` |
| `definir_rotacao` | método | `definir_rotacao(graus: float) -> 'Camera'` |
| `girar` | método | `girar(graus: float) -> 'Camera'` |
| `definir_deslocamento_visual` | método | `definir_deslocamento_visual(x: float = 0.0, y: float = 0.0) -> 'Camera'` |
| `limpar_deslocamento_visual` | método | `limpar_deslocamento_visual() -> 'Camera'` |
| `animar_com_clipe` | método | `animar_com_clipe(clipe: ClipeAnimacao, mapeamento: dict[str, str], *, modo: str = 'absoluto', restaurar_ao_final: bool = False, composicao: str = 'substituir', permitir_conflito: bool = False)` |
| `efeitos` | propriedade | `efeitos() -> tuple[EfeitoCamera, ...]` |
| `adicionar_efeito` | método | `adicionar_efeito(efeito: EfeitoCamera) -> EfeitoCamera` |
| `tremer` | método | `tremer(intensidade: float = 4.0, duracao: float = 0.2, *, semente: int = 0, frequencia: float = 24.0, curva: str \| Callable[[float], float] = 'linear') -> EfeitoCamera` |
| `impulsionar_deslocamento` | método | `impulsionar_deslocamento(x: float, y: float, duracao: float = 0.2, *, curva: str \| Callable[[float], float] = 'linear') -> EfeitoCamera` |
| `impulsionar_zoom` | método | `impulsionar_zoom(delta: float, duracao: float = 0.2, *, curva: str \| Callable[[float], float] = 'linear') -> EfeitoCamera` |
| `impulsionar_rotacao` | método | `impulsionar_rotacao(graus: float, duracao: float = 0.2, *, curva: str \| Callable[[float], float] = 'linear') -> EfeitoCamera` |
| `aproximar_temporariamente` | método | `aproximar_temporariamente(delta_zoom: float, duracao: float = 0.2, *, curva: str \| Callable[[float], float] = 'suave') -> EfeitoCamera` |
| `pausar_efeitos` | método | `pausar_efeitos() -> None` |
| `retomar_efeitos` | método | `retomar_efeitos() -> None` |
| `cancelar_efeitos` | método | `cancelar_efeitos() -> None` |
| `definir_constante_tempo` | método | `definir_constante_tempo(segundos: float \| None) -> 'Camera'` |
| `definir_zona_morta` | método | `definir_zona_morta(largura: float = 0.0, altura: float = 0.0) -> 'Camera'` |
| `definir_enquadramento` | método | `definir_enquadramento(x: float = 0.0, y: float = 0.0) -> 'Camera'` |
| `definir_antecipacao` | método | `definir_antecipacao(segundos: float = 0.0) -> 'Camera'` |
| `definir_limites` | método | `definir_limites(limites: Retangulo \| None) -> 'Camera'` |
| `travar_eixos` | método | `travar_eixos(*, x: bool \| None = None, y: bool \| None = None) -> 'Camera'` |
| `seguir` | método | `seguir(sprite: Sprite, suavidade: float = 1.0, *, constante_tempo: float \| None = None, zona_morta: tuple[float, float] \| None = None, enquadramento: tuple[float, float] \| None = None, antecipacao: float \| None = None, travar_x: bool \| None = None, travar_y: bool \| None = None)` |
| `seguir_representacao` | método | `seguir_representacao(representacao: RepresentacaoEntidade, **opcoes) -> 'Camera'` |
| `centralizar_no_alvo` | método | `centralizar_no_alvo() -> 'Camera'` |
| `enquadrar_alvos` | método | `enquadrar_alvos(alvos: list[Sprite] \| tuple[Sprite, ...], *, margem: float = 0.0, ajustar_zoom: bool = False) -> 'Camera'` |
| `atualizar` | método | `atualizar(dt: float \| None = None)` |
| `mundo_para_tela` | método | `mundo_para_tela(x: float, y: float) -> tuple[float, float]` |
| `mundo_para_tela_paralaxe` | método | `mundo_para_tela_paralaxe(x: float, y: float, paralaxe_x: float = 1.0, paralaxe_y: float \| None = None) -> tuple[float, float]` |
| `tela_para_mundo` | método | `tela_para_mundo(x: float, y: float) -> tuple[float, float]` |
| `area_visivel` | propriedade | `area_visivel() -> Retangulo` |
| `visivel` | método | `visivel(objeto: Sprite \| Retangulo, *, margem: float = 0.0) -> bool` |
| `tela` | método | `tela(x: float, y: float) -> tuple[float, float]` |

:::

#### `VinculoClipe`

Representa VinculoClipe na API de `coral.jogos`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `alvo` | Valor correspondente a alvo. | `Any` | obrigatório |
| `clipe` | Valor correspondente a clipe. | `ClipeAnimacao` | obrigatório |
| `mapeamento` | Valor correspondente a mapeamento. | `dict[str, str]` | obrigatório |
| `modo` | Valor correspondente a modo. | `str` | `'absoluto'` |
| `restaurar_ao_final` | Valor correspondente a restaurar ao final. | `bool` | `False` |
| `composicao` | Valor correspondente a composicao. | `str` | `'substituir'` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `alvo` | Valor correspondente a alvo. | `Any` | obrigatório |
| `clipe` | Valor correspondente a clipe. | `ClipeAnimacao` | obrigatório |
| `mapeamento` | Valor correspondente a mapeamento. | `dict[str, str]` | obrigatório |
| `modo` | Valor correspondente a modo. | `str` | `'absoluto'` |
| `restaurar_ao_final` | Valor correspondente a restaurar ao final. | `bool` | `False` |
| `composicao` | Valor correspondente a composicao. | `str` | `'substituir'` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `propriedades` | Obtém propriedades. | `tuple[str, ...]` |
| `finalizado` | Executa a operação `finalizado` disponibilizada por `coral.jogos`. | `bool` |
| `atualizar` | Atualiza o valor solicitado. | `dict[str, float]` |

:::details Detalhes técnicos

**Assinatura:** `VinculoClipe(alvo: Any, clipe: ClipeAnimacao, mapeamento: dict[str, str], modo: str = 'absoluto', restaurar_ao_final: bool = False, composicao: str = 'substituir')`

**Origem da implementação:** `coral.jogos.objetos`

**Arquivo na release:** `coral/jogos/objetos.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `propriedades` | propriedade | `propriedades() -> tuple[str, ...]` |
| `finalizado` | propriedade | `finalizado() -> bool` |
| `atualizar` | método | `atualizar(dt: float) -> dict[str, float]` |

:::

#### `QuadroSprite`

Região imutável de uma imagem usada como quadro de sprite.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `caminho` | Caminho do arquivo ou diretório usado pela operação. | `Path` | obrigatório |
| `x` | Coordenada horizontal. | `int` | obrigatório |
| `y` | Coordenada vertical. | `int` | obrigatório |
| `largura` | Largura usada pela operação. | `int` | obrigatório |
| `altura` | Altura usada pela operação. | `int` | obrigatório |
| `indice` | Valor correspondente a indice. | `int \| None` | `None` |
| `linha` | Valor correspondente a linha. | `int \| None` | `None` |
| `coluna` | Valor correspondente a coluna. | `int \| None` | `None` |
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str \| None` | `None` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `caminho` | Caminho do arquivo ou diretório usado pela operação. | `Path` | obrigatório |
| `x` | Coordenada horizontal. | `int` | obrigatório |
| `y` | Coordenada vertical. | `int` | obrigatório |
| `largura` | Largura usada pela operação. | `int` | obrigatório |
| `altura` | Altura usada pela operação. | `int` | obrigatório |
| `indice` | Valor correspondente a indice. | `int \| None` | `None` |
| `linha` | Valor correspondente a linha. | `int \| None` | `None` |
| `coluna` | Valor correspondente a coluna. | `int \| None` | `None` |
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str \| None` | `None` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `retangulo` | Obtém retangulo. | `tuple[int, int, int, int]` |

:::details Detalhes técnicos

**Assinatura:** `QuadroSprite(caminho: Path, x: int, y: int, largura: int, altura: int, indice: int \| None = None, linha: int \| None = None, coluna: int \| None = None, nome: str \| None = None)`

**Origem da implementação:** `coral.jogos.spritesheet`

**Arquivo na release:** `coral/jogos/spritesheet.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `retangulo` | propriedade | `retangulo() -> tuple[int, int, int, int]` |

:::

#### `Spritesheet`

Descrição headless de uma spritesheet ou atlas de imagens.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `caminho` | Caminho do arquivo ou diretório usado pela operação. | `str \| Path` | obrigatório |
| `largura_imagem` | Largura de imagem. | `int` | obrigatório |
| `altura_imagem` | Altura de imagem. | `int` | obrigatório |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `em_grade` | Executa a operação `em_grade` disponibilizada por `coral.jogos`. | `'Spritesheet'` |
| `quadro` | Executa a operação `quadro` disponibilizada por `coral.jogos`. | `QuadroSprite` |
| `quadro_em` | Obtém quadro em. | `QuadroSprite` |
| `quadros_de` | Obtém quadros de. | `tuple[QuadroSprite, ...]` |
| `quadros_da_linha` | Obtém quadros da linha. | `tuple[QuadroSprite, ...]` |
| `animacao_da_linha` | Executa a operação `animacao_da_linha` disponibilizada por `coral.jogos`. | `não declarado` |
| `animacao` | Cria uma Animacao usando um intervalo inclusivo de quadros. | `não declarado` |
| `animacoes_direcionais` | Cria um grupo de animações a partir de linhas nomeadas da grade. | `não declarado` |
| `regiao` | Obtém regiao. | `QuadroSprite` |

:::details Detalhes técnicos

**Assinatura:** `Spritesheet(caminho: str \| Path, *, largura_imagem: int, altura_imagem: int) -> None`

**Origem da implementação:** `coral.jogos.spritesheet`

**Arquivo na release:** `coral/jogos/spritesheet.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `caminho` | posicional |
| `largura_imagem` | nomeado |
| `altura_imagem` | nomeado |

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `em_grade` | método | `em_grade(caminho: str \| Path, *, largura_imagem: int, altura_imagem: int, largura_quadro: int, altura_quadro: int, margem: int = 0, espacamento: int = 0) -> 'Spritesheet'` |
| `quadro` | método | `quadro(indice: int) -> QuadroSprite` |
| `quadro_em` | método | `quadro_em(linha: int, coluna: int) -> QuadroSprite` |
| `quadros_de` | método | `quadros_de(inicio: int, fim: int) -> tuple[QuadroSprite, ...]` |
| `quadros_da_linha` | método | `quadros_da_linha(linha: int, coluna_inicial: int = 0, coluna_final: int \| None = None) -> tuple[QuadroSprite, ...]` |
| `animacao_da_linha` | método | `animacao_da_linha(linha: int, coluna_inicial: int = 0, coluna_final: int \| None = None, *, fps: float = 10.0, repetir: bool = True)` |
| `animacao` | método | `animacao(inicio: int, fim: int, *, fps: float = 10.0, repetir: bool = True)` |
| `animacoes_direcionais` | método | `animacoes_direcionais(linhas: dict[str, int], coluna_inicial: int = 0, coluna_final: int \| None = None, *, fps: float = 10.0, repetir: bool = True)` |
| `regiao` | método | `regiao(x: int, y: int, largura: int, altura: int, *, nome: str \| None = None) -> QuadroSprite` |

:::

#### `FormaTransformada`

Representa FormaTransformada na API de `coral.jogos`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `vertices` | Valor correspondente a vertices. | `tuple[tuple[float, float], ...]` | obrigatório |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `vertices` | Valor correspondente a vertices. | `tuple[tuple[float, float], ...]` | obrigatório |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `limites` | Obtém limites. | `tuple[float, float, float, float]` |

:::details Detalhes técnicos

**Assinatura:** `FormaTransformada(vertices: tuple[tuple[float, float], ...])`

**Origem da implementação:** `coral.jogos.transformacoes`

**Arquivo na release:** `coral/jogos/transformacoes.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `limites` | propriedade | `limites() -> tuple[float, float, float, float]` |

:::

#### `CanalAnimado`

Representa CanalAnimado na API de `coral.jogos`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `canal` | Valor correspondente a canal. | `str` | obrigatório |
| `base` | Base usada pela conversão ou cálculo. | `float` | obrigatório |
| `amplitude` | Valor correspondente a amplitude. | `float` | obrigatório |
| `frequencia` | Valor correspondente a frequencia. | `float` | obrigatório |
| `fase` | Valor correspondente a fase. | `float` | `0.0` |
| `modo` | Valor correspondente a modo. | `str` | `'absoluto'` |
| `onda` | Valor correspondente a onda. | `str \| Callable[[float], float]` | `'seno'` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `canal` | Valor correspondente a canal. | `str` | obrigatório |
| `base` | Base usada pela conversão ou cálculo. | `float` | obrigatório |
| `amplitude` | Valor correspondente a amplitude. | `float` | obrigatório |
| `frequencia` | Valor correspondente a frequencia. | `float` | obrigatório |
| `fase` | Valor correspondente a fase. | `float` | `0.0` |
| `modo` | Valor correspondente a modo. | `str` | `'absoluto'` |
| `onda` | Valor correspondente a onda. | `str \| Callable[[float], float]` | `'seno'` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `valor` | Obtém valor. | `float` |

:::details Detalhes técnicos

**Assinatura:** `CanalAnimado(canal: str, base: float, amplitude: float, frequencia: float, fase: float = 0.0, modo: str = 'absoluto', onda: str \| Callable[[float], float] = 'seno')`

**Origem da implementação:** `coral.jogos.transformacoes`

**Arquivo na release:** `coral/jogos/transformacoes.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `valor` | método | `valor(tempo: float, *, referencia: float = 0.0) -> float` |

:::

#### `AnimacaoTransformacao`

Representa AnimacaoTransformacao na API de `coral.jogos`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `canais` | Valor correspondente a canais. | `tuple[CanalAnimado, ...]` | obrigatório |
| `tempo` | Valor correspondente a tempo. | `float` | `0.0` |
| `estado` | Estado usado ou atualizado pela operação. | `str` | `'ativo'` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `canais` | Valor correspondente a canais. | `tuple[CanalAnimado, ...]` | obrigatório |
| `tempo` | Valor correspondente a tempo. | `float` | `0.0` |
| `estado` | Estado usado ou atualizado pela operação. | `str` | `'ativo'` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `pausar` | Pausa o valor solicitado. | `None` |
| `retomar` | Retoma o valor solicitado. | `None` |
| `reiniciar` | Reinicia o valor solicitado. | `None` |
| `encerrar` | Encerra o valor solicitado. | `None` |
| `avancar` | Avança o valor solicitado. | `None` |

:::details Detalhes técnicos

**Assinatura:** `AnimacaoTransformacao(canais: tuple[CanalAnimado, ...], tempo: float = 0.0, estado: str = 'ativo')`

**Origem da implementação:** `coral.jogos.transformacoes`

**Arquivo na release:** `coral/jogos/transformacoes.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `pausar` | método | `pausar() -> None` |
| `retomar` | método | `retomar() -> None` |
| `reiniciar` | método | `reiniciar() -> None` |
| `encerrar` | método | `encerrar() -> None` |
| `avancar` | método | `avancar(dt: float) -> None` |

:::

#### `QuadroChave`

Valor numérico associado a um instante de uma faixa temporal.

**Exemplo**

```coral
defina faixa_x como FaixaAnimacao("x", (
    QuadroChave(0.0, 0.0, "entrada_saida_suave"),
    QuadroChave(1.0, 100.0)
))
```

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `instante` | Valor correspondente a instante. | `float` | obrigatório |
| `valor` | Valor processado pela operação. | `float` | obrigatório |
| `curva` | Valor correspondente a curva. | `str \| Callable[[float], float]` | `'linear'` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `instante` | Valor correspondente a instante. | `float` | obrigatório |
| `valor` | Valor processado pela operação. | `float` | obrigatório |
| `curva` | Valor correspondente a curva. | `str \| Callable[[float], float]` | `'linear'` |

:::details Detalhes técnicos

**Assinatura:** `QuadroChave(instante: float, valor: float, curva: str \| Callable[[float], float] = 'linear')`

**Origem da implementação:** `coral.jogos.transformacoes`

**Arquivo na release:** `coral/jogos/transformacoes.py`

:::

#### `FaixaAnimacao`

Faixa temporal imutável de quadros chave para uma propriedade.

**Exemplo**

```coral
de coral.jogos importe QuadroChave, FaixaAnimacao, ClipeAnimacao, Sprite

defina faixa_x como FaixaAnimacao("x", (
    QuadroChave(0.0, 0.0, "entrada_saida_suave"),
    QuadroChave(1.0, 100.0)
))
```

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | obrigatório |
| `quadros` | Valor correspondente a quadros. | `tuple[QuadroChave, ...]` | obrigatório |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | obrigatório |
| `quadros` | Valor correspondente a quadros. | `tuple[QuadroChave, ...]` | obrigatório |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `duracao` | Executa a operação `duracao` disponibilizada por `coral.jogos`. | `float` |
| `valor_em` | Executa a operação `valor_em` disponibilizada por `coral.jogos`. | `float` |

:::details Detalhes técnicos

**Assinatura:** `FaixaAnimacao(nome: str, quadros: tuple[QuadroChave, ...])`

**Origem da implementação:** `coral.jogos.transformacoes`

**Arquivo na release:** `coral/jogos/transformacoes.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `duracao` | propriedade | `duracao() -> float` |
| `valor_em` | método | `valor_em(instante: float) -> float` |

:::

#### `ClipeAnimacao`

Reprodutor headless de uma ou mais faixas de quadros chave.

**Exemplo**

```coral
))

defina clipe como ClipeAnimacao((faixa_x,), modo="ida_volta")
defina heroi como Sprite(0, 0, 16, 16)
execute heroi.animar_com_clipe(clipe, {"x": "x"})
execute heroi.atualizar(0.5)
```

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `faixas` | Valor correspondente a faixas. | `tuple[FaixaAnimacao, ...]` | obrigatório |
| `velocidade` | Valor correspondente a velocidade. | `float` | `1.0` |
| `modo` | Valor correspondente a modo. | `str` | `'normal'` |
| `repetir` | Valor correspondente a repetir. | `bool` | `False` |
| `tempo` | Valor correspondente a tempo. | `float` | `0.0` |
| `estado` | Estado usado ou atualizado pela operação. | `str` | `'ativo'` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `faixas` | Valor correspondente a faixas. | `tuple[FaixaAnimacao, ...]` | obrigatório |
| `velocidade` | Valor correspondente a velocidade. | `float` | `1.0` |
| `modo` | Valor correspondente a modo. | `str` | `'normal'` |
| `repetir` | Valor correspondente a repetir. | `bool` | `False` |
| `tempo` | Valor correspondente a tempo. | `float` | `0.0` |
| `estado` | Estado usado ou atualizado pela operação. | `str` | `'ativo'` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `duracao` | Executa a operação `duracao` disponibilizada por `coral.jogos`. | `float` |
| `finalizado` | Executa a operação `finalizado` disponibilizada por `coral.jogos`. | `bool` |
| `progresso` | Executa a operação `progresso` disponibilizada por `coral.jogos`. | `float` |
| `valor` | Obtém valor. | `float` |
| `valores` | Executa a operação `valores` disponibilizada por `coral.jogos`. | `dict[str, float]` |
| `pausar` | Pausa o valor solicitado. | `'ClipeAnimacao'` |
| `retomar` | Retoma o valor solicitado. | `'ClipeAnimacao'` |
| `reiniciar` | Reinicia o valor solicitado. | `'ClipeAnimacao'` |
| `buscar` | Executa a operação `buscar` disponibilizada por `coral.jogos`. | `'ClipeAnimacao'` |
| `avancar` | Avança o valor solicitado. | `dict[str, float]` |

:::details Detalhes técnicos

**Assinatura:** `ClipeAnimacao(faixas: tuple[FaixaAnimacao, ...], velocidade: float = 1.0, modo: str = 'normal', repetir: bool = False, tempo: float = 0.0, estado: str = 'ativo')`

**Origem da implementação:** `coral.jogos.transformacoes`

**Arquivo na release:** `coral/jogos/transformacoes.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `duracao` | propriedade | `duracao() -> float` |
| `finalizado` | propriedade | `finalizado() -> bool` |
| `progresso` | propriedade | `progresso() -> float` |
| `valor` | método | `valor(faixa: str) -> float` |
| `valores` | método | `valores() -> dict[str, float]` |
| `pausar` | método | `pausar() -> 'ClipeAnimacao'` |
| `retomar` | método | `retomar() -> 'ClipeAnimacao'` |
| `reiniciar` | método | `reiniciar() -> 'ClipeAnimacao'` |
| `buscar` | método | `buscar(instante: float) -> 'ClipeAnimacao'` |
| `avancar` | método | `avancar(dt: float) -> dict[str, float]` |

:::

#### `AcaoApresentacao`

Representa AcaoApresentacao na API de `coral.jogos`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `acao` | Valor correspondente a acao. | `Callable[[], Any]` | obrigatório |
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str \| None` | `None` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `acao` | Valor correspondente a acao. | `Callable[[], Any]` | obrigatório |
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str \| None` | `None` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `finalizado` | Executa a operação `finalizado` disponibilizada por `coral.jogos`. | `bool` |
| `progresso` | Executa a operação `progresso` disponibilizada por `coral.jogos`. | `float` |
| `avancar` | Avança o valor solicitado. | `float` |
| `reiniciar` | Reinicia o valor solicitado. | `None` |

:::details Detalhes técnicos

**Assinatura:** `AcaoApresentacao(acao: Callable[[], Any], nome: str \| None = None)`

**Origem da implementação:** `coral.jogos.composicao`

**Arquivo na release:** `coral/jogos/composicao.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `finalizado` | propriedade | `finalizado() -> bool` |
| `progresso` | propriedade | `progresso() -> float` |
| `avancar` | método | `avancar(dt: float) -> float` |
| `reiniciar` | método | `reiniciar() -> None` |

:::

#### `EsperaApresentacao`

Representa EsperaApresentacao na API de `coral.jogos`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `duracao` | Valor correspondente a duracao. | `float` | obrigatório |
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str \| None` | `None` |
| `tempo` | Valor correspondente a tempo. | `float` | `0.0` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `duracao` | Valor correspondente a duracao. | `float` | obrigatório |
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str \| None` | `None` |
| `tempo` | Valor correspondente a tempo. | `float` | `0.0` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `finalizado` | Executa a operação `finalizado` disponibilizada por `coral.jogos`. | `bool` |
| `progresso` | Executa a operação `progresso` disponibilizada por `coral.jogos`. | `float` |
| `avancar` | Avança o valor solicitado. | `float` |
| `reiniciar` | Reinicia o valor solicitado. | `None` |

:::details Detalhes técnicos

**Assinatura:** `EsperaApresentacao(duracao: float, nome: str \| None = None, tempo: float = 0.0)`

**Origem da implementação:** `coral.jogos.composicao`

**Arquivo na release:** `coral/jogos/composicao.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `finalizado` | propriedade | `finalizado() -> bool` |
| `progresso` | propriedade | `progresso() -> float` |
| `avancar` | método | `avancar(dt: float) -> float` |
| `reiniciar` | método | `reiniciar() -> None` |

:::

#### `EsperaConclusao`

Representa EsperaConclusao na API de `coral.jogos`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `alvo` | Valor correspondente a alvo. | `Any` | obrigatório |
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str \| None` | `None` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `alvo` | Valor correspondente a alvo. | `Any` | obrigatório |
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str \| None` | `None` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `finalizado` | Executa a operação `finalizado` disponibilizada por `coral.jogos`. | `bool` |
| `progresso` | Executa a operação `progresso` disponibilizada por `coral.jogos`. | `float` |
| `avancar` | Avança o valor solicitado. | `float` |
| `reiniciar` | Reinicia o valor solicitado. | `None` |

:::details Detalhes técnicos

**Assinatura:** `EsperaConclusao(alvo: Any, nome: str \| None = None)`

**Origem da implementação:** `coral.jogos.composicao`

**Arquivo na release:** `coral/jogos/composicao.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `finalizado` | propriedade | `finalizado() -> bool` |
| `progresso` | propriedade | `progresso() -> float` |
| `avancar` | método | `avancar(dt: float) -> float` |
| `reiniciar` | método | `reiniciar() -> None` |

:::

#### `SequenciaApresentacao`

Representa SequenciaApresentacao na API de `coral.jogos`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `etapas` | Valor correspondente a etapas. | `tuple[NoApresentacao, ...]` | obrigatório |
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str \| None` | `None` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `etapas` | Valor correspondente a etapas. | `tuple[NoApresentacao, ...]` | obrigatório |
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str \| None` | `None` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `finalizado` | Executa a operação `finalizado` disponibilizada por `coral.jogos`. | `bool` |
| `progresso` | Executa a operação `progresso` disponibilizada por `coral.jogos`. | `float` |
| `etapa_atual` | Executa a operação `etapa_atual` disponibilizada por `coral.jogos`. | `NoApresentacao \| None` |
| `avancar` | Avança o valor solicitado. | `float` |
| `reiniciar` | Reinicia o valor solicitado. | `None` |

:::details Detalhes técnicos

**Assinatura:** `SequenciaApresentacao(etapas: tuple[NoApresentacao, ...], nome: str \| None = None)`

**Origem da implementação:** `coral.jogos.composicao`

**Arquivo na release:** `coral/jogos/composicao.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `finalizado` | propriedade | `finalizado() -> bool` |
| `progresso` | propriedade | `progresso() -> float` |
| `etapa_atual` | propriedade | `etapa_atual() -> NoApresentacao \| None` |
| `avancar` | método | `avancar(dt: float) -> float` |
| `reiniciar` | método | `reiniciar() -> None` |

:::

#### `ParaleloApresentacao`

Representa ParaleloApresentacao na API de `coral.jogos`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `etapas` | Valor correspondente a etapas. | `tuple[NoApresentacao, ...]` | obrigatório |
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str \| None` | `None` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `etapas` | Valor correspondente a etapas. | `tuple[NoApresentacao, ...]` | obrigatório |
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str \| None` | `None` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `finalizado` | Executa a operação `finalizado` disponibilizada por `coral.jogos`. | `bool` |
| `progresso` | Executa a operação `progresso` disponibilizada por `coral.jogos`. | `float` |
| `avancar` | Avança o valor solicitado. | `float` |
| `reiniciar` | Reinicia o valor solicitado. | `None` |

:::details Detalhes técnicos

**Assinatura:** `ParaleloApresentacao(etapas: tuple[NoApresentacao, ...], nome: str \| None = None)`

**Origem da implementação:** `coral.jogos.composicao`

**Arquivo na release:** `coral/jogos/composicao.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `finalizado` | propriedade | `finalizado() -> bool` |
| `progresso` | propriedade | `progresso() -> float` |
| `avancar` | método | `avancar(dt: float) -> float` |
| `reiniciar` | método | `reiniciar() -> None` |

:::

#### `ComposicaoTemporal`

Representa sequência e paralelismo de ações com tempo explícito.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `raiz` | Valor correspondente a raiz. | `NoApresentacao` | obrigatório |
| `repeticoes` | Valor correspondente a repeticoes. | `int \| None` | `1` |
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str \| None` | `None` |
| `estado` | Estado usado ou atualizado pela operação. | `str` | `'ativo'` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `raiz` | Valor correspondente a raiz. | `NoApresentacao` | obrigatório |
| `repeticoes` | Valor correspondente a repeticoes. | `int \| None` | `1` |
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str \| None` | `None` |
| `estado` | Estado usado ou atualizado pela operação. | `str` | `'ativo'` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `finalizado` | Executa a operação `finalizado` disponibilizada por `coral.jogos`. | `bool` |
| `cancelado` | Indica o estado de cancelado. | `bool` |
| `ciclos_concluidos` | Executa a operação `ciclos_concluidos` disponibilizada por `coral.jogos`. | `int` |
| `progresso` | Executa a operação `progresso` disponibilizada por `coral.jogos`. | `float` |
| `etapa_atual` | Executa a operação `etapa_atual` disponibilizada por `coral.jogos`. | `str \| None` |
| `pausar` | Pausa o valor solicitado. | `'ComposicaoTemporal'` |
| `retomar` | Retoma o valor solicitado. | `'ComposicaoTemporal'` |
| `cancelar` | Cancela o valor solicitado. | `'ComposicaoTemporal'` |
| `reiniciar` | Reinicia o valor solicitado. | `'ComposicaoTemporal'` |
| `avancar` | Avança o valor solicitado. | `'ComposicaoTemporal'` |

:::details Detalhes técnicos

**Assinatura:** `ComposicaoTemporal(raiz: NoApresentacao, repeticoes: int \| None = 1, nome: str \| None = None, estado: str = 'ativo')`

**Origem da implementação:** `coral.jogos.composicao`

**Arquivo na release:** `coral/jogos/composicao.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `finalizado` | propriedade | `finalizado() -> bool` |
| `cancelado` | propriedade | `cancelado() -> bool` |
| `ciclos_concluidos` | propriedade | `ciclos_concluidos() -> int` |
| `progresso` | propriedade | `progresso() -> float` |
| `etapa_atual` | propriedade | `etapa_atual() -> str \| None` |
| `pausar` | método | `pausar() -> 'ComposicaoTemporal'` |
| `retomar` | método | `retomar() -> 'ComposicaoTemporal'` |
| `cancelar` | método | `cancelar() -> 'ComposicaoTemporal'` |
| `reiniciar` | método | `reiniciar() -> 'ComposicaoTemporal'` |
| `avancar` | método | `avancar(dt: float) -> 'ComposicaoTemporal'` |

:::

#### `VinculoTempoApresentacao`

Avança uma composição a partir de uma fonte de tempo explicitamente escolhida.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `composicao` | Valor correspondente a composicao. | `ComposicaoTemporal` | obrigatório |
| `fonte` | Fonte explícita usada pela operação; quando omitida, vale o comportamento padrão do módulo. | `Any` | obrigatório |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `composicao` | Valor correspondente a composicao. | `ComposicaoTemporal` | obrigatório |
| `fonte` | Fonte explícita usada pela operação; quando omitida, vale o comportamento padrão do módulo. | `Any` | obrigatório |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `atualizar` | Atualiza o valor solicitado. | `float` |
| `ressincronizar` | Executa a operação `ressincronizar` disponibilizada por `coral.jogos`. | `'VinculoTempoApresentacao'` |

:::details Detalhes técnicos

**Assinatura:** `VinculoTempoApresentacao(composicao: ComposicaoTemporal, fonte: Any)`

**Origem da implementação:** `coral.jogos.composicao`

**Arquivo na release:** `coral/jogos/composicao.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `atualizar` | método | `atualizar() -> float` |
| `ressincronizar` | método | `ressincronizar() -> 'VinculoTempoApresentacao'` |

:::

#### `VinculoComposicaoEventos`

Controla uma composição por um evento sem acoplar o barramento a Jogos.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `composicao` | Valor correspondente a composicao. | `ComposicaoTemporal` | obrigatório |
| `eventos` | Fonte ou conjunto de eventos associado à operação. | `Any` | obrigatório |
| `evento` | Valor correspondente a evento. | `str` | obrigatório |
| `modo` | Valor correspondente a modo. | `str` | `'reiniciar'` |
| `ativo` | Valor correspondente a ativo. | `bool` | `field(default=True, init=False)` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `composicao` | Valor correspondente a composicao. | `ComposicaoTemporal` | obrigatório |
| `eventos` | Fonte ou conjunto de eventos associado à operação. | `Any` | obrigatório |
| `evento` | Valor correspondente a evento. | `str` | obrigatório |
| `modo` | Valor correspondente a modo. | `str` | `'reiniciar'` |
| `ativo` | Valor correspondente a ativo. | `bool` | `field(default=True, init=False)` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `desligar` | Desliga o valor solicitado. | `None` |

:::details Detalhes técnicos

**Assinatura:** `VinculoComposicaoEventos(composicao: ComposicaoTemporal, eventos: Any, evento: str, modo: str = 'reiniciar', ativo: bool = field(default=True, init=False))`

**Origem da implementação:** `coral.jogos.composicao`

**Arquivo na release:** `coral/jogos/composicao.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `desligar` | método | `desligar() -> None` |

:::

#### `ComandoComposicao`

Representa ComandoComposicao na API de `coral.jogos`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `operacao` | Valor correspondente a operacao. | `str` | obrigatório |
| `valor` | Valor processado pela operação. | `float \| None` | `None` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `operacao` | Valor correspondente a operacao. | `str` | obrigatório |
| `valor` | Valor processado pela operação. | `float \| None` | `None` |

:::details Detalhes técnicos

**Assinatura:** `ComandoComposicao(operacao: str, valor: float \| None = None)`

**Origem da implementação:** `coral.jogos.composicao`

**Arquivo na release:** `coral/jogos/composicao.py`

:::

#### `GravadorComposicao`

Grava comandos explícitos de uma composição para replay determinístico.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `composicao` | Valor correspondente a composicao. | `ComposicaoTemporal` | obrigatório |
| `comandos` | Valor correspondente a comandos. | `list[ComandoComposicao]` | `field(default_factory=list)` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `composicao` | Valor correspondente a composicao. | `ComposicaoTemporal` | obrigatório |
| `comandos` | Valor correspondente a comandos. | `list[ComandoComposicao]` | `field(default_factory=list)` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `avancar` | Avança o valor solicitado. | `'GravadorComposicao'` |
| `pausar` | Pausa o valor solicitado. | `'GravadorComposicao'` |
| `retomar` | Retoma o valor solicitado. | `'GravadorComposicao'` |
| `cancelar` | Cancela o valor solicitado. | `'GravadorComposicao'` |
| `reiniciar` | Reinicia o valor solicitado. | `'GravadorComposicao'` |
| `reproduzir_em` | Reproduz em. | `ComposicaoTemporal` |

:::details Detalhes técnicos

**Assinatura:** `GravadorComposicao(composicao: ComposicaoTemporal, comandos: list[ComandoComposicao] = field(default_factory=list))`

**Origem da implementação:** `coral.jogos.composicao`

**Arquivo na release:** `coral/jogos/composicao.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `avancar` | método | `avancar(dt: float) -> 'GravadorComposicao'` |
| `pausar` | método | `pausar() -> 'GravadorComposicao'` |
| `retomar` | método | `retomar() -> 'GravadorComposicao'` |
| `cancelar` | método | `cancelar() -> 'GravadorComposicao'` |
| `reiniciar` | método | `reiniciar() -> 'GravadorComposicao'` |
| `reproduzir_em` | método | `reproduzir_em(composicao: ComposicaoTemporal) -> ComposicaoTemporal` |

:::

#### `AdaptadorEventosJogo`

Publica acontecimentos de Jogos no barramento reativo do próprio Jogo.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `jogo` | Valor correspondente a jogo. | `Jogo` | obrigatório |
| `teclas` | Valor correspondente a teclas. | `Iterable[str]` | `()` |
| `botoes_mouse` | Valor correspondente a botoes mouse. | `Iterable[str]` | `()` |
| `observar_mouse` | Valor correspondente a observar mouse. | `bool` | `False` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `ativo` | Indica o estado de ativo. | `bool` |
| `desligar` | Desliga o valor solicitado. | `None` |
| `ligar` | Liga o valor solicitado. | `None` |
| `observar_colisao` | Observa colisao. | `_ColisaoObservada` |
| `publicar_transicao_visual` | Publica transicao visual. | `não declarado` |

:::details Detalhes técnicos

**Assinatura:** `AdaptadorEventosJogo(jogo: Jogo, *, teclas: Iterable[str] = (), botoes_mouse: Iterable[str] = (), observar_mouse: bool = False)`

**Origem da implementação:** `coral.jogos.eventos`

**Arquivo na release:** `coral/jogos/eventos.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `jogo` | posicional |
| `teclas` | nomeado |
| `botoes_mouse` | nomeado |
| `observar_mouse` | nomeado |

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `ativo` | propriedade | `ativo() -> bool` |
| `desligar` | método | `desligar() -> None` |
| `ligar` | método | `ligar() -> None` |
| `observar_colisao` | método | `observar_colisao(primeiro: Sprite, segundo: Sprite, *, nome: str \| None = None) -> _ColisaoObservada` |
| `publicar_transicao_visual` | método | `publicar_transicao_visual(sprite: Sprite, transicao: str, *, estado: str \| None = None)` |

:::

#### `Viewport`

Transformação entre a superfície física e a área lógica de Jogos.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `largura_logica` | Largura de logica. | `float` | obrigatório |
| `altura_logica` | Altura de logica. | `float` | obrigatório |
| `largura_fisica` | Largura de fisica. | `float` | obrigatório |
| `altura_fisica` | Altura de fisica. | `float` | obrigatório |
| `modo` | Valor correspondente a modo. | `str` | `'ajustar'` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `largura_logica` | Largura de logica. | `float` | obrigatório |
| `altura_logica` | Altura de logica. | `float` | obrigatório |
| `largura_fisica` | Largura de fisica. | `float` | obrigatório |
| `altura_fisica` | Altura de fisica. | `float` | obrigatório |
| `modo` | Valor correspondente a modo. | `str` | `'ajustar'` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `escala_x` | Executa a operação `escala_x` disponibilizada por `coral.jogos`. | `float` |
| `escala_y` | Executa a operação `escala_y` disponibilizada por `coral.jogos`. | `float` |
| `deslocamento_x` | Executa a operação `deslocamento_x` disponibilizada por `coral.jogos`. | `float` |
| `deslocamento_y` | Executa a operação `deslocamento_y` disponibilizada por `coral.jogos`. | `float` |
| `area_fisica_util` | Executa a operação `area_fisica_util` disponibilizada por `coral.jogos`. | `tuple[float, float, float, float]` |
| `logica_para_tela` | Executa a operação `logica_para_tela` disponibilizada por `coral.jogos`. | `tuple[float, float]` |
| `tela_para_logica` | Executa a operação `tela_para_logica` disponibilizada por `coral.jogos`. | `tuple[float, float]` |
| `contem_tela` | Executa a operação `contem_tela` disponibilizada por `coral.jogos`. | `bool` |
| `ancorar` | Retorna o canto superior esquerdo de um elemento na área lógica. | `tuple[float, float]` |

:::details Detalhes técnicos

**Assinatura:** `Viewport(largura_logica: float, altura_logica: float, largura_fisica: float, altura_fisica: float, modo: str = 'ajustar')`

**Origem da implementação:** `coral.jogos.viewport`

**Arquivo na release:** `coral/jogos/viewport.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `escala_x` | propriedade | `escala_x() -> float` |
| `escala_y` | propriedade | `escala_y() -> float` |
| `deslocamento_x` | propriedade | `deslocamento_x() -> float` |
| `deslocamento_y` | propriedade | `deslocamento_y() -> float` |
| `area_fisica_util` | propriedade | `area_fisica_util() -> tuple[float, float, float, float]` |
| `logica_para_tela` | método | `logica_para_tela(x: float, y: float) -> tuple[float, float]` |
| `tela_para_logica` | método | `tela_para_logica(x: float, y: float, *, limitar: bool = False) -> tuple[float, float]` |
| `contem_tela` | método | `contem_tela(x: float, y: float) -> bool` |
| `ancorar` | método | `ancorar(largura: float, altura: float, *, ancora: str = 'superior_esquerda', margem_x: float = 0.0, margem_y: float \| None = None) -> tuple[float, float]` |

:::

#### `PrimitivaDebug`

Representa PrimitivaDebug na API de `coral.jogos`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `tipo` | Tipo solicitado para o resultado, quando o módulo oferece essa escolha. | `str` | obrigatório |
| `categoria` | Valor correspondente a categoria. | `str` | obrigatório |
| `dados` | Dados processados pela operação. | `Mapping[str, Any]` | `field(default_factory=dict)` |
| `rotulo` | Valor correspondente a rotulo. | `str \| None` | `None` |
| `espaco` | Valor correspondente a espaco. | `str` | `'mundo'` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `tipo` | Tipo solicitado para o resultado, quando o módulo oferece essa escolha. | `str` | obrigatório |
| `categoria` | Valor correspondente a categoria. | `str` | obrigatório |
| `dados` | Dados processados pela operação. | `Mapping[str, Any]` | `field(default_factory=dict)` |
| `rotulo` | Valor correspondente a rotulo. | `str \| None` | `None` |
| `espaco` | Valor correspondente a espaco. | `str` | `'mundo'` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `para_dict` | Converte o valor para dict. | `dict[str, Any]` |

:::details Detalhes técnicos

**Assinatura:** `PrimitivaDebug(tipo: str, categoria: str, dados: Mapping[str, Any] = field(default_factory=dict), rotulo: str \| None = None, espaco: str = 'mundo')`

**Origem da implementação:** `coral.jogos.debug`

**Arquivo na release:** `coral/jogos/debug.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `para_dict` | método | `para_dict() -> dict[str, Any]` |

:::

#### `OverlayDebug`

Representa OverlayDebug na API de `coral.jogos`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `primitivas` | Valor correspondente a primitivas. | `tuple[PrimitivaDebug, ...]` | `()` |
| `assinatura_origem` | Valor correspondente a assinatura origem. | `str \| None` | `None` |
| `contrato` | Valor correspondente a contrato. | `str` | `CONTRATO_OVERLAY_DEBUG` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `primitivas` | Valor correspondente a primitivas. | `tuple[PrimitivaDebug, ...]` | `()` |
| `assinatura_origem` | Valor correspondente a assinatura origem. | `str \| None` | `None` |
| `contrato` | Valor correspondente a contrato. | `str` | `CONTRATO_OVERLAY_DEBUG` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `quantidade` | Executa a operação `quantidade` disponibilizada por `coral.jogos`. | `int` |
| `por_categoria` | Executa a operação `por_categoria` disponibilizada por `coral.jogos`. | `tuple[PrimitivaDebug, ...]` |
| `para_dict` | Converte o valor para dict. | `dict[str, Any]` |
| `para_json` | Converte o valor para JSON. | `str` |

:::details Detalhes técnicos

**Assinatura:** `OverlayDebug(primitivas: tuple[PrimitivaDebug, ...] = (), assinatura_origem: str \| None = None, contrato: str = CONTRATO_OVERLAY_DEBUG)`

**Origem da implementação:** `coral.jogos.debug`

**Arquivo na release:** `coral/jogos/debug.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `quantidade` | propriedade | `quantidade() -> int` |
| `por_categoria` | método | `por_categoria(categoria: str) -> tuple[PrimitivaDebug, ...]` |
| `para_dict` | método | `para_dict() -> dict[str, Any]` |
| `para_json` | método | `para_json(**kwargs: Any) -> str` |

:::

#### `EstiloOverlayDebug`

Estilo de desenho desacoplado da geração geométrica do overlay.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `limites` | Valor correspondente a limites. | `Any` | `None` |
| `colisor` | Valor correspondente a colisor. | `Any` | `None` |
| `pivo` | Valor correspondente a pivo. | `Any` | `None` |
| `camera` | Valor correspondente a camera. | `Any` | `None` |
| `camera_centro` | Valor correspondente a camera centro. | `Any` | `None` |
| `rotulo` | Valor correspondente a rotulo. | `Any` | `None` |
| `metricas` | Valor correspondente a metricas. | `Any` | `None` |
| `espessura` | Valor correspondente a espessura. | `int` | `1` |
| `tamanho_pivo` | Valor correspondente a tamanho pivo. | `int` | `3` |
| `tamanho_texto` | Valor correspondente a tamanho texto. | `int` | `14` |
| `opacidade` | Valor correspondente a opacidade. | `float` | `1.0` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `limites` | Valor correspondente a limites. | `Any` | `None` |
| `colisor` | Valor correspondente a colisor. | `Any` | `None` |
| `pivo` | Valor correspondente a pivo. | `Any` | `None` |
| `camera` | Valor correspondente a camera. | `Any` | `None` |
| `camera_centro` | Valor correspondente a camera centro. | `Any` | `None` |
| `rotulo` | Valor correspondente a rotulo. | `Any` | `None` |
| `metricas` | Valor correspondente a metricas. | `Any` | `None` |
| `espessura` | Valor correspondente a espessura. | `int` | `1` |
| `tamanho_pivo` | Valor correspondente a tamanho pivo. | `int` | `3` |
| `tamanho_texto` | Valor correspondente a tamanho texto. | `int` | `14` |
| `opacidade` | Valor correspondente a opacidade. | `float` | `1.0` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `cor_para` | Executa a operação `cor_para` disponibilizada por `coral.jogos`. | `não declarado` |

:::details Detalhes técnicos

**Assinatura:** `EstiloOverlayDebug(limites: Any = None, colisor: Any = None, pivo: Any = None, camera: Any = None, camera_centro: Any = None, rotulo: Any = None, metricas: Any = None, espessura: int = 1, tamanho_pivo: int = 3, tamanho_texto: int = 14, opacidade: float = 1.0)`

**Origem da implementação:** `coral.jogos.debug`

**Arquivo na release:** `coral/jogos/debug.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `cor_para` | método | `cor_para(categoria: str)` |

:::

#### `ConfiguracaoDebugJogo`

Configuração persistente e serializável do modo de debug de Jogo.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `ativo` | Valor correspondente a ativo. | `bool` | `False` |
| `categorias` | Valor correspondente a categorias. | `frozenset[str]` | `_CATEGORIAS_DEBUG_PADRAO` |
| `incluir_invisiveis` | Controla se deve incluir invisiveis. | `bool` | `False` |
| `estilo` | Valor correspondente a estilo. | `EstiloOverlayDebug` | `field(default_factory=EstiloOverlayDebug)` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `ativo` | Valor correspondente a ativo. | `bool` | `False` |
| `categorias` | Valor correspondente a categorias. | `frozenset[str]` | `_CATEGORIAS_DEBUG_PADRAO` |
| `incluir_invisiveis` | Controla se deve incluir invisiveis. | `bool` | `False` |
| `estilo` | Valor correspondente a estilo. | `EstiloOverlayDebug` | `field(default_factory=EstiloOverlayDebug)` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `estado_inspecao` | Executa a operação `estado_inspecao` disponibilizada por `coral.jogos`. | `dict[str, Any]` |
| `com_alteracoes` | Executa a operação `com_alteracoes` disponibilizada por `coral.jogos`. | `'ConfiguracaoDebugJogo'` |

:::details Detalhes técnicos

**Assinatura:** `ConfiguracaoDebugJogo(ativo: bool = False, categorias: frozenset[str] = _CATEGORIAS_DEBUG_PADRAO, incluir_invisiveis: bool = False, estilo: EstiloOverlayDebug = field(default_factory=EstiloOverlayDebug))`

**Origem da implementação:** `coral.jogos.debug`

**Arquivo na release:** `coral/jogos/debug.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `estado_inspecao` | método | `estado_inspecao() -> dict[str, Any]` |
| `com_alteracoes` | método | `com_alteracoes(*, ativo: bool \| None = None, categorias: Any = None, incluir_invisiveis: bool \| None = None, estilo: EstiloOverlayDebug \| None = None) -> 'ConfiguracaoDebugJogo'` |

:::

#### `EstiloCelula`

Representa EstiloCelula na API de `coral.jogos`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `cor` | Valor correspondente a cor. | `Cor \| None` | `None` |
| `imagem` | Valor correspondente a imagem. | `str \| QuadroSprite \| None` | `None` |
| `texto` | Texto processado pela operação. | `str \| None` | `None` |
| `cor_texto` | Valor correspondente a cor texto. | `Cor` | `BRANCO` |
| `tamanho_texto` | Valor correspondente a tamanho texto. | `int` | `16` |
| `contorno` | Valor correspondente a contorno. | `int` | `0` |
| `opacidade` | Valor correspondente a opacidade. | `float` | `1.0` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `cor` | Valor correspondente a cor. | `Cor \| None` | `None` |
| `imagem` | Valor correspondente a imagem. | `str \| QuadroSprite \| None` | `None` |
| `texto` | Texto processado pela operação. | `str \| None` | `None` |
| `cor_texto` | Valor correspondente a cor texto. | `Cor` | `BRANCO` |
| `tamanho_texto` | Valor correspondente a tamanho texto. | `int` | `16` |
| `contorno` | Valor correspondente a contorno. | `int` | `0` |
| `opacidade` | Valor correspondente a opacidade. | `float` | `1.0` |

:::details Detalhes técnicos

**Assinatura:** `EstiloCelula(cor: Cor \| None = None, imagem: str \| QuadroSprite \| None = None, texto: str \| None = None, cor_texto: Cor = BRANCO, tamanho_texto: int = 16, contorno: int = 0, opacidade: float = 1.0)`

**Origem da implementação:** `coral.jogos.mapas`

**Arquivo na release:** `coral/jogos/mapas.py`

:::

#### `RenderizadorMapa2D`

Representa apresentação de mapas de coral.mundo.

**Exemplo**

```coral
defina camera como Camera(0, 0, 64, 64)
defina backend como BackendNulo()
defina renderizador como RenderizadorMapa2D(sala, camera=camera)
defina desenhadas como renderizador.desenhar(backend)
```

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `mapa` | Valor correspondente a mapa. | `Mapa` | obrigatório |
| `camadas` | Valor correspondente a camadas. | `Iterable[str] \| None` | `None` |
| `camera` | Valor correspondente a camera. | `Camera \| None` | `None` |
| `resolvedor_estilo` | Valor correspondente a resolvedor estilo. | `ResolvedorEstiloMapa \| None` | `None` |
| `area_visivel` | Valor correspondente a area visivel. | `tuple[float, float, float, float] \| None` | `None` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `camadas` | Obtém camadas. | `tuple[CamadaMapa, ...]` |
| `celulas_visiveis` | Executa a operação `celulas_visiveis` disponibilizada por `coral.jogos`. | `tuple[Any, ...]` |
| `desenhar` | Executa a operação `desenhar` disponibilizada por `coral.jogos`. | `int` |

:::details Detalhes técnicos

**Assinatura:** `RenderizadorMapa2D(mapa: Mapa, *, camadas: Iterable[str] \| None = None, camera: Camera \| None = None, resolvedor_estilo: ResolvedorEstiloMapa \| None = None, area_visivel: tuple[float, float, float, float] \| None = None) -> None`

**Origem da implementação:** `coral.jogos.mapas`

**Arquivo na release:** `coral/jogos/mapas.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `mapa` | posicional |
| `camadas` | nomeado |
| `camera` | nomeado |
| `resolvedor_estilo` | nomeado |
| `area_visivel` | nomeado |

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `camadas` | propriedade | `camadas() -> tuple[CamadaMapa, ...]` |
| `celulas_visiveis` | método | `celulas_visiveis() -> tuple[Any, ...]` |
| `desenhar` | método | `desenhar(backend: BackendJogos) -> int` |

:::

### Exceções

#### `ErroJogosCoral`

Representa a condição de erro ErroJogosCoral.

:::details Detalhes técnicos

**Assinatura:** `ErroJogosCoral(...)`

**Origem da implementação:** `coral.jogos.base`

**Arquivo na release:** `coral/jogos/base.py`

:::

#### `DependenciaJogosAusente`

Representa a condição de erro DependenciaJogosAusente.

:::details Detalhes técnicos

**Assinatura:** `DependenciaJogosAusente(...)`

**Origem da implementação:** `coral.jogos.base`

**Arquivo na release:** `coral/jogos/base.py`

:::

#### `ErroAssetCoral`

Representa a condição de erro ErroAssetCoral.

:::details Detalhes técnicos

**Assinatura:** `ErroAssetCoral(...)`

**Origem da implementação:** `coral.jogos.objetos`

**Arquivo na release:** `coral/jogos/objetos.py`

:::

### Constantes e aliases

#### `PRETO`

Expõe a constante pública `PRETO`.

:::details Detalhes técnicos

**Assinatura:** `PRETO`

**Origem da implementação:** `coral.jogos.base`

**Arquivo na release:** `coral/jogos/base.py`

**Valor declarado:** `Cor(0, 0, 0)`

:::

#### `BRANCO`

Expõe a constante pública `BRANCO`.

:::details Detalhes técnicos

**Assinatura:** `BRANCO`

**Origem da implementação:** `coral.jogos.base`

**Arquivo na release:** `coral/jogos/base.py`

**Valor declarado:** `Cor(255, 255, 255)`

:::

#### `VERMELHO`

Expõe a constante pública `VERMELHO`.

:::details Detalhes técnicos

**Assinatura:** `VERMELHO`

**Origem da implementação:** `coral.jogos.base`

**Arquivo na release:** `coral/jogos/base.py`

**Valor declarado:** `Cor(220, 50, 47)`

:::

#### `VERDE`

Expõe a constante pública `VERDE`.

:::details Detalhes técnicos

**Assinatura:** `VERDE`

**Origem da implementação:** `coral.jogos.base`

**Arquivo na release:** `coral/jogos/base.py`

**Valor declarado:** `Cor(46, 160, 67)`

:::

#### `AZUL`

Expõe a constante pública `AZUL`.

:::details Detalhes técnicos

**Assinatura:** `AZUL`

**Origem da implementação:** `coral.jogos.base`

**Arquivo na release:** `coral/jogos/base.py`

**Valor declarado:** `Cor(38, 139, 210)`

:::

#### `AMARELO`

Expõe a constante pública `AMARELO`.

:::details Detalhes técnicos

**Assinatura:** `AMARELO`

**Origem da implementação:** `coral.jogos.base`

**Arquivo na release:** `coral/jogos/base.py`

**Valor declarado:** `Cor(255, 215, 0)`

:::

#### `CONTRATO_OVERLAY_DEBUG`

Expõe a constante pública `CONTRATO_OVERLAY_DEBUG`.

:::details Detalhes técnicos

**Assinatura:** `CONTRATO_OVERLAY_DEBUG`

**Origem da implementação:** `coral.jogos.debug`

**Arquivo na release:** `coral/jogos/debug.py`

**Valor declarado:** `'coral.jogos.debug.overlay/1'`

:::

<!-- /AUTO:API -->

## Compatibilidade e dependências

O backend gráfico real é opcional. A camada headless continua disponível sem janela. Recursos visuais dependem do backend e do ambiente, enquanto mapas, regras e mundo permanecem independentes.
