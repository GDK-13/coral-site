# coral.conversoes

## Visão geral

`coral.conversoes` oferece conversões explícitas entre valores Coral. Use para converter valores de forma explícita entre inteiro, decimal, texto e booleano.

<!-- AUTO:MODULO -->

**Importação:** `coral.conversoes`  
**Categoria:** runtime  

conversões explícitas entre valores Coral

### Superfície pública detectada

`ErroConversao`, `inteiro`, `decimal`, `texto`, `booleano`

<!-- /AUTO:MODULO -->

## Papel no ecossistema

Centraliza conversões explícitas e estritas entre valores básicos. O objetivo é evitar coerções implícitas surpreendentes em entradas de usuário, arquivos e APIs.

## Conceitos principais

### Inteiro estrito

`inteiro` aceita inteiro, decimal inteiro exato ou texto inteiro. Booleanos não são tratados como inteiros implicitamente.

### Decimal finito

`decimal` aceita número ou texto decimal; em texto, ponto e vírgula são aceitos individualmente, mas não ao mesmo tempo. Valores infinitos e NaN são recusados.

### Texto Coral

`texto` representa `nulo`, `verdadeiro` e `falso` com a grafia da linguagem.

### Booleano explícito

`booleano` reconhece apenas representações definidas, como verdadeiro/falso, sim/não e 1/0.

### Padrão opcional

As conversões aceitam um valor padrão opcional. Sem padrão, uma entrada inválida gera `ErroConversao`.

## Quando usar

Use este módulo quando o problema corresponder diretamente aos conceitos acima. Por ser um módulo complementar, ele normalmente entra em um programa para resolver uma responsabilidade específica e deve permanecer desacoplado da lógica central sempre que possível.

## Começando

A release inclui um exemplo real em `Exemplos/Dados/01_entrada_conversoes_e_texto.coral`:

```coral
de coral.entrada importe ler_linha
de coral.conversoes importe inteiro, decimal
de coral.formatacao importe montar_texto

defina nome como ler_linha("Nome: ")
defina idade como inteiro(ler_linha("Idade: "))
defina altura como decimal(ler_linha("Altura em metros: "))
mostre montar_texto("Olá, ", nome, ". Idade: ", idade, ". Altura: ", altura)
```

## API essencial

| Entrada | Papel |
|---|---|
| `inteiro` | converter para inteiro |
| `decimal` | converter para decimal finito |
| `texto` | produzir texto com literais Coral |
| `booleano` | converter representação explícita |
| `ErroConversao` | falha de conversão |

A seção **Referência da API** no fim desta página contém a superfície pública completa detectada na release, com assinaturas, parâmetros, retornos e docstrings quando presentes.

## Fluxos comuns

1. Leia ou receba o valor bruto.
2. Converta na fronteira de entrada, antes de espalhar texto cru pelo domínio.
3. Decida se entrada inválida deve gerar erro ou receber padrão explícito.
4. Depois da conversão, mantenha o restante da lógica trabalhando com o tipo correto.

## Erros e casos de borda

Uma string vazia, um número não finito, um decimal não inteiro em `inteiro` ou um booleano ambíguo são recusados. O comportamento é deliberadamente mais estrito do que coerções permissivas.

## Boas práticas

* Converta entrada externa cedo.
* Use padrão apenas quando houver significado real para ele.
* Não trate falha de conversão como zero ou falso automaticamente.

## Integração com outros módulos

Combina diretamente com `coral.entrada`; `coral.formatacao` usa a conversão textual para representar valores; `coral.tipos` ajuda quando a lógica precisa inspecionar tipos já convertidos.

## Testabilidade e previsibilidade

Teste entradas válidas, espaços laterais, formatos alternativos aceitos e valores inválidos. O contrato estrito é justamente o que torna o comportamento previsível.

## Compatibilidade e evolução

A documentação desta página descreve a superfície detectada na **Coral 1.5.12**. O gerador do site atualiza automaticamente o inventário e a referência da API quando uma nova release é importada, mas o texto pedagógico desta seção permanece sob revisão humana.

## Referência da API

<!-- AUTO:API -->

### Funções

#### `inteiro`

Converte para inteiro de forma estrita, com padrão opcional.

**Exemplo**

```coral
de coral.entrada importe ler_linha
de coral.conversoes importe inteiro, decimal
de coral.formatacao importe montar_texto

defina nome como ler_linha("Nome: ")
defina idade como inteiro(ler_linha("Idade: "))
defina altura como decimal(ler_linha("Altura em metros: "))
mostre montar_texto("Olá, ", nome, ". Idade: ", idade, ". Altura: ", altura)
```

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valor` | Valor processado pela operação. | `Any` | obrigatório |
| `padrao` | Valor usado quando não há resultado específico disponível. | `Any` | `_AUSENTE` |

**Retorno**

Retorna o número inteiro sorteado.

:::details Detalhes técnicos

**Assinatura:** `inteiro(valor: Any, padrao: Any = _AUSENTE) -> int \| Any`

**Origem da implementação:** `coral.conversoes`

**Arquivo na release:** `coral/conversoes.py`

**Exceções diretamente observáveis no corpo:** `TypeError`, `ValueError`

:::

#### `decimal`

Converte para decimal finito, aceitando ponto ou vírgula decimal em texto.

**Exemplo**

```coral
de coral.entrada importe ler_linha
de coral.conversoes importe inteiro, decimal
de coral.formatacao importe montar_texto

defina nome como ler_linha("Nome: ")
defina idade como inteiro(ler_linha("Idade: "))
defina altura como decimal(ler_linha("Altura em metros: "))
mostre montar_texto("Olá, ", nome, ". Idade: ", idade, ". Altura: ", altura)
```

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valor` | Valor processado pela operação. | `Any` | obrigatório |
| `padrao` | Valor usado quando não há resultado específico disponível. | `Any` | `_AUSENTE` |

**Retorno**

Retorna o número decimal sorteado.

:::details Detalhes técnicos

**Assinatura:** `decimal(valor: Any, padrao: Any = _AUSENTE) -> float \| Any`

**Origem da implementação:** `coral.conversoes`

**Arquivo na release:** `coral/conversoes.py`

**Exceções diretamente observáveis no corpo:** `ValueError`, `TypeError`

:::

#### `texto`

Produz texto com grafia coerente para os literais básicos da Coral.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valor` | Valor processado pela operação. | `Any` | obrigatório |
| `padrao` | Valor usado quando não há resultado específico disponível. | `Any` | `_AUSENTE` |

**Retorno**

Retorna um valor declarado como `str | Any`.

:::details Detalhes técnicos

**Assinatura:** `texto(valor: Any, padrao: Any = _AUSENTE) -> str \| Any`

**Origem da implementação:** `coral.conversoes`

**Arquivo na release:** `coral/conversoes.py`

:::

#### `booleano`

Converte apenas representações booleanas explícitas e não vazias.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valor` | Valor processado pela operação. | `Any` | obrigatório |
| `padrao` | Valor usado quando não há resultado específico disponível. | `Any` | `_AUSENTE` |

**Retorno**

Retorna um valor declarado como `bool | Any`.

:::details Detalhes técnicos

**Assinatura:** `booleano(valor: Any, padrao: Any = _AUSENTE) -> bool \| Any`

**Origem da implementação:** `coral.conversoes`

**Arquivo na release:** `coral/conversoes.py`

**Exceções diretamente observáveis no corpo:** `TypeError`, `ValueError`

:::

### Exceções

#### `ErroConversao`

Um valor não pôde ser convertido para o tipo Coral solicitado.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valor` | Valor processado pela operação. | `Any` | obrigatório |
| `destino` | Destino que receberá o resultado da operação. | `str` | obrigatório |
| `mensagem` | Valor correspondente a mensagem. | `str \| None` | `None` |
| `causa` | Valor correspondente a causa. | `BaseException \| None` | `None` |

:::details Detalhes técnicos

**Assinatura:** `ErroConversao(valor: Any, destino: str, mensagem: str \| None = None, *, causa: BaseException \| None = None)`

**Origem da implementação:** `coral.erros`

**Arquivo na release:** `coral/erros.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `valor` | posicional |
| `destino` | posicional |
| `mensagem` | posicional |
| `causa` | nomeado |

:::

<!-- /AUTO:API -->
