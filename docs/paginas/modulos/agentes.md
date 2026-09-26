# coral.agentes

## Visão geral

agentes genéricos, recursos, atributos, habilidades, efeitos e modificadores

<!-- AUTO:MODULO -->

**Importação:** `coral.agentes`  
**Categoria:** agentes  

agentes genéricos, recursos, atributos, habilidades, efeitos e modificadores

### Superfície pública detectada

`Agente`, `Atributo`, `Efeito`, `Habilidade`, `Modificador`, `MudancaRecurso`, `Recurso`, `criar_agente`

<!-- /AUTO:MODULO -->

## Papel no ecossistema

`coral.agentes` fornece uma base neutra para entidades que possuem recursos, atributos, efeitos e habilidades. A abstração não depende de RPG nem de Jogos. Isso permite modelar personagens, robôs, máquinas, estoques, veículos ou qualquer outra entidade com estado próprio usando os mesmos contratos.

## Conceitos principais

### Recursos

`Recurso` representa um valor limitado, como vida, energia, bateria, combustível ou estoque. O valor respeita mínimo e máximo e registra a alteração realmente aplicada quando uma operação tenta ultrapassar os limites.

### Atributos e modificadores

`Atributo` parte de um valor base e compõe `Modificador` em ordem determinística de prioridade. Modificadores podem somar, multiplicar ou substituir o valor, mantendo origem e explicação dos passos usados no cálculo.

### Efeitos

`Efeito` reúne duração, modificadores e política de empilhamento. Um efeito pode ser renovado, substituído, ignorado ou empilhado, e o agente pode declarar imunidades por nome.

### Habilidades

`Habilidade` representa uma ação reutilizável com custos de recursos, requisitos e recarga baseada em tempo simulado. O uso falha explicitamente quando a habilidade está em recarga, quando faltam recursos ou quando os requisitos não são satisfeitos.

### Agentes

`Agente` estende a entidade de `coral.mundo` e reúne recursos, atributos, habilidades, efeitos, estados e uma política opcional de ação. Ele pode existir em um `Mundo` sem criar dependência de Jogos ou RPG.

## Quando usar

Use este módulo quando o programa precisa representar entidades com capacidades e estado mutável, mas você não quer acoplar a solução a combate ou apresentação gráfica. Ele é adequado para simulações, logística, automação, jogos, modelos de produção e agentes controlados por regras.

## Começando

A release inclui `Exemplos/Agentes/01_recursos_atributos_e_efeitos.coral`:

```coral
# Recursos, atributos e efeitos sem depender de RPG ou Jogos.
de coral.agentes importe Efeito, Modificador

crie um mundo chamado fabrica
crie um agente chamado robo no mundo fabrica
defina o recurso bateria de robo como 80 de 100
consuma 25 do recurso bateria de robo
recupere 5 do recurso bateria de robo

execute robo.definir_atributo("potencia", 10)
defina turbo como Efeito("turbo", 2, modificadores={"potencia": [Modificador("bonus", 5)]})
aplique o efeito turbo a robo

execute robo.atualizar(2)
mostre robo.exigir_recurso("bateria").valor
```

## API essencial

| Entrada | Papel |
|---|---|
| `Agente` | entidade com recursos, atributos, habilidades, efeitos e estado |
| `Recurso` | valor limitado como energia, bateria, vida ou estoque |
| `Atributo` | valor base com modificadores determinísticos |
| `Modificador` | alteração rastreável aplicada a um atributo |
| `Efeito` | modificação temporária ou persistente com política de empilhamento |
| `Habilidade` | ação com custos, requisitos e recarga |
| `criar_agente` | cria e registra um agente em `coral.mundo` |

A seção **Referência da API** no fim desta página contém a superfície pública completa detectada na release.

## Fluxos comuns

1. Crie ou receba um `Mundo` quando o agente precisar participar da camada de mundo.
2. Defina recursos e atributos permanentes do agente.
3. Registre habilidades e efeitos de acordo com a regra do domínio.
4. Avance `atualizar(dt)` quando recargas e efeitos temporais precisarem evoluir.
5. Consulte eventos e o estado portável quando precisar de auditoria, persistência ou replay.

## Erros e casos de borda

Recursos rejeitam valores não finitos e impedem limites incoerentes. Custos negativos não são aceitos. Efeitos exigem uma política de empilhamento conhecida. Habilidades podem lançar erro quando ainda estão em recarga, quando faltam recursos ou quando um requisito não é atendido.

## Boas práticas

* Modele conceitos neutros em `coral.agentes` e deixe regras específicas de RPG em `coral.rpg`.
* Use nomes de recursos e atributos estáveis quando o estado será persistido.
* Prefira modificadores com `origem` quando for importante explicar de onde veio um bônus ou penalidade.
* Use tempo simulado para recargas e duração de efeitos em vez de misturar relógio real com estado de domínio.

## Integração com outros módulos

`coral.mundo` fornece identidade e participação em mundo. `coral.turnos` pode ordenar agentes sem depender de combate. `coral.simulacao` pode avançar regeneração, recargas e outros processos recorrentes. `coral.rpg` reutiliza esta fundação para especializações de personagem e combate.

## Testabilidade e previsibilidade

Recursos, atributos e modificadores são determinísticos para o mesmo estado de entrada. Em testes, avance o agente com valores explícitos de `dt`, verifique mudanças de recursos e confira `explicar()` quando a composição de atributos fizer parte do contrato.

## Compatibilidade e evolução

A superfície funcional foi introduzida na linha 1.5.10 e permanece publicada na **Coral 1.6.0**. A importação da 1.6.0 não detecta alteração nessa API; a release atual preserva a superfície enquanto fecha a coesão interna do runtime.

## Referência da API

<!-- AUTO:API -->

### Funções

#### `criar_agente`

Cria um agente genérico e o adiciona a um Mundo sem acoplar Mundo a agentes.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `mundo` | Mundo associado à operação. | `Mundo` | obrigatório |
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | obrigatório |
| `identificador` | Valor correspondente a identificador. | `str \| None` | `None` |
| `atributos` | Valor correspondente a atributos. | `Mapping[str, Any] \| None` | `None` |
| `estados` | Valor correspondente a estados. | `Iterable[str]` | `()` |

**Retorno**

Retorna um valor declarado como `Agente`.

:::details Detalhes técnicos

**Assinatura:** `criar_agente(mundo: Mundo, nome: str, *, identificador: str \| None = None, atributos: Mapping[str, Any] \| None = None, estados: Iterable[str] = ()) -> Agente`

**Origem da implementação:** `coral.agentes`

**Arquivo na release:** `coral/agentes.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `mundo` | posicional |
| `nome` | posicional |
| `identificador` | nomeado |
| `atributos` | nomeado |
| `estados` | nomeado |

**Exceções diretamente observáveis no corpo:** `TypeError`

:::

### Classes e protocolos

#### `Agente`

Entidade com identidade persistente, recursos, atributos e estado.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | obrigatório |
| `identificador` | Valor correspondente a identificador. | `str \| None` | `None` |
| `atributos` | Valor correspondente a atributos. | `Mapping[str, Any] \| None` | `None` |
| `estados` | Valor correspondente a estados. | `Iterable[str]` | `()` |
| `politica_acao` | Valor correspondente a politica acao. | `PoliticaAcao \| None` | `None` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `mundo` | Obtém mundo. | `Mundo \| None` |
| `politica_acao` | Executa a operação `politica_acao` disponibilizada por `coral.agentes`. | `PoliticaAcao \| None` |
| `definir_politica_acao` | Define politica acao. | `'Agente'` |
| `decidir` | Executa a operação `decidir` disponibilizada por `coral.agentes`. | `Any` |
| `adicionar_recurso` | Adiciona recurso. | `Recurso` |
| `definir_recurso` | Define recurso. | `Recurso` |
| `recurso` | Executa a operação `recurso` disponibilizada por `coral.agentes`. | `Recurso \| None` |
| `exigir_recurso` | Obtém recurso e sinaliza falha quando ele não está disponível. | `Recurso` |
| `adicionar_atributo` | Adiciona atributo. | `Atributo` |
| `definir_atributo` | Define atributo. | `Atributo` |
| `atributo` | Executa a operação `atributo` disponibilizada por `coral.agentes`. | `Atributo \| None` |
| `valor_atributo` | Executa a operação `valor_atributo` disponibilizada por `coral.agentes`. | `Any` |
| `adicionar_habilidade` | Adiciona habilidade. | `Habilidade` |
| `usar_habilidade` | Seleciona habilidade. | `Any` |
| `adicionar_estado` | Adiciona estado. | `bool` |
| `remover_estado` | Remove estado. | `bool` |
| `possui_estado` | Indica se possui estado. | `bool` |
| `adicionar_imunidade_efeito` | Adiciona imunidade efeito. | `bool` |
| `remover_imunidade_efeito` | Remove imunidade efeito. | `bool` |
| `imune_a` | Executa a operação `imune_a` disponibilizada por `coral.agentes`. | `bool` |
| `aplicar_efeito` | Executa a operação `aplicar_efeito` disponibilizada por `coral.agentes`. | `Efeito \| None` |
| `remover_efeito` | Remove efeito. | `bool` |
| `atualizar` | Atualiza o valor solicitado. | `None` |
| `posicao` | Executa a operação `posicao` disponibilizada por `coral.agentes`. | `tuple[float, float] \| None` |
| `definir_posicao` | Define posicao. | `'Agente'` |

:::details Detalhes técnicos

**Assinatura:** `Agente(nome: str, *, identificador: str \| None = None, atributos: Mapping[str, Any] \| None = None, estados: Iterable[str] = (), politica_acao: PoliticaAcao \| None = None) -> None`

**Origem da implementação:** `coral.agentes`

**Arquivo na release:** `coral/agentes.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `nome` | posicional |
| `identificador` | nomeado |
| `atributos` | nomeado |
| `estados` | nomeado |
| `politica_acao` | nomeado |

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `mundo` | propriedade | `mundo() -> Mundo \| None` |
| `politica_acao` | propriedade | `politica_acao() -> PoliticaAcao \| None` |
| `definir_politica_acao` | método | `definir_politica_acao(politica: PoliticaAcao \| None) -> 'Agente'` |
| `decidir` | método | `decidir(contexto: Any = None) -> Any` |
| `adicionar_recurso` | método | `adicionar_recurso(recurso: Recurso) -> Recurso` |
| `definir_recurso` | método | `definir_recurso(nome: str, valor: float = 0.0, *, minimo: float = 0.0, maximo: float \| None = None, unidade: str \| None = None) -> Recurso` |
| `recurso` | método | `recurso(nome: str) -> Recurso \| None` |
| `exigir_recurso` | método | `exigir_recurso(nome: str) -> Recurso` |
| `adicionar_atributo` | método | `adicionar_atributo(atributo: Atributo) -> Atributo` |
| `definir_atributo` | método | `definir_atributo(nome: str, base: float = 0.0) -> Atributo` |
| `atributo` | método | `atributo(nome: str) -> Atributo \| None` |
| `valor_atributo` | método | `valor_atributo(nome: str, padrao: Any = None) -> Any` |
| `adicionar_habilidade` | método | `adicionar_habilidade(habilidade: Habilidade) -> Habilidade` |
| `usar_habilidade` | método | `usar_habilidade(nome: str, alvo: Any = None, contexto: Any = None) -> Any` |
| `adicionar_estado` | método | `adicionar_estado(estado: str) -> bool` |
| `remover_estado` | método | `remover_estado(estado: str) -> bool` |
| `possui_estado` | método | `possui_estado(estado: str) -> bool` |
| `adicionar_imunidade_efeito` | método | `adicionar_imunidade_efeito(nome: str) -> bool` |
| `remover_imunidade_efeito` | método | `remover_imunidade_efeito(nome: str) -> bool` |
| `imune_a` | método | `imune_a(efeito: str \| Efeito) -> bool` |
| `aplicar_efeito` | método | `aplicar_efeito(efeito: Efeito) -> Efeito \| None` |
| `remover_efeito` | método | `remover_efeito(efeito: Efeito) -> bool` |
| `atualizar` | método | `atualizar(dt: float = 0.0) -> None` |
| `posicao` | propriedade | `posicao() -> tuple[float, float] \| None` |
| `definir_posicao` | método | `definir_posicao(x: float, y: float) -> 'Agente'` |

:::

#### `Atributo`

Valor base com composição determinística de modificadores rastreáveis.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | obrigatório |
| `base` | Base usada pela conversão ou cálculo. | `float` | `0.0` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `modificadores` | Executa a operação `modificadores` disponibilizada por `coral.agentes`. | `tuple[Modificador, ...]` |
| `valor` | Obtém valor. | `float` |
| `definir_base` | Define base. | `'Atributo'` |
| `adicionar` | Adiciona o valor solicitado. | `Modificador` |
| `modificar` | Executa a operação `modificar` disponibilizada por `coral.agentes`. | `Modificador` |
| `remover` | Remove o valor solicitado. | `bool` |
| `remover_origem` | Remove origem. | `int` |
| `explicar` | Executa a operação `explicar` disponibilizada por `coral.agentes`. | `dict[str, Any]` |

:::details Detalhes técnicos

**Assinatura:** `Atributo(nome: str, base: float = 0.0) -> None`

**Origem da implementação:** `coral.agentes`

**Arquivo na release:** `coral/agentes.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `modificadores` | propriedade | `modificadores() -> tuple[Modificador, ...]` |
| `valor` | propriedade | `valor() -> float` |
| `definir_base` | método | `definir_base(valor: float) -> 'Atributo'` |
| `adicionar` | método | `adicionar(modificador: Modificador) -> Modificador` |
| `modificar` | método | `modificar(nome: str, valor: float, *, operacao: str = 'somar', prioridade: int = 0, origem: str \| None = None, persistente: bool = True) -> Modificador` |
| `remover` | método | `remover(modificador: Modificador) -> bool` |
| `remover_origem` | método | `remover_origem(origem: str) -> int` |
| `explicar` | método | `explicar() -> dict[str, Any]` |

:::

#### `Efeito`

Condição temporal neutra que pode aplicar modificadores a um agente.

**Exemplo**

```coral
execute robo.definir_atributo("potencia", 10)
defina turbo como Efeito("turbo", 2, modificadores={"potencia": [Modificador("bonus", 5)]})
aplique o efeito turbo a robo

execute robo.atualizar(2)
```

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | obrigatório |
| `duracao` | Valor correspondente a duracao. | `float \| None` | `None` |
| `modificadores` | Valor correspondente a modificadores. | `Mapping[str, Iterable[Modificador]]` | `field(default_factory=dict)` |
| `empilhamento` | Valor correspondente a empilhamento. | `str` | `'renovar'` |
| `persistente` | Valor correspondente a persistente. | `bool` | `True` |
| `origem` | Origem usada pela operação. | `str \| None` | `None` |
| `restante` | Valor correspondente a restante. | `float \| None` | `None` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | obrigatório |
| `duracao` | Valor correspondente a duracao. | `float \| None` | `None` |
| `modificadores` | Valor correspondente a modificadores. | `Mapping[str, Iterable[Modificador]]` | `field(default_factory=dict)` |
| `empilhamento` | Valor correspondente a empilhamento. | `str` | `'renovar'` |
| `persistente` | Valor correspondente a persistente. | `bool` | `True` |
| `origem` | Origem usada pela operação. | `str \| None` | `None` |
| `restante` | Valor correspondente a restante. | `float \| None` | `None` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `ativo` | Indica o estado de ativo. | `bool` |
| `renovar` | Executa a operação `renovar` disponibilizada por `coral.agentes`. | `None` |
| `avancar` | Avança o valor solicitado. | `bool` |

:::details Detalhes técnicos

**Assinatura:** `Efeito(nome: str, duracao: float \| None = None, modificadores: Mapping[str, Iterable[Modificador]] = field(default_factory=dict), empilhamento: str = 'renovar', persistente: bool = True, origem: str \| None = None, restante: float \| None = None)`

**Origem da implementação:** `coral.agentes`

**Arquivo na release:** `coral/agentes.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `ativo` | propriedade | `ativo() -> bool` |
| `renovar` | método | `renovar() -> None` |
| `avancar` | método | `avancar(dt: float) -> bool` |

:::

#### `Habilidade`

Ação reutilizável com custos de recursos e recarga por tempo simulado.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | obrigatório |
| `acao` | Valor correspondente a acao. | `AcaoHabilidade \| None` | `None` |
| `custos` | Valor correspondente a custos. | `Mapping[str, float] \| None` | `None` |
| `recarga` | Valor correspondente a recarga. | `float` | `0.0` |
| `metadados` | Valor correspondente a metadados. | `Mapping[str, Any] \| None` | `None` |
| `requisitos` | Valor correspondente a requisitos. | `Iterable[RequisitoHabilidade]` | `()` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `pronta` | Executa a operação `pronta` disponibilizada por `coral.agentes`. | `bool` |
| `pode_usar` | Executa a operação `pode_usar` disponibilizada por `coral.agentes`. | `bool` |
| `usar` | Seleciona o valor solicitado. | `Any` |
| `atualizar` | Atualiza o valor solicitado. | `None` |

:::details Detalhes técnicos

**Assinatura:** `Habilidade(nome: str, acao: AcaoHabilidade \| None = None, *, custos: Mapping[str, float] \| None = None, recarga: float = 0.0, metadados: Mapping[str, Any] \| None = None, requisitos: Iterable[RequisitoHabilidade] = ()) -> None`

**Origem da implementação:** `coral.agentes`

**Arquivo na release:** `coral/agentes.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `nome` | posicional |
| `acao` | posicional |
| `custos` | nomeado |
| `recarga` | nomeado |
| `metadados` | nomeado |
| `requisitos` | nomeado |

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `pronta` | propriedade | `pronta() -> bool` |
| `pode_usar` | método | `pode_usar(agente: 'Agente', alvo: Any = None, contexto: Any = None) -> bool` |
| `usar` | método | `usar(agente: 'Agente', alvo: Any = None, contexto: Any = None) -> Any` |
| `atualizar` | método | `atualizar(dt: float) -> None` |

:::

#### `Modificador`

Representa alteração rastreável aplicada a um atributo.

**Exemplo**

```coral
execute robo.definir_atributo("potencia", 10)
defina turbo como Efeito("turbo", 2, modificadores={"potencia": [Modificador("bonus", 5)]})
aplique o efeito turbo a robo

execute robo.atualizar(2)
```

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | obrigatório |
| `valor` | Valor processado pela operação. | `float` | obrigatório |
| `operacao` | Valor correspondente a operacao. | `str` | `'somar'` |
| `prioridade` | Valor correspondente a prioridade. | `int` | `0` |
| `origem` | Origem usada pela operação. | `str \| None` | `None` |
| `persistente` | Valor correspondente a persistente. | `bool` | `True` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | obrigatório |
| `valor` | Valor processado pela operação. | `float` | obrigatório |
| `operacao` | Valor correspondente a operacao. | `str` | `'somar'` |
| `prioridade` | Valor correspondente a prioridade. | `int` | `0` |
| `origem` | Origem usada pela operação. | `str \| None` | `None` |
| `persistente` | Valor correspondente a persistente. | `bool` | `True` |

:::details Detalhes técnicos

**Assinatura:** `Modificador(nome: str, valor: float, operacao: str = 'somar', prioridade: int = 0, origem: str \| None = None, persistente: bool = True)`

**Origem da implementação:** `coral.agentes`

**Arquivo na release:** `coral/agentes.py`

:::

#### `MudancaRecurso`

Representa MudancaRecurso na API de `coral.agentes`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `recurso` | Valor correspondente a recurso. | `str` | obrigatório |
| `anterior` | Valor correspondente a anterior. | `float` | obrigatório |
| `atual` | Valor correspondente a atual. | `float` | obrigatório |
| `solicitado` | Valor correspondente a solicitado. | `float` | obrigatório |
| `aplicado` | Valor correspondente a aplicado. | `float` | obrigatório |
| `origem` | Origem usada pela operação. | `str \| None` | `None` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `recurso` | Valor correspondente a recurso. | `str` | obrigatório |
| `anterior` | Valor correspondente a anterior. | `float` | obrigatório |
| `atual` | Valor correspondente a atual. | `float` | obrigatório |
| `solicitado` | Valor correspondente a solicitado. | `float` | obrigatório |
| `aplicado` | Valor correspondente a aplicado. | `float` | obrigatório |
| `origem` | Origem usada pela operação. | `str \| None` | `None` |

:::details Detalhes técnicos

**Assinatura:** `MudancaRecurso(recurso: str, anterior: float, atual: float, solicitado: float, aplicado: float, origem: str \| None = None)`

**Origem da implementação:** `coral.agentes`

**Arquivo na release:** `coral/agentes.py`

:::

#### `Recurso`

Valor limitado reutilizável como vida, energia, bateria ou estoque.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | obrigatório |
| `valor` | Valor processado pela operação. | `float` | `0.0` |
| `minimo` | Limite mínimo considerado pela operação. | `float` | `0.0` |
| `maximo` | Limite máximo considerado pela operação. | `float \| None` | `None` |
| `unidade` | Valor correspondente a unidade. | `str \| None` | `None` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `valor` | Obtém valor. | `float` |
| `cheio` | Executa a operação `cheio` disponibilizada por `coral.agentes`. | `bool` |
| `vazio` | Executa a operação `vazio` disponibilizada por `coral.agentes`. | `bool` |
| `fracao` | Executa a operação `fracao` disponibilizada por `coral.agentes`. | `float \| None` |
| `definir` | Define o valor solicitado. | `MudancaRecurso` |
| `alterar` | Executa a operação `alterar` disponibilizada por `coral.agentes`. | `MudancaRecurso` |
| `consumir` | Executa a operação `consumir` disponibilizada por `coral.agentes`. | `float` |
| `recuperar` | Executa a operação `recuperar` disponibilizada por `coral.agentes`. | `float` |
| `pode_consumir` | Executa a operação `pode_consumir` disponibilizada por `coral.agentes`. | `bool` |

:::details Detalhes técnicos

**Assinatura:** `Recurso(nome: str, valor: float = 0.0, *, minimo: float = 0.0, maximo: float \| None = None, unidade: str \| None = None) -> None`

**Origem da implementação:** `coral.agentes`

**Arquivo na release:** `coral/agentes.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `nome` | posicional |
| `valor` | posicional |
| `minimo` | nomeado |
| `maximo` | nomeado |
| `unidade` | nomeado |

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `valor` | propriedade | `valor() -> float` |
| `cheio` | propriedade | `cheio() -> bool` |
| `vazio` | propriedade | `vazio() -> bool` |
| `fracao` | propriedade | `fracao() -> float \| None` |
| `definir` | método | `definir(valor: float, *, origem: str \| None = None) -> MudancaRecurso` |
| `alterar` | método | `alterar(quantidade: float, *, origem: str \| None = None) -> MudancaRecurso` |
| `consumir` | método | `consumir(quantidade: float, *, origem: str \| None = None) -> float` |
| `recuperar` | método | `recuperar(quantidade: float, *, origem: str \| None = None) -> float` |
| `pode_consumir` | método | `pode_consumir(quantidade: float) -> bool` |

:::

<!-- /AUTO:API -->
