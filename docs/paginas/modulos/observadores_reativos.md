# coral.observadores_reativos

## Visão geral

`coral.observadores_reativos` oferece observadores reutilizáveis de mudança e espaço. Use para observar mudanças de valor ou espaço e reagir sem acoplar diretamente produtor e consumidor.

<!-- AUTO:MODULO -->

**Importação:** `coral.observadores_reativos`  
**Categoria:** reativo  

observadores reutilizáveis de mudança e espaço

### Superfície pública detectada

`LeitorValor`, `AcaoMudanca`, `ObservadorMudanca`, `ObservadorEspacial`, `EstadoObservavel`

<!-- /AUTO:MODULO -->

## Quando usar

Use para observar mudanças de valor ou espaço e reagir sem acoplar diretamente produtor e consumidor.

Entre as entradas públicas detectadas estão `LeitorValor`, `AcaoMudanca`, `ObservadorMudanca`, `ObservadorEspacial`, `EstadoObservavel`.

## Começando

Uma importação seletiva começa assim:

```coral
de coral.observadores_reativos importe LeitorValor, AcaoMudanca, ObservadorMudanca
```

Depois da importação, use o hover e o preenchimento do VS Code para consultar a assinatura exata disponível na release.

## Cuidados

Evite cadeias reativas difíceis de rastrear. Combine observadores com rastreamento quando o fluxo crescer.

## Relações com outros módulos

Na mesma área, veja também `coral.rastreamento_reativo`, `coral.replay_reativo`, `coral.sequencias_reativas`.

## Referência da API

<!-- AUTO:API -->

### Classes e protocolos

#### `ObservadorMudanca(nome: str, leitor: LeitorValor, acao: AcaoMudanca, modo: str = 'mudanca', limite: Any = None)`

Entrada pública `ObservadorMudanca` da superfície `coral.observadores_reativos`.

**Atributos declarados**

| Nome | Tipo | Padrão |
|---|---|---|
| `nome` | `str` | obrigatório |
| `leitor` | `LeitorValor` | obrigatório |
| `acao` | `AcaoMudanca` | obrigatório |
| `modo` | `str` | `'mudanca'` |
| `limite` | `Any` | `None` |

**Métodos e propriedades públicas**

| Nome | Tipo | Assinatura | Retorno | Descrição |
|---|---|---|---|---|
| `passar_de` | método | `passar_de(nome: str, leitor: LeitorValor, limite: Any, acao: AcaoMudanca) -> 'ObservadorMudanca'` | `'ObservadorMudanca'` | Sem docstring própria na release. |
| `cair_abaixo_de` | método | `cair_abaixo_de(nome: str, leitor: LeitorValor, limite: Any, acao: AcaoMudanca) -> 'ObservadorMudanca'` | `'ObservadorMudanca'` | Sem docstring própria na release. |
| `inicializado` | propriedade | `inicializado() -> bool` | `bool` | Sem docstring própria na release. |
| `valor_anterior` | propriedade | `valor_anterior() -> Any` | `Any` | Sem docstring própria na release. |
| `avaliar` | método | `avaliar(contexto: Any) -> bool` | `bool` | Sem docstring própria na release. |

#### `ObservadorEspacial(nome: str, leitor: LeitorValor, referencia: Any, acao: Callable[[Any, Any, Any], Any], relacao: str, transicao: str = 'entrar', limite: Any = None, obter: Callable[[Any], Any] | None = None, obter_referencia: Callable[[Any], Any] | None = None)`

Entrada pública `ObservadorEspacial` da superfície `coral.observadores_reativos`.

**Atributos declarados**

| Nome | Tipo | Padrão |
|---|---|---|
| `nome` | `str` | obrigatório |
| `leitor` | `LeitorValor` | obrigatório |
| `referencia` | `Any` | obrigatório |
| `acao` | `Callable[[Any, Any, Any], Any]` | obrigatório |
| `relacao` | `str` | obrigatório |
| `transicao` | `str` | `'entrar'` |
| `limite` | `Any` | `None` |
| `obter` | `Callable[[Any], Any] \| None` | `None` |
| `obter_referencia` | `Callable[[Any], Any] \| None` | `None` |

**Métodos e propriedades públicas**

| Nome | Tipo | Assinatura | Retorno | Descrição |
|---|---|---|---|---|
| `entrar_em_regiao` | método | `entrar_em_regiao(nome, leitor, regiao_alvo, acao, *, obter = None, obter_referencia = None)` | `não declarado` | Sem docstring própria na release. |
| `sair_de_regiao` | método | `sair_de_regiao(nome, leitor, regiao_alvo, acao, *, obter = None, obter_referencia = None)` | `não declarado` | Sem docstring própria na release. |
| `chegar_a_menos_de` | método | `chegar_a_menos_de(nome, leitor, referencia, limite, acao, *, obter = None, obter_referencia = None)` | `não declarado` | Sem docstring própria na release. |
| `tocar` | método | `tocar(nome, leitor, referencia, acao, *, obter = None, obter_referencia = None)` | `não declarado` | Sem docstring própria na release. |
| `intersectar` | método | `intersectar(nome, leitor, referencia, acao, *, obter = None, obter_referencia = None)` | `não declarado` | Sem docstring própria na release. |
| `avaliar` | método | `avaliar(contexto: Any) -> bool` | `bool` | Sem docstring própria na release. |

#### `EstadoObservavel(nome: str, valor_inicial: Any, *, eventos: Eventos | None = None, enfileirar: bool = False) -> None`

Entrada pública `EstadoObservavel` da superfície `coral.observadores_reativos`.

**Métodos e propriedades públicas**

| Nome | Tipo | Assinatura | Retorno | Descrição |
|---|---|---|---|---|
| `valor` | propriedade | `valor() -> Any` | `Any` | Sem docstring própria na release. |
| `mudar` | método | `mudar(novo: Any) -> bool` | `bool` | Sem docstring própria na release. |

### Constantes e aliases

#### `LeitorValor`

Alias público de tipo ou valor.

**Valor declarado:** `Callable[[Any], Any]`

#### `AcaoMudanca`

Alias público de tipo ou valor.

**Valor declarado:** `Callable[[Any, Any, Any], Any]`

<!-- /AUTO:API -->
