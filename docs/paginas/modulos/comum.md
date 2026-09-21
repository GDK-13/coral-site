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

#### `diagnostico`

Construir diagnóstico.

**Exemplo**

```coral
de coral.comum importe diagnostico, agregar_diagnosticos

defina d1 como diagnostico("runtime", "exemplo", verdadeiro, "pronto")
defina d2 como diagnostico("arquivo", "exemplo", falso, "ausente", sugestao="crie o arquivo")
defina resumo como agregar_diagnosticos([d1, d2], origem="tutorial")
mostre resumo
```

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `id` | Valor correspondente a identificador. | `str` | obrigatório |
| `dominio` | Valor correspondente a dominio. | `str` | obrigatório |
| `ok` | Valor correspondente a ok. | `bool` | obrigatório |
| `mensagem` | Valor correspondente a mensagem. | `Any` | obrigatório |
| `capacidade` | Valor correspondente a capacidade. | `str \| None` | `None` |
| `sugestao` | Valor correspondente a sugestao. | `str \| None` | `None` |
| `detalhe` | Valor correspondente a detalhe. | `Mapping[str, Any] \| None` | `None` |

**Retorno**

Retorna um valor declarado como `DiagnosticoOperacional`.

:::details Detalhes técnicos

**Assinatura:** `diagnostico(id: str, dominio: str, ok: bool, mensagem: Any, *, capacidade: str \| None = None, sugestao: str \| None = None, detalhe: Mapping[str, Any] \| None = None) -> DiagnosticoOperacional`

**Origem da implementação:** `coral.comum`

**Arquivo na release:** `coral/comum.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `id` | posicional |
| `dominio` | posicional |
| `ok` | posicional |
| `mensagem` | posicional |
| `capacidade` | nomeado |
| `sugestao` | nomeado |
| `detalhe` | nomeado |

:::

#### `agregar_diagnosticos`

Agregar vários diagnósticos.

**Exemplo**

```coral
de coral.comum importe diagnostico, agregar_diagnosticos

defina d1 como diagnostico("runtime", "exemplo", verdadeiro, "pronto")
defina d2 como diagnostico("arquivo", "exemplo", falso, "ausente", sugestao="crie o arquivo")
defina resumo como agregar_diagnosticos([d1, d2], origem="tutorial")
mostre resumo
```

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `itens` | Valor correspondente a itens. | `Iterable[DiagnosticoOperacional \| Mapping[str, Any]]` | obrigatório |
| `origem` | Origem usada pela operação. | `str` | `'coral'` |

**Retorno**

Retorna um valor declarado como `dict[str, Any]`.

:::details Detalhes técnicos

**Assinatura:** `agregar_diagnosticos(itens: Iterable[DiagnosticoOperacional \| Mapping[str, Any]], *, origem: str = 'coral') -> dict[str, Any]`

**Origem da implementação:** `coral.comum`

**Arquivo na release:** `coral/comum.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `itens` | posicional |
| `origem` | nomeado |

:::

### Classes e protocolos

#### `FalhaOperacao`

Representa descrição de falha.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `codigo` | Valor correspondente a codigo. | `str` | obrigatório |
| `mensagem` | Valor correspondente a mensagem. | `str` | obrigatório |
| `dominio` | Valor correspondente a dominio. | `str` | obrigatório |
| `tipo` | Tipo solicitado para o resultado, quando o módulo oferece essa escolha. | `str` | `'operacional'` |
| `causa` | Valor correspondente a causa. | `str \| None` | `None` |
| `detalhe` | Valor correspondente a detalhe. | `Mapping[str, Any]` | `field(default_factory=dict)` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `codigo` | Valor correspondente a codigo. | `str` | obrigatório |
| `mensagem` | Valor correspondente a mensagem. | `str` | obrigatório |
| `dominio` | Valor correspondente a dominio. | `str` | obrigatório |
| `tipo` | Tipo solicitado para o resultado, quando o módulo oferece essa escolha. | `str` | `'operacional'` |
| `causa` | Valor correspondente a causa. | `str \| None` | `None` |
| `detalhe` | Valor correspondente a detalhe. | `Mapping[str, Any]` | `field(default_factory=dict)` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `de_excecao` | Interpreta ou reconstrói um valor a partir de excecao. | `'FalhaOperacao'` |
| `para_dict` | Converte o valor para dict. | `dict[str, Any]` |

:::details Detalhes técnicos

**Assinatura:** `FalhaOperacao(codigo: str, mensagem: str, dominio: str, tipo: str = 'operacional', causa: str \| None = None, detalhe: Mapping[str, Any] = field(default_factory=dict))`

**Origem da implementação:** `coral.comum`

**Arquivo na release:** `coral/comum.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `de_excecao` | método | `de_excecao(exc: BaseException, *, codigo: str, dominio: str, tipo: str = 'operacional', detalhe: Mapping[str, Any] \| None = None) -> 'FalhaOperacao'` |
| `para_dict` | método | `para_dict() -> dict[str, Any]` |

:::

#### `ResultadoOperacao`

Representação transversal sem substituir resultados ricos de domínio.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `ok` | Valor correspondente a ok. | `bool` | obrigatório |
| `valor` | Valor processado pela operação. | `Any` | `None` |
| `falha` | Valor correspondente a falha. | `FalhaOperacao \| None` | `None` |
| `metadados` | Valor correspondente a metadados. | `Mapping[str, Any]` | `field(default_factory=dict)` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `ok` | Valor correspondente a ok. | `bool` | obrigatório |
| `valor` | Valor processado pela operação. | `Any` | `None` |
| `falha` | Valor correspondente a falha. | `FalhaOperacao \| None` | `None` |
| `metadados` | Valor correspondente a metadados. | `Mapping[str, Any]` | `field(default_factory=dict)` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `sucesso` | Indica o estado de sucesso. | `'ResultadoOperacao'` |
| `erro` | Executa a operação `erro` disponibilizada por `coral.comum`. | `'ResultadoOperacao'` |
| `para_dict` | Converte o valor para dict. | `dict[str, Any]` |

:::details Detalhes técnicos

**Assinatura:** `ResultadoOperacao(ok: bool, valor: Any = None, falha: FalhaOperacao \| None = None, metadados: Mapping[str, Any] = field(default_factory=dict))`

**Origem da implementação:** `coral.comum`

**Arquivo na release:** `coral/comum.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `sucesso` | método | `sucesso(valor: Any = None, **metadados: Any) -> 'ResultadoOperacao'` |
| `erro` | método | `erro(falha: FalhaOperacao, **metadados: Any) -> 'ResultadoOperacao'` |
| `para_dict` | método | `para_dict() -> dict[str, Any]` |

:::

#### `DiagnosticoOperacional`

Representa diagnóstico estruturado.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `id` | Valor correspondente a identificador. | `str` | obrigatório |
| `dominio` | Valor correspondente a dominio. | `str` | obrigatório |
| `ok` | Valor correspondente a ok. | `bool` | obrigatório |
| `mensagem` | Valor correspondente a mensagem. | `str` | obrigatório |
| `capacidade` | Valor correspondente a capacidade. | `str \| None` | `None` |
| `sugestao` | Valor correspondente a sugestao. | `str \| None` | `None` |
| `detalhe` | Valor correspondente a detalhe. | `Mapping[str, Any]` | `field(default_factory=dict)` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `id` | Valor correspondente a identificador. | `str` | obrigatório |
| `dominio` | Valor correspondente a dominio. | `str` | obrigatório |
| `ok` | Valor correspondente a ok. | `bool` | obrigatório |
| `mensagem` | Valor correspondente a mensagem. | `str` | obrigatório |
| `capacidade` | Valor correspondente a capacidade. | `str \| None` | `None` |
| `sugestao` | Valor correspondente a sugestao. | `str \| None` | `None` |
| `detalhe` | Valor correspondente a detalhe. | `Mapping[str, Any]` | `field(default_factory=dict)` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `nivel` | Executa a operação `nivel` disponibilizada por `coral.comum`. | `str` |
| `para_dict` | Converte o valor para dict. | `dict[str, Any]` |

:::details Detalhes técnicos

**Assinatura:** `DiagnosticoOperacional(id: str, dominio: str, ok: bool, mensagem: str, capacidade: str \| None = None, sugestao: str \| None = None, detalhe: Mapping[str, Any] = field(default_factory=dict))`

**Origem da implementação:** `coral.comum`

**Arquivo na release:** `coral/comum.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `nivel` | propriedade | `nivel() -> str` |
| `para_dict` | método | `para_dict() -> dict[str, Any]` |

:::

### Exceções

#### `ErroCoral`

Raiz pública dos erros controlados pela linguagem e bibliotecas Coral.

:::details Detalhes técnicos

**Assinatura:** `ErroCoral(...)`

**Origem da implementação:** `coral.comum`

**Arquivo na release:** `coral/comum.py`

:::

#### `ErroOperacaoCoral`

Falha operacional de um recurso Coral ou de seu backend.

:::details Detalhes técnicos

**Assinatura:** `ErroOperacaoCoral(...)`

**Origem da implementação:** `coral.comum`

**Arquivo na release:** `coral/comum.py`

:::

#### `ErroDependenciaCoral`

Uma capacidade opcional não pode operar por ausência de dependência.

:::details Detalhes técnicos

**Assinatura:** `ErroDependenciaCoral(...)`

**Origem da implementação:** `coral.comum`

**Arquivo na release:** `coral/comum.py`

:::

### Constantes e aliases

#### `CONTRATO`

Expõe a constante pública `CONTRATO`.

:::details Detalhes técnicos

**Assinatura:** `CONTRATO`

**Origem da implementação:** `coral.comum`

**Arquivo na release:** `coral/comum.py`

**Valor declarado:** `'coral.comum/1'`

:::

#### `CONTRATO_DIAGNOSTICO`

Expõe a constante pública `CONTRATO_DIAGNOSTICO`.

:::details Detalhes técnicos

**Assinatura:** `CONTRATO_DIAGNOSTICO`

**Origem da implementação:** `coral.comum`

**Arquivo na release:** `coral/comum.py`

**Valor declarado:** `'coral.diagnostico.operacional/1'`

:::

<!-- /AUTO:API -->
