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

A documentação desta página descreve a superfície detectada na **Coral 1.5.9**. O gerador do site atualiza automaticamente o inventário e a referência da API quando uma nova release é importada, mas o texto pedagógico desta seção permanece sob revisão humana.

## Referência da API

<!-- AUTO:API -->

### Funções

#### `async aguardar_com_timeout(esperavel: Awaitable[Any], segundos: float)`

Aguarda ``esperavel`` por no máximo ``segundos``.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `esperavel` | `Awaitable[Any]` | obrigatório | posicional |
| `segundos` | `float` | obrigatório | posicional |

**Retorno:** `não declarado`

**Exceções observáveis no corpo:** `ErroValor`, `ErroTempoEsgotado`

#### `cancelar_tarefa(tarefa: Any, motivo: str | None = None) -> bool`

Solicita cancelamento cooperativo de uma tarefa asyncio.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `tarefa` | `Any` | obrigatório | posicional |
| `motivo` | `str \| None` | `None` | posicional |

**Retorno:** `bool`

**Exceções observáveis no corpo:** `ErroValor`

#### `async grupo_tarefas(*esperaveis: Awaitable[Any]) -> tuple[Any, ...]`

Aguarda vários awaitables e preserva a ordem dos resultados.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `*esperaveis` | `Awaitable[Any]` | obrigatório | variádico |

**Retorno:** `tuple[Any, ...]`

### Exceções

#### `ErroTempoEsgotado(...)`

Uma operação assíncrona excedeu o limite solicitado.

<!-- /AUTO:API -->
