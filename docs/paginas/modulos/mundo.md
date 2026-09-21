# coral.mundo

## Visão geral

`coral.mundo` é o modelo de domínio compartilhado para mundos, entidades, relações, mapas, regiões e topologias. Ele foi desenhado para servir jogos, RPGs e simulações sem depender de renderização.

<!-- AUTO:MODULO -->

**Importação:** `coral.mundo`  
**Categoria:** mundo  

mundos, entidades, relações, mapas, regiões e topologias

### Superfície pública detectada

`Mundo`, `Entidade`, `Relacao`, `criar_mundo`, `Mapa`, `CamadaMapa`, `ConteudoCelula`, `BlocoMapa`, `MudancaMapa`, `RegiaoMapa`, `ResultadoPassagem`, `ObservadorRegiaoMapa`, `CelulaQuadrada`, `CelulaHexagonal`, `CelulaVoxel`, `TopologiaQuadrada`, `TopologiaHexagonal`, `TopologiaVoxel`, `ErroMapaCoral`

<!-- /AUTO:MODULO -->

## Papel no ecossistema

`coral.mundo` guarda o que existe e como as coisas se relacionam. `coral.jogos` decide como apresentar. `coral.rpg` acrescenta mecânicas de RPG. `coral.regras` reage ao estado.

```text
coral.mundo  ── estado e espaço
    │
    ├── coral.rpg    ── personagens e combate
    ├── coral.regras ── reação e eventos
    └── coral.jogos  ── apresentação e interação
```

## Conceitos principais

### Mundo, entidades e relações

`Mundo` mantém entidades e relações. `Entidade` carrega atributos, tags e inventário. `Relacao` conecta duas entidades com um tipo e dados adicionais. O mundo pode procurar caminhos entre entidades relacionadas.

### Mapas e camadas

`Mapa` é uma estrutura espacial discreta independente de visualização. `CamadaMapa` permite separar terreno, objetos, temperatura, umidade ou qualquer outra dimensão do domínio.

### Topologias

A release oferece células e topologias quadrada, hexagonal e voxel. Isso permite representar tabuleiros, mapas hexagonais e volumes sem criar APIs separadas para cada caso de uso.

### Regiões e travessia

`RegiaoMapa` representa conjuntos de células ou formas. `ResultadoPassagem` descreve se uma travessia é permitida, seu custo e as camadas responsáveis.

## Quando usar

Use quando várias partes do programa precisam compartilhar entidades, relações ou espaço. Se o estado só existe para desenhar um efeito temporário, ele provavelmente pertence a `coral.jogos`, não ao mundo.

## Começando com mundo e RPG

Este exemplo é oficial da release:

```coral
crie um mundo chamado campanha com nome "Campanha"
crie uma entidade chamada vila no mundo campanha
crie uma entidade chamada bosque no mundo campanha
relacione vila com bosque como "estrada" no mundo campanha
encontre um caminho de bosque até vila no mundo campanha como rota

crie um personagem chamado heroina no mundo campanha com 12 de vida
crie um personagem chamado monstro no mundo campanha com 6 de vida
```

## Trabalhando com mapas

Outro exemplo oficial mostra que o mesmo modelo atende topologias diferentes:

```coral
crie um mapa chamado clima com topologia quadrada
adicione uma camada chamada temperatura ao mapa clima
defina 31.5 na célula (4, 2) da camada temperatura do mapa clima

crie um mapa chamado colmeia com topologia hexagonal
adicione uma camada chamada recurso ao mapa colmeia
defina "mel" na célula (2, menos 1) da camada recurso do mapa colmeia
```

## API essencial

| Entrada | Papel | Assinatura |
|---|---|---|
| `Mundo` | agregado do domínio | `Mundo(nome: str = 'mundo', *, relogio: FonteTempo \| None = None, eventos: Eventos \| None = None)` |
| `Entidade` | objeto do mundo | `Entidade(nome: str, atributos: dict[str, Any] = field(default_factory=dict), tags: set[str] = field(default_factory=set), inventario: list[Any] = field(default_factory=list))` |
| `Relacao` | ligação entre entidades | `Relacao(origem: Entidade, destino: Entidade, tipo: str, dados: dict[str, Any] = field(default_factory=dict, compare=False))` |
| `criar_mundo` | criar mundo via API | `criar_mundo(nome: str = 'mundo') -> Mundo` |
| `Mapa` | estrutura espacial | `Mapa(nome: str, topologia: Any, *, propriedades: Mapping[str, Any] \| None = None, eventos: Eventos \| None = None) -> None` |
| `CamadaMapa` | camada esparsa | `CamadaMapa(nome: str, *, ordem: int = 0, propriedades: Mapping[str, Any] \| None = None, participa_travessia: bool = True, _sequencia: int = 0) -> None` |
| `ConteudoCelula` | valor de célula | `ConteudoCelula(valor: Any, propriedades: Mapping[str, Any] \| None = None, *, travessia: bool \| None = None, custo: float \| int \| None = None, motivo: str \| None = None) -> None` |
| `RegiaoMapa` | região espacial | `RegiaoMapa(mapa: Any, nome: str, *, celulas: Iterable[object] \| None = None, forma: Any = None, referencia: str = 'centro', propriedades: Mapping[str, Any] \| None = None) -> None` |
| `ResultadoPassagem` | resultado de travessia | `ResultadoPassagem(permitida: bool, custo: float, motivo: str \| None, camadas_responsaveis: tuple[str, ...], origem: CelulaMapa, destino: CelulaMapa)` |
| `TopologiaQuadrada` | topologia 2D quadrada | `TopologiaQuadrada(largura_celula: float = 1.0, altura_celula: float = 1.0, origem: tuple[float, float] = (0.0, 0.0), limites_configurados: object = field(default=None, repr=False, compare=False))` |
| `TopologiaHexagonal` | topologia 2D hexagonal | `TopologiaHexagonal(tamanho_celula: float = 1.0, orientacao: str = 'topo_plano', origem: tuple[float, float] = (0.0, 0.0), limites_configurados: object = field(default=None, repr=False, compare=False))` |
| `TopologiaVoxel` | topologia 3D | `TopologiaVoxel(tamanho_x: float = 1.0, tamanho_y: float = 1.0, tamanho_z: float = 1.0, origem: tuple[float, float, float] = (0.0, 0.0, 0.0), limites_configurados: object = field(default=None, repr=False, compare=False))` |

## Fluxos comuns

### Grafo de entidades

Crie entidades, relacione as que realmente têm conexão no domínio e consulte caminhos quando a navegação semântica for necessária. Não use relação como substituto de qualquer atributo simples.

### Mundo espacial

Crie um mapa, escolha topologia, adicione camadas e só depois preencha conteúdo. Camadas diferentes podem participar de travessia e custo de maneiras distintas.

### Apresentação

Mantenha coordenadas e estado no mundo e use `RepresentacaoEntidade` ou renderizadores de `coral.jogos` para apresentar. Assim o mundo continua testável sem janela.

## Erros e invariantes

Nomes duplicados, relações que referenciam entidades externas ao mundo e operações incompatíveis com o mapa devem ser rejeitados. Métodos com semântica de exigência devem sinalizar ausência em vez de retornar silenciosamente um valor falso.

## Boas práticas

* Dê nomes estáveis a entidades e mapas que precisam ser persistidos.
* Separe camadas de mapa por responsabilidade.
* Não coloque cor, sprite ou efeito visual dentro do domínio só porque o programa é um jogo.
* Use eventos ou regras para integração reativa em vez de acoplamento circular entre módulos.

## Integração com outros módulos

`coral.rpg` especializa entidades. `coral.jogos` apresenta mapas e entidades. `coral.regras` observa e reage. `coral.persistencia` salva estruturas registradas pelo domínio.

## Testabilidade

O modelo de mundo é independente de Pygame e pode ser exercitado headless. Prefira testar caminhos, travessia, relações e regiões diretamente antes de adicionar apresentação.

## Referência da API

<!-- AUTO:API -->

### Funções

#### `criar_mundo(nome: str = 'mundo') -> Mundo`

Entrada pública `criar_mundo` da superfície `coral.mundo`.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `nome` | `str` | `'mundo'` | posicional |

**Retorno:** `Mundo`

### Classes e protocolos

#### `Mundo(nome: str = 'mundo', *, relogio: FonteTempo | None = None, eventos: Eventos | None = None)`

Mundo leve para jogos, RPGs e simulações Coral.

**Métodos e propriedades públicas**

| Nome | Tipo | Assinatura | Retorno | Descrição |
|---|---|---|---|---|
| `entidades` | propriedade | `entidades() -> tuple[Entidade, ...]` | `tuple[Entidade, ...]` | Sem docstring própria na release. |
| `relacoes` | propriedade | `relacoes() -> tuple[Relacao, ...]` | `tuple[Relacao, ...]` | Sem docstring própria na release. |
| `mapas` | propriedade | `mapas() -> tuple[Mapa, ...]` | `tuple[Mapa, ...]` | Sem docstring própria na release. |
| `adicionar_mapa` | método | `adicionar_mapa(mapa: Mapa) -> Mapa` | `Mapa` | Sem docstring própria na release. |
| `criar_mapa` | método | `criar_mapa(nome: str, topologia, *, propriedades: dict[str, Any] \| None = None) -> Mapa` | `Mapa` | Sem docstring própria na release. |
| `buscar_mapa` | método | `buscar_mapa(nome: str) -> Mapa \| None` | `Mapa \| None` | Sem docstring própria na release. |
| `exigir_mapa` | método | `exigir_mapa(nome: str) -> Mapa` | `Mapa` | Sem docstring própria na release. |
| `remover_mapa` | método | `remover_mapa(mapa: Mapa \| str) -> bool` | `bool` | Sem docstring própria na release. |
| `observar_regioes_mapa` | método | `observar_regioes_mapa(nome: str, alvo: Any, mapa: Mapa \| str, regioes, resolvedor, *, identificador_alvo: Any = None) -> ObservadorRegiaoMapa` | `ObservadorRegiaoMapa` | Sem docstring própria na release. |
| `adicionar` | método | `adicionar(entidade: Entidade) -> Entidade` | `Entidade` | Sem docstring própria na release. |
| `criar_entidade` | método | `criar_entidade(nome: str, **atributos: Any) -> Entidade` | `Entidade` | Sem docstring própria na release. |
| `buscar` | método | `buscar(nome: str) -> Entidade \| None` | `Entidade \| None` | Sem docstring própria na release. |
| `exigir` | método | `exigir(nome: str) -> Entidade` | `Entidade` | Sem docstring própria na release. |
| `remover` | método | `remover(entidade: Entidade \| str) -> bool` | `bool` | Sem docstring própria na release. |
| `relacionar` | método | `relacionar(origem: Entidade \| str, destino: Entidade \| str, tipo: str, **dados: Any) -> Relacao` | `Relacao` | Sem docstring própria na release. |
| `remover_relacao` | método | `remover_relacao(relacao: Relacao) -> bool` | `bool` | Sem docstring própria na release. |
| `relacionados` | método | `relacionados(entidade: Entidade \| str, tipo: str \| None = None, *, direcao: str = 'saida') -> tuple[Entidade, ...]` | `tuple[Entidade, ...]` | Sem docstring própria na release. |
| `caminho` | método | `caminho(origem: Entidade \| str, destino: Entidade \| str, *, tipo: str \| None = None, bidirecional: bool = True) -> tuple[Entidade, ...]` | `tuple[Entidade, ...]` | Sem docstring própria na release. |
| `com_tag` | método | `com_tag(tag: str) -> tuple[Entidade, ...]` | `tuple[Entidade, ...]` | Sem docstring própria na release. |
| `atualizar` | método | `atualizar(dt: float = 0.0) -> tuple[str, ...]` | `tuple[str, ...]` | Sem docstring própria na release. |
| `atualizar_por_relogio` | método | `atualizar_por_relogio() -> tuple[str, ...]` | `tuple[str, ...]` | Sem docstring própria na release. |
| `emitir` | método | `emitir(evento: str, *args, **kwargs) -> int` | `int` | Sem docstring própria na release. |
| `emitir_evento` | método | `emitir_evento(evento: str, *args, cancelavel: bool = False, metadados: dict[str, Any] \| None = None, **kwargs)` | `não declarado` | Sem docstring própria na release. |
| `enfileirar_evento` | método | `enfileirar_evento(evento: str, *args, **kwargs)` | `não declarado` | Sem docstring própria na release. |
| `processar_eventos` | método | `processar_eventos(limite: int \| None = None)` | `não declarado` | Sem docstring própria na release. |
| `emitir_propagado` | método | `emitir_propagado(evento: str, *args, **kwargs) -> int` | `int` | Sem docstring própria na release. |
| `emitir_evento_propagado` | método | `emitir_evento_propagado(evento: str, *args, cancelavel: bool = False, metadados: dict[str, Any] \| None = None, **kwargs)` | `não declarado` | Sem docstring própria na release. |
| `para_dict` | método | `para_dict() -> dict[str, Any]` | `dict[str, Any]` | Sem docstring própria na release. |
| `para_json` | método | `para_json(**kwargs) -> str` | `str` | Sem docstring própria na release. |

#### `Entidade(nome: str, atributos: dict[str, Any] = field(default_factory=dict), tags: set[str] = field(default_factory=set), inventario: list[Any] = field(default_factory=list))`

Entrada pública `Entidade` da superfície `coral.mundo`.

**Atributos declarados**

| Nome | Tipo | Padrão |
|---|---|---|
| `nome` | `str` | obrigatório |
| `atributos` | `dict[str, Any]` | `field(default_factory=dict)` |
| `tags` | `set[str]` | `field(default_factory=set)` |
| `inventario` | `list[Any]` | `field(default_factory=list)` |

**Métodos e propriedades públicas**

| Nome | Tipo | Assinatura | Retorno | Descrição |
|---|---|---|---|---|
| `definir` | método | `definir(nome: str, valor: Any) -> 'Entidade'` | `'Entidade'` | Sem docstring própria na release. |
| `obter` | método | `obter(nome: str, padrao: Any = None) -> Any` | `Any` | Sem docstring própria na release. |
| `adicionar_tag` | método | `adicionar_tag(tag: str) -> 'Entidade'` | `'Entidade'` | Sem docstring própria na release. |
| `remover_tag` | método | `remover_tag(tag: str) -> None` | `None` | Sem docstring própria na release. |
| `possui_tag` | método | `possui_tag(tag: str) -> bool` | `bool` | Sem docstring própria na release. |
| `guardar` | método | `guardar(item: Any) -> Any` | `Any` | Sem docstring própria na release. |
| `remover_item` | método | `remover_item(item: Any) -> bool` | `bool` | Sem docstring própria na release. |

#### `Relacao(origem: Entidade, destino: Entidade, tipo: str, dados: dict[str, Any] = field(default_factory=dict, compare=False))`

Entrada pública `Relacao` da superfície `coral.mundo`.

**Atributos declarados**

| Nome | Tipo | Padrão |
|---|---|---|
| `origem` | `Entidade` | obrigatório |
| `destino` | `Entidade` | obrigatório |
| `tipo` | `str` | obrigatório |
| `dados` | `dict[str, Any]` | `field(default_factory=dict, compare=False)` |

#### `Mapa(nome: str, topologia: Any, *, propriedades: Mapping[str, Any] | None = None, eventos: Eventos | None = None) -> None`

Estrutura espacial discreta genérica, independente de visualização.

**Implementação:** `coral._mapas.modelo`

**Métodos e propriedades públicas**

| Nome | Tipo | Assinatura | Retorno | Descrição |
|---|---|---|---|---|
| `eventos` | propriedade | `eventos() -> Eventos \| None` | `Eventos \| None` | Barramento associado, sem criar runtime oculto quando ausente. |
| `propriedades` | propriedade | `propriedades() -> Mapping[str, Any]` | `Mapping[str, Any]` | Sem docstring própria na release. |
| `camadas` | propriedade | `camadas() -> tuple[CamadaMapa, ...]` | `tuple[CamadaMapa, ...]` | Sem docstring própria na release. |
| `regioes` | propriedade | `regioes() -> tuple[Any, ...]` | `tuple[Any, ...]` | Sem docstring própria na release. |
| `adicionar_camada` | método | `adicionar_camada(nome: str, *, ordem: int \| None = None, propriedades: Mapping[str, Any] \| None = None, participa_travessia: bool = True) -> CamadaMapa` | `CamadaMapa` | Sem docstring própria na release. |
| `buscar_camada` | método | `buscar_camada(nome: str) -> CamadaMapa \| None` | `CamadaMapa \| None` | Sem docstring própria na release. |
| `exigir_camada` | método | `exigir_camada(nome: str) -> CamadaMapa` | `CamadaMapa` | Sem docstring própria na release. |
| `remover_camada` | método | `remover_camada(nome: str) -> bool` | `bool` | Sem docstring própria na release. |
| `adicionar_regiao` | método | `adicionar_regiao(regiao: Any) -> Any` | `Any` | Sem docstring própria na release. |
| `criar_regiao` | método | `criar_regiao(nome: str, *, celulas: Iterable[object] \| None = None, forma: Any = None, referencia: str = 'centro', propriedades: Mapping[str, Any] \| None = None) -> Any` | `Any` | Sem docstring própria na release. |
| `buscar_regiao` | método | `buscar_regiao(nome: str) -> Any \| None` | `Any \| None` | Sem docstring própria na release. |
| `exigir_regiao` | método | `exigir_regiao(nome: str) -> Any` | `Any` | Sem docstring própria na release. |
| `remover_regiao` | método | `remover_regiao(nome: str) -> bool` | `bool` | Sem docstring própria na release. |
| `regioes_em` | método | `regioes_em(celula_ou_posicao: object) -> tuple[Any, ...]` | `tuple[Any, ...]` | Sem docstring própria na release. |
| `celulas_da_regiao` | método | `celulas_da_regiao(nome: str, *, limites: object = None) -> tuple[CelulaMapa, ...]` | `tuple[CelulaMapa, ...]` | Sem docstring própria na release. |
| `possui_valor` | método | `possui_valor(camada: str, celula: object) -> bool` | `bool` | Sem docstring própria na release. |
| `conteudo_em` | método | `conteudo_em(camada: str, celula: object) -> ConteudoCelula \| None` | `ConteudoCelula \| None` | Sem docstring própria na release. |
| `obter` | método | `obter(camada: str, celula: object, padrao: Any = None) -> Any` | `Any` | Sem docstring própria na release. |
| `definir` | método | `definir(camada: str, celula: object, valor: Any, *, propriedades: Mapping[str, Any] \| None = None, travessia: bool \| None = None, custo: float \| int \| None = None, motivo: str \| None = None, causa: Any = None) -> MudancaMapa` | `MudancaMapa` | Sem docstring própria na release. |
| `remover` | método | `remover(camada: str, celula: object, *, causa: Any = None) -> MudancaMapa \| None` | `MudancaMapa \| None` | Sem docstring própria na release. |
| `definir_travessia` | método | `definir_travessia(camada: str, celula: object, *, permitida: bool \| None = None, custo: float \| int \| None = None, motivo: str \| None = None, causa: Any = None) -> MudancaMapa` | `MudancaMapa` | Sem docstring própria na release. |
| `bloquear_travessia` | método | `bloquear_travessia(camada: str, celula: object, *, motivo: str \| None = None, causa: Any = None) -> MudancaMapa` | `MudancaMapa` | Sem docstring própria na release. |
| `permitir_travessia` | método | `permitir_travessia(camada: str, celula: object, *, custo: float \| int \| None = None, motivo: str \| None = None, causa: Any = None) -> MudancaMapa` | `MudancaMapa` | Sem docstring própria na release. |
| `avaliar_travessia` | método | `avaliar_travessia(origem: object, destino: object) -> ResultadoPassagem` | `ResultadoPassagem` | Sem docstring própria na release. |
| `tentar_travessia` | método | `tentar_travessia(origem: object, destino: object, *, causa: Any = None) -> ResultadoPassagem` | `ResultadoPassagem` | Avalia uma tentativa e publica bloqueio apenas quando a ação é explícita. |
| `contexto_em` | método | `contexto_em(celula: object, *, origem: object \| None = None) -> ContextoLocalMapa` | `ContextoLocalMapa` | Sem docstring própria na release. |
| `vizinhos` | método | `vizinhos(celula: object, **opcoes: Any) -> tuple[CelulaMapa, ...]` | `tuple[CelulaMapa, ...]` | Sem docstring própria na release. |
| `aplicar_lote` | método | `aplicar_lote(operacoes: Iterable[Mapping[str, Any]]) -> tuple[MudancaMapa, ...]` | `tuple[MudancaMapa, ...]` | Valida todo o lote antes de aplicar qualquer escrita. |

#### `CamadaMapa(nome: str, *, ordem: int = 0, propriedades: Mapping[str, Any] | None = None, participa_travessia: bool = True, _sequencia: int = 0) -> None`

Camada nomeada, ordenada e esparsa de um mapa.

**Implementação:** `coral._mapas.modelo`

**Métodos e propriedades públicas**

| Nome | Tipo | Assinatura | Retorno | Descrição |
|---|---|---|---|---|
| `propriedades` | propriedade | `propriedades() -> Mapping[str, Any]` | `Mapping[str, Any]` | Sem docstring própria na release. |
| `quantidade` | propriedade | `quantidade() -> int` | `int` | Sem docstring própria na release. |
| `celulas` | propriedade | `celulas() -> tuple[CelulaMapa, ...]` | `tuple[CelulaMapa, ...]` | Sem docstring própria na release. |
| `possui` | método | `possui(celula: CelulaMapa) -> bool` | `bool` | Sem docstring própria na release. |
| `conteudo` | método | `conteudo(celula: CelulaMapa) -> ConteudoCelula \| None` | `ConteudoCelula \| None` | Sem docstring própria na release. |

#### `ConteudoCelula(valor: Any, propriedades: Mapping[str, Any] | None = None, *, travessia: bool | None = None, custo: float | int | None = None, motivo: str | None = None) -> None`

Valor imutável associado a uma célula, com travessia opcional.

**Implementação:** `coral._mapas.modelo`

**Atributos declarados**

| Nome | Tipo | Padrão |
|---|---|---|
| `travessia_permitida` | `bool \| None` | obrigatório |
| `custo_travessia` | `float \| None` | obrigatório |
| `motivo_travessia` | `str \| None` | obrigatório |

**Métodos e propriedades públicas**

| Nome | Tipo | Assinatura | Retorno | Descrição |
|---|---|---|---|---|
| `valor` | propriedade | `valor() -> Any` | `Any` | Sem docstring própria na release. |
| `propriedades` | propriedade | `propriedades() -> Mapping[str, Any]` | `Mapping[str, Any]` | Sem docstring própria na release. |
| `declarou_travessia` | propriedade | `declarou_travessia() -> bool` | `bool` | Sem docstring própria na release. |
| `com_valor` | método | `com_valor(valor: Any) -> 'ConteudoCelula'` | `'ConteudoCelula'` | Sem docstring própria na release. |
| `com_propriedades` | método | `com_propriedades(propriedades: Mapping[str, Any]) -> 'ConteudoCelula'` | `'ConteudoCelula'` | Sem docstring própria na release. |
| `com_travessia` | método | `com_travessia(*, permitida: bool \| None = None, custo: float \| int \| None = None, motivo: str \| None = None) -> 'ConteudoCelula'` | `'ConteudoCelula'` | Sem docstring própria na release. |

#### `BlocoMapa(identificador: str, propriedades: Mapping[str, Any] | None = None) -> None`

Conveniência para terreno, material, obstáculo ou tile.

**Implementação:** `coral._mapas.modelo`

**Atributos declarados**

| Nome | Tipo | Padrão |
|---|---|---|
| `identificador` | `str` | obrigatório |

**Métodos e propriedades públicas**

| Nome | Tipo | Assinatura | Retorno | Descrição |
|---|---|---|---|---|
| `propriedades` | propriedade | `propriedades() -> Mapping[str, Any]` | `Mapping[str, Any]` | Sem docstring própria na release. |

#### `MudancaMapa(mapa: str, camada: str, celula: CelulaMapa, operacao: str, anterior: ConteudoCelula | None, novo: ConteudoCelula | None, causa: Any = None, aplicada: bool = True, cancelada: bool = False, motivo_cancelamento: str | None = None, evento_sequencia: int | None = None)`

Entrada pública `MudancaMapa` da superfície `coral.mundo`.

**Implementação:** `coral._mapas.modelo`

**Atributos declarados**

| Nome | Tipo | Padrão |
|---|---|---|
| `mapa` | `str` | obrigatório |
| `camada` | `str` | obrigatório |
| `celula` | `CelulaMapa` | obrigatório |
| `operacao` | `str` | obrigatório |
| `anterior` | `ConteudoCelula \| None` | obrigatório |
| `novo` | `ConteudoCelula \| None` | obrigatório |
| `causa` | `Any` | `None` |
| `aplicada` | `bool` | `True` |
| `cancelada` | `bool` | `False` |
| `motivo_cancelamento` | `str \| None` | `None` |
| `evento_sequencia` | `int \| None` | `None` |

#### `RegiaoMapa(mapa: Any, nome: str, *, celulas: Iterable[object] | None = None, forma: Any = None, referencia: str = 'centro', propriedades: Mapping[str, Any] | None = None) -> None`

Região por conjunto de células ou por forma espacial oficial.

**Implementação:** `coral._mapas.regioes`

**Métodos e propriedades públicas**

| Nome | Tipo | Assinatura | Retorno | Descrição |
|---|---|---|---|---|
| `tipo` | propriedade | `tipo() -> str` | `str` | Sem docstring própria na release. |
| `forma` | propriedade | `forma() -> Any` | `Any` | Sem docstring própria na release. |
| `propriedades` | propriedade | `propriedades() -> Mapping[str, Any]` | `Mapping[str, Any]` | Sem docstring própria na release. |
| `celulas_explicitas` | propriedade | `celulas_explicitas() -> tuple[CelulaMapa, ...]` | `tuple[CelulaMapa, ...]` | Sem docstring própria na release. |
| `contem` | método | `contem(celula_ou_posicao: object) -> bool` | `bool` | Sem docstring própria na release. |
| `celulas` | método | `celulas(*, limites: object = None) -> tuple[CelulaMapa, ...]` | `tuple[CelulaMapa, ...]` | Sem docstring própria na release. |

#### `ResultadoPassagem(permitida: bool, custo: float, motivo: str | None, camadas_responsaveis: tuple[str, ...], origem: CelulaMapa, destino: CelulaMapa)`

Entrada pública `ResultadoPassagem` da superfície `coral.mundo`.

**Implementação:** `coral._mapas.modelo`

**Atributos declarados**

| Nome | Tipo | Padrão |
|---|---|---|
| `permitida` | `bool` | obrigatório |
| `custo` | `float` | obrigatório |
| `motivo` | `str \| None` | obrigatório |
| `camadas_responsaveis` | `tuple[str, ...]` | obrigatório |
| `origem` | `CelulaMapa` | obrigatório |
| `destino` | `CelulaMapa` | obrigatório |

#### `ObservadorRegiaoMapa(nome: str, alvo: Any, mapa: Mapa, regioes: Iterable[RegiaoMapa | str], resolvedor: ResolvedorLocalizacao, eventos: Eventos, *, identificador_alvo: Any = None) -> None`

Reconhece transições de entrada e saída entre avaliações sucessivas.

**Implementação:** `coral._mapas.observacao`

**Atributos declarados**

| Nome | Tipo | Padrão |
|---|---|---|
| `nome` | `str` | obrigatório |
| `alvo` | `Any` | obrigatório |
| `mapa` | `Mapa` | obrigatório |
| `regioes` | `tuple[RegiaoMapa, ...]` | obrigatório |
| `resolvedor` | `ResolvedorLocalizacao` | obrigatório |
| `eventos` | `Eventos` | obrigatório |
| `identificador_alvo` | `Any` | `None` |

**Métodos e propriedades públicas**

| Nome | Tipo | Assinatura | Retorno | Descrição |
|---|---|---|---|---|
| `regioes_anteriores` | propriedade | `regioes_anteriores() -> tuple[str, ...]` | `tuple[str, ...]` | Sem docstring própria na release. |
| `avaliar` | método | `avaliar(contexto: Any) -> bool` | `bool` | Sem docstring própria na release. |

#### `CelulaQuadrada(coluna: int, linha: int)`

Entrada pública `CelulaQuadrada` da superfície `coral.mundo`.

**Implementação:** `coral._mapas.modelo`

**Atributos declarados**

| Nome | Tipo | Padrão |
|---|---|---|
| `coluna` | `int` | obrigatório |
| `linha` | `int` | obrigatório |

**Métodos e propriedades públicas**

| Nome | Tipo | Assinatura | Retorno | Descrição |
|---|---|---|---|---|
| `como_tupla` | método | `como_tupla() -> tuple[int, int]` | `tuple[int, int]` | Sem docstring própria na release. |

#### `CelulaHexagonal(q: int, r: int)`

Entrada pública `CelulaHexagonal` da superfície `coral.mundo`.

**Implementação:** `coral._mapas.modelo`

**Atributos declarados**

| Nome | Tipo | Padrão |
|---|---|---|
| `q` | `int` | obrigatório |
| `r` | `int` | obrigatório |

**Métodos e propriedades públicas**

| Nome | Tipo | Assinatura | Retorno | Descrição |
|---|---|---|---|---|
| `como_tupla` | método | `como_tupla() -> tuple[int, int]` | `tuple[int, int]` | Sem docstring própria na release. |

#### `CelulaVoxel(x: int, y: int, z: int)`

Entrada pública `CelulaVoxel` da superfície `coral.mundo`.

**Implementação:** `coral._mapas.modelo`

**Atributos declarados**

| Nome | Tipo | Padrão |
|---|---|---|
| `x` | `int` | obrigatório |
| `y` | `int` | obrigatório |
| `z` | `int` | obrigatório |

**Métodos e propriedades públicas**

| Nome | Tipo | Assinatura | Retorno | Descrição |
|---|---|---|---|---|
| `como_tupla` | método | `como_tupla() -> tuple[int, int, int]` | `tuple[int, int, int]` | Sem docstring própria na release. |

#### `TopologiaQuadrada(largura_celula: float = 1.0, altura_celula: float = 1.0, origem: tuple[float, float] = (0.0, 0.0), limites_configurados: object = field(default=None, repr=False, compare=False))`

Entrada pública `TopologiaQuadrada` da superfície `coral.mundo`.

**Implementação:** `coral._mapas.topologias`

**Atributos declarados**

| Nome | Tipo | Padrão |
|---|---|---|
| `largura_celula` | `float` | `1.0` |
| `altura_celula` | `float` | `1.0` |
| `origem` | `tuple[float, float]` | `(0.0, 0.0)` |
| `limites_configurados` | `object` | `field(default=None, repr=False, compare=False)` |

**Métodos e propriedades públicas**

| Nome | Tipo | Assinatura | Retorno | Descrição |
|---|---|---|---|---|
| `vizinhos` | método | `vizinhos(celula: object, *, incluir_diagonais: bool = False) -> tuple[CelulaQuadrada, ...]` | `tuple[CelulaQuadrada, ...]` | Sem docstring própria na release. |
| `celula_para_mundo` | método | `celula_para_mundo(celula: object, *, ancora: str = 'centro') -> ValorEspacial` | `ValorEspacial` | Sem docstring própria na release. |
| `mundo_para_celula` | método | `mundo_para_celula(coordenada: object) -> CelulaQuadrada` | `CelulaQuadrada` | Sem docstring própria na release. |

#### `TopologiaHexagonal(tamanho_celula: float = 1.0, orientacao: str = 'topo_plano', origem: tuple[float, float] = (0.0, 0.0), limites_configurados: object = field(default=None, repr=False, compare=False))`

Entrada pública `TopologiaHexagonal` da superfície `coral.mundo`.

**Implementação:** `coral._mapas.topologias`

**Atributos declarados**

| Nome | Tipo | Padrão |
|---|---|---|
| `tamanho_celula` | `float` | `1.0` |
| `orientacao` | `str` | `'topo_plano'` |
| `origem` | `tuple[float, float]` | `(0.0, 0.0)` |
| `limites_configurados` | `object` | `field(default=None, repr=False, compare=False)` |

**Métodos e propriedades públicas**

| Nome | Tipo | Assinatura | Retorno | Descrição |
|---|---|---|---|---|
| `vizinhos` | método | `vizinhos(celula: object, **_: object) -> tuple[CelulaHexagonal, ...]` | `tuple[CelulaHexagonal, ...]` | Sem docstring própria na release. |
| `celula_para_mundo` | método | `celula_para_mundo(celula: object, *, ancora: str = 'centro') -> ValorEspacial` | `ValorEspacial` | Sem docstring própria na release. |
| `mundo_para_celula` | método | `mundo_para_celula(coordenada: object) -> CelulaHexagonal` | `CelulaHexagonal` | Sem docstring própria na release. |

#### `TopologiaVoxel(tamanho_x: float = 1.0, tamanho_y: float = 1.0, tamanho_z: float = 1.0, origem: tuple[float, float, float] = (0.0, 0.0, 0.0), limites_configurados: object = field(default=None, repr=False, compare=False))`

Entrada pública `TopologiaVoxel` da superfície `coral.mundo`.

**Implementação:** `coral._mapas.topologias`

**Atributos declarados**

| Nome | Tipo | Padrão |
|---|---|---|
| `tamanho_x` | `float` | `1.0` |
| `tamanho_y` | `float` | `1.0` |
| `tamanho_z` | `float` | `1.0` |
| `origem` | `tuple[float, float, float]` | `(0.0, 0.0, 0.0)` |
| `limites_configurados` | `object` | `field(default=None, repr=False, compare=False)` |

**Métodos e propriedades públicas**

| Nome | Tipo | Assinatura | Retorno | Descrição |
|---|---|---|---|---|
| `vizinhos` | método | `vizinhos(celula: object, **_: object) -> tuple[CelulaVoxel, ...]` | `tuple[CelulaVoxel, ...]` | Sem docstring própria na release. |
| `celula_para_mundo` | método | `celula_para_mundo(celula: object, *, ancora: str = 'centro') -> ValorEspacial` | `ValorEspacial` | Sem docstring própria na release. |
| `mundo_para_celula` | método | `mundo_para_celula(coordenada: object) -> CelulaVoxel` | `CelulaVoxel` | Sem docstring própria na release. |

### Exceções

#### `ErroMapaCoral(mensagem: str, *, codigo: str = 'mapa.invalido', contexto: dict[str, Any] | None = None) -> None`

Erro de domínio para operações inválidas de mapas Coral.

**Implementação:** `coral._mapas.modelo`

<!-- /AUTO:API -->

## Compatibilidade

O núcleo é independente do backend gráfico. Topologias e mapas são estruturas de domínio e podem ser usados em scripts, testes, servidores ou aplicações visuais.
