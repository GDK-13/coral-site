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

A documentação desta página descreve a superfície detectada na **Coral 1.6.0**. O gerador do site atualiza automaticamente o inventário e a referência da API quando uma nova release é importada, mas o texto pedagógico desta seção permanece sob revisão humana.

## Referência da API

<!-- AUTO:API -->

### Classes e protocolos

#### `ObservadorMudanca`

Representa ObservadorMudanca na API de `coral.observadores_reativos`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | obrigatório |
| `leitor` | Valor correspondente a leitor. | `LeitorValor` | obrigatório |
| `acao` | Valor correspondente a acao. | `AcaoMudanca` | obrigatório |
| `modo` | Valor correspondente a modo. | `str` | `'mudanca'` |
| `limite` | Valor correspondente a limite. | `Any` | `None` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | obrigatório |
| `leitor` | Valor correspondente a leitor. | `LeitorValor` | obrigatório |
| `acao` | Valor correspondente a acao. | `AcaoMudanca` | obrigatório |
| `modo` | Valor correspondente a modo. | `str` | `'mudanca'` |
| `limite` | Valor correspondente a limite. | `Any` | `None` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `passar_de` | Executa a operação `passar_de` disponibilizada por `coral.observadores_reativos`. | `'ObservadorMudanca'` |
| `cair_abaixo_de` | Executa a operação `cair_abaixo_de` disponibilizada por `coral.observadores_reativos`. | `'ObservadorMudanca'` |
| `inicializado` | Indica o estado de inicializado. | `bool` |
| `valor_anterior` | Obtém valor anterior. | `Any` |
| `avaliar` | Executa a operação `avaliar` disponibilizada por `coral.observadores_reativos`. | `bool` |

:::details Detalhes técnicos

**Assinatura:** `ObservadorMudanca(nome: str, leitor: LeitorValor, acao: AcaoMudanca, modo: str = 'mudanca', limite: Any = None)`

**Origem da implementação:** `coral.observadores_reativos`

**Arquivo na release:** `coral/observadores_reativos.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `passar_de` | método | `passar_de(nome: str, leitor: LeitorValor, limite: Any, acao: AcaoMudanca) -> 'ObservadorMudanca'` |
| `cair_abaixo_de` | método | `cair_abaixo_de(nome: str, leitor: LeitorValor, limite: Any, acao: AcaoMudanca) -> 'ObservadorMudanca'` |
| `inicializado` | propriedade | `inicializado() -> bool` |
| `valor_anterior` | propriedade | `valor_anterior() -> Any` |
| `avaliar` | método | `avaliar(contexto: Any) -> bool` |

:::

#### `ObservadorEspacial`

Representa ObservadorEspacial na API de `coral.observadores_reativos`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | obrigatório |
| `leitor` | Valor correspondente a leitor. | `LeitorValor` | obrigatório |
| `referencia` | Valor correspondente a referencia. | `Any` | obrigatório |
| `acao` | Valor correspondente a acao. | `Callable[[Any, Any, Any], Any]` | obrigatório |
| `relacao` | Valor correspondente a relacao. | `str` | obrigatório |
| `transicao` | Valor correspondente a transicao. | `str` | `'entrar'` |
| `limite` | Valor correspondente a limite. | `Any` | `None` |
| `obter` | Valor correspondente a obter. | `Callable[[Any], Any] \| None` | `None` |
| `obter_referencia` | Valor correspondente a obter referencia. | `Callable[[Any], Any] \| None` | `None` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | obrigatório |
| `leitor` | Valor correspondente a leitor. | `LeitorValor` | obrigatório |
| `referencia` | Valor correspondente a referencia. | `Any` | obrigatório |
| `acao` | Valor correspondente a acao. | `Callable[[Any, Any, Any], Any]` | obrigatório |
| `relacao` | Valor correspondente a relacao. | `str` | obrigatório |
| `transicao` | Valor correspondente a transicao. | `str` | `'entrar'` |
| `limite` | Valor correspondente a limite. | `Any` | `None` |
| `obter` | Valor correspondente a obter. | `Callable[[Any], Any] \| None` | `None` |
| `obter_referencia` | Valor correspondente a obter referencia. | `Callable[[Any], Any] \| None` | `None` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `entrar_em_regiao` | Executa a operação `entrar_em_regiao` disponibilizada por `coral.observadores_reativos`. | `não declarado` |
| `sair_de_regiao` | Executa a operação `sair_de_regiao` disponibilizada por `coral.observadores_reativos`. | `não declarado` |
| `chegar_a_menos_de` | Executa a operação `chegar_a_menos_de` disponibilizada por `coral.observadores_reativos`. | `não declarado` |
| `tocar` | Executa o valor solicitado. | `não declarado` |
| `intersectar` | Verifica a interseção de o valor solicitado. | `não declarado` |
| `avaliar` | Executa a operação `avaliar` disponibilizada por `coral.observadores_reativos`. | `bool` |

:::details Detalhes técnicos

**Assinatura:** `ObservadorEspacial(nome: str, leitor: LeitorValor, referencia: Any, acao: Callable[[Any, Any, Any], Any], relacao: str, transicao: str = 'entrar', limite: Any = None, obter: Callable[[Any], Any] \| None = None, obter_referencia: Callable[[Any], Any] \| None = None)`

**Origem da implementação:** `coral.observadores_reativos`

**Arquivo na release:** `coral/observadores_reativos.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `entrar_em_regiao` | método | `entrar_em_regiao(nome, leitor, regiao_alvo, acao, *, obter = None, obter_referencia = None)` |
| `sair_de_regiao` | método | `sair_de_regiao(nome, leitor, regiao_alvo, acao, *, obter = None, obter_referencia = None)` |
| `chegar_a_menos_de` | método | `chegar_a_menos_de(nome, leitor, referencia, limite, acao, *, obter = None, obter_referencia = None)` |
| `tocar` | método | `tocar(nome, leitor, referencia, acao, *, obter = None, obter_referencia = None)` |
| `intersectar` | método | `intersectar(nome, leitor, referencia, acao, *, obter = None, obter_referencia = None)` |
| `avaliar` | método | `avaliar(contexto: Any) -> bool` |

:::

#### `EstadoObservavel`

Representa estado que publica mudança.

**Exemplo**

```coral
de coral.observadores_reativos importe EstadoObservavel
de coral.tempo_eventos importe Eventos

defina eventos como Eventos()
defina estado como EstadoObservavel("energia", 10, eventos=eventos)
mostre estado
```

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | obrigatório |
| `valor_inicial` | Valor correspondente a valor inicial. | `Any` | obrigatório |
| `eventos` | Fonte ou conjunto de eventos associado à operação. | `Eventos \| None` | `None` |
| `enfileirar` | Valor correspondente a enfileirar. | `bool` | `False` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `valor` | Obtém valor. | `Any` |
| `mudar` | Executa a operação `mudar` disponibilizada por `coral.observadores_reativos`. | `bool` |

:::details Detalhes técnicos

**Assinatura:** `EstadoObservavel(nome: str, valor_inicial: Any, *, eventos: Eventos \| None = None, enfileirar: bool = False) -> None`

**Origem da implementação:** `coral.observadores_reativos`

**Arquivo na release:** `coral/observadores_reativos.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `nome` | posicional |
| `valor_inicial` | posicional |
| `eventos` | nomeado |
| `enfileirar` | nomeado |

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `valor` | propriedade | `valor() -> Any` |
| `mudar` | método | `mudar(novo: Any) -> bool` |

:::

### Constantes e aliases

#### `LeitorValor`

Expõe `LeitorValor` como parte da API pública do módulo.

:::details Detalhes técnicos

**Assinatura:** `LeitorValor`

**Origem da implementação:** `coral.observadores_reativos`

**Arquivo na release:** `coral/observadores_reativos.py`

**Valor declarado:** `Callable[[Any], Any]`

:::

#### `AcaoMudanca`

Expõe `AcaoMudanca` como parte da API pública do módulo.

:::details Detalhes técnicos

**Assinatura:** `AcaoMudanca`

**Origem da implementação:** `coral.observadores_reativos`

**Arquivo na release:** `coral/observadores_reativos.py`

**Valor declarado:** `Callable[[Any, Any, Any], Any]`

:::

<!-- /AUTO:API -->
