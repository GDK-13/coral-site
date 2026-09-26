# coral.assincrono

## Visão geral

`coral.assincrono` oferece timeout, cancelamento e agrupamento sobre o modelo assíncrono existente. Use quando uma tarefa assíncrona precisa de limite de tempo, cancelamento cooperativo ou espera agrupada.

<!-- AUTO:MODULO -->

**Importação:** `coral.assincrono`  
**Categoria:** runtime  

timeout, cancelamento e agrupamento sobre o modelo assíncrono existente

### Superfície pública detectada

`ErroTempoEsgotado`, `aguardar_com_timeout`, `cancelar_tarefa`, `grupo_tarefas`

<!-- /AUTO:MODULO -->

## Papel no ecossistema

Complementa a sintaxe assíncrona existente da Coral sem criar um segundo modelo de concorrência. O foco da release é resolver três necessidades práticas: limite de tempo, cancelamento cooperativo e espera agrupada.

## Conceitos principais

### Timeout

`aguardar_com_timeout` envolve um awaitable e converte o estouro de prazo em `ErroTempoEsgotado`.

### Cancelamento cooperativo

`cancelar_tarefa` solicita cancelamento; a tarefa ainda precisa chegar a um ponto em que o runtime possa entregar esse cancelamento.

### Agrupamento

`grupo_tarefas` aguarda múltiplos awaitables e preserva a ordem dos resultados.

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
| `ErroTempoEsgotado` | erro controlado de timeout |

A seção **Referência da API** no fim desta página contém a superfície pública completa detectada na release, com assinaturas, parâmetros, retornos e docstrings quando presentes.

## Fluxos comuns

1. Crie ou obtenha as tarefas pelo modelo assíncrono normal da linguagem.
2. Use timeout apenas na fronteira que realmente possui um prazo.
3. Ao encerrar uma operação longa, solicite cancelamento e deixe o código cooperar com a interrupção.
4. Agrupe tarefas independentes quando o chamador precisa aguardar todas.

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

A documentação desta página descreve a superfície detectada na **Coral 1.6.0**. O gerador do site atualiza automaticamente o inventário e a referência da API quando uma nova release é importada, mas o texto pedagógico desta seção permanece sob revisão humana.

## Referência da API

<!-- AUTO:API -->

### Funções

#### `aguardar_com_timeout`

Aguarda ``esperavel`` por no máximo ``segundos``.

**Exemplo**

```coral
crie a função assíncrona principal
    defina resultado como aguarde aguardar_com_timeout(leia_dados(), 2)
    mostre resultado
fim
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

**Exceções diretamente observáveis no corpo:** `ErroValor`, `ErroTempoEsgotado`

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

### Exceções

#### `ErroTempoEsgotado`

Uma operação assíncrona excedeu o limite solicitado.

:::details Detalhes técnicos

**Assinatura:** `ErroTempoEsgotado(...)`

**Origem da implementação:** `coral.assincrono`

**Arquivo na release:** `coral/assincrono.py`

:::

<!-- /AUTO:API -->
