# coral.comum

## Visão geral

`coral.comum` oferece contratos transversais de erros, resultados e diagnósticos. Este módulo reúne contratos compartilhados de erro, resultado e diagnóstico usados por outras partes da biblioteca.

<!-- AUTO:MODULO -->

**Importação:** `coral.comum`  
**Categoria:** runtime  

contratos transversais de erros, resultados e diagnósticos

### Superfície pública detectada

`CONTRATO`, `CONTRATO_DIAGNOSTICO`, `ErroCoral`, `ErroOperacaoCoral`, `ErroDependenciaCoral`, `FalhaOperacao`, `ResultadoOperacao`, `DiagnosticoOperacional`, `diagnostico`, `agregar_diagnosticos`

<!-- /AUTO:MODULO -->

## Quando usar

Este módulo reúne contratos compartilhados de erro, resultado e diagnóstico usados por outras partes da biblioteca.

Entre as entradas públicas detectadas estão `CONTRATO`, `CONTRATO_DIAGNOSTICO`, `ErroCoral`, `ErroOperacaoCoral`, `ErroDependenciaCoral`, `FalhaOperacao`.

## Começando

Uma importação seletiva começa assim:

```coral
de coral.comum importe CONTRATO, CONTRATO_DIAGNOSTICO, ErroCoral
```

Depois da importação, use o hover e o preenchimento do VS Code para consultar a assinatura exata disponível na release.

## Cuidados

É uma superfície mais estrutural. Em programas simples, normalmente você chega a esses tipos por meio de outro módulo.

## Relações com outros módulos

Na mesma área, veja também `coral.assincrono`, `coral.conversoes`, `coral.entrada`, `coral.tipos`.

## Referência da API

<!-- AUTO:API -->

### Funções

#### `diagnostico(id: str, dominio: str, ok: bool, mensagem: Any, *, capacidade: str | None = None, sugestao: str | None = None, detalhe: Mapping[str, Any] | None = None) -> DiagnosticoOperacional`

Entrada pública `diagnostico` da superfície `coral.comum`.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `id` | `str` | obrigatório | posicional |
| `dominio` | `str` | obrigatório | posicional |
| `ok` | `bool` | obrigatório | posicional |
| `mensagem` | `Any` | obrigatório | posicional |
| `capacidade` | `str \| None` | `None` | nomeado |
| `sugestao` | `str \| None` | `None` | nomeado |
| `detalhe` | `Mapping[str, Any] \| None` | `None` | nomeado |

**Retorno:** `DiagnosticoOperacional`

#### `agregar_diagnosticos(itens: Iterable[DiagnosticoOperacional | Mapping[str, Any]], *, origem: str = 'coral') -> dict[str, Any]`

Entrada pública `agregar_diagnosticos` da superfície `coral.comum`.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `itens` | `Iterable[DiagnosticoOperacional \| Mapping[str, Any]]` | obrigatório | posicional |
| `origem` | `str` | `'coral'` | nomeado |

**Retorno:** `dict[str, Any]`

### Classes e protocolos

#### `FalhaOperacao(codigo: str, mensagem: str, dominio: str, tipo: str = 'operacional', causa: str | None = None, detalhe: Mapping[str, Any] = field(default_factory=dict))`

Entrada pública `FalhaOperacao` da superfície `coral.comum`.

**Atributos declarados**

| Nome | Tipo | Padrão |
|---|---|---|
| `codigo` | `str` | obrigatório |
| `mensagem` | `str` | obrigatório |
| `dominio` | `str` | obrigatório |
| `tipo` | `str` | `'operacional'` |
| `causa` | `str \| None` | `None` |
| `detalhe` | `Mapping[str, Any]` | `field(default_factory=dict)` |

**Métodos e propriedades públicas**

| Nome | Tipo | Assinatura | Retorno | Descrição |
|---|---|---|---|---|
| `de_excecao` | método | `de_excecao(exc: BaseException, *, codigo: str, dominio: str, tipo: str = 'operacional', detalhe: Mapping[str, Any] \| None = None) -> 'FalhaOperacao'` | `'FalhaOperacao'` | Sem docstring própria na release. |
| `para_dict` | método | `para_dict() -> dict[str, Any]` | `dict[str, Any]` | Sem docstring própria na release. |

#### `ResultadoOperacao(ok: bool, valor: Any = None, falha: FalhaOperacao | None = None, metadados: Mapping[str, Any] = field(default_factory=dict))`

Representação transversal sem substituir resultados ricos de domínio.

**Atributos declarados**

| Nome | Tipo | Padrão |
|---|---|---|
| `ok` | `bool` | obrigatório |
| `valor` | `Any` | `None` |
| `falha` | `FalhaOperacao \| None` | `None` |
| `metadados` | `Mapping[str, Any]` | `field(default_factory=dict)` |

**Métodos e propriedades públicas**

| Nome | Tipo | Assinatura | Retorno | Descrição |
|---|---|---|---|---|
| `sucesso` | método | `sucesso(valor: Any = None, **metadados: Any) -> 'ResultadoOperacao'` | `'ResultadoOperacao'` | Sem docstring própria na release. |
| `erro` | método | `erro(falha: FalhaOperacao, **metadados: Any) -> 'ResultadoOperacao'` | `'ResultadoOperacao'` | Sem docstring própria na release. |
| `para_dict` | método | `para_dict() -> dict[str, Any]` | `dict[str, Any]` | Sem docstring própria na release. |

#### `DiagnosticoOperacional(id: str, dominio: str, ok: bool, mensagem: str, capacidade: str | None = None, sugestao: str | None = None, detalhe: Mapping[str, Any] = field(default_factory=dict))`

Entrada pública `DiagnosticoOperacional` da superfície `coral.comum`.

**Atributos declarados**

| Nome | Tipo | Padrão |
|---|---|---|
| `id` | `str` | obrigatório |
| `dominio` | `str` | obrigatório |
| `ok` | `bool` | obrigatório |
| `mensagem` | `str` | obrigatório |
| `capacidade` | `str \| None` | `None` |
| `sugestao` | `str \| None` | `None` |
| `detalhe` | `Mapping[str, Any]` | `field(default_factory=dict)` |

**Métodos e propriedades públicas**

| Nome | Tipo | Assinatura | Retorno | Descrição |
|---|---|---|---|---|
| `nivel` | propriedade | `nivel() -> str` | `str` | Sem docstring própria na release. |
| `para_dict` | método | `para_dict() -> dict[str, Any]` | `dict[str, Any]` | Sem docstring própria na release. |

### Exceções

#### `ErroCoral(...)`

Raiz pública dos erros controlados pela linguagem e bibliotecas Coral.

#### `ErroOperacaoCoral(...)`

Falha operacional de um recurso Coral ou de seu backend.

#### `ErroDependenciaCoral(...)`

Uma capacidade opcional não pode operar por ausência de dependência.

### Constantes e aliases

#### `CONTRATO`

Constante pública do módulo.

**Valor declarado:** `'coral.comum/1'`

#### `CONTRATO_DIAGNOSTICO`

Constante pública do módulo.

**Valor declarado:** `'coral.diagnostico.operacional/1'`

<!-- /AUTO:API -->
