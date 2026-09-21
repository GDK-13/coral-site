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

#### `agora`

Obtém o instante civil atual.

**Exemplo**

```coral
de coral.datas importe agora, para_iso, horas

defina inicio como agora("UTC")
mostre para_iso(inicio)
defina intervalo como horas(2)
mostre intervalo
```

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `fuso` | Valor correspondente a fuso. | `str \| tzinfo \| None` | `None` |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `agora(fuso: str \| tzinfo \| None = None)`

**Origem da implementação:** `coral.stdlib.datas`

**Arquivo na release:** `coral/stdlib/datas.py`

:::

#### `hoje`

Obtém a data civil atual.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `fuso` | Valor correspondente a fuso. | `str \| tzinfo \| None` | `None` |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `hoje(fuso: str \| tzinfo \| None = None)`

**Origem da implementação:** `coral.stdlib.datas`

**Arquivo na release:** `coral/stdlib/datas.py`

:::

#### `dias`

Construir duração.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valor` | Valor processado pela operação. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `dias(valor)`

**Origem da implementação:** `coral.stdlib.datas`

**Arquivo na release:** `coral/stdlib/datas.py`

:::

#### `segundos`

Cria uma duração expressa em segundos.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valor` | Valor processado pela operação. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `segundos(valor)`

**Origem da implementação:** `coral.stdlib.datas`

**Arquivo na release:** `coral/stdlib/datas.py`

:::

#### `minutos`

Construir duração.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valor` | Valor processado pela operação. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `minutos(valor)`

**Origem da implementação:** `coral.stdlib.datas`

**Arquivo na release:** `coral/stdlib/datas.py`

:::

#### `horas`

Construir duração.

**Exemplo**

```coral
de coral.datas importe agora, para_iso, horas

defina inicio como agora("UTC")
mostre para_iso(inicio)
defina intervalo como horas(2)
mostre intervalo
```

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valor` | Valor processado pela operação. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `horas(valor)`

**Origem da implementação:** `coral.stdlib.datas`

**Arquivo na release:** `coral/stdlib/datas.py`

:::

#### `semanas`

Cria uma duração expressa em semanas.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valor` | Valor processado pela operação. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `semanas(valor)`

**Origem da implementação:** `coral.stdlib.datas`

**Arquivo na release:** `coral/stdlib/datas.py`

:::

#### `formatar`

Formata o valor usando a representação solicitada.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valor` | Valor processado pela operação. | `não declarado` | obrigatório |
| `formato` | Formato usado para interpretar ou produzir o valor. | `não declarado` | `'%d/%m/%Y'` |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `formatar(valor, formato = '%d/%m/%Y')`

**Origem da implementação:** `coral.stdlib.datas`

**Arquivo na release:** `coral/stdlib/datas.py`

:::

#### `analisar`

Interpreta o texto e produz o valor correspondente.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `texto` | Texto processado pela operação. | `str` | obrigatório |
| `formato` | Formato usado para interpretar ou produzir o valor. | `str \| None` | `None` |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `analisar(texto: str, formato: str \| None = None)`

**Origem da implementação:** `coral.stdlib.datas`

**Arquivo na release:** `coral/stdlib/datas.py`

**Exceções diretamente observáveis no corpo:** `ValueError`

:::

#### `de_iso`

Interpreta ou reconstrói um valor a partir de iso.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `texto` | Texto processado pela operação. | `str` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `de_iso(texto: str)`

**Origem da implementação:** `coral.stdlib.datas`

**Arquivo na release:** `coral/stdlib/datas.py`

:::

#### `para_iso`

Converte o valor para iso.

**Exemplo**

```coral
de coral.datas importe agora, para_iso, horas

defina inicio como agora("UTC")
mostre para_iso(inicio)
defina intervalo como horas(2)
mostre intervalo
```

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valor` | Valor processado pela operação. | `não declarado` | obrigatório |
| `vezespec` | Valor correspondente a vezespec. | `não declarado` | `'auto'` |

**Retorno**

Retorna um valor declarado como `str`.

:::details Detalhes técnicos

**Assinatura:** `para_iso(valor, *, vezespec = 'auto') -> str`

**Origem da implementação:** `coral.stdlib.datas`

**Arquivo na release:** `coral/stdlib/datas.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `valor` | posicional |
| `vezespec` | nomeado |

**Exceções diretamente observáveis no corpo:** `TypeError`

:::

#### `fuso_horario`

Obter fuso.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | `'UTC'` |

**Retorno**

Retorna um valor declarado como `tzinfo`.

:::details Detalhes técnicos

**Assinatura:** `fuso_horario(nome: str = 'UTC') -> tzinfo`

**Origem da implementação:** `coral.stdlib.datas`

**Arquivo na release:** `coral/stdlib/datas.py`

:::

#### `converter_fuso`

Converter fuso.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valor` | Valor processado pela operação. | `datetime` | obrigatório |
| `fuso` | Valor correspondente a fuso. | `str \| tzinfo` | obrigatório |

**Retorno**

Retorna um valor declarado como `datetime`.

:::details Detalhes técnicos

**Assinatura:** `converter_fuso(valor: datetime, fuso: str \| tzinfo) -> datetime`

**Origem da implementação:** `coral.stdlib.datas`

**Arquivo na release:** `coral/stdlib/datas.py`

**Exceções diretamente observáveis no corpo:** `TypeError`, `ValueError`

:::

#### `diferenca`

Calcular duração.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `final` | Valor correspondente a final. | `não declarado` | obrigatório |
| `inicial` | Valor correspondente a inicial. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `diferenca(final, inicial)`

**Origem da implementação:** `coral.stdlib.datas`

**Arquivo na release:** `coral/stdlib/datas.py`

**Exceções diretamente observáveis no corpo:** `TypeError`

:::

<!-- /AUTO:API -->
