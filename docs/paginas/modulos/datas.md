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

## Papel no ecossistema

Reúne data, data e hora, fuso e duração numa superfície única. Serve para representar tempo civil e conversões de calendário, enquanto `coral.tempo_eventos` trata relógios de execução e eventos determinísticos.

## Conceitos principais

### Agora e hoje

`agora` retorna data e hora e `hoje` trabalha com a data civil, ambos podendo receber fuso.

### Durações

`dias`, `horas`, `minutos`, `segundos` e `semanas` criam durações explícitas.

### Formatação e análise

`formatar`, `analisar`, `de_iso` e `para_iso` transformam entre valores temporais e texto.

### Fusos

`fuso_horario` obtém um fuso e `converter_fuso` converte uma data e hora consciente de fuso.

### Diferença

`diferenca` produz a duração entre dois valores temporais compatíveis.

## Quando usar

Use este módulo quando o problema corresponder diretamente aos conceitos acima. Por ser um módulo complementar, ele normalmente entra em um programa para resolver uma responsabilidade específica e deve permanecer desacoplado da lógica central sempre que possível.

## Começando

```coral
de coral.datas importe agora, para_iso, horas

defina inicio como agora("UTC")
mostre para_iso(inicio)
defina intervalo como horas(2)
mostre intervalo
```

## API essencial

| Entrada | Papel |
|---|---|
| `agora` / `hoje` | tempo civil atual |
| `dias` / `horas` / `minutos` | construir duração |
| `analisar` / `formatar` | texto e valor temporal |
| `de_iso` / `para_iso` | ISO 8601 |
| `fuso_horario` | obter fuso |
| `converter_fuso` | converter fuso |
| `diferenca` | calcular duração |

A seção **Referência da API** no fim desta página contém a superfície pública completa detectada na release, com assinaturas, parâmetros, retornos e docstrings quando presentes.

## Fluxos comuns

1. Para armazenamento e intercâmbio, prefira ISO quando possível.
2. Associe fuso a valores que representam um instante global.
3. Use durações para somar ou comparar intervalos em vez de números “mágicos” de segundos.
4. Use `coral.tempo_eventos` quando o problema for simulação de tempo ou controle determinístico de execução.

## Erros e casos de borda

Datas sem fuso e datas com fuso não devem ser misturadas sem decisão explícita. Formatos livres de data são ambíguos; quando o formato não for ISO, informe o padrão esperado.

## Boas práticas

* Armazene instantes interoperáveis em ISO com fuso.
* Evite interpretar texto de data sem formato conhecido.
* Não use relógio civil para medir duração de execução.

## Integração com outros módulos

`coral.formatacao` e `coral.texto` cuidam da apresentação; `coral.json` pode transportar strings ISO; `coral.tempo_eventos` cobre relógios monotônicos ou simulados.

## Testabilidade e previsibilidade

Teste datas de fronteira, mudanças de fuso e round trip `para_iso`/`de_iso`. Para duração, prefira valores controlados a consultar o relógio real.

## Compatibilidade e evolução

A documentação desta página descreve a superfície detectada na **Coral 1.5.9**. O gerador do site atualiza automaticamente o inventário e a referência da API quando uma nova release é importada, mas o texto pedagógico desta seção permanece sob revisão humana.

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
