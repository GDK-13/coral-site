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

#### `rolar`

Realizar rolagem.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `expressao` | Valor correspondente a expressao. | `str` | `'1d20'` |
| `semente` | Semente usada para tornar a sequência reproduzível. | `int \| None` | `None` |
| `gerador` | Valor correspondente a gerador. | `random.Random \| None` | `None` |

**Retorno**

Retorna um valor declarado como `Rolagem`.

:::details Detalhes técnicos

**Assinatura:** `rolar(expressao: str = '1d20', semente: int \| None = None, *, gerador: random.Random \| None = None) -> Rolagem`

**Origem da implementação:** `coral.rpg`

**Arquivo na release:** `coral/rpg.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `expressao` | posicional |
| `semente` | posicional |
| `gerador` | nomeado |

**Exceções diretamente observáveis no corpo:** `ValueError`

:::

#### `criar_personagem`

Criar personagem em um mundo.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `mundo` | Mundo associado à operação. | `Mundo` | obrigatório |
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | obrigatório |
| `vida` | Valor correspondente a vida. | `int` | `10` |
| `**atributos` | Valor correspondente a atributos. | `Any` | obrigatório |

**Retorno**

Retorna um valor declarado como `Personagem`.

:::details Detalhes técnicos

**Assinatura:** `criar_personagem(mundo: Mundo, nome: str, vida: int = 10, **atributos: Any) -> Personagem`

**Origem da implementação:** `coral.rpg`

**Arquivo na release:** `coral/rpg.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `mundo` | posicional |
| `nome` | posicional |
| `vida` | posicional |
| `**atributos` | variádico nomeado |

:::

#### `registrar_combate`

Registrar combate.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `mundo` | Mundo associado à operação. | `Mundo` | obrigatório |
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | obrigatório |
| `combate` | Valor correspondente a combate. | `'CombateTurnos'` | obrigatório |

**Retorno**

Retorna um valor declarado como `'CombateTurnos'`.

:::details Detalhes técnicos

**Assinatura:** `registrar_combate(mundo: Mundo, nome: str, combate: 'CombateTurnos') -> 'CombateTurnos'`

**Origem da implementação:** `coral.rpg`

**Arquivo na release:** `coral/rpg.py`

**Exceções diretamente observáveis no corpo:** `TypeError`, `ValueError`

:::

#### `buscar_combate`

Procura combate e devolve o resultado quando encontrado.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `mundo` | Mundo associado à operação. | `Mundo` | obrigatório |
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | obrigatório |

**Retorno**

Retorna um valor declarado como `'CombateTurnos | None'`.

:::details Detalhes técnicos

**Assinatura:** `buscar_combate(mundo: Mundo, nome: str) -> 'CombateTurnos \| None'`

**Origem da implementação:** `coral.rpg`

**Arquivo na release:** `coral/rpg.py`

:::

#### `combates_do_mundo`

Obtém combates do mundo.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `mundo` | Mundo associado à operação. | `Mundo` | obrigatório |

**Retorno**

Retorna um valor declarado como `tuple['CombateTurnos', ...]`.

:::details Detalhes técnicos

**Assinatura:** `combates_do_mundo(mundo: Mundo) -> tuple['CombateTurnos', ...]`

**Origem da implementação:** `coral.rpg`

**Arquivo na release:** `coral/rpg.py`

:::

#### `estado_rpg`

Obtém o agregado de estado RPG associado ao mundo.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `mundo` | Mundo associado à operação. | `Mundo` | obrigatório |

**Retorno**

Retorna um valor declarado como `EstadoRPG`.

:::details Detalhes técnicos

**Assinatura:** `estado_rpg(mundo: Mundo) -> EstadoRPG`

**Origem da implementação:** `coral.rpg`

**Arquivo na release:** `coral/rpg.py`

:::

#### `salvar_estado_rpg`

Persistir estado.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `mundo` | Mundo associado à operação. | `Mundo` | obrigatório |
| `caminho` | Caminho do arquivo ou diretório usado pela operação. | `str \| Path` | obrigatório |

**Retorno**

Retorna um valor declarado como `Path`.

:::details Detalhes técnicos

**Assinatura:** `salvar_estado_rpg(mundo: Mundo, caminho: str \| Path) -> Path`

**Origem da implementação:** `coral.rpg`

**Arquivo na release:** `coral/rpg.py`

:::

#### `carregar_estado_rpg`

Restaurar mundo de RPG.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `caminho` | Caminho do arquivo ou diretório usado pela operação. | `str \| Path` | obrigatório |

**Retorno**

Retorna um valor declarado como `Mundo`.

:::details Detalhes técnicos

**Assinatura:** `carregar_estado_rpg(caminho: str \| Path) -> Mundo`

**Origem da implementação:** `coral.rpg`

**Arquivo na release:** `coral/rpg.py`

:::

### Classes e protocolos

#### `Rolagem`

Representa resultado de dados.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `expressao` | Valor correspondente a expressao. | `str` | obrigatório |
| `dados` | Dados processados pela operação. | `tuple[int, ...]` | obrigatório |
| `modificador` | Valor correspondente a modificador. | `int` | `0` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `expressao` | Valor correspondente a expressao. | `str` | obrigatório |
| `dados` | Dados processados pela operação. | `tuple[int, ...]` | obrigatório |
| `modificador` | Valor correspondente a modificador. | `int` | `0` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `total` | Obtém total. | `int` |

:::details Detalhes técnicos

**Assinatura:** `Rolagem(expressao: str, dados: tuple[int, ...], modificador: int = 0)`

**Origem da implementação:** `coral.rpg`

**Arquivo na release:** `coral/rpg.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `total` | propriedade | `total() -> int` |

:::

#### `Personagem`

Representa entidade de RPG.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | obrigatório |
| `vida` | Valor correspondente a vida. | `int` | `10` |
| `vida_max` | Valor correspondente a vida max. | `int \| None` | `None` |
| `**atributos` | Valor correspondente a atributos. | `Any` | obrigatório |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `mundo` | Obtém mundo. | `não declarado` |
| `vivo` | Indica o estado de vivo. | `bool` |
| `receber_dano` | Executa a operação `receber_dano` disponibilizada por `coral.rpg`. | `int` |
| `curar` | Executa a operação `curar` disponibilizada por `coral.rpg`. | `int` |
| `teste` | Executa a operação `teste` disponibilizada por `coral.rpg`. | `tuple[Rolagem, bool]` |

:::details Detalhes técnicos

**Assinatura:** `Personagem(nome: str, vida: int = 10, *, vida_max: int \| None = None, **atributos: Any)`

**Origem da implementação:** `coral.rpg`

**Arquivo na release:** `coral/rpg.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `nome` | posicional |
| `vida` | posicional |
| `vida_max` | nomeado |
| `**atributos` | variádico nomeado |

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `mundo` | propriedade | `mundo()` |
| `vivo` | propriedade | `vivo() -> bool` |
| `receber_dano` | método | `receber_dano(quantidade: int) -> int` |
| `curar` | método | `curar(quantidade: int) -> int` |
| `teste` | método | `teste(atributo: str, dificuldade: int = 10, *, semente: int \| None = None) -> tuple[Rolagem, bool]` |

:::

#### `CombateTurnos`

Representa CombateTurnos na API de `coral.rpg`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `participantes` | Valor correspondente a participantes. | `Iterable[Personagem]` | `()` |
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str \| None` | `None` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `adicionar` | Adiciona o valor solicitado. | `Personagem` |
| `iniciar` | Inicia o valor solicitado. | `tuple[Personagem, ...]` |
| `atual` | Obtém atual. | `Personagem \| None` |
| `proximo` | Executa a operação `proximo` disponibilizada por `coral.rpg`. | `Personagem \| None` |
| `terminou` | Indica o estado de terminou. | `bool` |

:::details Detalhes técnicos

**Assinatura:** `CombateTurnos(participantes: Iterable[Personagem] = (), *, nome: str \| None = None)`

**Origem da implementação:** `coral.rpg`

**Arquivo na release:** `coral/rpg.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `participantes` | posicional |
| `nome` | nomeado |

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `adicionar` | método | `adicionar(personagem: Personagem) -> Personagem` |
| `iniciar` | método | `iniciar(*, iniciativas: dict[str, int] \| None = None, semente: int \| None = None) -> tuple[Personagem, ...]` |
| `atual` | propriedade | `atual() -> Personagem \| None` |
| `proximo` | método | `proximo() -> Personagem \| None` |
| `terminou` | propriedade | `terminou() -> bool` |

:::

#### `EstadoRPG`

Agregado persistente do domínio RPG sobre um Mundo genérico.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `mundo` | Mundo associado à operação. | `Mundo` | obrigatório |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `mundo` | Mundo associado à operação. | `Mundo` | obrigatório |

:::details Detalhes técnicos

**Assinatura:** `EstadoRPG(mundo: Mundo)`

**Origem da implementação:** `coral.rpg`

**Arquivo na release:** `coral/rpg.py`

:::

<!-- /AUTO:API -->

## Compatibilidade

O módulo faz parte do runtime padrão e pode ser usado headless. A apresentação visual não é requisito para o domínio de RPG.
