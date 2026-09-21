# coral.datas

## Visão geral

`coral.datas` oferece datas, datas e horas, fusos e durações. Use para obter data e hora, construir durações, formatar valores e trabalhar com fusos horários.

<!-- AUTO:MODULO -->

**Importação:** `coral.datas`  
**Categoria:** tempo  

datas, datas e horas, fusos e durações

### Superfície pública detectada

`agora`, `hoje`, `dias`, `segundos`, `minutos`, `horas`, `semanas`, `formatar`, `analisar`, `de_iso`, `para_iso`, `fuso_horario`, `converter_fuso`, `diferenca`

<!-- /AUTO:MODULO -->

## Quando usar

Use para obter data e hora, construir durações, formatar valores e trabalhar com fusos horários.

Entre as entradas públicas detectadas estão `agora`, `hoje`, `dias`, `segundos`, `minutos`, `horas`.

## Começando

Uma importação seletiva começa assim:

```coral
de coral.datas importe agora, hoje, dias
```

Depois da importação, use o hover e o preenchimento do VS Code para consultar a assinatura exata disponível na release.

## Cuidados

Ao trocar dados entre sistemas, prefira representações explícitas como ISO e declare o fuso quando ele for relevante.

## Relações com outros módulos

Consulte a navegação lateral para módulos que fornecem dados, sistema, texto ou runtime complementar.

## Referência da API

<!-- AUTO:API -->

### Funções

#### `agora(fuso: str | tzinfo | None = None)`

Entrada pública `agora` da superfície `coral.datas`.

**Implementação:** `coral.stdlib.datas`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `fuso` | `str \| tzinfo \| None` | `None` | posicional |

**Retorno:** `não declarado`

#### `hoje(fuso: str | tzinfo | None = None)`

Entrada pública `hoje` da superfície `coral.datas`.

**Implementação:** `coral.stdlib.datas`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `fuso` | `str \| tzinfo \| None` | `None` | posicional |

**Retorno:** `não declarado`

#### `dias(valor)`

Entrada pública `dias` da superfície `coral.datas`.

**Implementação:** `coral.stdlib.datas`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `valor` | `não declarado` | obrigatório | posicional |

**Retorno:** `não declarado`

#### `segundos(valor)`

Entrada pública `segundos` da superfície `coral.datas`.

**Implementação:** `coral.stdlib.datas`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `valor` | `não declarado` | obrigatório | posicional |

**Retorno:** `não declarado`

#### `minutos(valor)`

Entrada pública `minutos` da superfície `coral.datas`.

**Implementação:** `coral.stdlib.datas`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `valor` | `não declarado` | obrigatório | posicional |

**Retorno:** `não declarado`

#### `horas(valor)`

Entrada pública `horas` da superfície `coral.datas`.

**Implementação:** `coral.stdlib.datas`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `valor` | `não declarado` | obrigatório | posicional |

**Retorno:** `não declarado`

#### `semanas(valor)`

Entrada pública `semanas` da superfície `coral.datas`.

**Implementação:** `coral.stdlib.datas`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `valor` | `não declarado` | obrigatório | posicional |

**Retorno:** `não declarado`

#### `formatar(valor, formato = '%d/%m/%Y')`

Entrada pública `formatar` da superfície `coral.datas`.

**Implementação:** `coral.stdlib.datas`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `valor` | `não declarado` | obrigatório | posicional |
| `formato` | `não declarado` | `'%d/%m/%Y'` | posicional |

**Retorno:** `não declarado`

#### `analisar(texto: str, formato: str | None = None)`

Entrada pública `analisar` da superfície `coral.datas`.

**Implementação:** `coral.stdlib.datas`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `texto` | `str` | obrigatório | posicional |
| `formato` | `str \| None` | `None` | posicional |

**Retorno:** `não declarado`

**Exceções observáveis no corpo:** `ValueError`

#### `de_iso(texto: str)`

Entrada pública `de_iso` da superfície `coral.datas`.

**Implementação:** `coral.stdlib.datas`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `texto` | `str` | obrigatório | posicional |

**Retorno:** `não declarado`

#### `para_iso(valor, *, vezespec = 'auto') -> str`

Entrada pública `para_iso` da superfície `coral.datas`.

**Implementação:** `coral.stdlib.datas`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `valor` | `não declarado` | obrigatório | posicional |
| `vezespec` | `não declarado` | `'auto'` | nomeado |

**Retorno:** `str`

**Exceções observáveis no corpo:** `TypeError`

#### `fuso_horario(nome: str = 'UTC') -> tzinfo`

Entrada pública `fuso_horario` da superfície `coral.datas`.

**Implementação:** `coral.stdlib.datas`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `nome` | `str` | `'UTC'` | posicional |

**Retorno:** `tzinfo`

#### `converter_fuso(valor: datetime, fuso: str | tzinfo) -> datetime`

Entrada pública `converter_fuso` da superfície `coral.datas`.

**Implementação:** `coral.stdlib.datas`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `valor` | `datetime` | obrigatório | posicional |
| `fuso` | `str \| tzinfo` | obrigatório | posicional |

**Retorno:** `datetime`

**Exceções observáveis no corpo:** `TypeError`, `ValueError`

#### `diferenca(final, inicial)`

Entrada pública `diferenca` da superfície `coral.datas`.

**Implementação:** `coral.stdlib.datas`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `final` | `não declarado` | obrigatório | posicional |
| `inicial` | `não declarado` | obrigatório | posicional |

**Retorno:** `não declarado`

**Exceções observáveis no corpo:** `TypeError`

<!-- /AUTO:API -->
