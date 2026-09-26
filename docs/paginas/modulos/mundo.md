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

:::resultado
O mundo `campanha` passa a conter `vila`, `bosque`, uma relação `estrada` entre as duas entidades e os personagens `heroina` e `monstro`.
:::

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

#### `criar_mundo`

Criar mundo via API.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | `'mundo'` |

**Retorno**

Retorna um valor declarado como `Mundo`.

:::details Detalhes técnicos

**Assinatura:** `criar_mundo(nome: str = 'mundo') -> Mundo`

**Origem da implementação:** `coral.mundo`

**Arquivo na release:** `coral/mundo.py`

:::

### Classes e protocolos

#### `Mundo`

Mundo leve para jogos, RPGs e simulações Coral.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | `'mundo'` |
| `relogio` | Relógio usado para controlar tempo ou atualização. | `FonteTempo \| None` | `None` |
| `eventos` | Fonte ou conjunto de eventos associado à operação. | `Eventos \| None` | `None` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `entidades` | Obtém entidades. | `tuple[Entidade, ...]` |
| `relacoes` | Obtém relacoes. | `tuple[Relacao, ...]` |
| `mapas` | Obtém mapas. | `tuple[Mapa, ...]` |
| `simulacao` | Simulação temporal associada, quando criada explicitamente. | `não declarado` |
| `criar_simulacao` | Cria ou devolve a simulação temporal do mundo sem exigir Jogos. | `não declarado` |
| `avancar_tempo` | Avança a simulação e depois atualiza regras e temporizadores pelo mesmo delta. | `não declarado` |
| `atualizar_simulacao` | Atualiza a simulação respeitando pausa e escala temporal. | `não declarado` |
| `adicionar_mapa` | Adiciona mapa. | `Mapa` |
| `criar_mapa` | Cria mapa. | `Mapa` |
| `buscar_mapa` | Procura mapa e devolve o resultado quando encontrado. | `Mapa \| None` |
| `exigir_mapa` | Obtém mapa e sinaliza falha quando ele não está disponível. | `Mapa` |
| `remover_mapa` | Remove mapa. | `bool` |
| `observar_regioes_mapa` | Observa regioes mapa. | `ObservadorRegiaoMapa` |
| `adicionar` | Adiciona o valor solicitado. | `Entidade` |
| `criar_entidade` | Cria entidade. | `Entidade` |
| `buscar` | Executa a operação `buscar` disponibilizada por `coral.mundo`. | `Entidade \| None` |
| `exigir` | Executa a operação `exigir` disponibilizada por `coral.mundo`. | `Entidade` |
| `remover` | Remove o valor solicitado. | `bool` |
| `relacionar` | Relaciona o valor solicitado. | `Relacao` |
| `remover_relacao` | Remove relacao. | `bool` |
| `relacionados` | Executa a operação `relacionados` disponibilizada por `coral.mundo`. | `tuple[Entidade, ...]` |
| `caminho` | Executa a operação `caminho` disponibilizada por `coral.mundo`. | `tuple[Entidade, ...]` |
| `com_tag` | Executa a operação `com_tag` disponibilizada por `coral.mundo`. | `tuple[Entidade, ...]` |
| `atualizar` | Atualiza o valor solicitado. | `tuple[str, ...]` |
| `atualizar_por_relogio` | Atualiza por relogio. | `tuple[str, ...]` |
| `emitir` | Emite o valor solicitado. | `int` |
| `emitir_evento` | Emite evento. | `não declarado` |
| `enfileirar_evento` | Enfileira evento. | `não declarado` |
| `processar_eventos` | Processa eventos. | `não declarado` |
| `emitir_propagado` | Emite propagado. | `int` |
| `emitir_evento_propagado` | Emite evento propagado. | `não declarado` |
| `estado_inspecao` | Executa a operação `estado_inspecao` disponibilizada por `coral.mundo`. | `dict[str, Any]` |
| `para_dict` | Converte o valor para dict. | `dict[str, Any]` |
| `para_json` | Converte o valor para JSON. | `str` |

:::details Detalhes técnicos

**Assinatura:** `Mundo(nome: str = 'mundo', *, relogio: FonteTempo \| None = None, eventos: Eventos \| None = None)`

**Origem da implementação:** `coral.mundo`

**Arquivo na release:** `coral/mundo.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `nome` | posicional |
| `relogio` | nomeado |
| `eventos` | nomeado |

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `entidades` | propriedade | `entidades() -> tuple[Entidade, ...]` |
| `relacoes` | propriedade | `relacoes() -> tuple[Relacao, ...]` |
| `mapas` | propriedade | `mapas() -> tuple[Mapa, ...]` |
| `simulacao` | propriedade | `simulacao()` |
| `criar_simulacao` | método | `criar_simulacao(*, tempo = None)` |
| `avancar_tempo` | método | `avancar_tempo(duracao: float)` |
| `atualizar_simulacao` | método | `atualizar_simulacao(dt_externo: float)` |
| `adicionar_mapa` | método | `adicionar_mapa(mapa: Mapa) -> Mapa` |
| `criar_mapa` | método | `criar_mapa(nome: str, topologia, *, propriedades: dict[str, Any] \| None = None) -> Mapa` |
| `buscar_mapa` | método | `buscar_mapa(nome: str) -> Mapa \| None` |
| `exigir_mapa` | método | `exigir_mapa(nome: str) -> Mapa` |
| `remover_mapa` | método | `remover_mapa(mapa: Mapa \| str) -> bool` |
| `observar_regioes_mapa` | método | `observar_regioes_mapa(nome: str, alvo: Any, mapa: Mapa \| str, regioes, resolvedor, *, identificador_alvo: Any = None) -> ObservadorRegiaoMapa` |
| `adicionar` | método | `adicionar(entidade: Entidade) -> Entidade` |
| `criar_entidade` | método | `criar_entidade(nome: str, **atributos: Any) -> Entidade` |
| `buscar` | método | `buscar(nome: str) -> Entidade \| None` |
| `exigir` | método | `exigir(nome: str) -> Entidade` |
| `remover` | método | `remover(entidade: Entidade \| str) -> bool` |
| `relacionar` | método | `relacionar(origem: Entidade \| str, destino: Entidade \| str, tipo: str, **dados: Any) -> Relacao` |
| `remover_relacao` | método | `remover_relacao(relacao: Relacao) -> bool` |
| `relacionados` | método | `relacionados(entidade: Entidade \| str, tipo: str \| None = None, *, direcao: str = 'saida') -> tuple[Entidade, ...]` |
| `caminho` | método | `caminho(origem: Entidade \| str, destino: Entidade \| str, *, tipo: str \| None = None, bidirecional: bool = True) -> tuple[Entidade, ...]` |
| `com_tag` | método | `com_tag(tag: str) -> tuple[Entidade, ...]` |
| `atualizar` | método | `atualizar(dt: float = 0.0) -> tuple[str, ...]` |
| `atualizar_por_relogio` | método | `atualizar_por_relogio() -> tuple[str, ...]` |
| `emitir` | método | `emitir(evento: str, *args, **kwargs) -> int` |
| `emitir_evento` | método | `emitir_evento(evento: str, *args, cancelavel: bool = False, metadados: dict[str, Any] \| None = None, **kwargs)` |
| `enfileirar_evento` | método | `enfileirar_evento(evento: str, *args, **kwargs)` |
| `processar_eventos` | método | `processar_eventos(limite: int \| None = None)` |
| `emitir_propagado` | método | `emitir_propagado(evento: str, *args, **kwargs) -> int` |
| `emitir_evento_propagado` | método | `emitir_evento_propagado(evento: str, *args, cancelavel: bool = False, metadados: dict[str, Any] \| None = None, **kwargs)` |
| `estado_inspecao` | método | `estado_inspecao() -> dict[str, Any]` |
| `para_dict` | método | `para_dict() -> dict[str, Any]` |
| `para_json` | método | `para_json(**kwargs) -> str` |

:::

#### `Entidade`

Representa objeto do mundo.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | obrigatório |
| `atributos` | Valor correspondente a atributos. | `dict[str, Any]` | `field(default_factory=dict)` |
| `tags` | Valor correspondente a tags. | `set[str]` | `field(default_factory=set)` |
| `inventario` | Valor correspondente a inventario. | `list[Any]` | `field(default_factory=list)` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | obrigatório |
| `atributos` | Valor correspondente a atributos. | `dict[str, Any]` | `field(default_factory=dict)` |
| `tags` | Valor correspondente a tags. | `set[str]` | `field(default_factory=set)` |
| `inventario` | Valor correspondente a inventario. | `list[Any]` | `field(default_factory=list)` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `definir` | Define o valor solicitado. | `'Entidade'` |
| `obter` | Executa a operação `obter` disponibilizada por `coral.mundo`. | `Any` |
| `adicionar_tag` | Adiciona tag. | `'Entidade'` |
| `remover_tag` | Remove tag. | `None` |
| `possui_tag` | Indica se possui tag. | `bool` |
| `guardar` | Armazena o valor solicitado. | `Any` |
| `remover_item` | Remove item. | `bool` |
| `estado_inspecao` | Executa a operação `estado_inspecao` disponibilizada por `coral.mundo`. | `dict[str, Any]` |

:::details Detalhes técnicos

**Assinatura:** `Entidade(nome: str, atributos: dict[str, Any] = field(default_factory=dict), tags: set[str] = field(default_factory=set), inventario: list[Any] = field(default_factory=list))`

**Origem da implementação:** `coral.mundo`

**Arquivo na release:** `coral/mundo.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `definir` | método | `definir(nome: str, valor: Any) -> 'Entidade'` |
| `obter` | método | `obter(nome: str, padrao: Any = None) -> Any` |
| `adicionar_tag` | método | `adicionar_tag(tag: str) -> 'Entidade'` |
| `remover_tag` | método | `remover_tag(tag: str) -> None` |
| `possui_tag` | método | `possui_tag(tag: str) -> bool` |
| `guardar` | método | `guardar(item: Any) -> Any` |
| `remover_item` | método | `remover_item(item: Any) -> bool` |
| `estado_inspecao` | método | `estado_inspecao() -> dict[str, Any]` |

:::

#### `Relacao`

Representa ligação entre entidades.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `origem` | Origem usada pela operação. | `Entidade` | obrigatório |
| `destino` | Destino que receberá o resultado da operação. | `Entidade` | obrigatório |
| `tipo` | Tipo solicitado para o resultado, quando o módulo oferece essa escolha. | `str` | obrigatório |
| `dados` | Dados processados pela operação. | `dict[str, Any]` | `field(default_factory=dict, compare=False)` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `origem` | Origem usada pela operação. | `Entidade` | obrigatório |
| `destino` | Destino que receberá o resultado da operação. | `Entidade` | obrigatório |
| `tipo` | Tipo solicitado para o resultado, quando o módulo oferece essa escolha. | `str` | obrigatório |
| `dados` | Dados processados pela operação. | `dict[str, Any]` | `field(default_factory=dict, compare=False)` |

:::details Detalhes técnicos

**Assinatura:** `Relacao(origem: Entidade, destino: Entidade, tipo: str, dados: dict[str, Any] = field(default_factory=dict, compare=False))`

**Origem da implementação:** `coral.mundo`

**Arquivo na release:** `coral/mundo.py`

:::

#### `Mapa`

Estrutura espacial discreta genérica, independente de visualização.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | obrigatório |
| `topologia` | Valor correspondente a topologia. | `Any` | obrigatório |
| `propriedades` | Valor correspondente a propriedades. | `Mapping[str, Any] \| None` | `None` |
| `eventos` | Fonte ou conjunto de eventos associado à operação. | `Eventos \| None` | `None` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `eventos` | Barramento associado, sem criar runtime oculto quando ausente. | `Eventos \| None` |
| `propriedades` | Obtém propriedades. | `Mapping[str, Any]` |
| `camadas` | Obtém camadas. | `tuple[CamadaMapa, ...]` |
| `regioes` | Executa a operação `regioes` disponibilizada por `coral.mundo`. | `tuple[Any, ...]` |
| `adicionar_camada` | Adiciona camada. | `CamadaMapa` |
| `buscar_camada` | Procura camada e devolve o resultado quando encontrado. | `CamadaMapa \| None` |
| `exigir_camada` | Obtém camada e sinaliza falha quando ele não está disponível. | `CamadaMapa` |
| `remover_camada` | Remove camada. | `bool` |
| `adicionar_regiao` | Adiciona regiao. | `Any` |
| `criar_regiao` | Cria regiao. | `Any` |
| `buscar_regiao` | Procura regiao e devolve o resultado quando encontrado. | `Any \| None` |
| `exigir_regiao` | Obtém regiao e sinaliza falha quando ele não está disponível. | `Any` |
| `remover_regiao` | Remove regiao. | `bool` |
| `regioes_em` | Executa a operação `regioes_em` disponibilizada por `coral.mundo`. | `tuple[Any, ...]` |
| `celulas_da_regiao` | Executa a operação `celulas_da_regiao` disponibilizada por `coral.mundo`. | `tuple[CelulaMapa, ...]` |
| `possui_valor` | Indica se possui valor. | `bool` |
| `conteudo_em` | Executa a operação `conteudo_em` disponibilizada por `coral.mundo`. | `ConteudoCelula \| None` |
| `obter` | Executa a operação `obter` disponibilizada por `coral.mundo`. | `Any` |
| `definir` | Define o valor solicitado. | `MudancaMapa` |
| `remover` | Remove o valor solicitado. | `MudancaMapa \| None` |
| `definir_travessia` | Define travessia. | `MudancaMapa` |
| `bloquear_travessia` | Executa a operação `bloquear_travessia` disponibilizada por `coral.mundo`. | `MudancaMapa` |
| `permitir_travessia` | Executa a operação `permitir_travessia` disponibilizada por `coral.mundo`. | `MudancaMapa` |
| `avaliar_travessia` | Executa a operação `avaliar_travessia` disponibilizada por `coral.mundo`. | `ResultadoPassagem` |
| `tentar_travessia` | Avalia uma tentativa e publica bloqueio apenas quando a ação é explícita. | `ResultadoPassagem` |
| `contexto_em` | Executa a operação `contexto_em` disponibilizada por `coral.mundo`. | `ContextoLocalMapa` |
| `vizinhos` | Executa a operação `vizinhos` disponibilizada por `coral.mundo`. | `tuple[CelulaMapa, ...]` |
| `aplicar_lote` | Valida todo o lote antes de aplicar qualquer escrita. | `tuple[MudancaMapa, ...]` |

:::details Detalhes técnicos

**Assinatura:** `Mapa(nome: str, topologia: Any, *, propriedades: Mapping[str, Any] \| None = None, eventos: Eventos \| None = None) -> None`

**Origem da implementação:** `coral._mapas.modelo`

**Arquivo na release:** `coral/_mapas/modelo.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `nome` | posicional |
| `topologia` | posicional |
| `propriedades` | nomeado |
| `eventos` | nomeado |

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `eventos` | propriedade | `eventos() -> Eventos \| None` |
| `propriedades` | propriedade | `propriedades() -> Mapping[str, Any]` |
| `camadas` | propriedade | `camadas() -> tuple[CamadaMapa, ...]` |
| `regioes` | propriedade | `regioes() -> tuple[Any, ...]` |
| `adicionar_camada` | método | `adicionar_camada(nome: str, *, ordem: int \| None = None, propriedades: Mapping[str, Any] \| None = None, participa_travessia: bool = True) -> CamadaMapa` |
| `buscar_camada` | método | `buscar_camada(nome: str) -> CamadaMapa \| None` |
| `exigir_camada` | método | `exigir_camada(nome: str) -> CamadaMapa` |
| `remover_camada` | método | `remover_camada(nome: str) -> bool` |
| `adicionar_regiao` | método | `adicionar_regiao(regiao: Any) -> Any` |
| `criar_regiao` | método | `criar_regiao(nome: str, *, celulas: Iterable[object] \| None = None, forma: Any = None, referencia: str = 'centro', propriedades: Mapping[str, Any] \| None = None) -> Any` |
| `buscar_regiao` | método | `buscar_regiao(nome: str) -> Any \| None` |
| `exigir_regiao` | método | `exigir_regiao(nome: str) -> Any` |
| `remover_regiao` | método | `remover_regiao(nome: str) -> bool` |
| `regioes_em` | método | `regioes_em(celula_ou_posicao: object) -> tuple[Any, ...]` |
| `celulas_da_regiao` | método | `celulas_da_regiao(nome: str, *, limites: object = None) -> tuple[CelulaMapa, ...]` |
| `possui_valor` | método | `possui_valor(camada: str, celula: object) -> bool` |
| `conteudo_em` | método | `conteudo_em(camada: str, celula: object) -> ConteudoCelula \| None` |
| `obter` | método | `obter(camada: str, celula: object, padrao: Any = None) -> Any` |
| `definir` | método | `definir(camada: str, celula: object, valor: Any, *, propriedades: Mapping[str, Any] \| None = None, travessia: bool \| None = None, custo: float \| int \| None = None, motivo: str \| None = None, causa: Any = None) -> MudancaMapa` |
| `remover` | método | `remover(camada: str, celula: object, *, causa: Any = None) -> MudancaMapa \| None` |
| `definir_travessia` | método | `definir_travessia(camada: str, celula: object, *, permitida: bool \| None = None, custo: float \| int \| None = None, motivo: str \| None = None, causa: Any = None) -> MudancaMapa` |
| `bloquear_travessia` | método | `bloquear_travessia(camada: str, celula: object, *, motivo: str \| None = None, causa: Any = None) -> MudancaMapa` |
| `permitir_travessia` | método | `permitir_travessia(camada: str, celula: object, *, custo: float \| int \| None = None, motivo: str \| None = None, causa: Any = None) -> MudancaMapa` |
| `avaliar_travessia` | método | `avaliar_travessia(origem: object, destino: object) -> ResultadoPassagem` |
| `tentar_travessia` | método | `tentar_travessia(origem: object, destino: object, *, causa: Any = None) -> ResultadoPassagem` |
| `contexto_em` | método | `contexto_em(celula: object, *, origem: object \| None = None) -> ContextoLocalMapa` |
| `vizinhos` | método | `vizinhos(celula: object, **opcoes: Any) -> tuple[CelulaMapa, ...]` |
| `aplicar_lote` | método | `aplicar_lote(operacoes: Iterable[Mapping[str, Any]]) -> tuple[MudancaMapa, ...]` |

:::

#### `CamadaMapa`

Camada nomeada, ordenada e esparsa de um mapa.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | obrigatório |
| `ordem` | Valor correspondente a ordem. | `int` | `0` |
| `propriedades` | Valor correspondente a propriedades. | `Mapping[str, Any] \| None` | `None` |
| `participa_travessia` | Valor correspondente a participa travessia. | `bool` | `True` |
| `_sequencia` | Valor correspondente a sequencia. | `int` | `0` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `propriedades` | Obtém propriedades. | `Mapping[str, Any]` |
| `quantidade` | Executa a operação `quantidade` disponibilizada por `coral.mundo`. | `int` |
| `celulas` | Executa a operação `celulas` disponibilizada por `coral.mundo`. | `tuple[CelulaMapa, ...]` |
| `possui` | Executa a operação `possui` disponibilizada por `coral.mundo`. | `bool` |
| `conteudo` | Executa a operação `conteudo` disponibilizada por `coral.mundo`. | `ConteudoCelula \| None` |

:::details Detalhes técnicos

**Assinatura:** `CamadaMapa(nome: str, *, ordem: int = 0, propriedades: Mapping[str, Any] \| None = None, participa_travessia: bool = True, _sequencia: int = 0) -> None`

**Origem da implementação:** `coral._mapas.modelo`

**Arquivo na release:** `coral/_mapas/modelo.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `nome` | posicional |
| `ordem` | nomeado |
| `propriedades` | nomeado |
| `participa_travessia` | nomeado |
| `_sequencia` | nomeado |

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `propriedades` | propriedade | `propriedades() -> Mapping[str, Any]` |
| `quantidade` | propriedade | `quantidade() -> int` |
| `celulas` | propriedade | `celulas() -> tuple[CelulaMapa, ...]` |
| `possui` | método | `possui(celula: CelulaMapa) -> bool` |
| `conteudo` | método | `conteudo(celula: CelulaMapa) -> ConteudoCelula \| None` |

:::

#### `ConteudoCelula`

Valor imutável associado a uma célula, com travessia opcional.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valor` | Valor processado pela operação. | `Any` | obrigatório |
| `propriedades` | Valor correspondente a propriedades. | `Mapping[str, Any] \| None` | `None` |
| `travessia` | Valor correspondente a travessia. | `bool \| None` | `None` |
| `custo` | Valor correspondente a custo. | `float \| int \| None` | `None` |
| `motivo` | Texto que descreve o motivo associado à operação. | `str \| None` | `None` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `travessia_permitida` | Valor correspondente a travessia permitida. | `bool \| None` | obrigatório |
| `custo_travessia` | Valor correspondente a custo travessia. | `float \| None` | obrigatório |
| `motivo_travessia` | Valor correspondente a motivo travessia. | `str \| None` | obrigatório |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `valor` | Obtém valor. | `Any` |
| `propriedades` | Obtém propriedades. | `Mapping[str, Any]` |
| `declarou_travessia` | Executa a operação `declarou_travessia` disponibilizada por `coral.mundo`. | `bool` |
| `com_valor` | Executa a operação `com_valor` disponibilizada por `coral.mundo`. | `'ConteudoCelula'` |
| `com_propriedades` | Executa a operação `com_propriedades` disponibilizada por `coral.mundo`. | `'ConteudoCelula'` |
| `com_travessia` | Executa a operação `com_travessia` disponibilizada por `coral.mundo`. | `'ConteudoCelula'` |

:::details Detalhes técnicos

**Assinatura:** `ConteudoCelula(valor: Any, propriedades: Mapping[str, Any] \| None = None, *, travessia: bool \| None = None, custo: float \| int \| None = None, motivo: str \| None = None) -> None`

**Origem da implementação:** `coral._mapas.modelo`

**Arquivo na release:** `coral/_mapas/modelo.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `valor` | posicional |
| `propriedades` | posicional |
| `travessia` | nomeado |
| `custo` | nomeado |
| `motivo` | nomeado |

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `valor` | propriedade | `valor() -> Any` |
| `propriedades` | propriedade | `propriedades() -> Mapping[str, Any]` |
| `declarou_travessia` | propriedade | `declarou_travessia() -> bool` |
| `com_valor` | método | `com_valor(valor: Any) -> 'ConteudoCelula'` |
| `com_propriedades` | método | `com_propriedades(propriedades: Mapping[str, Any]) -> 'ConteudoCelula'` |
| `com_travessia` | método | `com_travessia(*, permitida: bool \| None = None, custo: float \| int \| None = None, motivo: str \| None = None) -> 'ConteudoCelula'` |

:::

#### `BlocoMapa`

Conveniência para terreno, material, obstáculo ou tile.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `identificador` | Valor correspondente a identificador. | `str` | obrigatório |
| `propriedades` | Valor correspondente a propriedades. | `Mapping[str, Any] \| None` | `None` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `identificador` | Valor correspondente a identificador. | `str` | obrigatório |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `propriedades` | Obtém propriedades. | `Mapping[str, Any]` |

:::details Detalhes técnicos

**Assinatura:** `BlocoMapa(identificador: str, propriedades: Mapping[str, Any] \| None = None) -> None`

**Origem da implementação:** `coral._mapas.modelo`

**Arquivo na release:** `coral/_mapas/modelo.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `propriedades` | propriedade | `propriedades() -> Mapping[str, Any]` |

:::

#### `MudancaMapa`

Representa MudancaMapa na API de `coral.mundo`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `mapa` | Valor correspondente a mapa. | `str` | obrigatório |
| `camada` | Valor correspondente a camada. | `str` | obrigatório |
| `celula` | Valor correspondente a celula. | `CelulaMapa` | obrigatório |
| `operacao` | Valor correspondente a operacao. | `str` | obrigatório |
| `anterior` | Valor correspondente a anterior. | `ConteudoCelula \| None` | obrigatório |
| `novo` | Valor correspondente a novo. | `ConteudoCelula \| None` | obrigatório |
| `causa` | Valor correspondente a causa. | `Any` | `None` |
| `aplicada` | Valor correspondente a aplicada. | `bool` | `True` |
| `cancelada` | Valor correspondente a cancelada. | `bool` | `False` |
| `motivo_cancelamento` | Valor correspondente a motivo cancelamento. | `str \| None` | `None` |
| `evento_sequencia` | Valor correspondente a evento sequencia. | `int \| None` | `None` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `mapa` | Valor correspondente a mapa. | `str` | obrigatório |
| `camada` | Valor correspondente a camada. | `str` | obrigatório |
| `celula` | Valor correspondente a celula. | `CelulaMapa` | obrigatório |
| `operacao` | Valor correspondente a operacao. | `str` | obrigatório |
| `anterior` | Valor correspondente a anterior. | `ConteudoCelula \| None` | obrigatório |
| `novo` | Valor correspondente a novo. | `ConteudoCelula \| None` | obrigatório |
| `causa` | Valor correspondente a causa. | `Any` | `None` |
| `aplicada` | Valor correspondente a aplicada. | `bool` | `True` |
| `cancelada` | Valor correspondente a cancelada. | `bool` | `False` |
| `motivo_cancelamento` | Valor correspondente a motivo cancelamento. | `str \| None` | `None` |
| `evento_sequencia` | Valor correspondente a evento sequencia. | `int \| None` | `None` |

:::details Detalhes técnicos

**Assinatura:** `MudancaMapa(mapa: str, camada: str, celula: CelulaMapa, operacao: str, anterior: ConteudoCelula \| None, novo: ConteudoCelula \| None, causa: Any = None, aplicada: bool = True, cancelada: bool = False, motivo_cancelamento: str \| None = None, evento_sequencia: int \| None = None)`

**Origem da implementação:** `coral._mapas.modelo`

**Arquivo na release:** `coral/_mapas/modelo.py`

:::

#### `RegiaoMapa`

Região por conjunto de células ou por forma espacial oficial.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `mapa` | Valor correspondente a mapa. | `Any` | obrigatório |
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | obrigatório |
| `celulas` | Valor correspondente a celulas. | `Iterable[object] \| None` | `None` |
| `forma` | Forma ou dimensões da estrutura a criar. | `Any` | `None` |
| `referencia` | Valor correspondente a referencia. | `str` | `'centro'` |
| `propriedades` | Valor correspondente a propriedades. | `Mapping[str, Any] \| None` | `None` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `tipo` | Executa a operação `tipo` disponibilizada por `coral.mundo`. | `str` |
| `forma` | Obtém forma. | `Any` |
| `propriedades` | Obtém propriedades. | `Mapping[str, Any]` |
| `celulas_explicitas` | Executa a operação `celulas_explicitas` disponibilizada por `coral.mundo`. | `tuple[CelulaMapa, ...]` |
| `contem` | Executa a operação `contem` disponibilizada por `coral.mundo`. | `bool` |
| `celulas` | Executa a operação `celulas` disponibilizada por `coral.mundo`. | `tuple[CelulaMapa, ...]` |

:::details Detalhes técnicos

**Assinatura:** `RegiaoMapa(mapa: Any, nome: str, *, celulas: Iterable[object] \| None = None, forma: Any = None, referencia: str = 'centro', propriedades: Mapping[str, Any] \| None = None) -> None`

**Origem da implementação:** `coral._mapas.regioes`

**Arquivo na release:** `coral/_mapas/regioes.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `mapa` | posicional |
| `nome` | posicional |
| `celulas` | nomeado |
| `forma` | nomeado |
| `referencia` | nomeado |
| `propriedades` | nomeado |

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `tipo` | propriedade | `tipo() -> str` |
| `forma` | propriedade | `forma() -> Any` |
| `propriedades` | propriedade | `propriedades() -> Mapping[str, Any]` |
| `celulas_explicitas` | propriedade | `celulas_explicitas() -> tuple[CelulaMapa, ...]` |
| `contem` | método | `contem(celula_ou_posicao: object) -> bool` |
| `celulas` | método | `celulas(*, limites: object = None) -> tuple[CelulaMapa, ...]` |

:::

#### `ResultadoPassagem`

Representa resultado de travessia.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `permitida` | Valor correspondente a permitida. | `bool` | obrigatório |
| `custo` | Valor correspondente a custo. | `float` | obrigatório |
| `motivo` | Texto que descreve o motivo associado à operação. | `str \| None` | obrigatório |
| `camadas_responsaveis` | Valor correspondente a camadas responsaveis. | `tuple[str, ...]` | obrigatório |
| `origem` | Origem usada pela operação. | `CelulaMapa` | obrigatório |
| `destino` | Destino que receberá o resultado da operação. | `CelulaMapa` | obrigatório |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `permitida` | Valor correspondente a permitida. | `bool` | obrigatório |
| `custo` | Valor correspondente a custo. | `float` | obrigatório |
| `motivo` | Texto que descreve o motivo associado à operação. | `str \| None` | obrigatório |
| `camadas_responsaveis` | Valor correspondente a camadas responsaveis. | `tuple[str, ...]` | obrigatório |
| `origem` | Origem usada pela operação. | `CelulaMapa` | obrigatório |
| `destino` | Destino que receberá o resultado da operação. | `CelulaMapa` | obrigatório |

:::details Detalhes técnicos

**Assinatura:** `ResultadoPassagem(permitida: bool, custo: float, motivo: str \| None, camadas_responsaveis: tuple[str, ...], origem: CelulaMapa, destino: CelulaMapa)`

**Origem da implementação:** `coral._mapas.modelo`

**Arquivo na release:** `coral/_mapas/modelo.py`

:::

#### `ObservadorRegiaoMapa`

Reconhece transições de entrada e saída entre avaliações sucessivas.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | obrigatório |
| `alvo` | Valor correspondente a alvo. | `Any` | obrigatório |
| `mapa` | Valor correspondente a mapa. | `Mapa` | obrigatório |
| `regioes` | Valor correspondente a regioes. | `Iterable[RegiaoMapa \| str]` | obrigatório |
| `resolvedor` | Valor correspondente a resolvedor. | `ResolvedorLocalizacao` | obrigatório |
| `eventos` | Fonte ou conjunto de eventos associado à operação. | `Eventos` | obrigatório |
| `identificador_alvo` | Valor correspondente a identificador alvo. | `Any` | `None` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | obrigatório |
| `alvo` | Valor correspondente a alvo. | `Any` | obrigatório |
| `mapa` | Valor correspondente a mapa. | `Mapa` | obrigatório |
| `regioes` | Valor correspondente a regioes. | `tuple[RegiaoMapa, ...]` | obrigatório |
| `resolvedor` | Valor correspondente a resolvedor. | `ResolvedorLocalizacao` | obrigatório |
| `eventos` | Fonte ou conjunto de eventos associado à operação. | `Eventos` | obrigatório |
| `identificador_alvo` | Valor correspondente a identificador alvo. | `Any` | `None` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `regioes_anteriores` | Executa a operação `regioes_anteriores` disponibilizada por `coral.mundo`. | `tuple[str, ...]` |
| `avaliar` | Executa a operação `avaliar` disponibilizada por `coral.mundo`. | `bool` |

:::details Detalhes técnicos

**Assinatura:** `ObservadorRegiaoMapa(nome: str, alvo: Any, mapa: Mapa, regioes: Iterable[RegiaoMapa \| str], resolvedor: ResolvedorLocalizacao, eventos: Eventos, *, identificador_alvo: Any = None) -> None`

**Origem da implementação:** `coral._mapas.observacao`

**Arquivo na release:** `coral/_mapas/observacao.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `nome` | posicional |
| `alvo` | posicional |
| `mapa` | posicional |
| `regioes` | posicional |
| `resolvedor` | posicional |
| `eventos` | posicional |
| `identificador_alvo` | nomeado |

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `regioes_anteriores` | propriedade | `regioes_anteriores() -> tuple[str, ...]` |
| `avaliar` | método | `avaliar(contexto: Any) -> bool` |

:::

#### `CelulaQuadrada`

Representa CelulaQuadrada na API de `coral.mundo`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `coluna` | Valor correspondente a coluna. | `int` | obrigatório |
| `linha` | Valor correspondente a linha. | `int` | obrigatório |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `coluna` | Valor correspondente a coluna. | `int` | obrigatório |
| `linha` | Valor correspondente a linha. | `int` | obrigatório |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `como_tupla` | Representa o valor como tupla. | `tuple[int, int]` |

:::details Detalhes técnicos

**Assinatura:** `CelulaQuadrada(coluna: int, linha: int)`

**Origem da implementação:** `coral._mapas.modelo`

**Arquivo na release:** `coral/_mapas/modelo.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `como_tupla` | método | `como_tupla() -> tuple[int, int]` |

:::

#### `CelulaHexagonal`

Representa CelulaHexagonal na API de `coral.mundo`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `q` | Valor correspondente a q. | `int` | obrigatório |
| `r` | Valor correspondente a r. | `int` | obrigatório |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `q` | Valor correspondente a q. | `int` | obrigatório |
| `r` | Valor correspondente a r. | `int` | obrigatório |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `como_tupla` | Representa o valor como tupla. | `tuple[int, int]` |

:::details Detalhes técnicos

**Assinatura:** `CelulaHexagonal(q: int, r: int)`

**Origem da implementação:** `coral._mapas.modelo`

**Arquivo na release:** `coral/_mapas/modelo.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `como_tupla` | método | `como_tupla() -> tuple[int, int]` |

:::

#### `CelulaVoxel`

Representa CelulaVoxel na API de `coral.mundo`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `x` | Coordenada horizontal. | `int` | obrigatório |
| `y` | Coordenada vertical. | `int` | obrigatório |
| `z` | Valor correspondente a z. | `int` | obrigatório |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `x` | Coordenada horizontal. | `int` | obrigatório |
| `y` | Coordenada vertical. | `int` | obrigatório |
| `z` | Valor correspondente a z. | `int` | obrigatório |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `como_tupla` | Representa o valor como tupla. | `tuple[int, int, int]` |

:::details Detalhes técnicos

**Assinatura:** `CelulaVoxel(x: int, y: int, z: int)`

**Origem da implementação:** `coral._mapas.modelo`

**Arquivo na release:** `coral/_mapas/modelo.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `como_tupla` | método | `como_tupla() -> tuple[int, int, int]` |

:::

#### `TopologiaQuadrada`

Representa topologia 2D quadrada.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `largura_celula` | Largura de celula. | `float` | `1.0` |
| `altura_celula` | Altura de celula. | `float` | `1.0` |
| `origem` | Origem usada pela operação. | `tuple[float, float]` | `(0.0, 0.0)` |
| `limites_configurados` | Valor correspondente a limites configurados. | `object` | `field(default=None, repr=False, compare=False)` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `largura_celula` | Largura de celula. | `float` | `1.0` |
| `altura_celula` | Altura de celula. | `float` | `1.0` |
| `origem` | Origem usada pela operação. | `tuple[float, float]` | `(0.0, 0.0)` |
| `limites_configurados` | Valor correspondente a limites configurados. | `object` | `field(default=None, repr=False, compare=False)` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `vizinhos` | Executa a operação `vizinhos` disponibilizada por `coral.mundo`. | `tuple[CelulaQuadrada, ...]` |
| `celula_para_mundo` | Executa a operação `celula_para_mundo` disponibilizada por `coral.mundo`. | `ValorEspacial` |
| `mundo_para_celula` | Executa a operação `mundo_para_celula` disponibilizada por `coral.mundo`. | `CelulaQuadrada` |

:::details Detalhes técnicos

**Assinatura:** `TopologiaQuadrada(largura_celula: float = 1.0, altura_celula: float = 1.0, origem: tuple[float, float] = (0.0, 0.0), limites_configurados: object = field(default=None, repr=False, compare=False))`

**Origem da implementação:** `coral._mapas.topologias`

**Arquivo na release:** `coral/_mapas/topologias.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `vizinhos` | método | `vizinhos(celula: object, *, incluir_diagonais: bool = False) -> tuple[CelulaQuadrada, ...]` |
| `celula_para_mundo` | método | `celula_para_mundo(celula: object, *, ancora: str = 'centro') -> ValorEspacial` |
| `mundo_para_celula` | método | `mundo_para_celula(coordenada: object) -> CelulaQuadrada` |

:::

#### `TopologiaHexagonal`

Representa topologia 2D hexagonal.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `tamanho_celula` | Valor correspondente a tamanho celula. | `float` | `1.0` |
| `orientacao` | Valor correspondente a orientacao. | `str` | `'topo_plano'` |
| `origem` | Origem usada pela operação. | `tuple[float, float]` | `(0.0, 0.0)` |
| `limites_configurados` | Valor correspondente a limites configurados. | `object` | `field(default=None, repr=False, compare=False)` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `tamanho_celula` | Valor correspondente a tamanho celula. | `float` | `1.0` |
| `orientacao` | Valor correspondente a orientacao. | `str` | `'topo_plano'` |
| `origem` | Origem usada pela operação. | `tuple[float, float]` | `(0.0, 0.0)` |
| `limites_configurados` | Valor correspondente a limites configurados. | `object` | `field(default=None, repr=False, compare=False)` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `vizinhos` | Executa a operação `vizinhos` disponibilizada por `coral.mundo`. | `tuple[CelulaHexagonal, ...]` |
| `celula_para_mundo` | Executa a operação `celula_para_mundo` disponibilizada por `coral.mundo`. | `ValorEspacial` |
| `mundo_para_celula` | Executa a operação `mundo_para_celula` disponibilizada por `coral.mundo`. | `CelulaHexagonal` |

:::details Detalhes técnicos

**Assinatura:** `TopologiaHexagonal(tamanho_celula: float = 1.0, orientacao: str = 'topo_plano', origem: tuple[float, float] = (0.0, 0.0), limites_configurados: object = field(default=None, repr=False, compare=False))`

**Origem da implementação:** `coral._mapas.topologias`

**Arquivo na release:** `coral/_mapas/topologias.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `vizinhos` | método | `vizinhos(celula: object, **_: object) -> tuple[CelulaHexagonal, ...]` |
| `celula_para_mundo` | método | `celula_para_mundo(celula: object, *, ancora: str = 'centro') -> ValorEspacial` |
| `mundo_para_celula` | método | `mundo_para_celula(coordenada: object) -> CelulaHexagonal` |

:::

#### `TopologiaVoxel`

Representa topologia 3D.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `tamanho_x` | Valor correspondente a tamanho x. | `float` | `1.0` |
| `tamanho_y` | Valor correspondente a tamanho y. | `float` | `1.0` |
| `tamanho_z` | Valor correspondente a tamanho z. | `float` | `1.0` |
| `origem` | Origem usada pela operação. | `tuple[float, float, float]` | `(0.0, 0.0, 0.0)` |
| `limites_configurados` | Valor correspondente a limites configurados. | `object` | `field(default=None, repr=False, compare=False)` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `tamanho_x` | Valor correspondente a tamanho x. | `float` | `1.0` |
| `tamanho_y` | Valor correspondente a tamanho y. | `float` | `1.0` |
| `tamanho_z` | Valor correspondente a tamanho z. | `float` | `1.0` |
| `origem` | Origem usada pela operação. | `tuple[float, float, float]` | `(0.0, 0.0, 0.0)` |
| `limites_configurados` | Valor correspondente a limites configurados. | `object` | `field(default=None, repr=False, compare=False)` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `vizinhos` | Executa a operação `vizinhos` disponibilizada por `coral.mundo`. | `tuple[CelulaVoxel, ...]` |
| `celula_para_mundo` | Executa a operação `celula_para_mundo` disponibilizada por `coral.mundo`. | `ValorEspacial` |
| `mundo_para_celula` | Executa a operação `mundo_para_celula` disponibilizada por `coral.mundo`. | `CelulaVoxel` |

:::details Detalhes técnicos

**Assinatura:** `TopologiaVoxel(tamanho_x: float = 1.0, tamanho_y: float = 1.0, tamanho_z: float = 1.0, origem: tuple[float, float, float] = (0.0, 0.0, 0.0), limites_configurados: object = field(default=None, repr=False, compare=False))`

**Origem da implementação:** `coral._mapas.topologias`

**Arquivo na release:** `coral/_mapas/topologias.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `vizinhos` | método | `vizinhos(celula: object, **_: object) -> tuple[CelulaVoxel, ...]` |
| `celula_para_mundo` | método | `celula_para_mundo(celula: object, *, ancora: str = 'centro') -> ValorEspacial` |
| `mundo_para_celula` | método | `mundo_para_celula(coordenada: object) -> CelulaVoxel` |

:::

### Exceções

#### `ErroMapaCoral`

Erro de domínio para operações inválidas de mapas Coral.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `mensagem` | Valor correspondente a mensagem. | `str` | obrigatório |
| `codigo` | Valor correspondente a codigo. | `str` | `'mapa.invalido'` |
| `contexto` | Valor correspondente a contexto. | `dict[str, Any] \| None` | `None` |

:::details Detalhes técnicos

**Assinatura:** `ErroMapaCoral(mensagem: str, *, codigo: str = 'mapa.invalido', contexto: dict[str, Any] \| None = None) -> None`

**Origem da implementação:** `coral._mapas.modelo`

**Arquivo na release:** `coral/_mapas/modelo.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `mensagem` | posicional |
| `codigo` | nomeado |
| `contexto` | nomeado |

:::

<!-- /AUTO:API -->

## Compatibilidade

O núcleo é independente do backend gráfico. Topologias e mapas são estruturas de domínio e podem ser usados em scripts, testes, servidores ou aplicações visuais.
