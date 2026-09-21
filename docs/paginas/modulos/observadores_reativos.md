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

## Papel no ecossistema

Transforma mudanças de valor ou relações espaciais em reações reutilizáveis. Ele complementa o motor de regras sem obrigar cada programa a escrever manualmente o mesmo padrão “ler estado anterior, comparar, disparar ação”.

## Conceitos principais

### Mudança de valor

`ObservadorMudanca` lê um valor e decide quando uma alteração ou condição deve acionar a ação configurada.

### Relação espacial

`ObservadorEspacial` observa uma relação entre alvo e referência, com transições como entrada em uma relação espacial.

### Estado observável

`EstadoObservavel` encapsula um valor e pode publicar mudanças em um barramento `Eventos`.

### Leitor e ação

`LeitorValor` e `AcaoMudanca` documentam os contratos usados pelos observadores.

## Quando usar

Use este módulo quando o problema corresponder diretamente aos conceitos acima. Por ser um módulo complementar, ele normalmente entra em um programa para resolver uma responsabilidade específica e deve permanecer desacoplado da lógica central sempre que possível.

## Começando

```coral
de coral.observadores_reativos importe EstadoObservavel
de coral.tempo_eventos importe Eventos

defina eventos como Eventos()
defina estado como EstadoObservavel("energia", 10, eventos=eventos)
mostre estado
```

## API essencial

| Entrada | Papel |
|---|---|
| `ObservadorMudanca` | observar mudança de valor |
| `ObservadorEspacial` | observar relação espacial |
| `EstadoObservavel` | estado que publica mudança |
| `LeitorValor` | contrato de leitura |
| `AcaoMudanca` | contrato de reação |

A seção **Referência da API** no fim desta página contém a superfície pública completa detectada na release, com assinaturas, parâmetros, retornos e docstrings quando presentes.

## Fluxos comuns

1. Defina qual valor ou relação é observável.
2. Separe leitura de estado da ação produzida.
3. Atualize ou avalie o observador no ciclo apropriado do domínio.
4. Ative rastreamento quando múltiplas reações começarem a formar uma cadeia difícil de explicar.

## Erros e casos de borda

Observadores encadeados podem formar ciclos. Uma ação que altera exatamente o valor que dispara outro observador precisa de política clara de ordem e término.

## Boas práticas

* Dê nomes descritivos aos observadores.
* Mantenha a ação pequena e previsível.
* Evite efeitos externos escondidos em leitores.
* Use `coral.rastreamento_reativo` para diagnosticar cadeias maiores.

## Integração com outros módulos

`coral.tempo_eventos.Eventos` pode receber mudanças; `coral.rastreamento_reativo` explica cadeias e ciclos; `coral.replay_reativo` grava entradas reativas; `coral.regras` fornece regras de domínio mais amplas.

## Testabilidade e previsibilidade

Use estado controlado e ações registradas em memória nos testes. Assim é possível provar exatamente quando um observador dispara sem depender de interface ou tempo real.

## Compatibilidade e evolução

A documentação desta página descreve a superfície detectada na **Coral 1.5.9**. O gerador do site atualiza automaticamente o inventário e a referência da API quando uma nova release é importada, mas o texto pedagógico desta seção permanece sob revisão humana.

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
