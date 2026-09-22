# coral.rpg

## Visão geral

`coral.rpg` acrescenta mecânicas de RPG sobre as fundações genéricas de mundo, agentes e turnos: rolagens, personagens, vida, testes de atributo, combate e persistência do estado do domínio.

<!-- AUTO:MODULO -->

**Importação:** `coral.rpg`  
**Categoria:** rpg  

rolagens, personagens, combate e estado de RPG

### Superfície pública detectada

`Rolagem`, `ResultadoAtaque`, `rolar`, `Personagem`, `CombateTurnos`, `criar_personagem`, `registrar_combate`, `buscar_combate`, `combates_do_mundo`, `EstadoRPG`, `estado_rpg`, `salvar_estado_rpg`, `carregar_estado_rpg`

<!-- /AUTO:MODULO -->

## Papel no ecossistema

O módulo não substitui `coral.mundo`, `coral.agentes` nem `coral.turnos`. `Personagem` especializa `Agente`, vida reutiliza `Recurso` e `CombateTurnos` usa `FilaTurnos`. A apresentação continua opcional e pode ser feita por `coral.jogos`.

## Conceitos principais

### Rolagem

`rolar` interpreta uma expressão de dados e produz `Rolagem`, que preserva expressão, dados individuais, modificador e total. Semente ou gerador explícito tornam a rolagem reproduzível.

### Personagem

`Personagem` é uma conveniência de RPG construída sobre `coral.agentes.Agente`. A vida é armazenada como um `Recurso` chamado `vida`, enquanto atributos usam a mesma fundação genérica de atributos e modificadores. Métodos de dano, cura e teste concentram as regras específicas do domínio de RPG.

### Combate por turnos

`CombateTurnos` delega ordem, índice, rodada e pausa a `coral.turnos.FilaTurnos`. O combate adiciona iniciativa, participantes vivos, condições de encerramento e eventos de domínio. Combates podem ser registrados no mundo e recuperados por nome.

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

## Base genérica compartilhada

Use `coral.agentes` quando o conceito não for especificamente de RPG. Recursos como energia, bateria ou combustível, efeitos genéricos e habilidades reutilizáveis pertencem à fundação de agentes. `coral.rpg` acrescenta a semântica de personagem, vida, rolagem e combate sem duplicar esses mecanismos.

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

`coral.mundo` fornece o contexto de mundo. `coral.agentes` fornece recursos, atributos, efeitos e habilidades. `coral.turnos` fornece a fila genérica usada pelo combate. `coral.aleatorio` ajuda em sorteios, `coral.regras` modela gatilhos, `coral.persistencia` sustenta o armazenamento e `coral.jogos` apresenta personagens e combate.

## Testabilidade

Personagens, rolagens e combate funcionam sem janela. Testes podem fixar sementes, inspecionar o `Recurso` de vida e verificar estado e ordem da `FilaTurnos` antes de testar animações ou interface.

## Compatibilidade e evolução

A partir da linha 1.5.10, a API pública de RPG preserva as formas existentes enquanto sua implementação reutiliza as fundações genéricas de agentes e turnos. Essa arquitetura permanece na **Coral 1.5.12**.

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

#### `ResultadoAtaque`

Representa ResultadoAtaque na API de `coral.rpg`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `atacante` | Valor correspondente a atacante. | `'Personagem'` | obrigatório |
| `alvo` | Valor correspondente a alvo. | `'Personagem'` | obrigatório |
| `dano_base` | Valor correspondente a dano base. | `int` | obrigatório |
| `defesa` | Valor correspondente a defesa. | `int` | obrigatório |
| `critico` | Valor correspondente a critico. | `bool` | obrigatório |
| `multiplicador_critico` | Valor correspondente a multiplicador critico. | `float` | obrigatório |
| `dano_calculado` | Valor correspondente a dano calculado. | `int` | obrigatório |
| `dano_aplicado` | Valor correspondente a dano aplicado. | `int \| float` | obrigatório |
| `cancelado` | Valor correspondente a cancelado. | `bool` | `False` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `atacante` | Valor correspondente a atacante. | `'Personagem'` | obrigatório |
| `alvo` | Valor correspondente a alvo. | `'Personagem'` | obrigatório |
| `dano_base` | Valor correspondente a dano base. | `int` | obrigatório |
| `defesa` | Valor correspondente a defesa. | `int` | obrigatório |
| `critico` | Valor correspondente a critico. | `bool` | obrigatório |
| `multiplicador_critico` | Valor correspondente a multiplicador critico. | `float` | obrigatório |
| `dano_calculado` | Valor correspondente a dano calculado. | `int` | obrigatório |
| `dano_aplicado` | Valor correspondente a dano aplicado. | `int \| float` | obrigatório |
| `cancelado` | Valor correspondente a cancelado. | `bool` | `False` |

:::details Detalhes técnicos

**Assinatura:** `ResultadoAtaque(atacante: 'Personagem', alvo: 'Personagem', dano_base: int, defesa: int, critico: bool, multiplicador_critico: float, dano_calculado: int, dano_aplicado: int \| float, cancelado: bool = False)`

**Origem da implementação:** `coral.rpg`

**Arquivo na release:** `coral/rpg.py`

:::

#### `Personagem`

Conveniência de RPG construída sobre :class:`coral.agentes.Agente`.

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
| `vida` | Executa a operação `vida` disponibilizada por `coral.rpg`. | `int \| float` |
| `vida` | Executa a operação `vida` disponibilizada por `coral.rpg`. | `None` |
| `vida_max` | Executa a operação `vida_max` disponibilizada por `coral.rpg`. | `int \| float` |
| `vida_max` | Executa a operação `vida_max` disponibilizada por `coral.rpg`. | `None` |
| `vivo` | Indica o estado de vivo. | `bool` |
| `receber_dano` | Executa a operação `receber_dano` disponibilizada por `coral.rpg`. | `int \| float` |
| `curar` | Executa a operação `curar` disponibilizada por `coral.rpg`. | `int \| float` |
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
| `vida` | propriedade | `vida() -> int \| float` |
| `vida` | método | `vida(valor: int \| float) -> None` |
| `vida_max` | propriedade | `vida_max() -> int \| float` |
| `vida_max` | método | `vida_max(valor: int \| float) -> None` |
| `vivo` | propriedade | `vivo() -> bool` |
| `receber_dano` | método | `receber_dano(quantidade: int) -> int \| float` |
| `curar` | método | `curar(quantidade: int) -> int \| float` |
| `teste` | método | `teste(atributo: str, dificuldade: int = 10, *, semente: int \| None = None) -> tuple[Rolagem, bool]` |

:::

#### `CombateTurnos`

Representa CombateTurnos na API de `coral.rpg`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `participantes` | Valor correspondente a participantes. | `Iterable[Personagem]` | `()` |
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str \| None` | `None` |
| `encerramento` | Valor correspondente a encerramento. | `str` | `'ultimo_vivo'` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `ordem` | Executa a operação `ordem` disponibilizada por `coral.rpg`. | `list[Personagem]` |
| `ordem` | Executa a operação `ordem` disponibilizada por `coral.rpg`. | `None` |
| `indice` | Executa a operação `indice` disponibilizada por `coral.rpg`. | `int` |
| `indice` | Executa a operação `indice` disponibilizada por `coral.rpg`. | `None` |
| `rodada` | Executa a operação `rodada` disponibilizada por `coral.rpg`. | `int` |
| `rodada` | Executa a operação `rodada` disponibilizada por `coral.rpg`. | `None` |
| `iniciado` | Executa a operação `iniciado` disponibilizada por `coral.rpg`. | `bool` |
| `iniciado` | Executa a operação `iniciado` disponibilizada por `coral.rpg`. | `None` |
| `pausar` | Pausa o valor solicitado. | `None` |
| `retomar` | Retoma o valor solicitado. | `None` |
| `pausado` | Executa a operação `pausado` disponibilizada por `coral.rpg`. | `bool` |
| `adicionar` | Adiciona o valor solicitado. | `Personagem` |
| `iniciar` | Inicia o valor solicitado. | `tuple[Personagem, ...]` |
| `atual` | Obtém atual. | `Personagem \| None` |
| `proximo` | Executa a operação `proximo` disponibilizada por `coral.rpg`. | `Personagem \| None` |
| `atacar` | Executa a operação `atacar` disponibilizada por `coral.rpg`. | `ResultadoAtaque` |
| `encerrar` | Encerra o valor solicitado. | `None` |
| `terminou` | Indica o estado de terminou. | `bool` |

:::details Detalhes técnicos

**Assinatura:** `CombateTurnos(participantes: Iterable[Personagem] = (), *, nome: str \| None = None, encerramento: str = 'ultimo_vivo')`

**Origem da implementação:** `coral.rpg`

**Arquivo na release:** `coral/rpg.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `participantes` | posicional |
| `nome` | nomeado |
| `encerramento` | nomeado |

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `ordem` | propriedade | `ordem() -> list[Personagem]` |
| `ordem` | método | `ordem(valor: Iterable[Personagem]) -> None` |
| `indice` | propriedade | `indice() -> int` |
| `indice` | método | `indice(valor: int) -> None` |
| `rodada` | propriedade | `rodada() -> int` |
| `rodada` | método | `rodada(valor: int) -> None` |
| `iniciado` | propriedade | `iniciado() -> bool` |
| `iniciado` | método | `iniciado(valor: bool) -> None` |
| `pausar` | método | `pausar() -> None` |
| `retomar` | método | `retomar() -> None` |
| `pausado` | propriedade | `pausado() -> bool` |
| `adicionar` | método | `adicionar(personagem: Personagem) -> Personagem` |
| `iniciar` | método | `iniciar(*, iniciativas: dict[str, int] \| None = None, semente: int \| None = None) -> tuple[Personagem, ...]` |
| `atual` | propriedade | `atual() -> Personagem \| None` |
| `proximo` | método | `proximo() -> Personagem \| None` |
| `atacar` | método | `atacar(atacante: Personagem, alvo: Personagem, dano: int, *, defesa: int \| None = None, chance_critico: float = 0.0, multiplicador_critico: float = 2.0, exigir_turno: bool = True) -> ResultadoAtaque` |
| `encerrar` | método | `encerrar() -> None` |
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
