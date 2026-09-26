# coral.rastreamento_reativo

## Visão geral

`coral.rastreamento_reativo` oferece rastreamento estruturado e proteção de ciclos reativos. Use para registrar a cadeia de reações e proteger o sistema contra ciclos reativos.

<!-- AUTO:MODULO -->

**Importação:** `coral.rastreamento_reativo`  
**Categoria:** reativo  

rastreamento estruturado e proteção de ciclos reativos

### Superfície pública detectada

`MODOS_RASTREAMENTO`, `ErroCicloReativo`, `EntradaRastreamentoReativo`, `RastreamentoReativo`

<!-- /AUTO:MODULO -->

## Papel no ecossistema

Registra decisões do sistema reativo de forma estruturada e impõe proteção contra ciclos. É uma ferramenta de explicabilidade e segurança operacional, não apenas um log textual.

## Conceitos principais

### Entrada estruturada

`EntradaRastreamentoReativo` registra sequência, instante, tipo, nome, decisão, causa, prioridade, condição e detalhes.

### Modos

`MODOS_RASTREAMENTO` define os níveis aceitos e `RastreamentoReativo` controla como o registro é produzido.

### Causalidade

`causa_sequencia` permite ligar uma reação à entrada que a originou.

### Proteção de ciclo

`ErroCicloReativo` sinaliza que o sistema ultrapassou o limite seguro em uma cadeia reativa.

## Quando usar

Use este módulo quando o problema corresponder diretamente aos conceitos acima. Por ser um módulo complementar, ele normalmente entra em um programa para resolver uma responsabilidade específica e deve permanecer desacoplado da lógica central sempre que possível.

## Começando

```coral
de coral.rastreamento_reativo importe RastreamentoReativo

defina rastreamento como RastreamentoReativo("resumo")
mostre rastreamento
```

## API essencial

| Entrada | Papel |
|---|---|
| `RastreamentoReativo` | coletar rastreamento |
| `EntradaRastreamentoReativo` | registro estruturado |
| `ErroCicloReativo` | proteção de ciclo |
| `MODOS_RASTREAMENTO` | modos aceitos |

A seção **Referência da API** no fim desta página contém a superfície pública completa detectada na release, com assinaturas, parâmetros, retornos e docstrings quando presentes.

## Fluxos comuns

1. Ative rastreamento quando precisar explicar uma cadeia de reações.
2. Registre causa e sequência para preservar a ordem causal.
3. Ao detectar ciclo, trate a causa; não aumente limites apenas para silenciar o sintoma.
4. Use os registros em diagnóstico, testes ou replay conforme a necessidade.

## Erros e casos de borda

Uma cadeia infinita de mudanças pode parecer apenas “muitos eventos”. A proteção de ciclo existe para transformar esse crescimento em falha explicável antes que o processo consuma recursos indefinidamente.

## Boas práticas

* Mantenha nomes estáveis para regras e observadores.
* Registre detalhes úteis, mas não coloque objetos enormes em cada entrada.
* Use o modo mais detalhado apenas quando necessário para diagnóstico.

## Integração com outros módulos

`coral.observadores_reativos` gera reações observáveis; `coral.regras` coordena regras; `coral.replay_reativo` pode preservar entradas para reprodução.

## Testabilidade e previsibilidade

Testes devem verificar ordem, causa e decisão, não apenas quantidade de logs. Inclua um caso que provoque ciclo controlado e confirme `ErroCicloReativo`.

## Compatibilidade e evolução

A documentação desta página descreve a superfície detectada na **Coral 1.6.0**. O gerador do site atualiza automaticamente o inventário e a referência da API quando uma nova release é importada, mas o texto pedagógico desta seção permanece sob revisão humana.

## Referência da API

<!-- AUTO:API -->

### Classes e protocolos

#### `EntradaRastreamentoReativo`

Representa registro estruturado.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `sequencia` | Valor correspondente a sequencia. | `int \| None` | obrigatório |
| `instante` | Valor correspondente a instante. | `float \| None` | obrigatório |
| `tipo` | Tipo solicitado para o resultado, quando o módulo oferece essa escolha. | `str` | obrigatório |
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | obrigatório |
| `decisao` | Valor correspondente a decisao. | `str` | obrigatório |
| `causa_sequencia` | Valor correspondente a causa sequencia. | `int \| None` | `None` |
| `prioridade` | Valor correspondente a prioridade. | `int \| None` | `None` |
| `condicao` | Valor correspondente a condicao. | `str \| None` | `None` |
| `resultado_condicao` | Valor correspondente a resultado condicao. | `bool \| None` | `None` |
| `detalhes` | Valor correspondente a detalhes. | `Mapping[str, Any]` | `field(default_factory=dict)` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `sequencia` | Valor correspondente a sequencia. | `int \| None` | obrigatório |
| `instante` | Valor correspondente a instante. | `float \| None` | obrigatório |
| `tipo` | Tipo solicitado para o resultado, quando o módulo oferece essa escolha. | `str` | obrigatório |
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | obrigatório |
| `decisao` | Valor correspondente a decisao. | `str` | obrigatório |
| `causa_sequencia` | Valor correspondente a causa sequencia. | `int \| None` | `None` |
| `prioridade` | Valor correspondente a prioridade. | `int \| None` | `None` |
| `condicao` | Valor correspondente a condicao. | `str \| None` | `None` |
| `resultado_condicao` | Valor correspondente a resultado condicao. | `bool \| None` | `None` |
| `detalhes` | Valor correspondente a detalhes. | `Mapping[str, Any]` | `field(default_factory=dict)` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `como_dict` | Representa o valor como dict. | `dict[str, Any]` |

:::details Detalhes técnicos

**Assinatura:** `EntradaRastreamentoReativo(sequencia: int \| None, instante: float \| None, tipo: str, nome: str, decisao: str, causa_sequencia: int \| None = None, prioridade: int \| None = None, condicao: str \| None = None, resultado_condicao: bool \| None = None, detalhes: Mapping[str, Any] = field(default_factory=dict))`

**Origem da implementação:** `coral.rastreamento_reativo`

**Arquivo na release:** `coral/rastreamento_reativo.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `como_dict` | método | `como_dict() -> dict[str, Any]` |

:::

#### `RastreamentoReativo`

Representa RastreamentoReativo na API de `coral.rastreamento_reativo`.

**Exemplo**

```coral
de coral.rastreamento_reativo importe RastreamentoReativo

defina rastreamento como RastreamentoReativo("resumo")
mostre rastreamento
```

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `modo` | Valor correspondente a modo. | `str` | `'desligado'` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `historico` | Obtém historico. | `tuple[EntradaRastreamentoReativo, ...]` |
| `limpar` | Limpa o valor solicitado. | `None` |
| `registrar` | Registra o valor solicitado. | `EntradaRastreamentoReativo \| None` |
| `como_dados` | Representa o valor como dados. | `list[dict[str, Any]]` |
| `resumo_texto` | Executa a operação `resumo_texto` disponibilizada por `coral.rastreamento_reativo`. | `str` |

:::details Detalhes técnicos

**Assinatura:** `RastreamentoReativo(modo: str = 'desligado')`

**Origem da implementação:** `coral.rastreamento_reativo`

**Arquivo na release:** `coral/rastreamento_reativo.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `historico` | propriedade | `historico() -> tuple[EntradaRastreamentoReativo, ...]` |
| `limpar` | método | `limpar() -> None` |
| `registrar` | método | `registrar(*, sequencia: int \| None, instante: float \| None, tipo: str, nome: str, decisao: str, causa_sequencia: int \| None = None, prioridade: int \| None = None, condicao: str \| None = None, resultado_condicao: bool \| None = None, detalhes: Mapping[str, Any] \| None = None) -> EntradaRastreamentoReativo \| None` |
| `como_dados` | método | `como_dados() -> list[dict[str, Any]]` |
| `resumo_texto` | método | `resumo_texto() -> str` |

:::

### Exceções

#### `ErroCicloReativo`

O ciclo reativo excedeu o limite seguro configurado.

:::details Detalhes técnicos

**Assinatura:** `ErroCicloReativo(...)`

**Origem da implementação:** `coral.rastreamento_reativo`

**Arquivo na release:** `coral/rastreamento_reativo.py`

:::

### Constantes e aliases

#### `MODOS_RASTREAMENTO`

Expõe a constante pública `MODOS_RASTREAMENTO`.

:::details Detalhes técnicos

**Assinatura:** `MODOS_RASTREAMENTO`

**Origem da implementação:** `coral.rastreamento_reativo`

**Arquivo na release:** `coral/rastreamento_reativo.py`

**Valor declarado:** `frozenset({'desligado', 'resumido', 'detalhado'})`

:::

<!-- /AUTO:API -->
