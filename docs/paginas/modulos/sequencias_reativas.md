# coral.sequencias_reativas

## Visão geral

`coral.sequencias_reativas` oferece sequências temporais reutilizáveis de eventos. Use para organizar sequências temporais reutilizáveis de eventos em sistemas reativos.

<!-- AUTO:MODULO -->

**Importação:** `coral.sequencias_reativas`  
**Categoria:** reativo  

sequências temporais reutilizáveis de eventos

### Superfície pública detectada

`AcaoSequencia`, `SequenciaDoisPassos`

<!-- /AUTO:MODULO -->

## Papel no ecossistema

Encapsula padrões temporais simples de eventos. Na 1.5.12 a superfície pública é deliberadamente pequena e oferece `SequenciaDoisPassos` como bloco reutilizável.

## Conceitos principais

### Dois passos

`SequenciaDoisPassos` observa um primeiro evento e aguarda um segundo antes de executar a ação.

### Janela temporal

A sequência pode ter uma janela máxima entre os dois eventos.

### Ação

`AcaoSequencia` descreve o callback executado quando a sequência é reconhecida.

### Nome

A sequência possui nome explícito, útil em diagnóstico e rastreamento.

## Quando usar

Use este módulo quando o problema corresponder diretamente aos conceitos acima. Por ser um módulo complementar, ele normalmente entra em um programa para resolver uma responsabilidade específica e deve permanecer desacoplado da lógica central sempre que possível.

## Começando

```coral
de coral.tempo_eventos importe Eventos
de coral.sequencias_reativas importe SequenciaDoisPassos

defina eventos como Eventos()
crie a função concluiu com primeiro e segundo
    mostre "sequência reconhecida"
fim

defina sequencia como SequenciaDoisPassos(eventos, "abrir", "confirmar", concluiu, janela=2)
mostre sequencia
```

## API essencial

| Entrada | Papel |
|---|---|
| `SequenciaDoisPassos` | reconhecer padrão de dois eventos |
| `AcaoSequencia` | contrato da ação |

A seção **Referência da API** no fim desta página contém a superfície pública completa detectada na release, com assinaturas, parâmetros, retornos e docstrings quando presentes.

## Fluxos comuns

1. Escolha dois eventos semanticamente relevantes.
2. Defina se existe janela máxima entre eles.
3. Crie uma ação pequena para o reconhecimento.
4. Associe a sequência ao mesmo barramento de eventos do domínio.

## Erros e casos de borda

Eventos fora de ordem ou depois da janela não devem ser tratados como sequência válida. Ao combinar muitas sequências sobre os mesmos eventos, observe interações e consumo de eventos.

## Boas práticas

* Use nomes descritivos.
* Mantenha sequências pequenas; regras mais complexas pertencem a `coral.regras`.
* Teste ordem correta, ordem invertida e expiração da janela.

## Integração com outros módulos

Depende conceitualmente de `coral.tempo_eventos.Eventos`; pode participar de regras, observadores, rastreamento e replay.

## Testabilidade e previsibilidade

Um relógio controlável permite testar a janela sem `sleep`. Casos mínimos: sucesso dentro da janela, segundo evento atrasado e segundo evento sem primeiro.

## Compatibilidade e evolução

A documentação desta página descreve a superfície detectada na **Coral 1.5.12**. O gerador do site atualiza automaticamente o inventário e a referência da API quando uma nova release é importada, mas o texto pedagógico desta seção permanece sob revisão humana.

## Referência da API

<!-- AUTO:API -->

### Classes e protocolos

#### `SequenciaDoisPassos`

Representa SequenciaDoisPassos na API de `coral.sequencias_reativas`.

**Exemplo**

```coral
fim

defina sequencia como SequenciaDoisPassos(eventos, "abrir", "confirmar", concluiu, janela=2)
mostre sequencia
```

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `eventos` | Fonte ou conjunto de eventos associado à operação. | `Eventos` | obrigatório |
| `primeiro` | Valor correspondente a primeiro. | `str` | obrigatório |
| `segundo` | Valor correspondente a segundo. | `str` | obrigatório |
| `acao` | Valor correspondente a acao. | `AcaoSequencia` | obrigatório |
| `janela` | Valor correspondente a janela. | `float \| None` | `None` |
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | `'sequencia'` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `eventos` | Fonte ou conjunto de eventos associado à operação. | `Eventos` | obrigatório |
| `primeiro` | Valor correspondente a primeiro. | `str` | obrigatório |
| `segundo` | Valor correspondente a segundo. | `str` | obrigatório |
| `acao` | Valor correspondente a acao. | `AcaoSequencia` | obrigatório |
| `janela` | Valor correspondente a janela. | `float \| None` | `None` |
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | `'sequencia'` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `resetar` | Executa a operação `resetar` disponibilizada por `coral.sequencias_reativas`. | `None` |

:::details Detalhes técnicos

**Assinatura:** `SequenciaDoisPassos(eventos: Eventos, primeiro: str, segundo: str, acao: AcaoSequencia, janela: float \| None = None, nome: str = 'sequencia')`

**Origem da implementação:** `coral.sequencias_reativas`

**Arquivo na release:** `coral/sequencias_reativas.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `resetar` | método | `resetar() -> None` |

:::

### Constantes e aliases

#### `AcaoSequencia`

Expõe `AcaoSequencia` como parte da API pública do módulo.

:::details Detalhes técnicos

**Assinatura:** `AcaoSequencia`

**Origem da implementação:** `coral.sequencias_reativas`

**Arquivo na release:** `coral/sequencias_reativas.py`

**Valor declarado:** `Callable[[Evento, Evento], Any]`

:::

<!-- /AUTO:API -->
