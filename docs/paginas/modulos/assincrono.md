# coral.assincrono

## Visão geral

`coral.assincrono` oferece timeout, cancelamento, agrupamento e filas com concorrência limitada sobre o modelo assíncrono existente. Use quando uma tarefa precisa de prazo, cancelamento cooperativo, sucesso parcial, progresso ou controle de simultaneidade.

<!-- AUTO:MODULO -->

**Importação:** `coral.assincrono`  
**Categoria:** runtime  

timeout, cancelamento, agrupamento e filas limitadas sobre o modelo assíncrono existente

### Superfície pública detectada

`ErroTempoEsgotado`, `ErroFilaTarefas`, `ErroFilaCheia`, `ErroFilaFechada`, `ResultadoTarefa`, `ProgressoTarefas`, `RelatorioTarefas`, `FilaTarefas`, `aguardar_com_timeout`, `cancelar_tarefa`, `grupo_tarefas`, `executar_bloqueante`, `executar_fila`

<!-- /AUTO:MODULO -->

## Papel no ecossistema

Complementa a sintaxe assíncrona existente da Coral sem criar um segundo modelo de concorrência. Além de timeout, cancelamento e agrupamento, a superfície corrente inclui `FilaTarefas` para organizar lotes com limite de simultaneidade, capacidade, política de falha e relatórios estruturados.

## Conceitos principais

### Timeout

`aguardar_com_timeout` envolve um awaitable e converte o estouro de prazo em `ErroTempoEsgotado`.

### Cancelamento cooperativo

`cancelar_tarefa` solicita cancelamento; a tarefa ainda precisa chegar a um ponto em que o runtime possa entregar esse cancelamento.

### Agrupamento

`grupo_tarefas` aguarda múltiplos awaitables e preserva a ordem dos resultados.

### Fila de tarefas

`FilaTarefas(limite_ativas=4, capacidade=nulo, politica_falha="continuar", timeout_tarefa=nulo)` organiza awaitables em um lote com ciclo de vida explícito. Adicione os trabalhos primeiro e execute a fila uma vez. Depois do início, novas submissões são recusadas.

A política `continuar` preserva sucessos mesmo quando uma tarefa falha. A política `parar` impede novos inícios depois da primeira falha observada, mas tarefas que já começaram podem terminar.

`ProgressoTarefas` descreve iniciadas, concluídas, sucessos, falhas, canceladas, pendentes e ativas. `RelatorioTarefas` preserva a ordem de submissão, não a ordem em que as tarefas terminaram.

### Operações bloqueantes

`executar_bloqueante` move uma função síncrona para uma thread auxiliar. Isso evita bloquear o ciclo assíncrono enquanto a função roda, mas cancelar quem espera pelo resultado não encerra à força a função que já começou na thread.

## Quando usar

Use este módulo quando o problema corresponder diretamente aos conceitos acima. Por ser um módulo complementar, ele normalmente entra em um programa para resolver uma responsabilidade específica e deve permanecer desacoplado da lógica central sempre que possível.

## Começando

```coral
de coral.assincrono importe aguardar_com_timeout

crie a função assíncrona leia_dados
    retorne "ok"
fim

crie a função assíncrona principal
    defina resultado como aguarde aguardar_com_timeout(leia_dados(), 2)
    mostre resultado
fim

execute assincronamente principal()
```

## API essencial

| Entrada | Papel |
|---|---|
| `aguardar_com_timeout` | aplicar limite de tempo |
| `cancelar_tarefa` | solicitar cancelamento |
| `grupo_tarefas` | aguardar várias operações |
| `FilaTarefas` | limitar concorrência e organizar um lote |
| `executar_fila` | executar um lote com configuração direta |
| `executar_bloqueante` | levar trabalho síncrono para thread auxiliar |
| `ErroTempoEsgotado` | erro controlado de timeout |

A seção **Referência da API** no fim desta página contém a superfície pública completa detectada na release, com assinaturas, parâmetros, retornos e docstrings quando presentes.

## Fluxos comuns

1. Crie ou obtenha as tarefas pelo modelo assíncrono normal da linguagem.
2. Use timeout apenas na fronteira que realmente possui um prazo.
3. Ao encerrar uma operação longa, solicite cancelamento e deixe o código cooperar com a interrupção.
4. Agrupe tarefas independentes quando o chamador precisa aguardar todas.
5. Use `FilaTarefas` quando precisar limitar simultaneidade, manter sucesso parcial, acompanhar progresso ou aplicar política de falha.

## Erros e casos de borda

Timeout não significa necessariamente que um efeito externo foi revertido. Cancelamento também não é transação. Se uma operação modifica estado externo, documente quais fases podem já ter ocorrido quando o prazo expira.

## Boas práticas

* Não use timeout como substituto de correção de deadlock.
* Mantenha tarefas canceláveis em pontos seguros.
* Propague erros das tarefas em vez de descartá los silenciosamente.

## Integração com outros módulos

`coral.tempo_eventos` cobre tempo injetável e cancelamento cooperativo compartilhado por bibliotecas. `coral.comum` fornece contratos transversais de falha e diagnóstico.

## Testabilidade e previsibilidade

Em testes, prefira operações curtas e determinísticas. O objetivo é provar a política de timeout e cancelamento sem depender de esperas reais longas.

## Compatibilidade e evolução

A documentação desta página descreve a superfície detectada na **Coral 1.8.0**. O gerador do site atualiza automaticamente o inventário e a referência da API quando uma nova release é importada, mas o texto pedagógico desta seção permanece sob revisão humana.

## Referência da API

<!-- AUTO:API -->

### Funções

#### `aguardar_com_timeout`

Aguarda ``esperavel`` por no máximo ``segundos``.

**Exemplo**

```coral
de coral.assincrono importe aguardar_com_timeout

crie a função assíncrona leia_dados
    retorne "ok"
fim

crie a função assíncrona principal
    defina resultado como aguarde aguardar_com_timeout(leia_dados(), 2)
    mostre resultado
fim

execute assincronamente principal()
```

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `esperavel` | Valor correspondente a esperavel. | `Awaitable[Any]` | obrigatório |
| `segundos` | Valor correspondente a segundos. | `float` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `async aguardar_com_timeout(esperavel: Awaitable[Any], segundos: float)`

**Origem da implementação:** `coral.assincrono`

**Arquivo na release:** `coral/assincrono.py`

**Exceções diretamente observáveis no corpo:** `ErroTempoEsgotado`

:::

#### `cancelar_tarefa`

Solicita cancelamento cooperativo de uma tarefa asyncio.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `tarefa` | Valor correspondente a tarefa. | `Any` | obrigatório |
| `motivo` | Texto que descreve o motivo associado à operação. | `str \| None` | `None` |

**Retorno**

Retorna um valor declarado como `bool`.

:::details Detalhes técnicos

**Assinatura:** `cancelar_tarefa(tarefa: Any, motivo: str \| None = None) -> bool`

**Origem da implementação:** `coral.assincrono`

**Arquivo na release:** `coral/assincrono.py`

**Exceções diretamente observáveis no corpo:** `ErroValor`

:::

#### `grupo_tarefas`

Aguarda vários awaitables e preserva a ordem dos resultados.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `*esperaveis` | Valor correspondente a esperaveis. | `Awaitable[Any]` | obrigatório |

**Retorno**

Retorna um valor declarado como `tuple[Any, ...]`.

:::details Detalhes técnicos

**Assinatura:** `async grupo_tarefas(*esperaveis: Awaitable[Any]) -> tuple[Any, ...]`

**Origem da implementação:** `coral.assincrono`

**Arquivo na release:** `coral/assincrono.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `*esperaveis` | variádico |

:::

#### `executar_bloqueante`

Executa uma função síncrona em uma thread auxiliar.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `funcao` | Função fornecida para executar a operação. | `Callable[..., Any]` | obrigatório |
| `*args` | Valor correspondente a args. | `Any` | obrigatório |
| `**kwargs` | Valor correspondente a kwargs. | `Any` | obrigatório |

**Retorno**

Retorna um valor declarado como `Any`.

:::details Detalhes técnicos

**Assinatura:** `async executar_bloqueante(funcao: Callable[..., Any], *args: Any, **kwargs: Any) -> Any`

**Origem da implementação:** `coral.assincrono`

**Arquivo na release:** `coral/assincrono.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `funcao` | posicional |
| `*args` | variádico |
| `**kwargs` | variádico nomeado |

**Exceções diretamente observáveis no corpo:** `ErroValor`

:::

#### `executar_fila`

Atalho para executar um lote de awaitables com :class:`FilaTarefas`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `*esperaveis` | Valor correspondente a esperaveis. | `Awaitable[Any]` | obrigatório |
| `limite_ativas` | Valor correspondente a limite ativas. | `int` | `4` |
| `politica_falha` | Valor correspondente a politica falha. | `str` | `'continuar'` |
| `timeout_tarefa` | Valor correspondente a timeout tarefa. | `float \| None` | `None` |
| `timeout_grupo` | Valor correspondente a timeout grupo. | `float \| None` | `None` |
| `ao_progresso` | Valor correspondente a ao progresso. | `Callable[[ProgressoTarefas], Any] \| None` | `None` |

**Retorno**

Retorna um valor declarado como `RelatorioTarefas`.

:::details Detalhes técnicos

**Assinatura:** `async executar_fila(*esperaveis: Awaitable[Any], limite_ativas: int = 4, politica_falha: str = 'continuar', timeout_tarefa: float \| None = None, timeout_grupo: float \| None = None, ao_progresso: Callable[[ProgressoTarefas], Any] \| None = None) -> RelatorioTarefas`

**Origem da implementação:** `coral.assincrono`

**Arquivo na release:** `coral/assincrono.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `*esperaveis` | variádico |
| `limite_ativas` | nomeado |
| `politica_falha` | nomeado |
| `timeout_tarefa` | nomeado |
| `timeout_grupo` | nomeado |
| `ao_progresso` | nomeado |

:::

### Classes e protocolos

#### `ResultadoTarefa`

Resultado estruturado de uma tarefa submetida à fila.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `indice` | Valor correspondente a indice. | `int` | obrigatório |
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | obrigatório |
| `estado` | Estado usado ou atualizado pela operação. | `str` | obrigatório |
| `valor` | Valor processado pela operação. | `Any` | `None` |
| `erro` | Valor correspondente a erro. | `BaseException \| None` | `None` |
| `segundos` | Valor correspondente a segundos. | `float` | `0.0` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `indice` | Valor correspondente a indice. | `int` | obrigatório |
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | obrigatório |
| `estado` | Estado usado ou atualizado pela operação. | `str` | obrigatório |
| `valor` | Valor processado pela operação. | `Any` | `None` |
| `erro` | Valor correspondente a erro. | `BaseException \| None` | `None` |
| `segundos` | Valor correspondente a segundos. | `float` | `0.0` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `ok` | Retorna verdadeiro somente para uma tarefa concluída com sucesso. | `bool` |
| `para_dict` | Converte o resultado para dados simples adequados a relatório/UI. | `dict[str, Any]` |

:::details Detalhes técnicos

**Assinatura:** `ResultadoTarefa(indice: int, nome: str, estado: str, valor: Any = None, erro: BaseException \| None = None, segundos: float = 0.0)`

**Origem da implementação:** `coral.assincrono`

**Arquivo na release:** `coral/assincrono.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `ok` | propriedade | `ok() -> bool` |
| `para_dict` | método | `para_dict() -> dict[str, Any]` |

:::

#### `ProgressoTarefas`

Instantâneo imutável do progresso de uma fila.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `total` | Valor correspondente a total. | `int` | obrigatório |
| `iniciadas` | Valor correspondente a iniciadas. | `int` | obrigatório |
| `concluidas` | Valor correspondente a concluidas. | `int` | obrigatório |
| `sucessos` | Valor correspondente a sucessos. | `int` | obrigatório |
| `falhas` | Valor correspondente a falhas. | `int` | obrigatório |
| `canceladas` | Valor correspondente a canceladas. | `int` | obrigatório |
| `pendentes` | Valor correspondente a pendentes. | `int` | obrigatório |
| `ativas` | Valor correspondente a ativas. | `int` | obrigatório |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `total` | Valor correspondente a total. | `int` | obrigatório |
| `iniciadas` | Valor correspondente a iniciadas. | `int` | obrigatório |
| `concluidas` | Valor correspondente a concluidas. | `int` | obrigatório |
| `sucessos` | Valor correspondente a sucessos. | `int` | obrigatório |
| `falhas` | Valor correspondente a falhas. | `int` | obrigatório |
| `canceladas` | Valor correspondente a canceladas. | `int` | obrigatório |
| `pendentes` | Valor correspondente a pendentes. | `int` | obrigatório |
| `ativas` | Valor correspondente a ativas. | `int` | obrigatório |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `fracao` | Fração concluída entre 0 e 1; fila vazia é considerada concluída. | `float` |
| `para_dict` | Converte o valor para dict. | `dict[str, Any]` |

:::details Detalhes técnicos

**Assinatura:** `ProgressoTarefas(total: int, iniciadas: int, concluidas: int, sucessos: int, falhas: int, canceladas: int, pendentes: int, ativas: int)`

**Origem da implementação:** `coral.assincrono`

**Arquivo na release:** `coral/assincrono.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `fracao` | propriedade | `fracao() -> float` |
| `para_dict` | método | `para_dict() -> dict[str, Any]` |

:::

#### `RelatorioTarefas`

Relatório final ordenado produzido por :class:`FilaTarefas`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `resultados` | Valor correspondente a resultados. | `tuple[ResultadoTarefa, ...]` | obrigatório |
| `progresso` | Valor correspondente a progresso. | `ProgressoTarefas` | obrigatório |
| `estado` | Estado usado ou atualizado pela operação. | `str` | obrigatório |
| `motivo` | Texto que descreve o motivo associado à operação. | `str \| None` | `None` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `resultados` | Valor correspondente a resultados. | `tuple[ResultadoTarefa, ...]` | obrigatório |
| `progresso` | Valor correspondente a progresso. | `ProgressoTarefas` | obrigatório |
| `estado` | Estado usado ou atualizado pela operação. | `str` | obrigatório |
| `motivo` | Texto que descreve o motivo associado à operação. | `str \| None` | `None` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `ok` | Executa a operação `ok` disponibilizada por `coral.assincrono`. | `bool` |
| `para_dict` | Converte o valor para dict. | `dict[str, Any]` |

:::details Detalhes técnicos

**Assinatura:** `RelatorioTarefas(resultados: tuple[ResultadoTarefa, ...], progresso: ProgressoTarefas, estado: str, motivo: str \| None = None)`

**Origem da implementação:** `coral.assincrono`

**Arquivo na release:** `coral/assincrono.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `ok` | propriedade | `ok() -> bool` |
| `para_dict` | método | `para_dict() -> dict[str, Any]` |

:::

#### `FilaTarefas`

Executa um lote assíncrono com simultaneidade e políticas explícitas.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `limite_ativas` | Valor correspondente a limite ativas. | `int` | `4` |
| `capacidade` | Valor correspondente a capacidade. | `int \| None` | `None` |
| `politica_falha` | Valor correspondente a politica falha. | `str` | `'continuar'` |
| `timeout_tarefa` | Valor correspondente a timeout tarefa. | `float \| None` | `None` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `fechada` | Executa a operação `fechada` disponibilizada por `coral.assincrono`. | `bool` |
| `executando` | Executa a operação `executando` disponibilizada por `coral.assincrono`. | `bool` |
| `adicionar` | Adiciona uma tarefa e retorna seu índice estável de submissão. | `int` |
| `fechar` | Fecha a entrada da fila. Tarefas já adicionadas continuam executáveis. | `bool` |
| `cancelar` | Solicita cancelamento cooperativo e impede novos trabalhos. | `bool` |
| `progresso` | Executa a operação `progresso` disponibilizada por `coral.assincrono`. | `ProgressoTarefas` |
| `executar` | Executa o lote uma única vez e retorna relatório ordenado. | `RelatorioTarefas` |

:::details Detalhes técnicos

**Assinatura:** `FilaTarefas(limite_ativas: int = 4, capacidade: int \| None = None, politica_falha: str = 'continuar', timeout_tarefa: float \| None = None)`

**Origem da implementação:** `coral.assincrono`

**Arquivo na release:** `coral/assincrono.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `fechada` | propriedade | `fechada() -> bool` |
| `executando` | propriedade | `executando() -> bool` |
| `adicionar` | método | `adicionar(esperavel: Awaitable[Any] \| Callable[[], Awaitable[Any]], nome: str \| None = None, timeout: float \| None = None) -> int` |
| `fechar` | método | `fechar() -> bool` |
| `cancelar` | método | `cancelar(motivo: str \| None = None) -> bool` |
| `progresso` | método | `progresso() -> ProgressoTarefas` |
| `executar` | método | `async executar(timeout_grupo: float \| None = None, ao_progresso: Callable[[ProgressoTarefas], Any] \| None = None) -> RelatorioTarefas` |

:::

### Exceções

#### `ErroTempoEsgotado`

Uma operação assíncrona excedeu o limite solicitado.

:::details Detalhes técnicos

**Assinatura:** `ErroTempoEsgotado(...)`

**Origem da implementação:** `coral.assincrono`

**Arquivo na release:** `coral/assincrono.py`

:::

#### `ErroFilaTarefas`

Base das falhas controladas de :class:`FilaTarefas`.

:::details Detalhes técnicos

**Assinatura:** `ErroFilaTarefas(...)`

**Origem da implementação:** `coral.assincrono`

**Arquivo na release:** `coral/assincrono.py`

:::

#### `ErroFilaCheia`

A fila atingiu sua capacidade configurada.

:::details Detalhes técnicos

**Assinatura:** `ErroFilaCheia(...)`

**Origem da implementação:** `coral.assincrono`

**Arquivo na release:** `coral/assincrono.py`

:::

#### `ErroFilaFechada`

A fila não aceita novas tarefas ou uma nova execução.

:::details Detalhes técnicos

**Assinatura:** `ErroFilaFechada(...)`

**Origem da implementação:** `coral.assincrono`

**Arquivo na release:** `coral/assincrono.py`

:::

<!-- /AUTO:API -->
