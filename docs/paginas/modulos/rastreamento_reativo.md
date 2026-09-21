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

A documentação desta página descreve a superfície detectada na **Coral 1.5.9**. O gerador do site atualiza automaticamente o inventário e a referência da API quando uma nova release é importada, mas o texto pedagógico desta seção permanece sob revisão humana.

## Referência da API

<!-- AUTO:API -->

### Classes e protocolos

#### `EntradaRastreamentoReativo(sequencia: int | None, instante: float | None, tipo: str, nome: str, decisao: str, causa_sequencia: int | None = None, prioridade: int | None = None, condicao: str | None = None, resultado_condicao: bool | None = None, detalhes: Mapping[str, Any] = field(default_factory=dict))`

Entrada pública `EntradaRastreamentoReativo` da superfície `coral.rastreamento_reativo`.

**Atributos declarados**

| Nome | Tipo | Padrão |
|---|---|---|
| `sequencia` | `int \| None` | obrigatório |
| `instante` | `float \| None` | obrigatório |
| `tipo` | `str` | obrigatório |
| `nome` | `str` | obrigatório |
| `decisao` | `str` | obrigatório |
| `causa_sequencia` | `int \| None` | `None` |
| `prioridade` | `int \| None` | `None` |
| `condicao` | `str \| None` | `None` |
| `resultado_condicao` | `bool \| None` | `None` |
| `detalhes` | `Mapping[str, Any]` | `field(default_factory=dict)` |

**Métodos e propriedades públicas**

| Nome | Tipo | Assinatura | Retorno | Descrição |
|---|---|---|---|---|
| `como_dict` | método | `como_dict() -> dict[str, Any]` | `dict[str, Any]` | Sem docstring própria na release. |

#### `RastreamentoReativo(modo: str = 'desligado')`

Entrada pública `RastreamentoReativo` da superfície `coral.rastreamento_reativo`.

**Métodos e propriedades públicas**

| Nome | Tipo | Assinatura | Retorno | Descrição |
|---|---|---|---|---|
| `historico` | propriedade | `historico() -> tuple[EntradaRastreamentoReativo, ...]` | `tuple[EntradaRastreamentoReativo, ...]` | Sem docstring própria na release. |
| `limpar` | método | `limpar() -> None` | `None` | Sem docstring própria na release. |
| `registrar` | método | `registrar(*, sequencia: int \| None, instante: float \| None, tipo: str, nome: str, decisao: str, causa_sequencia: int \| None = None, prioridade: int \| None = None, condicao: str \| None = None, resultado_condicao: bool \| None = None, detalhes: Mapping[str, Any] \| None = None) -> EntradaRastreamentoReativo \| None` | `EntradaRastreamentoReativo \| None` | Sem docstring própria na release. |
| `como_dados` | método | `como_dados() -> list[dict[str, Any]]` | `list[dict[str, Any]]` | Sem docstring própria na release. |
| `resumo_texto` | método | `resumo_texto() -> str` | `str` | Sem docstring própria na release. |

### Exceções

#### `ErroCicloReativo(...)`

O ciclo reativo excedeu o limite seguro configurado.

### Constantes e aliases

#### `MODOS_RASTREAMENTO`

Constante pública do módulo.

**Valor declarado:** `frozenset({'desligado', 'resumido', 'detalhado'})`

<!-- /AUTO:API -->
