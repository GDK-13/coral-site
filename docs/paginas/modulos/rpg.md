# coral.rpg

## Visão geral

`coral.rpg` acrescenta mecânicas de RPG ao modelo genérico de mundo: rolagens, personagens, vida, testes de atributo, combate por turnos e persistência do estado do domínio.

<!-- AUTO:MODULO -->

**Importação:** `coral.rpg`  
**Categoria:** rpg  

rolagens, personagens, combate e estado de RPG

### Superfície pública detectada

`Rolagem`, `rolar`, `Personagem`, `CombateTurnos`, `criar_personagem`, `registrar_combate`, `buscar_combate`, `combates_do_mundo`, `EstadoRPG`, `estado_rpg`, `salvar_estado_rpg`, `carregar_estado_rpg`

<!-- /AUTO:MODULO -->

## Papel no ecossistema

O módulo não substitui `coral.mundo`. Personagens e combates vivem sobre um mundo reutilizável. A apresentação continua opcional e pode ser feita por `coral.jogos`.

## Conceitos principais

### Rolagem

`rolar` interpreta uma expressão de dados e produz `Rolagem`, que preserva expressão, dados individuais, modificador e total. Semente ou gerador explícito tornam a rolagem reproduzível.

### Personagem

`Personagem` possui nome, vida, vida máxima e atributos adicionais. Métodos de dano, cura e teste concentram regras básicas de estado.

### Combate por turnos

`CombateTurnos` mantém participantes, inicia ordem de atuação e avança o personagem atual. Combates podem ser registrados no mundo e recuperados por nome.

### Estado persistente

`EstadoRPG` agrega o domínio sobre `Mundo`, com helpers para salvar e carregar o estado oficial.

## Quando usar

Use para protótipos e sistemas de RPG que precisam de personagens e combate, inclusive sem interface gráfica. Regras específicas de um sistema de jogo podem ser compostas com `coral.regras` em vez de modificar o núcleo.

## Começando

Trecho do exemplo oficial `Exemplos/Mundo/01_mundo_e_rpg.coral`:

```coral
crie um mundo chamado campanha com nome "Campanha"
crie um personagem chamado heroina no mundo campanha com 12 de vida
crie um personagem chamado monstro no mundo campanha com 6 de vida
role um dado de 6 lados usando a semente 7 como ataque
cause ataque.total de dano a monstro
cure 1 de vida de monstro
crie um combate chamado batalha com heroina e monstro
inicie o combate batalha usando a semente 4
```

## API essencial

| Entrada | Papel | Assinatura |
|---|---|---|
| `Rolagem` | resultado de dados | `Rolagem(expressao: str, dados: tuple[int, ...], modificador: int = 0)` |
| `rolar` | realizar rolagem | `rolar(expressao: str = '1d20', semente: int \| None = None, *, gerador: random.Random \| None = None) -> Rolagem` |
| `Personagem` | entidade de RPG | `Personagem(nome: str, vida: int = 10, *, vida_max: int \| None = None, **atributos: Any)` |
| `CombateTurnos` | coordenar turnos | `CombateTurnos(participantes: Iterable[Personagem] = (), *, nome: str \| None = None)` |
| `criar_personagem` | criar personagem em um mundo | `criar_personagem(mundo: Mundo, nome: str, vida: int = 10, **atributos: Any) -> Personagem` |
| `registrar_combate` | registrar combate | `registrar_combate(mundo: Mundo, nome: str, combate: 'CombateTurnos') -> 'CombateTurnos'` |
| `EstadoRPG` | agregado persistente | `EstadoRPG(mundo: Mundo)` |
| `salvar_estado_rpg` | persistir estado | `salvar_estado_rpg(mundo: Mundo, caminho: str \| Path) -> Path` |
| `carregar_estado_rpg` | restaurar mundo de RPG | `carregar_estado_rpg(caminho: str \| Path) -> Mundo` |

## Fluxo de personagem

Crie o personagem dentro de um `Mundo`, manipule vida e atributos pela API do domínio e use `teste()` ou rolagens explícitas quando precisar de incerteza. Isso mantém a entidade ligada ao mundo e evita duas fontes de verdade.

## Fluxo de combate

Crie `CombateTurnos`, adicione participantes, inicie com iniciativa calculada ou fornecida e avance por `proximo()`. `terminou()` permite ao controlador encerrar a cena ou emitir um evento de domínio.

## Aleatoriedade reproduzível

Passe semente em testes e exemplos. Em um jogo real, você pode usar uma fonte apropriada ao domínio, mas preservar a capacidade de repetir uma sequência facilita depuração de combate.

## Erros e invariantes

Vida deve permanecer coerente com vida máxima e operações de dano ou cura. Personagens e combates registrados precisam pertencer ao contexto correto de mundo. Persistência herda as validações do domínio e do formato persistido.

## Boas práticas

* Mantenha geografia, relações e entidades gerais em `coral.mundo`.
* Coloque reações e gatilhos em `coral.regras` quando a mecânica for naturalmente reativa.
* Use `coral.jogos` apenas para apresentação e entrada.
* Salve por meio da superfície oficial, não serializando internamente os objetos por conta própria.

## Integração com outros módulos

`coral.mundo` é a base. `coral.aleatorio` ajuda em geração e sorteios. `coral.regras` modela gatilhos. `coral.persistencia` sustenta o armazenamento e `coral.jogos` apresenta personagens e combate.

## Testabilidade

Personagens, rolagens e combate funcionam sem janela. Testes podem fixar sementes e verificar estado final antes de testar animações ou interface.

## Referência da API

<!-- AUTO:API -->

### Funções

#### `rolar(expressao: str = '1d20', semente: int | None = None, *, gerador: random.Random | None = None) -> Rolagem`

Entrada pública `rolar` da superfície `coral.rpg`.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `expressao` | `str` | `'1d20'` | posicional |
| `semente` | `int \| None` | `None` | posicional |
| `gerador` | `random.Random \| None` | `None` | nomeado |

**Retorno:** `Rolagem`

**Exceções observáveis no corpo:** `ValueError`

#### `criar_personagem(mundo: Mundo, nome: str, vida: int = 10, **atributos: Any) -> Personagem`

Entrada pública `criar_personagem` da superfície `coral.rpg`.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `mundo` | `Mundo` | obrigatório | posicional |
| `nome` | `str` | obrigatório | posicional |
| `vida` | `int` | `10` | posicional |
| `**atributos` | `Any` | obrigatório | variádico nomeado |

**Retorno:** `Personagem`

#### `registrar_combate(mundo: Mundo, nome: str, combate: 'CombateTurnos') -> 'CombateTurnos'`

Entrada pública `registrar_combate` da superfície `coral.rpg`.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `mundo` | `Mundo` | obrigatório | posicional |
| `nome` | `str` | obrigatório | posicional |
| `combate` | `'CombateTurnos'` | obrigatório | posicional |

**Retorno:** `'CombateTurnos'`

**Exceções observáveis no corpo:** `TypeError`, `ValueError`

#### `buscar_combate(mundo: Mundo, nome: str) -> 'CombateTurnos | None'`

Entrada pública `buscar_combate` da superfície `coral.rpg`.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `mundo` | `Mundo` | obrigatório | posicional |
| `nome` | `str` | obrigatório | posicional |

**Retorno:** `'CombateTurnos | None'`

#### `combates_do_mundo(mundo: Mundo) -> tuple['CombateTurnos', ...]`

Entrada pública `combates_do_mundo` da superfície `coral.rpg`.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `mundo` | `Mundo` | obrigatório | posicional |

**Retorno:** `tuple['CombateTurnos', ...]`

#### `estado_rpg(mundo: Mundo) -> EstadoRPG`

Entrada pública `estado_rpg` da superfície `coral.rpg`.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `mundo` | `Mundo` | obrigatório | posicional |

**Retorno:** `EstadoRPG`

#### `salvar_estado_rpg(mundo: Mundo, caminho: str | Path) -> Path`

Entrada pública `salvar_estado_rpg` da superfície `coral.rpg`.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `mundo` | `Mundo` | obrigatório | posicional |
| `caminho` | `str \| Path` | obrigatório | posicional |

**Retorno:** `Path`

#### `carregar_estado_rpg(caminho: str | Path) -> Mundo`

Entrada pública `carregar_estado_rpg` da superfície `coral.rpg`.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `caminho` | `str \| Path` | obrigatório | posicional |

**Retorno:** `Mundo`

### Classes e protocolos

#### `Rolagem(expressao: str, dados: tuple[int, ...], modificador: int = 0)`

Entrada pública `Rolagem` da superfície `coral.rpg`.

**Atributos declarados**

| Nome | Tipo | Padrão |
|---|---|---|
| `expressao` | `str` | obrigatório |
| `dados` | `tuple[int, ...]` | obrigatório |
| `modificador` | `int` | `0` |

**Métodos e propriedades públicas**

| Nome | Tipo | Assinatura | Retorno | Descrição |
|---|---|---|---|---|
| `total` | propriedade | `total() -> int` | `int` | Sem docstring própria na release. |

#### `Personagem(nome: str, vida: int = 10, *, vida_max: int | None = None, **atributos: Any)`

Entrada pública `Personagem` da superfície `coral.rpg`.

**Métodos e propriedades públicas**

| Nome | Tipo | Assinatura | Retorno | Descrição |
|---|---|---|---|---|
| `mundo` | propriedade | `mundo()` | `não declarado` | Sem docstring própria na release. |
| `vivo` | propriedade | `vivo() -> bool` | `bool` | Sem docstring própria na release. |
| `receber_dano` | método | `receber_dano(quantidade: int) -> int` | `int` | Sem docstring própria na release. |
| `curar` | método | `curar(quantidade: int) -> int` | `int` | Sem docstring própria na release. |
| `teste` | método | `teste(atributo: str, dificuldade: int = 10, *, semente: int \| None = None) -> tuple[Rolagem, bool]` | `tuple[Rolagem, bool]` | Sem docstring própria na release. |

#### `CombateTurnos(participantes: Iterable[Personagem] = (), *, nome: str | None = None)`

Entrada pública `CombateTurnos` da superfície `coral.rpg`.

**Métodos e propriedades públicas**

| Nome | Tipo | Assinatura | Retorno | Descrição |
|---|---|---|---|---|
| `adicionar` | método | `adicionar(personagem: Personagem) -> Personagem` | `Personagem` | Sem docstring própria na release. |
| `iniciar` | método | `iniciar(*, iniciativas: dict[str, int] \| None = None, semente: int \| None = None) -> tuple[Personagem, ...]` | `tuple[Personagem, ...]` | Sem docstring própria na release. |
| `atual` | propriedade | `atual() -> Personagem \| None` | `Personagem \| None` | Sem docstring própria na release. |
| `proximo` | método | `proximo() -> Personagem \| None` | `Personagem \| None` | Sem docstring própria na release. |
| `terminou` | propriedade | `terminou() -> bool` | `bool` | Sem docstring própria na release. |

#### `EstadoRPG(mundo: Mundo)`

Agregado persistente do domínio RPG sobre um Mundo genérico.

**Atributos declarados**

| Nome | Tipo | Padrão |
|---|---|---|
| `mundo` | `Mundo` | obrigatório |

<!-- /AUTO:API -->

## Compatibilidade

O módulo faz parte do runtime padrão e pode ser usado headless. A apresentação visual não é requisito para o domínio de RPG.
