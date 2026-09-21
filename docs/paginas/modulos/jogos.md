# coral.jogos

## Visão geral

`coral.jogos` é a camada de apresentação interativa da Coral. Ela reúne loop de jogo, entrada, desenho, sprites, cenas, animação, câmera, colisão e renderização de mapas sem obrigar o modelo de mundo a conhecer a biblioteca gráfica.

<!-- AUTO:MODULO -->

**Importação:** `coral.jogos`  
**Categoria:** jogos  

janela, desenho, sprites, animação, cenas, mapas e eventos de jogo

### Superfície pública detectada

`Jogo`, `Cor`, `Retangulo`, `BackendNulo`, `ErroJogosCoral`, `DependenciaJogosAusente`, `PRETO`, `BRANCO`, `VERMELHO`, `VERDE`, `AZUL`, `AMARELO`, `criar_jogo`, `pygame_disponivel`, `Assets`, `Sprite`, `Cena`, `RepresentacaoEntidade`, `ErroAssetCoral`, `Animacao`, `AnimacoesDirecionais`, `VinculoAnimacaoMovimento`, `EstadosAnimacao`, `VinculoEstadosAnimacaoMovimento`, `TransicoesEstadosAnimacao`, `VinculoTransicoesEstadosMovimento`, `VinculoTransicoesEventos`, `Camera`, `QuadroSprite`, `Spritesheet`, `carregar_spritesheet`, `FormaTransformada`, `formas_colidem`, `CanalAnimado`, `AnimacaoTransformacao`, `onda_seno`, `onda_cosseno`, `onda_triangular`, `onda_serra`, `onda_pulso`, `forma_espacial_sprite`, `posicao_espacial_sprite`, `sprites_colidem`, `AdaptadorEventosJogo`, `adaptar_eventos`, `EstiloCelula`, `RenderizadorMapa2D`, `celula_para_tela`, `mundo_para_tela`, `tela_para_celula`, `tela_para_mundo`

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

### Câmera e mapas

`Camera` converte entre coordenadas de mundo e tela. `RenderizadorMapa2D` consome mapas genéricos de `coral.mundo`, preservando a separação entre domínio e apresentação.

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

## Mapas e câmera

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
| `Camera` | conversão mundo tela | `Camera(x: float = 0.0, y: float = 0.0, largura: float = 800.0, altura: float = 450.0, alvo: Sprite \| None = None, suavidade: float = 1.0)` |
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

`coral.mundo` fornece mapas e entidades. `coral.regras` pode emitir eventos para transições visuais. `coral.rpg` fornece personagens. `coral.aleatorio` ajuda em geração procedural. `coral.laboratorio` pode medir algoritmos e visualizações sem misturar a medição ao loop.

## Testabilidade e ambientes

O backend nulo existe para execução determinística em testes, servidores e CI. Gates gráficos reais continuam necessários para validar janela, driver, renderização, áudio e entrada física.

## Referência da API

<!-- AUTO:API -->

### Funções

#### `criar_jogo(titulo: str, largura: int = 800, altura: int = 450, fps: int = 60, *, backend = None, mundo = None, relogio = None, eventos = None, tela_cheia: bool = False) -> Jogo`

Entrada pública `criar_jogo` da superfície `coral.jogos`.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `titulo` | `str` | obrigatório | posicional |
| `largura` | `int` | `800` | posicional |
| `altura` | `int` | `450` | posicional |
| `fps` | `int` | `60` | posicional |
| `backend` | `não declarado` | `None` | nomeado |
| `mundo` | `não declarado` | `None` | nomeado |
| `relogio` | `não declarado` | `None` | nomeado |
| `eventos` | `não declarado` | `None` | nomeado |
| `tela_cheia` | `bool` | `False` | nomeado |

**Retorno:** `Jogo`

#### `pygame_disponivel() -> bool`

Entrada pública `pygame_disponivel` da superfície `coral.jogos`.

**Retorno:** `bool`

#### `carregar_spritesheet(caminho: str | Path, largura_imagem: int, altura_imagem: int, largura_quadro: int, altura_quadro: int, *, margem: int = 0, espacamento: int = 0) -> Spritesheet`

Atalho funcional para criar uma spritesheet em grade uniforme.

**Implementação:** `coral.jogos.spritesheet`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `caminho` | `str \| Path` | obrigatório | posicional |
| `largura_imagem` | `int` | obrigatório | posicional |
| `altura_imagem` | `int` | obrigatório | posicional |
| `largura_quadro` | `int` | obrigatório | posicional |
| `altura_quadro` | `int` | obrigatório | posicional |
| `margem` | `int` | `0` | nomeado |
| `espacamento` | `int` | `0` | nomeado |

**Retorno:** `Spritesheet`

#### `formas_colidem(a: FormaTransformada, b: FormaTransformada) -> bool`

Colisão convexa por SAT. Toque de borda não conta como colisão.

**Implementação:** `coral.jogos.transformacoes`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `a` | `FormaTransformada` | obrigatório | posicional |
| `b` | `FormaTransformada` | obrigatório | posicional |

**Retorno:** `bool`

#### `onda_seno(fase: float) -> float`

Entrada pública `onda_seno` da superfície `coral.jogos`.

**Implementação:** `coral.jogos.transformacoes`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `fase` | `float` | obrigatório | posicional |

**Retorno:** `float`

#### `onda_cosseno(fase: float) -> float`

Entrada pública `onda_cosseno` da superfície `coral.jogos`.

**Implementação:** `coral.jogos.transformacoes`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `fase` | `float` | obrigatório | posicional |

**Retorno:** `float`

#### `onda_triangular(fase: float) -> float`

Entrada pública `onda_triangular` da superfície `coral.jogos`.

**Implementação:** `coral.jogos.transformacoes`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `fase` | `float` | obrigatório | posicional |

**Retorno:** `float`

#### `onda_serra(fase: float) -> float`

Entrada pública `onda_serra` da superfície `coral.jogos`.

**Implementação:** `coral.jogos.transformacoes`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `fase` | `float` | obrigatório | posicional |

**Retorno:** `float`

#### `onda_pulso(fase: float) -> float`

Entrada pública `onda_pulso` da superfície `coral.jogos`.

**Implementação:** `coral.jogos.transformacoes`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `fase` | `float` | obrigatório | posicional |

**Retorno:** `float`

#### `forma_espacial_sprite(sprite: Any) -> Poligono`

Entrada pública `forma_espacial_sprite` da superfície `coral.jogos`.

**Implementação:** `coral.jogos.espacial`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `sprite` | `Any` | obrigatório | posicional |

**Retorno:** `Poligono`

**Exceções observáveis no corpo:** `TypeError`

#### `posicao_espacial_sprite(sprite: Any)`

Entrada pública `posicao_espacial_sprite` da superfície `coral.jogos`.

**Implementação:** `coral.jogos.espacial`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `sprite` | `Any` | obrigatório | posicional |

**Retorno:** `não declarado`

#### `sprites_colidem(a: Any, b: Any) -> bool`

Colisão 2D de Jogos usando sobreposição interior da baseline.

**Implementação:** `coral.jogos.espacial`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `a` | `Any` | obrigatório | posicional |
| `b` | `Any` | obrigatório | posicional |

**Retorno:** `bool`

#### `adaptar_eventos(jogo: Jogo, *, teclas: Iterable[str] = (), botoes_mouse: Iterable[str] = (), observar_mouse: bool = False) -> AdaptadorEventosJogo`

Entrada pública `adaptar_eventos` da superfície `coral.jogos`.

**Implementação:** `coral.jogos.eventos`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `jogo` | `Jogo` | obrigatório | posicional |
| `teclas` | `Iterable[str]` | `()` | nomeado |
| `botoes_mouse` | `Iterable[str]` | `()` | nomeado |
| `observar_mouse` | `bool` | `False` | nomeado |

**Retorno:** `AdaptadorEventosJogo`

#### `celula_para_tela(mapa: Mapa, camera: Camera | None, celula: Any, *, ancora: str = 'centro') -> tuple[float, float]`

Entrada pública `celula_para_tela` da superfície `coral.jogos`.

**Implementação:** `coral.jogos.mapas`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `mapa` | `Mapa` | obrigatório | posicional |
| `camera` | `Camera \| None` | obrigatório | posicional |
| `celula` | `Any` | obrigatório | posicional |
| `ancora` | `str` | `'centro'` | nomeado |

**Retorno:** `tuple[float, float]`

#### `mundo_para_tela(camera: Camera | None, coordenada: Any) -> tuple[float, float]`

Entrada pública `mundo_para_tela` da superfície `coral.jogos`.

**Implementação:** `coral.jogos.mapas`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `camera` | `Camera \| None` | obrigatório | posicional |
| `coordenada` | `Any` | obrigatório | posicional |

**Retorno:** `tuple[float, float]`

**Exceções observáveis no corpo:** `ErroMapaCoral`

#### `tela_para_celula(mapa: Mapa, camera: Camera | None, x: float, y: float)`

Entrada pública `tela_para_celula` da superfície `coral.jogos`.

**Implementação:** `coral.jogos.mapas`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `mapa` | `Mapa` | obrigatório | posicional |
| `camera` | `Camera \| None` | obrigatório | posicional |
| `x` | `float` | obrigatório | posicional |
| `y` | `float` | obrigatório | posicional |

**Retorno:** `não declarado`

#### `tela_para_mundo(camera: Camera | None, x: float, y: float)`

Entrada pública `tela_para_mundo` da superfície `coral.jogos`.

**Implementação:** `coral.jogos.mapas`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `camera` | `Camera \| None` | obrigatório | posicional |
| `x` | `float` | obrigatório | posicional |
| `y` | `float` | obrigatório | posicional |

**Retorno:** `não declarado`

**Exceções observáveis no corpo:** `ErroMapaCoral`

### Classes e protocolos

#### `Jogo(titulo: str, largura: int = 800, altura: int = 450, fps: int = 60, *, backend: BackendJogos, mundo = None, relogio: FonteTempo | None = None, eventos: Eventos | None = None, tela_cheia: bool = False)`

Entrada pública `Jogo` da superfície `coral.jogos`.

**Implementação:** `coral.jogos.base`

**Métodos e propriedades públicas**

| Nome | Tipo | Assinatura | Retorno | Descrição |
|---|---|---|---|---|
| `quando_iniciar` | método | `quando_iniciar(funcao: Callable[['Jogo'], Any])` | `não declarado` | Sem docstring própria na release. |
| `quando_atualizar` | método | `quando_atualizar(funcao: Callable[['Jogo', float], Any])` | `não declarado` | Sem docstring própria na release. |
| `quando_desenhar` | método | `quando_desenhar(funcao: Callable[['Jogo'], Any])` | `não declarado` | Sem docstring própria na release. |
| `quando_encerrar` | método | `quando_encerrar(funcao: Callable[['Jogo'], Any])` | `não declarado` | Sem docstring própria na release. |
| `parar` | método | `parar() -> None` | `None` | Sem docstring própria na release. |
| `remover_mundo` | método | `remover_mundo()` | `não declarado` | Desassocia o Mundo atual e remove somente a propagação criada pelo Jogo. |
| `usar_mundo` | método | `usar_mundo(mundo)` | `não declarado` | Associa um Mundo ao jogo e propaga eventos do Mundo para o Jogo. |
| `tecla_pressionada` | método | `tecla_pressionada(tecla: str) -> bool` | `bool` | Sem docstring própria na release. |
| `posicao_mouse` | método | `posicao_mouse() -> tuple[int, int]` | `tuple[int, int]` | Sem docstring própria na release. |
| `botao_mouse_pressionado` | método | `botao_mouse_pressionado(botao: str = 'esquerdo') -> bool` | `bool` | Sem docstring própria na release. |
| `mouse_clicado` | método | `mouse_clicado(botao: str = 'esquerdo') -> bool` | `bool` | Sem docstring própria na release. |
| `mouse_solto` | método | `mouse_solto(botao: str = 'esquerdo') -> bool` | `bool` | Sem docstring própria na release. |
| `roda_mouse` | método | `roda_mouse() -> tuple[int, int]` | `tuple[int, int]` | Sem docstring própria na release. |
| `em_tela_cheia` | método | `em_tela_cheia() -> bool` | `bool` | Sem docstring própria na release. |
| `definir_tela_cheia` | método | `definir_tela_cheia(ativa: bool) -> None` | `None` | Sem docstring própria na release. |
| `alternar_tela_cheia` | método | `alternar_tela_cheia() -> bool` | `bool` | Sem docstring própria na release. |
| `limpar` | método | `limpar(cor: Cor = PRETO) -> None` | `None` | Sem docstring própria na release. |
| `desenhar_retangulo` | método | `desenhar_retangulo(x: float, y: float, largura: float, altura: float, cor: Cor = BRANCO, *, contorno: int = 0, opacidade: float = 1.0) -> Retangulo` | `Retangulo` | Sem docstring própria na release. |
| `desenhar_circulo` | método | `desenhar_circulo(x: float, y: float, raio: float, cor: Cor = BRANCO, *, contorno: int = 0, opacidade: float = 1.0) -> None` | `None` | Sem docstring própria na release. |
| `desenhar_linha` | método | `desenhar_linha(x1: float, y1: float, x2: float, y2: float, cor: Cor = BRANCO, *, espessura: int = 1, opacidade: float = 1.0) -> None` | `None` | Sem docstring própria na release. |
| `desenhar_ponto` | método | `desenhar_ponto(x: float, y: float, cor: Cor = BRANCO, *, tamanho: int = 1, opacidade: float = 1.0) -> None` | `None` | Sem docstring própria na release. |
| `desenhar_texto` | método | `desenhar_texto(texto: str, x: float, y: float, tamanho: int = 24, cor: Cor = BRANCO, *, origem: str = 'topo_esquerdo', opacidade: float = 1.0) -> None` | `None` | Sem docstring própria na release. |
| `desenhar_imagem` | método | `desenhar_imagem(caminho: str \| QuadroSprite, x: float, y: float, largura: float \| None = None, altura: float \| None = None, *, escala: float = 1.0, rotacao: float = 0.0, espelhar_horizontalmente: bool = False, espelhar_verticalmente: bool = False, origem: str = 'topo_esquerdo', pivo: tuple[float, float] \| None = None, opacidade: float = 1.0) -> None` | `None` | Sem docstring própria na release. |
| `tocar_som` | método | `tocar_som(caminho: str, volume: float = 1.0) -> None` | `None` | Sem docstring própria na release. |
| `mudar_cena` | método | `mudar_cena(cena) -> None` | `None` | Sem docstring própria na release. |
| `executar` | método | `executar(*, max_quadros: int \| None = None) -> None` | `None` | Sem docstring própria na release. |

#### `Cor(vermelho: int, verde: int, azul: int, alfa: int = 255)`

Entrada pública `Cor` da superfície `coral.jogos`.

**Implementação:** `coral.jogos.base`

**Atributos declarados**

| Nome | Tipo | Padrão |
|---|---|---|
| `vermelho` | `int` | obrigatório |
| `verde` | `int` | obrigatório |
| `azul` | `int` | obrigatório |
| `alfa` | `int` | `255` |

**Métodos e propriedades públicas**

| Nome | Tipo | Assinatura | Retorno | Descrição |
|---|---|---|---|---|
| `rgb` | método | `rgb() -> tuple[int, int, int]` | `tuple[int, int, int]` | Sem docstring própria na release. |

#### `Retangulo(x: float, y: float, largura: float, altura: float)`

Entrada pública `Retangulo` da superfície `coral.jogos`.

**Implementação:** `coral.jogos.base`

**Atributos declarados**

| Nome | Tipo | Padrão |
|---|---|---|
| `x` | `float` | obrigatório |
| `y` | `float` | obrigatório |
| `largura` | `float` | obrigatório |
| `altura` | `float` | obrigatório |

**Métodos e propriedades públicas**

| Nome | Tipo | Assinatura | Retorno | Descrição |
|---|---|---|---|---|
| `colide_com` | método | `colide_com(outro: 'Retangulo') -> bool` | `bool` | Sem docstring própria na release. |

#### `BackendNulo(*, dt_fixo: float | None = None)`

Backend determinístico para testes, servidores e execução sem interface gráfica.

**Implementação:** `coral.jogos.base`

**Métodos e propriedades públicas**

| Nome | Tipo | Assinatura | Retorno | Descrição |
|---|---|---|---|---|
| `definir_teclas` | método | `definir_teclas(*teclas: str) -> None` | `None` | Substitui o estado atual de teclado do backend sem janela. |
| `programar_teclas` | método | `programar_teclas(*quadros) -> None` | `None` | Programa estados de teclado por quadro para testes determinísticos. |
| `definir_mouse` | método | `definir_mouse(*, posicao: tuple[int, int] = (0, 0), pressionados = (), clicados = (), soltos = (), roda: tuple[int, int] = (0, 0)) -> None` | `None` | Sem docstring própria na release. |
| `programar_mouse` | método | `programar_mouse(*quadros: dict[str, Any]) -> None` | `None` | Sem docstring própria na release. |
| `iniciar` | método | `iniciar(titulo: str, largura: int, altura: int, *, tela_cheia: bool = False) -> None` | `None` | Sem docstring própria na release. |
| `processar_eventos` | método | `processar_eventos() -> bool` | `bool` | Sem docstring própria na release. |
| `tecla_pressionada` | método | `tecla_pressionada(tecla: str) -> bool` | `bool` | Sem docstring própria na release. |
| `posicao_mouse` | método | `posicao_mouse() -> tuple[int, int]` | `tuple[int, int]` | Sem docstring própria na release. |
| `botao_mouse_pressionado` | método | `botao_mouse_pressionado(botao: str) -> bool` | `bool` | Sem docstring própria na release. |
| `mouse_clicado` | método | `mouse_clicado(botao: str) -> bool` | `bool` | Sem docstring própria na release. |
| `mouse_solto` | método | `mouse_solto(botao: str) -> bool` | `bool` | Sem docstring própria na release. |
| `roda_mouse` | método | `roda_mouse() -> tuple[int, int]` | `tuple[int, int]` | Sem docstring própria na release. |
| `definir_tela_cheia` | método | `definir_tela_cheia(ativa: bool) -> None` | `None` | Sem docstring própria na release. |
| `limpar` | método | `limpar(cor: Cor) -> None` | `None` | Sem docstring própria na release. |
| `desenhar_retangulo` | método | `desenhar_retangulo(retangulo: Retangulo, cor: Cor, *, contorno: int = 0, opacidade: float = 1.0) -> None` | `None` | Sem docstring própria na release. |
| `desenhar_circulo` | método | `desenhar_circulo(x: float, y: float, raio: float, cor: Cor, *, contorno: int = 0, opacidade: float = 1.0) -> None` | `None` | Sem docstring própria na release. |
| `desenhar_linha` | método | `desenhar_linha(x1: float, y1: float, x2: float, y2: float, cor: Cor, *, espessura: int = 1, opacidade: float = 1.0) -> None` | `None` | Sem docstring própria na release. |
| `desenhar_ponto` | método | `desenhar_ponto(x: float, y: float, cor: Cor, *, tamanho: int = 1, opacidade: float = 1.0) -> None` | `None` | Sem docstring própria na release. |
| `desenhar_texto` | método | `desenhar_texto(texto: str, x: float, y: float, tamanho: int, cor: Cor, *, origem: str = 'topo_esquerdo', opacidade: float = 1.0) -> None` | `None` | Sem docstring própria na release. |
| `desenhar_imagem` | método | `desenhar_imagem(caminho: str \| QuadroSprite, x: float, y: float, largura: float \| None = None, altura: float \| None = None, *, escala: float = 1.0, rotacao: float = 0.0, espelhar_horizontalmente: bool = False, espelhar_verticalmente: bool = False, origem: str = 'topo_esquerdo', pivo: tuple[float, float] \| None = None, opacidade: float = 1.0) -> None` | `None` | Sem docstring própria na release. |
| `apresentar` | método | `apresentar() -> None` | `None` | Sem docstring própria na release. |
| `tocar_som` | método | `tocar_som(caminho: str, *, volume: float = 1.0) -> None` | `None` | Sem docstring própria na release. |
| `limitar_fps` | método | `limitar_fps(fps: int) -> float` | `float` | Sem docstring própria na release. |
| `encerrar` | método | `encerrar() -> None` | `None` | Sem docstring própria na release. |

#### `Assets(raiz: str | Path = 'assets')`

Entrada pública `Assets` da superfície `coral.jogos`.

**Implementação:** `coral.jogos.objetos`

**Métodos e propriedades públicas**

| Nome | Tipo | Assinatura | Retorno | Descrição |
|---|---|---|---|---|
| `imagem` | método | `imagem(nome: str \| Path) -> Path` | `Path` | Sem docstring própria na release. |
| `som` | método | `som(nome: str \| Path) -> Path` | `Path` | Sem docstring própria na release. |
| `spritesheet` | método | `spritesheet(nome: str \| Path, *, largura_imagem: int, altura_imagem: int, largura_quadro: int, altura_quadro: int, margem: int = 0, espacamento: int = 0) -> Spritesheet` | `Spritesheet` | Sem docstring própria na release. |

#### `Sprite(x: float, y: float, largura: float, altura: float, imagem: str | Path | QuadroSprite | None = None, cor: Cor = BRANCO, velocidade_x: float = 0.0, velocidade_y: float = 0.0, visivel: bool = True, nome: str = 'sprite', dados: dict[str, Any] = field(default_factory=dict), animacao: Any = None, escala: float = 1.0, rotacao: float = 0.0, espelhado_horizontalmente: bool = False, espelhado_verticalmente: bool = False, origem: str = 'topo_esquerdo', pivo: tuple[float, float] | None = None, opacidade: float = 1.0, colisao_acompanha_escala: bool = False, colisao_acompanha_rotacao: bool = False)`

Entrada pública `Sprite` da superfície `coral.jogos`.

**Implementação:** `coral.jogos.objetos`

**Atributos declarados**

| Nome | Tipo | Padrão |
|---|---|---|
| `x` | `float` | obrigatório |
| `y` | `float` | obrigatório |
| `largura` | `float` | obrigatório |
| `altura` | `float` | obrigatório |
| `imagem` | `str \| Path \| QuadroSprite \| None` | `None` |
| `cor` | `Cor` | `BRANCO` |
| `velocidade_x` | `float` | `0.0` |
| `velocidade_y` | `float` | `0.0` |
| `visivel` | `bool` | `True` |
| `nome` | `str` | `'sprite'` |
| `dados` | `dict[str, Any]` | `field(default_factory=dict)` |
| `animacao` | `Any` | `None` |
| `escala` | `float` | `1.0` |
| `rotacao` | `float` | `0.0` |
| `espelhado_horizontalmente` | `bool` | `False` |
| `espelhado_verticalmente` | `bool` | `False` |
| `origem` | `str` | `'topo_esquerdo'` |
| `pivo` | `tuple[float, float] \| None` | `None` |
| `opacidade` | `float` | `1.0` |
| `colisao_acompanha_escala` | `bool` | `False` |
| `colisao_acompanha_rotacao` | `bool` | `False` |

**Métodos e propriedades públicas**

| Nome | Tipo | Assinatura | Retorno | Descrição |
|---|---|---|---|---|
| `retangulo` | propriedade | `retangulo() -> Retangulo` | `Retangulo` | Sem docstring própria na release. |
| `forma_colisao` | propriedade | `forma_colisao()` | `não declarado` | Sem docstring própria na release. |
| `mover` | método | `mover(dx: float, dy: float) -> None` | `None` | Sem docstring própria na release. |
| `definir_escala` | método | `definir_escala(escala: float)` | `não declarado` | Sem docstring própria na release. |
| `aumentar` | método | `aumentar(percentual: float)` | `não declarado` | Sem docstring própria na release. |
| `diminuir` | método | `diminuir(percentual: float)` | `não declarado` | Sem docstring própria na release. |
| `definir_rotacao` | método | `definir_rotacao(graus: float)` | `não declarado` | Sem docstring própria na release. |
| `girar` | método | `girar(graus: float)` | `não declarado` | Sem docstring própria na release. |
| `definir_opacidade` | método | `definir_opacidade(opacidade: float)` | `não declarado` | Sem docstring própria na release. |
| `alternar_espelhamento` | método | `alternar_espelhamento(eixo: str)` | `não declarado` | Sem docstring própria na release. |
| `remover_espelhamento` | método | `remover_espelhamento(eixo: str)` | `não declarado` | Sem docstring própria na release. |
| `restaurar_transformacoes` | método | `restaurar_transformacoes()` | `não declarado` | Sem docstring própria na release. |
| `configurar_colisao` | método | `configurar_colisao(*, acompanhar_escala: bool \| None = None, acompanhar_rotacao: bool \| None = None)` | `não declarado` | Sem docstring própria na release. |
| `manter_colisao_fixa` | método | `manter_colisao_fixa()` | `não declarado` | Sem docstring própria na release. |
| `animar_transformacoes` | método | `animar_transformacoes(**canais)` | `não declarado` | Sem docstring própria na release. |
| `pausar_automacao` | método | `pausar_automacao(automacao = None)` | `não declarado` | Sem docstring própria na release. |
| `retomar_automacao` | método | `retomar_automacao(automacao = None)` | `não declarado` | Sem docstring própria na release. |
| `reiniciar_automacao` | método | `reiniciar_automacao(automacao = None)` | `não declarado` | Sem docstring própria na release. |
| `remover_automacao` | método | `remover_automacao(automacao, *, restaurar_base: bool = False)` | `não declarado` | Sem docstring própria na release. |
| `atualizar` | método | `atualizar(dt: float) -> None` | `None` | Sem docstring própria na release. |
| `colide_com` | método | `colide_com(outro: 'Sprite') -> bool` | `bool` | Sem docstring própria na release. |

#### `Cena(nome: str)`

Entrada pública `Cena` da superfície `coral.jogos`.

**Implementação:** `coral.jogos.objetos`

**Métodos e propriedades públicas**

| Nome | Tipo | Assinatura | Retorno | Descrição |
|---|---|---|---|---|
| `representacoes` | propriedade | `representacoes() -> tuple[RepresentacaoEntidade, ...]` | `tuple[RepresentacaoEntidade, ...]` | Sem docstring própria na release. |
| `adicionar` | método | `adicionar(sprite: Sprite) -> Sprite` | `Sprite` | Sem docstring própria na release. |
| `representar` | método | `representar(entidade: Any, sprite: Sprite, *, atributo_x: str = 'x', atributo_y: str = 'y') -> RepresentacaoEntidade` | `RepresentacaoEntidade` | Sem docstring própria na release. |
| `remover` | método | `remover(sprite: Sprite) -> None` | `None` | Sem docstring própria na release. |
| `quando_entrar` | método | `quando_entrar(f)` | `não declarado` | Sem docstring própria na release. |
| `quando_sair` | método | `quando_sair(f)` | `não declarado` | Sem docstring própria na release. |
| `quando_atualizar` | método | `quando_atualizar(f)` | `não declarado` | Sem docstring própria na release. |
| `quando_desenhar` | método | `quando_desenhar(f)` | `não declarado` | Sem docstring própria na release. |
| `entrar` | método | `entrar(jogo)` | `não declarado` | Sem docstring própria na release. |
| `sair` | método | `sair(jogo)` | `não declarado` | Sem docstring própria na release. |
| `atualizar` | método | `atualizar(jogo, dt: float)` | `não declarado` | Sem docstring própria na release. |
| `desenhar` | método | `desenhar(jogo)` | `não declarado` | Sem docstring própria na release. |

#### `RepresentacaoEntidade(entidade: Any, sprite: Sprite, atributo_x: str = 'x', atributo_y: str = 'y')`

Liga uma entidade de mundo a um Sprite sem acoplar coral.mundo a jogos.

**Implementação:** `coral.jogos.objetos`

**Atributos declarados**

| Nome | Tipo | Padrão |
|---|---|---|
| `entidade` | `Any` | obrigatório |
| `sprite` | `Sprite` | obrigatório |
| `atributo_x` | `str` | `'x'` |
| `atributo_y` | `str` | `'y'` |

**Métodos e propriedades públicas**

| Nome | Tipo | Assinatura | Retorno | Descrição |
|---|---|---|---|---|
| `sincronizar` | método | `sincronizar() -> Sprite` | `Sprite` | Sem docstring própria na release. |

#### `Animacao(quadros: tuple[str | Path | QuadroSprite, ...], fps: float = 10.0, repetir: bool = True, finalizada: bool = False)`

Entrada pública `Animacao` da superfície `coral.jogos`.

**Implementação:** `coral.jogos.objetos`

**Atributos declarados**

| Nome | Tipo | Padrão |
|---|---|---|
| `quadros` | `tuple[str \| Path \| QuadroSprite, ...]` | obrigatório |
| `fps` | `float` | `10.0` |
| `repetir` | `bool` | `True` |
| `finalizada` | `bool` | `False` |

**Métodos e propriedades públicas**

| Nome | Tipo | Assinatura | Retorno | Descrição |
|---|---|---|---|---|
| `quadro_atual` | propriedade | `quadro_atual()` | `não declarado` | Sem docstring própria na release. |
| `reiniciar` | método | `reiniciar()` | `não declarado` | Sem docstring própria na release. |
| `atualizar` | método | `atualizar(dt: float)` | `não declarado` | Sem docstring própria na release. |

#### `AnimacoesDirecionais(animacoes: dict[str, Animacao])`

Conjunto nomeado de animações para direções de movimento.

**Implementação:** `coral.jogos.objetos`

**Atributos declarados**

| Nome | Tipo | Padrão |
|---|---|---|
| `animacoes` | `dict[str, Animacao]` | obrigatório |

**Métodos e propriedades públicas**

| Nome | Tipo | Assinatura | Retorno | Descrição |
|---|---|---|---|---|
| `direcoes` | propriedade | `direcoes() -> tuple[str, ...]` | `tuple[str, ...]` | Sem docstring própria na release. |
| `para` | método | `para(direcao: str) -> Animacao` | `Animacao` | Sem docstring própria na release. |
| `usar` | método | `usar(sprite: Sprite, direcao: str) -> Animacao` | `Animacao` | Sem docstring própria na release. |
| `ligar` | método | `ligar(movimento: MovimentoDirecional, sprite: Sprite) -> VinculoAnimacaoMovimento` | `VinculoAnimacaoMovimento` | Sem docstring própria na release. |

#### `VinculoAnimacaoMovimento(grupo: 'AnimacoesDirecionais', movimento: MovimentoDirecional, sprite: Sprite, direcoes_compativeis: tuple[str, ...], direcao_visual: str | None = None)`

Entrada pública `VinculoAnimacaoMovimento` da superfície `coral.jogos`.

**Implementação:** `coral.jogos.objetos`

**Atributos declarados**

| Nome | Tipo | Padrão |
|---|---|---|
| `grupo` | `'AnimacoesDirecionais'` | obrigatório |
| `movimento` | `MovimentoDirecional` | obrigatório |
| `sprite` | `Sprite` | obrigatório |
| `direcoes_compativeis` | `tuple[str, ...]` | obrigatório |
| `direcao_visual` | `str \| None` | `None` |

#### `EstadosAnimacao(estados: dict[str, Animacao | AnimacoesDirecionais])`

Agrupa estados visuais sem fixar quantidades de direções ou políticas de movimento.

**Implementação:** `coral.jogos.objetos`

**Métodos e propriedades públicas**

| Nome | Tipo | Assinatura | Retorno | Descrição |
|---|---|---|---|---|
| `estados` | propriedade | `estados() -> tuple[str, ...]` | `tuple[str, ...]` | Sem docstring própria na release. |
| `para` | método | `para(estado: str) -> Animacao \| AnimacoesDirecionais` | `Animacao \| AnimacoesDirecionais` | Sem docstring própria na release. |
| `ligar` | método | `ligar(movimento: MovimentoDirecional, sprite: Sprite) -> VinculoEstadosAnimacaoMovimento` | `VinculoEstadosAnimacaoMovimento` | Sem docstring própria na release. |
| `usar` | método | `usar(sprite: Sprite, estado: str, *, direcao: str \| None = None) -> Animacao` | `Animacao` | Sem docstring própria na release. |

#### `VinculoEstadosAnimacaoMovimento(grupo: 'EstadosAnimacao', movimento: MovimentoDirecional, sprite: Sprite, estado_atual: str | None = None, direcao_visual: str | None = None)`

Mantém estado visual e direção de movimento como dimensões independentes.

**Implementação:** `coral.jogos.objetos`

**Atributos declarados**

| Nome | Tipo | Padrão |
|---|---|---|
| `grupo` | `'EstadosAnimacao'` | obrigatório |
| `movimento` | `MovimentoDirecional` | obrigatório |
| `sprite` | `Sprite` | obrigatório |
| `estado_atual` | `str \| None` | `None` |
| `direcao_visual` | `str \| None` | `None` |

**Métodos e propriedades públicas**

| Nome | Tipo | Assinatura | Retorno | Descrição |
|---|---|---|---|---|
| `usar` | método | `usar(estado: str, *, direcao: str \| None = None) -> Animacao` | `Animacao` | Sem docstring própria na release. |

#### `TransicoesEstadosAnimacao(estados: EstadosAnimacao, transicoes: dict[str, str])`

Mapeia eventos nomeados para estados visuais; automação de movimento é opcional.

**Implementação:** `coral.jogos.objetos`

**Métodos e propriedades públicas**

| Nome | Tipo | Assinatura | Retorno | Descrição |
|---|---|---|---|---|
| `eventos` | propriedade | `eventos() -> tuple[str, ...]` | `tuple[str, ...]` | Sem docstring própria na release. |
| `para` | método | `para(evento: str) -> str` | `str` | Sem docstring própria na release. |
| `ligar` | método | `ligar(movimento: MovimentoDirecional, sprite: Sprite) -> VinculoTransicoesEstadosMovimento` | `VinculoTransicoesEstadosMovimento` | Sem docstring própria na release. |
| `ligar_eventos` | método | `ligar_eventos(eventos: Any, sprite: Sprite) -> VinculoTransicoesEventos` | `VinculoTransicoesEventos` | Sem docstring própria na release. |
| `acionar` | método | `acionar(sprite: Sprite, evento: str) -> Animacao` | `Animacao` | Sem docstring própria na release. |

#### `VinculoTransicoesEstadosMovimento(grupo: 'TransicoesEstadosAnimacao', movimento: MovimentoDirecional, sprite: Sprite, vinculo_estados: VinculoEstadosAnimacaoMovimento, ultimo_evento: str | None = None)`

Aplica transições opt-in sem confundir mudança de direção com início de movimento.

**Implementação:** `coral.jogos.objetos`

**Atributos declarados**

| Nome | Tipo | Padrão |
|---|---|---|
| `grupo` | `'TransicoesEstadosAnimacao'` | obrigatório |
| `movimento` | `MovimentoDirecional` | obrigatório |
| `sprite` | `Sprite` | obrigatório |
| `vinculo_estados` | `VinculoEstadosAnimacaoMovimento` | obrigatório |
| `ultimo_evento` | `str \| None` | `None` |

**Métodos e propriedades públicas**

| Nome | Tipo | Assinatura | Retorno | Descrição |
|---|---|---|---|---|
| `acionar` | método | `acionar(evento: str) -> Animacao` | `Animacao` | Sem docstring própria na release. |

#### `VinculoTransicoesEventos(grupo: 'TransicoesEstadosAnimacao', eventos: Any, sprite: Sprite, vinculo_movimento: VinculoTransicoesEstadosMovimento, ativo: bool = field(default=True, init=False))`

Escuta um barramento genérico e encaminha eventos declarados para transições visuais.

**Implementação:** `coral.jogos.objetos`

**Atributos declarados**

| Nome | Tipo | Padrão |
|---|---|---|
| `grupo` | `'TransicoesEstadosAnimacao'` | obrigatório |
| `eventos` | `Any` | obrigatório |
| `sprite` | `Sprite` | obrigatório |
| `vinculo_movimento` | `VinculoTransicoesEstadosMovimento` | obrigatório |
| `ativo` | `bool` | `field(default=True, init=False)` |

**Métodos e propriedades públicas**

| Nome | Tipo | Assinatura | Retorno | Descrição |
|---|---|---|---|---|
| `desligar` | método | `desligar() -> None` | `None` | Sem docstring própria na release. |

#### `Camera(x: float = 0.0, y: float = 0.0, largura: float = 800.0, altura: float = 450.0, alvo: Sprite | None = None, suavidade: float = 1.0)`

Entrada pública `Camera` da superfície `coral.jogos`.

**Implementação:** `coral.jogos.objetos`

**Atributos declarados**

| Nome | Tipo | Padrão |
|---|---|---|
| `x` | `float` | `0.0` |
| `y` | `float` | `0.0` |
| `largura` | `float` | `800.0` |
| `altura` | `float` | `450.0` |
| `alvo` | `Sprite \| None` | `None` |
| `suavidade` | `float` | `1.0` |

**Métodos e propriedades públicas**

| Nome | Tipo | Assinatura | Retorno | Descrição |
|---|---|---|---|---|
| `seguir` | método | `seguir(sprite: Sprite, suavidade: float = 1.0)` | `não declarado` | Sem docstring própria na release. |
| `atualizar` | método | `atualizar()` | `não declarado` | Sem docstring própria na release. |
| `mundo_para_tela` | método | `mundo_para_tela(x: float, y: float) -> tuple[float, float]` | `tuple[float, float]` | Sem docstring própria na release. |
| `tela_para_mundo` | método | `tela_para_mundo(x: float, y: float) -> tuple[float, float]` | `tuple[float, float]` | Sem docstring própria na release. |
| `tela` | método | `tela(x: float, y: float) -> tuple[float, float]` | `tuple[float, float]` | Compatibilidade histórica: converte coordenadas de mundo para tela. |

#### `QuadroSprite(caminho: Path, x: int, y: int, largura: int, altura: int, indice: int | None = None, linha: int | None = None, coluna: int | None = None, nome: str | None = None)`

Região imutável de uma imagem usada como quadro de sprite.

**Implementação:** `coral.jogos.spritesheet`

**Atributos declarados**

| Nome | Tipo | Padrão |
|---|---|---|
| `caminho` | `Path` | obrigatório |
| `x` | `int` | obrigatório |
| `y` | `int` | obrigatório |
| `largura` | `int` | obrigatório |
| `altura` | `int` | obrigatório |
| `indice` | `int \| None` | `None` |
| `linha` | `int \| None` | `None` |
| `coluna` | `int \| None` | `None` |
| `nome` | `str \| None` | `None` |

**Métodos e propriedades públicas**

| Nome | Tipo | Assinatura | Retorno | Descrição |
|---|---|---|---|---|
| `retangulo` | propriedade | `retangulo() -> tuple[int, int, int, int]` | `tuple[int, int, int, int]` | Sem docstring própria na release. |

#### `Spritesheet(caminho: str | Path, *, largura_imagem: int, altura_imagem: int) -> None`

Descrição headless de uma spritesheet ou atlas de imagens.

**Implementação:** `coral.jogos.spritesheet`

**Métodos e propriedades públicas**

| Nome | Tipo | Assinatura | Retorno | Descrição |
|---|---|---|---|---|
| `em_grade` | método | `em_grade(caminho: str \| Path, *, largura_imagem: int, altura_imagem: int, largura_quadro: int, altura_quadro: int, margem: int = 0, espacamento: int = 0) -> 'Spritesheet'` | `'Spritesheet'` | Sem docstring própria na release. |
| `quadro` | método | `quadro(indice: int) -> QuadroSprite` | `QuadroSprite` | Sem docstring própria na release. |
| `quadro_em` | método | `quadro_em(linha: int, coluna: int) -> QuadroSprite` | `QuadroSprite` | Sem docstring própria na release. |
| `quadros_de` | método | `quadros_de(inicio: int, fim: int) -> tuple[QuadroSprite, ...]` | `tuple[QuadroSprite, ...]` | Sem docstring própria na release. |
| `quadros_da_linha` | método | `quadros_da_linha(linha: int, coluna_inicial: int = 0, coluna_final: int \| None = None) -> tuple[QuadroSprite, ...]` | `tuple[QuadroSprite, ...]` | Sem docstring própria na release. |
| `animacao_da_linha` | método | `animacao_da_linha(linha: int, coluna_inicial: int = 0, coluna_final: int \| None = None, *, fps: float = 10.0, repetir: bool = True)` | `não declarado` | Sem docstring própria na release. |
| `animacao` | método | `animacao(inicio: int, fim: int, *, fps: float = 10.0, repetir: bool = True)` | `não declarado` | Cria uma Animacao usando um intervalo inclusivo de quadros. |
| `animacoes_direcionais` | método | `animacoes_direcionais(linhas: dict[str, int], coluna_inicial: int = 0, coluna_final: int \| None = None, *, fps: float = 10.0, repetir: bool = True)` | `não declarado` | Cria um grupo de animações a partir de linhas nomeadas da grade. |
| `regiao` | método | `regiao(x: int, y: int, largura: int, altura: int, *, nome: str \| None = None) -> QuadroSprite` | `QuadroSprite` | Sem docstring própria na release. |

#### `FormaTransformada(vertices: tuple[tuple[float, float], ...])`

Entrada pública `FormaTransformada` da superfície `coral.jogos`.

**Implementação:** `coral.jogos.transformacoes`

**Atributos declarados**

| Nome | Tipo | Padrão |
|---|---|---|
| `vertices` | `tuple[tuple[float, float], ...]` | obrigatório |

**Métodos e propriedades públicas**

| Nome | Tipo | Assinatura | Retorno | Descrição |
|---|---|---|---|---|
| `limites` | propriedade | `limites() -> tuple[float, float, float, float]` | `tuple[float, float, float, float]` | Sem docstring própria na release. |

#### `CanalAnimado(canal: str, base: float, amplitude: float, frequencia: float, fase: float = 0.0, modo: str = 'absoluto', onda: str | Callable[[float], float] = 'seno')`

Entrada pública `CanalAnimado` da superfície `coral.jogos`.

**Implementação:** `coral.jogos.transformacoes`

**Atributos declarados**

| Nome | Tipo | Padrão |
|---|---|---|
| `canal` | `str` | obrigatório |
| `base` | `float` | obrigatório |
| `amplitude` | `float` | obrigatório |
| `frequencia` | `float` | obrigatório |
| `fase` | `float` | `0.0` |
| `modo` | `str` | `'absoluto'` |
| `onda` | `str \| Callable[[float], float]` | `'seno'` |

**Métodos e propriedades públicas**

| Nome | Tipo | Assinatura | Retorno | Descrição |
|---|---|---|---|---|
| `valor` | método | `valor(tempo: float, *, referencia: float = 0.0) -> float` | `float` | Sem docstring própria na release. |

#### `AnimacaoTransformacao(canais: tuple[CanalAnimado, ...], tempo: float = 0.0, estado: str = 'ativo')`

Entrada pública `AnimacaoTransformacao` da superfície `coral.jogos`.

**Implementação:** `coral.jogos.transformacoes`

**Atributos declarados**

| Nome | Tipo | Padrão |
|---|---|---|
| `canais` | `tuple[CanalAnimado, ...]` | obrigatório |
| `tempo` | `float` | `0.0` |
| `estado` | `str` | `'ativo'` |

**Métodos e propriedades públicas**

| Nome | Tipo | Assinatura | Retorno | Descrição |
|---|---|---|---|---|
| `pausar` | método | `pausar() -> None` | `None` | Sem docstring própria na release. |
| `retomar` | método | `retomar() -> None` | `None` | Sem docstring própria na release. |
| `reiniciar` | método | `reiniciar() -> None` | `None` | Sem docstring própria na release. |
| `encerrar` | método | `encerrar() -> None` | `None` | Sem docstring própria na release. |
| `avancar` | método | `avancar(dt: float) -> None` | `None` | Sem docstring própria na release. |

#### `AdaptadorEventosJogo(jogo: Jogo, *, teclas: Iterable[str] = (), botoes_mouse: Iterable[str] = (), observar_mouse: bool = False)`

Publica acontecimentos de Jogos no barramento reativo do próprio Jogo.

**Implementação:** `coral.jogos.eventos`

**Métodos e propriedades públicas**

| Nome | Tipo | Assinatura | Retorno | Descrição |
|---|---|---|---|---|
| `ativo` | propriedade | `ativo() -> bool` | `bool` | Sem docstring própria na release. |
| `desligar` | método | `desligar() -> None` | `None` | Sem docstring própria na release. |
| `ligar` | método | `ligar() -> None` | `None` | Sem docstring própria na release. |
| `observar_colisao` | método | `observar_colisao(primeiro: Sprite, segundo: Sprite, *, nome: str \| None = None) -> _ColisaoObservada` | `_ColisaoObservada` | Sem docstring própria na release. |
| `publicar_transicao_visual` | método | `publicar_transicao_visual(sprite: Sprite, transicao: str, *, estado: str \| None = None)` | `não declarado` | Sem docstring própria na release. |

#### `EstiloCelula(cor: Cor | None = None, imagem: str | QuadroSprite | None = None, texto: str | None = None, cor_texto: Cor = BRANCO, tamanho_texto: int = 16, contorno: int = 0, opacidade: float = 1.0)`

Entrada pública `EstiloCelula` da superfície `coral.jogos`.

**Implementação:** `coral.jogos.mapas`

**Atributos declarados**

| Nome | Tipo | Padrão |
|---|---|---|
| `cor` | `Cor \| None` | `None` |
| `imagem` | `str \| QuadroSprite \| None` | `None` |
| `texto` | `str \| None` | `None` |
| `cor_texto` | `Cor` | `BRANCO` |
| `tamanho_texto` | `int` | `16` |
| `contorno` | `int` | `0` |
| `opacidade` | `float` | `1.0` |

#### `RenderizadorMapa2D(mapa: Mapa, *, camadas: Iterable[str] | None = None, camera: Camera | None = None, resolvedor_estilo: ResolvedorEstiloMapa | None = None, area_visivel: tuple[float, float, float, float] | None = None) -> None`

Entrada pública `RenderizadorMapa2D` da superfície `coral.jogos`.

**Implementação:** `coral.jogos.mapas`

**Métodos e propriedades públicas**

| Nome | Tipo | Assinatura | Retorno | Descrição |
|---|---|---|---|---|
| `camadas` | propriedade | `camadas() -> tuple[CamadaMapa, ...]` | `tuple[CamadaMapa, ...]` | Sem docstring própria na release. |
| `celulas_visiveis` | método | `celulas_visiveis() -> tuple[Any, ...]` | `tuple[Any, ...]` | Sem docstring própria na release. |
| `desenhar` | método | `desenhar(backend: BackendJogos) -> int` | `int` | Sem docstring própria na release. |

### Exceções

#### `ErroJogosCoral(...)`

Entrada pública `ErroJogosCoral` da superfície `coral.jogos`.

**Implementação:** `coral.jogos.base`

#### `DependenciaJogosAusente(...)`

Entrada pública `DependenciaJogosAusente` da superfície `coral.jogos`.

**Implementação:** `coral.jogos.base`

#### `ErroAssetCoral(...)`

Entrada pública `ErroAssetCoral` da superfície `coral.jogos`.

**Implementação:** `coral.jogos.objetos`

### Constantes e aliases

#### `PRETO`

Constante pública do módulo.

**Implementação:** `coral.jogos.base`

**Valor declarado:** `Cor(0, 0, 0)`

#### `BRANCO`

Constante pública do módulo.

**Implementação:** `coral.jogos.base`

**Valor declarado:** `Cor(255, 255, 255)`

#### `VERMELHO`

Constante pública do módulo.

**Implementação:** `coral.jogos.base`

**Valor declarado:** `Cor(220, 50, 47)`

#### `VERDE`

Constante pública do módulo.

**Implementação:** `coral.jogos.base`

**Valor declarado:** `Cor(46, 160, 67)`

#### `AZUL`

Constante pública do módulo.

**Implementação:** `coral.jogos.base`

**Valor declarado:** `Cor(38, 139, 210)`

#### `AMARELO`

Constante pública do módulo.

**Implementação:** `coral.jogos.base`

**Valor declarado:** `Cor(255, 215, 0)`

<!-- /AUTO:API -->

## Compatibilidade e dependências

O backend gráfico real é opcional. A camada headless continua disponível sem janela. Recursos visuais dependem do backend e do ambiente, enquanto mapas, regras e mundo permanecem independentes.
