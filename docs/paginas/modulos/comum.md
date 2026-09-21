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

## Papel no ecossistema

É a camada transversal de contratos operacionais do runtime. A maior parte dos programas não precisa começar por ela, mas bibliotecas e ferramentas a usam para expressar falhas, resultados e diagnósticos de forma uniforme.

## Conceitos principais

### Hierarquia de erros

`ErroCoral`, `ErroOperacaoCoral` e `ErroDependenciaCoral` distinguem erro controlado geral, falha operacional e ausência de dependência opcional.

### Resultado estruturado

`ResultadoOperacao` pode transportar sucesso, valor, falha e metadados sem transformar toda condição operacional em exceção.

### Diagnóstico

`DiagnosticoOperacional`, `diagnostico` e `agregar_diagnosticos` produzem informações consumíveis por CLI, VS Code e ferramentas.

### Contratos

`CONTRATO` e `CONTRATO_DIAGNOSTICO` identificam formatos transversais estáveis usados pelas superfícies que aderem a eles.

## Quando usar

Use este módulo quando o problema corresponder diretamente aos conceitos acima. Por ser um módulo complementar, ele normalmente entra em um programa para resolver uma responsabilidade específica e deve permanecer desacoplado da lógica central sempre que possível.

## Começando

```coral
de coral.comum importe diagnostico, agregar_diagnosticos

defina d1 como diagnostico("runtime", "exemplo", verdadeiro, "pronto")
defina d2 como diagnostico("arquivo", "exemplo", falso, "ausente", sugestao="crie o arquivo")
defina resumo como agregar_diagnosticos([d1, d2], origem="tutorial")
mostre resumo
```

## API essencial

| Entrada | Papel |
|---|---|
| `ResultadoOperacao` | resultado estruturado |
| `FalhaOperacao` | descrição de falha |
| `DiagnosticoOperacional` | diagnóstico estruturado |
| `diagnostico` | construir diagnóstico |
| `agregar_diagnosticos` | agregar vários diagnósticos |
| `ErroDependenciaCoral` | dependência opcional ausente |

A seção **Referência da API** no fim desta página contém a superfície pública completa detectada na release, com assinaturas, parâmetros, retornos e docstrings quando presentes.

## Fluxos comuns

1. Uma biblioteca detecta uma capacidade ou executa uma operação.
2. Quando a falha é parte do contrato operacional, ela pode ser representada por resultado ou diagnóstico estruturado.
3. Ferramentas agregam diagnósticos sem precisar interpretar textos livres de cada módulo.

## Erros e casos de borda

Não use `ResultadoOperacao` para esconder erros de programação. A camada comum serve a falhas operacionais previstas, enquanto invariantes quebradas continuam merecendo erro explícito.

## Boas práticas

* Preserve `codigo`, `dominio` e metadados úteis ao criar falhas.
* Inclua sugestão somente quando houver uma ação concreta possível.
* Evite depender do texto humano da mensagem para lógica do programa.

## Integração com outros módulos

É usada transversalmente por módulos de sistema, hardware, laboratório e ferramentas. O editor pode consumir diagnósticos estruturados sem conhecer a implementação interna de cada domínio.

## Testabilidade e previsibilidade

Teste tanto a estrutura serializável do diagnóstico quanto o conteúdo mínimo exigido pelo consumidor. Mensagens humanas podem evoluir; códigos e campos contratuais são mais apropriados para automação.

## Compatibilidade e evolução

A documentação desta página descreve a superfície detectada na **Coral 1.5.9**. O gerador do site atualiza automaticamente o inventário e a referência da API quando uma nova release é importada, mas o texto pedagógico desta seção permanece sob revisão humana.

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
