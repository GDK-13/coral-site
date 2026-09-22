# coral.jogos

## Visão geral

`coral.jogos` é a camada de apresentação interativa da Coral. Ela reúne loop de jogo, entrada, desenho, sprites, cenas, animação, câmera, colisão e renderização de mapas sem obrigar o modelo de mundo a conhecer a biblioteca gráfica.

<!-- AUTO:MODULO -->

**Importação:** `coral.jogos`  
**Categoria:** jogos  

janela, desenho, sprites, animação, cenas, mapas e eventos de jogo

### Superfície pública detectada

`Jogo`, `Cor`, `Retangulo`, `BackendNulo`, `ErroJogosCoral`, `DependenciaJogosAusente`, `PRETO`, `BRANCO`, `VERMELHO`, `VERDE`, `AZUL`, `AMARELO`, `criar_jogo`, `pygame_disponivel`, `Assets`, `Sprite`, `Cena`, `RepresentacaoEntidade`, `ErroAssetCoral`, `Animacao`, `AnimacoesDirecionais`, `VinculoAnimacaoMovimento`, `EstadosAnimacao`, `VinculoEstadosAnimacaoMovimento`, `TransicoesEstadosAnimacao`, `VinculoTransicoesEstadosMovimento`, `VinculoTransicoesEventos`, `Camera`, `QuadroSprite`, `Spritesheet`, `carregar_spritesheet`, `FormaTransformada`, `formas_colidem`, `CanalAnimado`, `AnimacaoTransformacao`, `onda_seno`, `onda_cosseno`, `onda_triangular`, `onda_serra`, `onda_pulso`, `forma_espacial_sprite`, `posicao_espacial_sprite`, `sprites_colidem`, `AdaptadorEventosJogo`, `adaptar_eventos`, `Viewport`, `EstiloCelula`, `RenderizadorMapa2D`, `celula_para_tela`, `mundo_para_tela`, `tela_para_celula`, `tela_para_mundo`

<!-- /AUTO:MODULO -->

## Papel no ecossistema

O módulo deve apresentar e controlar interação. Estado persistente e semântica do domínio pertencem a `coral.mundo`, `coral.rpg` ou outro módulo. `RepresentacaoEntidade` existe justamente para ligar uma entidade a um `Sprite` sem acoplar os dois sistemas.

## Conceitos principais

### Jogo e backend

`Jogo` organiza ciclo de vida, atualização, desenho, entrada e eventos. `criar_jogo` é o helper funcional. `BackendNulo` executa a mesma camada de controle sem abrir janela e é o caminho preferido para testes automatizados.

### Sprites e cenas

`Sprite` reúne posição, dimensão, imagem, cor, velocidade, visibilidade e transformações. `Cena` agrupa sprites e callbacks de entrada, saída, atualização e desenho.

### Transformações

Sprites suportam escala, rotação, opacidade e espelhamento. Colisão pode acompanhar escala e rotação de maneira configurável, evitando que apresentação e hitbox precisem ser sempre idênticas.

### Animação

`Animacao`, `AnimacoesDirecionais`, `EstadosAnimacao` e transições de estado separam quadro visual, direção e estado. Canais animados permitem automatizar propriedades por ondas matemáticas.

### Câmera, viewport e mapas

`Camera` converte entre coordenadas de mundo e tela e também decide visibilidade para culling. `Viewport` separa a resolução lógica do tamanho físico da janela, incluindo redimensionamento e conversão de coordenadas. `RenderizadorMapa2D` consome mapas genéricos de `coral.mundo`, preservando a separação entre domínio e apresentação.

## Quando usar

Use para jogos 2D, protótipos interativos, visualizações e interfaces que precisam de entrada em tempo real. Se você só precisa modelar um mapa ou simulação sem janela, `coral.mundo` pode ser suficiente.

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

## Mapas, câmera e viewport

Trecho oficial de `Exemplos/Jogos/03_tilemap_e_camera.coral`:

```coral
de coral.jogos importe Camera, RenderizadorMapa2D, BackendNulo

crie um mapa chamado sala com topologia quadrada
adicione uma camada chamada terreno ao mapa sala
coloque o bloco "parede" na célula (1, 1) da camada terreno do mapa sala

defina camera como Camera(0, 0, 64, 64)
defina backend como BackendNulo()
defina renderizador como RenderizadorMapa2D(sala, camera=camera)
defina desenhadas como renderizador.desenhar(backend)
```

## API essencial

| Entrada | Papel | Assinatura |
|---|---|---|
| `Jogo` | loop e entrada | `Jogo(titulo: str, largura: int = 800, altura: int = 450, fps: int = 60, *, backend: BackendJogos, mundo = None, relogio: FonteTempo \| None = None, eventos: Eventos \| None = None, tela_cheia: bool = False)` |
| `criar_jogo` | criar jogo | `criar_jogo(titulo: str, largura: int = 800, altura: int = 450, fps: int = 60, *, backend = None, mundo = None, relogio = None, eventos = None, tela_cheia: bool = False) -> Jogo` |
| `BackendNulo` | backend headless | `BackendNulo(*, dt_fixo: float \| None = None)` |
| `Sprite` | objeto visual | `Sprite(x: float, y: float, largura: float, altura: float, imagem: str \| Path \| QuadroSprite \| None = None, cor: Cor = BRANCO, velocidade_x: float = 0.0, velocidade_y: float = 0.0, visivel: bool = True, nome: str = 'sprite', dados: dict[str, Any] = field(default_factory=dict), animacao: Any = None, escala: float = 1.0, rotacao: float = 0.0, espelhado_horizontalmente: bool = False, espelhado_verticalmente: bool = False, origem: str = 'topo_esquerdo', pivo: tuple[float, float] \| None = None, opacidade: float = 1.0, colisao_acompanha_escala: bool = False, colisao_acompanha_rotacao: bool = False)` |
| `Cena` | agrupar ciclo visual | `Cena(nome: str)` |
| `RepresentacaoEntidade` | ligar mundo a sprite | `RepresentacaoEntidade(entidade: Any, sprite: Sprite, atributo_x: str = 'x', atributo_y: str = 'y')` |
| `Animacao` | sequência de quadros | `Animacao(quadros: tuple[str \| Path \| QuadroSprite, ...], fps: float = 10.0, repetir: bool = True, finalizada: bool = False)` |
| `EstadosAnimacao` | estados visuais | `EstadosAnimacao(estados: dict[str, Animacao \| AnimacoesDirecionais])` |
| `Camera` | conversão mundo tela e culling | `Camera(x: float = 0.0, y: float = 0.0, largura: float = 800.0, altura: float = 450.0, alvo: Sprite \| None = None, suavidade: float = 1.0)` |
| `Viewport` | resolução lógica, área física e conversão de tela | `Viewport(largura_logica: float, altura_logica: float, largura_fisica: float, altura_fisica: float, *, modo: str = 'ajustar')` |
| `Spritesheet` | atlas de quadros | `Spritesheet(caminho: str \| Path, *, largura_imagem: int, altura_imagem: int) -> None` |
| `formas_colidem` | colisão convexa | `formas_colidem(a: FormaTransformada, b: FormaTransformada) -> bool` |
| `sprites_colidem` | colisão entre sprites | `sprites_colidem(a: Any, b: Any) -> bool` |
| `RenderizadorMapa2D` | renderizar mapa genérico | `RenderizadorMapa2D(mapa: Mapa, *, camadas: Iterable[str] \| None = None, camera: Camera \| None = None, resolvedor_estilo: ResolvedorEstiloMapa \| None = None, area_visivel: tuple[float, float, float, float] \| None = None) -> None` |

## Sprites, escala e colisão

`Sprite.definir_escala`, `aumentar`, `diminuir`, `definir_rotacao`, `girar` e os controles de espelhamento alteram a apresentação. `colisao_acompanha_escala` e `colisao_acompanha_rotacao` permitem decidir se a geometria de colisão acompanha a transformação.

## Automação matemática

`CanalAnimado` e `AnimacaoTransformacao` podem dirigir propriedades com seno, cosseno, onda triangular, serra ou pulso. Isso atende animações como flutuação, respiração, idle e movimentos repetitivos sem criar contadores manuais para cada propriedade.

## Estados e eventos

As classes de estados e transições permitem mapear eventos para animações. O vínculo com `Eventos` é opcional, então um sprite pode ser dirigido por movimento, por eventos de regras ou explicitamente pelo programa.

## Janela, tela cheia e redimensionamento

`Jogo` pode iniciar em tela cheia, alternar esse estado em execução e atualizar o tamanho físico quando a janela é redimensionada. O `Viewport` mantém as conversões entre coordenadas físicas e lógicas, evitando que a lógica do jogo dependa diretamente da resolução real da janela.

## Erros e diagnóstico

`DependenciaJogosAusente` representa ausência do backend gráfico real quando ele é necessário. `pygame_disponivel()` permite detectar a capacidade. Para lógica de jogo, prefira provar comportamento com `BackendNulo` antes de depender de uma janela real.

Assets inválidos usam `ErroAssetCoral`. Separar assets, sprites e domínio ajuda a localizar rapidamente se a falha está no arquivo, na transformação ou na lógica do mundo.

## Boas práticas

* Teste entrada e atualização com `BackendNulo`.
* Mantenha modelo de mundo fora do sprite.
* Use câmera para conversão de coordenadas em vez de subtrair offsets manualmente por toda a aplicação.
* Faça colisão acompanhar transformação apenas quando essa for a semântica desejada.
* Use estados e eventos em vez de uma cadeia grande de `se` para animação complexa.

## Integração com outros módulos

`coral.mundo` fornece mapas e entidades. `coral.regras` pode emitir eventos para transições visuais. `coral.rpg` fornece personagens. `coral.procedural` cuida de geração determinística e `coral.simulacao` pode evoluir o estado temporal sem depender da janela. `coral.laboratorio` pode medir algoritmos e visualizações sem misturar a medição ao loop.

## Testabilidade e ambientes

O backend nulo existe para execução determinística em testes, servidores e CI. Gates gráficos reais continuam necessários para validar janela, driver, renderização, áudio e entrada física.

## Referência da API

<!-- AUTO:API -->

### Funções

#### `criar_jogo`

Criar jogo.

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

### Classes e protocolos

#### `Jogo`

Representa loop e entrada.

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
| `desenhar_ponto` | Desenha ponto. | `None` |
| `desenhar_texto` | Desenha texto. | `None` |
| `desenhar_imagem` | Desenha imagem. | `None` |
| `tocar_som` | Executa som. | `None` |
| `mudar_cena` | Executa a operação `mudar_cena` disponibilizada por `coral.jogos`. | `None` |
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
| `desenhar_ponto` | método | `desenhar_ponto(x: float, y: float, cor: Cor = BRANCO, *, tamanho: int = 1, opacidade: float = 1.0) -> None` |
| `desenhar_texto` | método | `desenhar_texto(texto: str, x: float, y: float, tamanho: int = 24, cor: Cor = BRANCO, *, origem: str = 'topo_esquerdo', opacidade: float = 1.0) -> None` |
| `desenhar_imagem` | método | `desenhar_imagem(caminho: str \| QuadroSprite, x: float, y: float, largura: float \| None = None, altura: float \| None = None, *, escala: float = 1.0, rotacao: float = 0.0, espelhar_horizontalmente: bool = False, espelhar_verticalmente: bool = False, origem: str = 'topo_esquerdo', pivo: tuple[float, float] \| None = None, opacidade: float = 1.0) -> None` |
| `tocar_som` | método | `tocar_som(caminho: str, volume: float = 1.0) -> None` |
| `mudar_cena` | método | `mudar_cena(cena) -> None` |
| `executar` | método | `executar(*, max_quadros: int \| None = None) -> None` |

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
| `limpar` | Limpa o valor solicitado. | `None` |
| `desenhar_retangulo` | Desenha retangulo. | `None` |
| `desenhar_circulo` | Desenha circulo. | `None` |
| `desenhar_linha` | Desenha linha. | `None` |
| `desenhar_ponto` | Desenha ponto. | `None` |
| `desenhar_texto` | Desenha texto. | `None` |
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
| `limpar` | método | `limpar(cor: Cor) -> None` |
| `desenhar_retangulo` | método | `desenhar_retangulo(retangulo: Retangulo, cor: Cor, *, contorno: int = 0, opacidade: float = 1.0) -> None` |
| `desenhar_circulo` | método | `desenhar_circulo(x: float, y: float, raio: float, cor: Cor, *, contorno: int = 0, opacidade: float = 1.0) -> None` |
| `desenhar_linha` | método | `desenhar_linha(x1: float, y1: float, x2: float, y2: float, cor: Cor, *, espessura: int = 1, opacidade: float = 1.0) -> None` |
| `desenhar_ponto` | método | `desenhar_ponto(x: float, y: float, cor: Cor, *, tamanho: int = 1, opacidade: float = 1.0) -> None` |
| `desenhar_texto` | método | `desenhar_texto(texto: str, x: float, y: float, tamanho: int, cor: Cor, *, origem: str = 'topo_esquerdo', opacidade: float = 1.0) -> None` |
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

Representa objeto visual.

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
| `atualizar` | Atualiza o valor solicitado. | `None` |
| `colide_com` | Executa a operação `colide_com` disponibilizada por `coral.jogos`. | `bool` |

:::details Detalhes técnicos

**Assinatura:** `Sprite(x: float, y: float, largura: float, altura: float, imagem: str \| Path \| QuadroSprite \| None = None, cor: Cor = BRANCO, velocidade_x: float = 0.0, velocidade_y: float = 0.0, visivel: bool = True, nome: str = 'sprite', dados: dict[str, Any] = field(default_factory=dict), animacao: Any = None, escala: float = 1.0, rotacao: float = 0.0, espelhado_horizontalmente: bool = False, espelhado_verticalmente: bool = False, origem: str = 'topo_esquerdo', pivo: tuple[float, float] \| None = None, opacidade: float = 1.0, colisao_acompanha_escala: bool = False, colisao_acompanha_rotacao: bool = False)`

**Origem da implementação:** `coral.jogos.objetos`

**Arquivo na release:** `coral/jogos/objetos.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
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
| `atualizar` | método | `atualizar(dt: float) -> None` |
| `colide_com` | método | `colide_com(outro: 'Sprite') -> bool` |

:::

#### `Cena`

Representa Cena na API de `coral.jogos`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | obrigatório |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `representacoes` | Obtém representacoes. | `tuple[RepresentacaoEntidade, ...]` |
| `adicionar` | Adiciona o valor solicitado. | `Sprite` |
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
| `representacoes` | propriedade | `representacoes() -> tuple[RepresentacaoEntidade, ...]` |
| `adicionar` | método | `adicionar(sprite: Sprite) -> Sprite` |
| `representar` | método | `representar(entidade: Any, sprite: Sprite, *, atributo_x: str = 'x', atributo_y: str = 'y') -> RepresentacaoEntidade` |
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
| `sincronizar` | Sincroniza o valor solicitado. | `Sprite` |

:::details Detalhes técnicos

**Assinatura:** `RepresentacaoEntidade(entidade: Any, sprite: Sprite, atributo_x: str = 'x', atributo_y: str = 'y')`

**Origem da implementação:** `coral.jogos.objetos`

**Arquivo na release:** `coral/jogos/objetos.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `sincronizar` | método | `sincronizar() -> Sprite` |

:::

#### `Animacao`

Representa sequência de quadros.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `quadros` | Valor correspondente a quadros. | `tuple[str \| Path \| QuadroSprite, ...]` | obrigatório |
| `fps` | Quantidade alvo de quadros por segundo. | `float` | `10.0` |
| `repetir` | Valor correspondente a repetir. | `bool` | `True` |
| `finalizada` | Valor correspondente a finalizada. | `bool` | `False` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `quadros` | Valor correspondente a quadros. | `tuple[str \| Path \| QuadroSprite, ...]` | obrigatório |
| `fps` | Quantidade alvo de quadros por segundo. | `float` | `10.0` |
| `repetir` | Valor correspondente a repetir. | `bool` | `True` |
| `finalizada` | Valor correspondente a finalizada. | `bool` | `False` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `quadro_atual` | Obtém quadro atual. | `não declarado` |
| `reiniciar` | Reinicia o valor solicitado. | `não declarado` |
| `atualizar` | Atualiza o valor solicitado. | `não declarado` |

:::details Detalhes técnicos

**Assinatura:** `Animacao(quadros: tuple[str \| Path \| QuadroSprite, ...], fps: float = 10.0, repetir: bool = True, finalizada: bool = False)`

**Origem da implementação:** `coral.jogos.objetos`

**Arquivo na release:** `coral/jogos/objetos.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `quadro_atual` | propriedade | `quadro_atual()` |
| `reiniciar` | método | `reiniciar()` |
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
| `usar` | método | `usar(sprite: Sprite, direcao: str) -> Animacao` |
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

Agrupa estados visuais sem fixar quantidades de direções ou políticas de movimento.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `estados` | Valor correspondente a estados. | `dict[str, Animacao \| AnimacoesDirecionais]` | obrigatório |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `estados` | Obtém estados. | `tuple[str, ...]` |
| `para` | Executa a operação `para` disponibilizada por `coral.jogos`. | `Animacao \| AnimacoesDirecionais` |
| `ligar` | Liga o valor solicitado. | `VinculoEstadosAnimacaoMovimento` |
| `usar` | Seleciona o valor solicitado. | `Animacao` |

:::details Detalhes técnicos

**Assinatura:** `EstadosAnimacao(estados: dict[str, Animacao \| AnimacoesDirecionais])`

**Origem da implementação:** `coral.jogos.objetos`

**Arquivo na release:** `coral/jogos/objetos.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `estados` | propriedade | `estados() -> tuple[str, ...]` |
| `para` | método | `para(estado: str) -> Animacao \| AnimacoesDirecionais` |
| `ligar` | método | `ligar(movimento: MovimentoDirecional, sprite: Sprite) -> VinculoEstadosAnimacaoMovimento` |
| `usar` | método | `usar(sprite: Sprite, estado: str, *, direcao: str \| None = None) -> Animacao` |

:::

#### `VinculoEstadosAnimacaoMovimento`

Mantém estado visual e direção de movimento como dimensões independentes.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `grupo` | Valor correspondente a grupo. | `'EstadosAnimacao'` | obrigatório |
| `movimento` | Valor correspondente a movimento. | `MovimentoDirecional` | obrigatório |
| `sprite` | Valor correspondente a sprite. | `Sprite` | obrigatório |
| `estado_atual` | Valor correspondente a estado atual. | `str \| None` | `None` |
| `direcao_visual` | Valor correspondente a direcao visual. | `str \| None` | `None` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `grupo` | Valor correspondente a grupo. | `'EstadosAnimacao'` | obrigatório |
| `movimento` | Valor correspondente a movimento. | `MovimentoDirecional` | obrigatório |
| `sprite` | Valor correspondente a sprite. | `Sprite` | obrigatório |
| `estado_atual` | Valor correspondente a estado atual. | `str \| None` | `None` |
| `direcao_visual` | Valor correspondente a direcao visual. | `str \| None` | `None` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `usar` | Seleciona o valor solicitado. | `Animacao` |

:::details Detalhes técnicos

**Assinatura:** `VinculoEstadosAnimacaoMovimento(grupo: 'EstadosAnimacao', movimento: MovimentoDirecional, sprite: Sprite, estado_atual: str \| None = None, direcao_visual: str \| None = None)`

**Origem da implementação:** `coral.jogos.objetos`

**Arquivo na release:** `coral/jogos/objetos.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `usar` | método | `usar(estado: str, *, direcao: str \| None = None) -> Animacao` |

:::

#### `TransicoesEstadosAnimacao`

Mapeia eventos nomeados para estados visuais; automação de movimento é opcional.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `estados` | Valor correspondente a estados. | `EstadosAnimacao` | obrigatório |
| `transicoes` | Valor correspondente a transicoes. | `dict[str, str]` | obrigatório |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `eventos` | Obtém eventos. | `tuple[str, ...]` |
| `para` | Executa a operação `para` disponibilizada por `coral.jogos`. | `str` |
| `ligar` | Liga o valor solicitado. | `VinculoTransicoesEstadosMovimento` |
| `ligar_eventos` | Liga eventos. | `VinculoTransicoesEventos` |
| `acionar` | Aciona o valor solicitado. | `Animacao` |

:::details Detalhes técnicos

**Assinatura:** `TransicoesEstadosAnimacao(estados: EstadosAnimacao, transicoes: dict[str, str])`

**Origem da implementação:** `coral.jogos.objetos`

**Arquivo na release:** `coral/jogos/objetos.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `eventos` | propriedade | `eventos() -> tuple[str, ...]` |
| `para` | método | `para(evento: str) -> str` |
| `ligar` | método | `ligar(movimento: MovimentoDirecional, sprite: Sprite) -> VinculoTransicoesEstadosMovimento` |
| `ligar_eventos` | método | `ligar_eventos(eventos: Any, sprite: Sprite) -> VinculoTransicoesEventos` |
| `acionar` | método | `acionar(sprite: Sprite, evento: str) -> Animacao` |

:::

#### `VinculoTransicoesEstadosMovimento`

Aplica transições opt-in sem confundir mudança de direção com início de movimento.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `grupo` | Valor correspondente a grupo. | `'TransicoesEstadosAnimacao'` | obrigatório |
| `movimento` | Valor correspondente a movimento. | `MovimentoDirecional` | obrigatório |
| `sprite` | Valor correspondente a sprite. | `Sprite` | obrigatório |
| `vinculo_estados` | Valor correspondente a vinculo estados. | `VinculoEstadosAnimacaoMovimento` | obrigatório |
| `ultimo_evento` | Valor correspondente a ultimo evento. | `str \| None` | `None` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `grupo` | Valor correspondente a grupo. | `'TransicoesEstadosAnimacao'` | obrigatório |
| `movimento` | Valor correspondente a movimento. | `MovimentoDirecional` | obrigatório |
| `sprite` | Valor correspondente a sprite. | `Sprite` | obrigatório |
| `vinculo_estados` | Valor correspondente a vinculo estados. | `VinculoEstadosAnimacaoMovimento` | obrigatório |
| `ultimo_evento` | Valor correspondente a ultimo evento. | `str \| None` | `None` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `acionar` | Aciona o valor solicitado. | `Animacao` |

:::details Detalhes técnicos

**Assinatura:** `VinculoTransicoesEstadosMovimento(grupo: 'TransicoesEstadosAnimacao', movimento: MovimentoDirecional, sprite: Sprite, vinculo_estados: VinculoEstadosAnimacaoMovimento, ultimo_evento: str \| None = None)`

**Origem da implementação:** `coral.jogos.objetos`

**Arquivo na release:** `coral/jogos/objetos.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `acionar` | método | `acionar(evento: str) -> Animacao` |

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

#### `Camera`

Representa conversão mundo tela.

**Exemplo**

```coral
coloque o bloco "parede" na célula (1, 1) da camada terreno do mapa sala

defina camera como Camera(0, 0, 64, 64)
defina backend como BackendNulo()
defina renderizador como RenderizadorMapa2D(sala, camera=camera)
defina desenhadas como renderizador.desenhar(backend)
```

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `x` | Coordenada horizontal. | `float` | `0.0` |
| `y` | Coordenada vertical. | `float` | `0.0` |
| `largura` | Largura usada pela operação. | `float` | `800.0` |
| `altura` | Altura usada pela operação. | `float` | `450.0` |
| `alvo` | Valor correspondente a alvo. | `Sprite \| None` | `None` |
| `suavidade` | Valor correspondente a suavidade. | `float` | `1.0` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `x` | Coordenada horizontal. | `float` | `0.0` |
| `y` | Coordenada vertical. | `float` | `0.0` |
| `largura` | Largura usada pela operação. | `float` | `800.0` |
| `altura` | Altura usada pela operação. | `float` | `450.0` |
| `alvo` | Valor correspondente a alvo. | `Sprite \| None` | `None` |
| `suavidade` | Valor correspondente a suavidade. | `float` | `1.0` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `seguir` | Passa a seguir o valor solicitado. | `não declarado` |
| `atualizar` | Atualiza o valor solicitado. | `não declarado` |
| `mundo_para_tela` | Converte coordenadas de mundo para tela. | `tuple[float, float]` |
| `tela_para_mundo` | Converte coordenadas de tela para mundo. | `tuple[float, float]` |
| `area_visivel` | Executa a operação `area_visivel` disponibilizada por `coral.jogos`. | `Retangulo` |
| `visivel` | Executa a operação `visivel` disponibilizada por `coral.jogos`. | `bool` |
| `tela` | Compatibilidade histórica: converte coordenadas de mundo para tela. | `tuple[float, float]` |

:::details Detalhes técnicos

**Assinatura:** `Camera(x: float = 0.0, y: float = 0.0, largura: float = 800.0, altura: float = 450.0, alvo: Sprite \| None = None, suavidade: float = 1.0)`

**Origem da implementação:** `coral.jogos.objetos`

**Arquivo na release:** `coral/jogos/objetos.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `seguir` | método | `seguir(sprite: Sprite, suavidade: float = 1.0)` |
| `atualizar` | método | `atualizar()` |
| `mundo_para_tela` | método | `mundo_para_tela(x: float, y: float) -> tuple[float, float]` |
| `tela_para_mundo` | método | `tela_para_mundo(x: float, y: float) -> tuple[float, float]` |
| `area_visivel` | propriedade | `area_visivel() -> Retangulo` |
| `visivel` | método | `visivel(objeto: Sprite \| Retangulo, *, margem: float = 0.0) -> bool` |
| `tela` | método | `tela(x: float, y: float) -> tuple[float, float]` |

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

Representa RenderizadorMapa2D na API de `coral.jogos`.

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

<!-- /AUTO:API -->

## Compatibilidade e dependências

O backend gráfico real é opcional. A camada headless continua disponível sem janela. Recursos visuais dependem do backend e do ambiente, enquanto mapas, regras e mundo permanecem independentes.
