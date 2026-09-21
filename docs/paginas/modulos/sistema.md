# coral.sistema

## Visão geral

`coral.sistema` é a fronteira oficial entre um programa Coral e o sistema operacional. Ele concentra informações do host, variáveis de ambiente, caminhos de processo e execução segura de programas externos.

<!-- AUTO:MODULO -->

**Importação:** `coral.sistema`  
**Categoria:** sistema  

informações do sistema, ambiente, caminhos e processos

### Superfície pública detectada

`ErroSistema`, `ProgramaNaoEncontrado`, `TempoLimiteExcedido`, `FalhaSistemaOperacional`, `InformacoesSistema`, `ResultadoComando`, `informacoes`, `diagnosticar_sistema`, `variavel_ambiente`, `definir_variavel_ambiente`, `remover_variavel_ambiente`, `variaveis_ambiente`, `pasta_atual`, `pasta_usuario`, `caminho`, `executar_comando`, `processo_atual`

<!-- /AUTO:MODULO -->

## Papel no ecossistema

O módulo existe para impedir que cada biblioteca invente sua própria forma de consultar o sistema ou lançar processos. Assim, erros operacionais, tempo limite e resultados de comando usam contratos previsíveis.

## Conceitos principais

### Informações do host

`InformacoesSistema` reúne sistema, versão, arquitetura, máquina, processador, versão do Python, PID e pasta atual. `informacoes()` retorna esse retrato e `diagnosticar_sistema()` acrescenta diagnóstico estruturado.

### Ambiente do processo

`variavel_ambiente`, `definir_variavel_ambiente`, `remover_variavel_ambiente` e `variaveis_ambiente` trabalham com o ambiente do processo atual. Alterar uma variável aqui não deve ser confundido com editar permanentemente a configuração do sistema do usuário.

### Caminhos

`pasta_atual`, `pasta_usuario` e `caminho` evitam espalhar concatenação manual de caminhos. Para manipulação mais ampla de caminhos e arquivos, combine com `coral.caminhos` e `coral.arquivos`.

### Processos externos

`executar_comando` recebe programa e argumentos separadamente e usa execução sem shell por padrão. O retorno é `ResultadoComando`, com código, saída, erro e duração.

## Quando usar

Use quando o programa precisa descobrir características do ambiente, ler configuração por variável, localizar pastas, executar uma ferramenta externa ou produzir um diagnóstico de suporte.

Não use como substituto de APIs de alto nível que já existem em outros módulos. Para ler um arquivo, use `coral.arquivos`; para hardware, use `coral.hardware`.

## Começando

O exemplo abaixo foi validado com o runtime 1.5.9:

```coral
de coral.sistema importe informacoes, pasta_atual, variavel_ambiente

defina ambiente como informacoes()
mostre ambiente.sistema
mostre pasta_atual()
mostre variavel_ambiente("HOME", "")
```

## API essencial

| Entrada | Papel | Assinatura |
|---|---|---|
| `informacoes` | obter retrato do host | `informacoes() -> InformacoesSistema` |
| `diagnosticar_sistema` | diagnóstico estruturado | `diagnosticar_sistema() -> dict[str, Any]` |
| `variavel_ambiente` | ler variável | `variavel_ambiente(nome: str, padrao: str \| None = None) -> str \| None` |
| `definir_variavel_ambiente` | definir variável no processo | `definir_variavel_ambiente(nome: str, valor: Any) -> None` |
| `pasta_atual` | obter diretório atual | `pasta_atual() -> Path` |
| `pasta_usuario` | obter diretório do usuário | `pasta_usuario() -> Path` |
| `caminho` | montar caminho | `caminho(*partes: Any) -> Path` |
| `executar_comando` | executar processo externo | `executar_comando(programa: str, argumentos: Iterable[Any] = (), *, pasta: str \| Path \| None = None, timeout: float \| None = None, ambiente: Mapping[str, Any] \| None = None, entrada: str \| None = None, relogio: FonteTempo \| None = None) -> ResultadoComando` |
| `processo_atual` | inspecionar processo Coral | `processo_atual() -> dict[str, Any]` |

## Executando programas externos

Passe o executável em `programa` e os argumentos em `argumentos`. Isso mantém a fronteira entre comando e dados, reduz problemas de quoting e evita depender de um shell quando ele não é necessário.

`timeout` limita o tempo de execução. `pasta` troca o diretório de trabalho do processo filho. `ambiente` permite fornecer um ambiente específico sem alterar necessariamente todo o processo pai.

## Erros e diagnóstico

`ProgramaNaoEncontrado` representa executável ausente. `TempoLimiteExcedido` registra o comando e o limite associado. `FalhaSistemaOperacional` cobre demais falhas do host. Todos derivam da superfície pública de erro do módulo.

Ao diagnosticar um problema, registre `informacoes().para_dict()` e o `ResultadoComando.para_dict()` quando isso puder ser feito sem expor segredos.

## Segurança operacional

* Prefira `executar_comando` com argumentos estruturados.
* Não coloque senhas e tokens em logs de ambiente.
* Trate stdout e stderr de programas externos como dados não confiáveis.
* Use timeout para ferramentas que podem travar ou aguardar indefinidamente.

## Integração com outros módulos

`coral.arquivos` e `coral.caminhos` cobrem armazenamento local. `coral.hardware` cobre capacidades físicas. `coral.laboratorio` pode registrar informações do sistema junto de medições.

## Testabilidade

Encapsule chamadas externas em funções pequenas. Assim, a lógica do programa pode ser testada sem lançar processos reais em todos os casos. Para código de biblioteca, prefira aceitar resultados ou adaptadores como dependência quando a interação externa for complexa.

## Referência da API

<!-- AUTO:API -->

### Funções

#### `informacoes() -> InformacoesSistema`

Entrada pública `informacoes` da superfície `coral.sistema`.

**Retorno:** `InformacoesSistema`

#### `diagnosticar_sistema() -> dict[str, Any]`

Entrada pública `diagnosticar_sistema` da superfície `coral.sistema`.

**Retorno:** `dict[str, Any]`

#### `variavel_ambiente(nome: str, padrao: str | None = None) -> str | None`

Entrada pública `variavel_ambiente` da superfície `coral.sistema`.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `nome` | `str` | obrigatório | posicional |
| `padrao` | `str \| None` | `None` | posicional |

**Retorno:** `str | None`

#### `definir_variavel_ambiente(nome: str, valor: Any) -> None`

Entrada pública `definir_variavel_ambiente` da superfície `coral.sistema`.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `nome` | `str` | obrigatório | posicional |
| `valor` | `Any` | obrigatório | posicional |

**Retorno:** `None`

#### `remover_variavel_ambiente(nome: str) -> bool`

Entrada pública `remover_variavel_ambiente` da superfície `coral.sistema`.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `nome` | `str` | obrigatório | posicional |

**Retorno:** `bool`

#### `variaveis_ambiente() -> dict[str, str]`

Entrada pública `variaveis_ambiente` da superfície `coral.sistema`.

**Retorno:** `dict[str, str]`

#### `pasta_atual() -> Path`

Entrada pública `pasta_atual` da superfície `coral.sistema`.

**Retorno:** `Path`

#### `pasta_usuario() -> Path`

Entrada pública `pasta_usuario` da superfície `coral.sistema`.

**Retorno:** `Path`

#### `caminho(*partes: Any) -> Path`

Entrada pública `caminho` da superfície `coral.sistema`.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `*partes` | `Any` | obrigatório | variádico |

**Retorno:** `Path`

#### `executar_comando(programa: str, argumentos: Iterable[Any] = (), *, pasta: str | Path | None = None, timeout: float | None = None, ambiente: Mapping[str, Any] | None = None, entrada: str | None = None, relogio: FonteTempo | None = None) -> ResultadoComando`

Executa um processo sem shell por padrão.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `programa` | `str` | obrigatório | posicional |
| `argumentos` | `Iterable[Any]` | `()` | posicional |
| `pasta` | `str \| Path \| None` | `None` | nomeado |
| `timeout` | `float \| None` | `None` | nomeado |
| `ambiente` | `Mapping[str, Any] \| None` | `None` | nomeado |
| `entrada` | `str \| None` | `None` | nomeado |
| `relogio` | `FonteTempo \| None` | `None` | nomeado |

**Retorno:** `ResultadoComando`

**Exceções observáveis no corpo:** `ValueError`, `ProgramaNaoEncontrado`, `TempoLimiteExcedido`, `FalhaSistemaOperacional`

#### `processo_atual() -> dict[str, Any]`

Entrada pública `processo_atual` da superfície `coral.sistema`.

**Retorno:** `dict[str, Any]`

### Classes e protocolos

#### `TempoLimiteExcedido(comando: tuple[str, ...], timeout: float | None, mensagem: str)`

Timeout de processo, compatível com subprocess.TimeoutExpired da linha 1.4.1.

#### `InformacoesSistema(sistema: str, versao: str, arquitetura: str, maquina: str, processador: str, python: str, pid: int, pasta_atual: str)`

Entrada pública `InformacoesSistema` da superfície `coral.sistema`.

**Atributos declarados**

| Nome | Tipo | Padrão |
|---|---|---|
| `sistema` | `str` | obrigatório |
| `versao` | `str` | obrigatório |
| `arquitetura` | `str` | obrigatório |
| `maquina` | `str` | obrigatório |
| `processador` | `str` | obrigatório |
| `python` | `str` | obrigatório |
| `pid` | `int` | obrigatório |
| `pasta_atual` | `str` | obrigatório |

**Métodos e propriedades públicas**

| Nome | Tipo | Assinatura | Retorno | Descrição |
|---|---|---|---|---|
| `para_dict` | método | `para_dict() -> dict[str, Any]` | `dict[str, Any]` | Sem docstring própria na release. |

#### `ResultadoComando(comando: tuple[str, ...], codigo: int, saida: str, erro: str, duracao_segundos: float)`

Entrada pública `ResultadoComando` da superfície `coral.sistema`.

**Atributos declarados**

| Nome | Tipo | Padrão |
|---|---|---|
| `comando` | `tuple[str, ...]` | obrigatório |
| `codigo` | `int` | obrigatório |
| `saida` | `str` | obrigatório |
| `erro` | `str` | obrigatório |
| `duracao_segundos` | `float` | obrigatório |

**Métodos e propriedades públicas**

| Nome | Tipo | Assinatura | Retorno | Descrição |
|---|---|---|---|---|
| `sucesso` | propriedade | `sucesso() -> bool` | `bool` | Sem docstring própria na release. |
| `para_dict` | método | `para_dict() -> dict[str, Any]` | `dict[str, Any]` | Sem docstring própria na release. |
| `resultado_operacao` | método | `resultado_operacao() -> ResultadoOperacao` | `ResultadoOperacao` | Sem docstring própria na release. |

### Exceções

#### `ErroSistema(...)`

Falha operacional do sistema hospedeiro traduzida para a superfície Coral.

#### `ProgramaNaoEncontrado(...)`

Executável ausente, compatível com o FileNotFoundError exposto até a 1.4.2.

#### `FalhaSistemaOperacional(...)`

Demais falhas do SO, mantendo compatibilidade com captura por OSError.

<!-- /AUTO:API -->

## Compatibilidade

Os contratos são portáveis, mas os valores refletem o sistema hospedeiro. Nome de sistema, caminhos, variáveis, disponibilidade de executáveis e comportamento de ferramentas externas variam entre Windows, Linux e outros ambientes.
