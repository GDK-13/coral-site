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

O exemplo abaixo foi validado com o runtime 1.6.0:

```coral
de coral.sistema importe informacoes, pasta_atual, variavel_ambiente

defina ambiente como informacoes()
mostre ambiente.sistema
mostre pasta_atual()
mostre variavel_ambiente("HOME", "")
```

:::resultado
O programa mostra três informações do ambiente atual: o sistema operacional identificado, a pasta de trabalho e o valor de `HOME`. Os valores exatos dependem do computador.
:::

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

#### `informacoes`

Obter retrato do host.

**Exemplo**

```coral
de coral.sistema importe informacoes, pasta_atual, variavel_ambiente

defina ambiente como informacoes()
mostre ambiente.sistema
mostre pasta_atual()
mostre variavel_ambiente("HOME", "")
```

**Retorno**

Retorna um valor declarado como `InformacoesSistema`.

:::details Detalhes técnicos

**Assinatura:** `informacoes() -> InformacoesSistema`

**Origem da implementação:** `coral.sistema`

**Arquivo na release:** `coral/sistema.py`

:::

#### `diagnosticar_sistema`

Produz informações de diagnóstico para sistema.

**Retorno**

Retorna um valor declarado como `dict[str, Any]`.

:::details Detalhes técnicos

**Assinatura:** `diagnosticar_sistema() -> dict[str, Any]`

**Origem da implementação:** `coral.sistema`

**Arquivo na release:** `coral/sistema.py`

:::

#### `variavel_ambiente`

Ler variável.

**Exemplo**

```coral
de coral.sistema importe informacoes, pasta_atual, variavel_ambiente

defina ambiente como informacoes()
mostre ambiente.sistema
mostre pasta_atual()
mostre variavel_ambiente("HOME", "")
```

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | obrigatório |
| `padrao` | Valor usado quando não há resultado específico disponível. | `str \| None` | `None` |

**Retorno**

Retorna um valor declarado como `str | None`.

:::details Detalhes técnicos

**Assinatura:** `variavel_ambiente(nome: str, padrao: str \| None = None) -> str \| None`

**Origem da implementação:** `coral.sistema`

**Arquivo na release:** `coral/sistema.py`

:::

#### `definir_variavel_ambiente`

Definir variável no processo.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | obrigatório |
| `valor` | Valor processado pela operação. | `Any` | obrigatório |

**Retorno**

Não produz um valor de retorno útil; o efeito ocorre no estado ou recurso alvo.

:::details Detalhes técnicos

**Assinatura:** `definir_variavel_ambiente(nome: str, valor: Any) -> None`

**Origem da implementação:** `coral.sistema`

**Arquivo na release:** `coral/sistema.py`

:::

#### `remover_variavel_ambiente`

Remove variavel ambiente.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | obrigatório |

**Retorno**

Retorna um valor declarado como `bool`.

:::details Detalhes técnicos

**Assinatura:** `remover_variavel_ambiente(nome: str) -> bool`

**Origem da implementação:** `coral.sistema`

**Arquivo na release:** `coral/sistema.py`

:::

#### `variaveis_ambiente`

Obtém variaveis ambiente.

**Retorno**

Retorna um valor declarado como `dict[str, str]`.

:::details Detalhes técnicos

**Assinatura:** `variaveis_ambiente() -> dict[str, str]`

**Origem da implementação:** `coral.sistema`

**Arquivo na release:** `coral/sistema.py`

:::

#### `pasta_atual`

Obter diretório atual.

**Exemplo**

```coral
de coral.sistema importe informacoes, pasta_atual, variavel_ambiente

defina ambiente como informacoes()
mostre ambiente.sistema
mostre pasta_atual()
mostre variavel_ambiente("HOME", "")
```

**Retorno**

Retorna um valor declarado como `Path`.

:::details Detalhes técnicos

**Assinatura:** `pasta_atual() -> Path`

**Origem da implementação:** `coral.sistema`

**Arquivo na release:** `coral/sistema.py`

:::

#### `pasta_usuario`

Obter diretório do usuário.

**Retorno**

Retorna um valor declarado como `Path`.

:::details Detalhes técnicos

**Assinatura:** `pasta_usuario() -> Path`

**Origem da implementação:** `coral.sistema`

**Arquivo na release:** `coral/sistema.py`

:::

#### `caminho`

Montar caminho.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `*partes` | Valor correspondente a partes. | `Any` | obrigatório |

**Retorno**

Retorna um valor declarado como `Path`.

:::details Detalhes técnicos

**Assinatura:** `caminho(*partes: Any) -> Path`

**Origem da implementação:** `coral.sistema`

**Arquivo na release:** `coral/sistema.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `*partes` | variádico |

:::

#### `executar_comando`

Executa um processo sem shell por padrão.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `programa` | Valor correspondente a programa. | `str` | obrigatório |
| `argumentos` | Valor correspondente a argumentos. | `Iterable[Any]` | `()` |
| `pasta` | Valor correspondente a pasta. | `str \| Path \| None` | `None` |
| `timeout` | Valor correspondente a timeout. | `float \| None` | `None` |
| `ambiente` | Valor correspondente a ambiente. | `Mapping[str, Any] \| None` | `None` |
| `entrada` | Valor correspondente a entrada. | `str \| None` | `None` |
| `relogio` | Relógio usado para controlar tempo ou atualização. | `FonteTempo \| None` | `None` |

**Retorno**

Retorna um valor declarado como `ResultadoComando`.

:::details Detalhes técnicos

**Assinatura:** `executar_comando(programa: str, argumentos: Iterable[Any] = (), *, pasta: str \| Path \| None = None, timeout: float \| None = None, ambiente: Mapping[str, Any] \| None = None, entrada: str \| None = None, relogio: FonteTempo \| None = None) -> ResultadoComando`

**Origem da implementação:** `coral.sistema`

**Arquivo na release:** `coral/sistema.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `programa` | posicional |
| `argumentos` | posicional |
| `pasta` | nomeado |
| `timeout` | nomeado |
| `ambiente` | nomeado |
| `entrada` | nomeado |
| `relogio` | nomeado |

**Exceções diretamente observáveis no corpo:** `ValueError`, `ProgramaNaoEncontrado`, `TempoLimiteExcedido`, `FalhaSistemaOperacional`

:::

#### `processo_atual`

Inspecionar processo Coral.

**Retorno**

Retorna um valor declarado como `dict[str, Any]`.

:::details Detalhes técnicos

**Assinatura:** `processo_atual() -> dict[str, Any]`

**Origem da implementação:** `coral.sistema`

**Arquivo na release:** `coral/sistema.py`

:::

### Classes e protocolos

#### `TempoLimiteExcedido`

Timeout de processo, compatível com subprocess.TimeoutExpired da linha 1.4.1.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `comando` | Valor correspondente a comando. | `tuple[str, ...]` | obrigatório |
| `timeout` | Valor correspondente a timeout. | `float \| None` | obrigatório |
| `mensagem` | Valor correspondente a mensagem. | `str` | obrigatório |

:::details Detalhes técnicos

**Assinatura:** `TempoLimiteExcedido(comando: tuple[str, ...], timeout: float \| None, mensagem: str)`

**Origem da implementação:** `coral.sistema`

**Arquivo na release:** `coral/sistema.py`

:::

#### `InformacoesSistema`

Representa InformacoesSistema na API de `coral.sistema`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `sistema` | Valor correspondente a sistema. | `str` | obrigatório |
| `versao` | Valor correspondente a versao. | `str` | obrigatório |
| `arquitetura` | Valor correspondente a arquitetura. | `str` | obrigatório |
| `maquina` | Valor correspondente a maquina. | `str` | obrigatório |
| `processador` | Valor correspondente a processador. | `str` | obrigatório |
| `python` | Valor correspondente a python. | `str` | obrigatório |
| `pid` | Valor correspondente a pid. | `int` | obrigatório |
| `pasta_atual` | Valor correspondente a pasta atual. | `str` | obrigatório |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `sistema` | Valor correspondente a sistema. | `str` | obrigatório |
| `versao` | Valor correspondente a versao. | `str` | obrigatório |
| `arquitetura` | Valor correspondente a arquitetura. | `str` | obrigatório |
| `maquina` | Valor correspondente a maquina. | `str` | obrigatório |
| `processador` | Valor correspondente a processador. | `str` | obrigatório |
| `python` | Valor correspondente a python. | `str` | obrigatório |
| `pid` | Valor correspondente a pid. | `int` | obrigatório |
| `pasta_atual` | Valor correspondente a pasta atual. | `str` | obrigatório |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `para_dict` | Converte o valor para dict. | `dict[str, Any]` |

:::details Detalhes técnicos

**Assinatura:** `InformacoesSistema(sistema: str, versao: str, arquitetura: str, maquina: str, processador: str, python: str, pid: int, pasta_atual: str)`

**Origem da implementação:** `coral.sistema`

**Arquivo na release:** `coral/sistema.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `para_dict` | método | `para_dict() -> dict[str, Any]` |

:::

#### `ResultadoComando`

Representa ResultadoComando na API de `coral.sistema`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `comando` | Valor correspondente a comando. | `tuple[str, ...]` | obrigatório |
| `codigo` | Valor correspondente a codigo. | `int` | obrigatório |
| `saida` | Valor correspondente a saida. | `str` | obrigatório |
| `erro` | Valor correspondente a erro. | `str` | obrigatório |
| `duracao_segundos` | Valor correspondente a duracao segundos. | `float` | obrigatório |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `comando` | Valor correspondente a comando. | `tuple[str, ...]` | obrigatório |
| `codigo` | Valor correspondente a codigo. | `int` | obrigatório |
| `saida` | Valor correspondente a saida. | `str` | obrigatório |
| `erro` | Valor correspondente a erro. | `str` | obrigatório |
| `duracao_segundos` | Valor correspondente a duracao segundos. | `float` | obrigatório |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `sucesso` | Indica o estado de sucesso. | `bool` |
| `para_dict` | Converte o valor para dict. | `dict[str, Any]` |
| `resultado_operacao` | Executa a operação `resultado_operacao` disponibilizada por `coral.sistema`. | `ResultadoOperacao` |

:::details Detalhes técnicos

**Assinatura:** `ResultadoComando(comando: tuple[str, ...], codigo: int, saida: str, erro: str, duracao_segundos: float)`

**Origem da implementação:** `coral.sistema`

**Arquivo na release:** `coral/sistema.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `sucesso` | propriedade | `sucesso() -> bool` |
| `para_dict` | método | `para_dict() -> dict[str, Any]` |
| `resultado_operacao` | método | `resultado_operacao() -> ResultadoOperacao` |

:::

### Exceções

#### `ErroSistema`

Falha operacional do sistema hospedeiro traduzida para a superfície Coral.

:::details Detalhes técnicos

**Assinatura:** `ErroSistema(...)`

**Origem da implementação:** `coral.sistema`

**Arquivo na release:** `coral/sistema.py`

:::

#### `ProgramaNaoEncontrado`

Executável ausente, compatível com o FileNotFoundError exposto até a 1.4.2.

:::details Detalhes técnicos

**Assinatura:** `ProgramaNaoEncontrado(...)`

**Origem da implementação:** `coral.sistema`

**Arquivo na release:** `coral/sistema.py`

:::

#### `FalhaSistemaOperacional`

Demais falhas do SO, mantendo compatibilidade com captura por OSError.

:::details Detalhes técnicos

**Assinatura:** `FalhaSistemaOperacional(...)`

**Origem da implementação:** `coral.sistema`

**Arquivo na release:** `coral/sistema.py`

:::

<!-- /AUTO:API -->

## Compatibilidade

Os contratos são portáveis, mas os valores refletem o sistema hospedeiro. Nome de sistema, caminhos, variáveis, disponibilidade de executáveis e comportamento de ferramentas externas variam entre Windows, Linux e outros ambientes.
