# coral.texto

## Visão geral

`coral.texto` oferece transformar, localizar, normalizar e formatar texto. Use para transformar, localizar, normalizar e formatar texto.

<!-- AUTO:MODULO -->

**Importação:** `coral.texto`  
**Categoria:** texto  

transformar, localizar, normalizar e formatar texto

### Superfície pública detectada

`maiusculas`, `minusculas`, `aparar`, `dividir`, `juntar`, `substituir`, `comeca_com`, `termina_com`, `localizar`, `contar`, `normalizar_unicode`, `linhas`, `remover_prefixo`, `remover_sufixo`, `preencher`, `formatar`

<!-- /AUTO:MODULO -->

## Papel no ecossistema

É a caixa de ferramentas para transformação, busca e normalização de texto. As operações são pequenas, explícitas e projetadas para compor pipelines de tratamento de entrada humana e dados textuais.

## Conceitos principais

### Caixa e espaços

`maiusculas`, `minusculas` e `aparar` cuidam de normalização básica.

### Divisão e junção

`dividir` e `juntar` transformam entre texto e sequências.

### Busca

`comeca_com`, `termina_com`, `localizar` e `contar` inspecionam conteúdo.

### Substituição

`substituir`, `remover_prefixo` e `remover_sufixo` alteram trechos conhecidos.

### Unicode

`normalizar_unicode` torna explícita a forma Unicode antes de comparação ou armazenamento.

### Linhas e preenchimento

`linhas` separa linhas com controle de quebras e `preencher` alinha ou completa texto.

### Formatação por modelo

`formatar` fornece a operação textual publicada pelo módulo; para montagem simples por partes, `coral.formatacao` também é apropriado.

## Quando usar

Use este módulo quando o problema corresponder diretamente aos conceitos acima. Por ser um módulo complementar, ele normalmente entra em um programa para resolver uma responsabilidade específica e deve permanecer desacoplado da lógica central sempre que possível.

## Começando

A release inclui um exemplo real em `Exemplos/Dados/05_utilitarios_e_interoperabilidade.coral`:

```coral
# Biblioteca padrão Coral e interoperabilidade explícita com Python.
de coral.texto importe maiusculas

crie um vetor chamado dados com [7, 8, 9]
calcule a média de dados como media_dados
mostre media_dados
mostre maiusculas("Coral")

python: import math
defina raiz como math.sqrt(81)
mostre raiz
```

## API essencial

| Entrada | Papel |
|---|---|
| `aparar` | remover bordas de espaço |
| `dividir` / `juntar` | segmentar e recompor |
| `substituir` | trocar trecho |
| `localizar` / `contar` | buscar ocorrências |
| `normalizar_unicode` | normalizar Unicode |
| `linhas` | separar linhas |
| `preencher` | alinhar/preencher |
| `formatar` | formatar texto |

A seção **Referência da API** no fim desta página contém a superfície pública completa detectada na release, com assinaturas, parâmetros, retornos e docstrings quando presentes.

## Fluxos comuns

1. Normalize Unicode quando o texto pode vir de fontes diferentes.
2. Apare e normalize caixa somente quando isso fizer sentido para a regra de comparação.
3. Separe parsing textual da lógica de domínio.
4. Mantenha o texto original quando a apresentação ou auditoria exigir fidelidade.

## Erros e casos de borda

Duas strings visualmente iguais podem ter sequências Unicode diferentes. Busca sensível a caixa e substituição literal também podem surpreender quando o programa presume normalização implícita.

## Boas práticas

* Normalize antes de comparar identificadores humanos quando apropriado.
* Não destrua caixa ou acentuação se elas fazem parte do dado.
* Evite cadeias longas de transformação sem nomes intermediários quando a intenção ficar difícil de ler.

## Integração com outros módulos

`coral.entrada` fornece texto bruto; `coral.conversoes` transforma texto em tipos; `coral.formatacao` monta saída; `coral.formatos` trabalha com representações estruturadas.

## Testabilidade e previsibilidade

Inclua acentos, Unicode composto/decomposto, string vazia, múltiplas linhas e ausência de trecho nos testes relevantes.

## Compatibilidade e evolução

A documentação desta página descreve a superfície detectada na **Coral 1.6.0**. O gerador do site atualiza automaticamente o inventário e a referência da API quando uma nova release é importada, mas o texto pedagógico desta seção permanece sob revisão humana.

## Referência da API

<!-- AUTO:API -->

### Funções

#### `maiusculas`

Converte o texto para maiusculas.

**Exemplo**

```coral
calcule a média de dados como media_dados
mostre media_dados
mostre maiusculas("Coral")

python: import math
defina raiz como math.sqrt(81)
```

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valor` | Valor processado pela operação. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `maiusculas(valor)`

**Origem da implementação:** `coral.stdlib.texto`

**Arquivo na release:** `coral/stdlib/texto.py`

:::

#### `minusculas`

Converte o texto para minusculas.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valor` | Valor processado pela operação. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `minusculas(valor)`

**Origem da implementação:** `coral.stdlib.texto`

**Arquivo na release:** `coral/stdlib/texto.py`

:::

#### `aparar`

Remover bordas de espaço.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valor` | Valor processado pela operação. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `aparar(valor)`

**Origem da implementação:** `coral.stdlib.texto`

**Arquivo na release:** `coral/stdlib/texto.py`

:::

#### `dividir`

Segmentar e recompor.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valor` | Valor processado pela operação. | `não declarado` | obrigatório |
| `separador` | Texto usado para separar partes do resultado. | `não declarado` | `None` |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `dividir(valor, separador = None)`

**Origem da implementação:** `coral.stdlib.texto`

**Arquivo na release:** `coral/stdlib/texto.py`

:::

#### `juntar`

Segmentar e recompor.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `separador` | Texto usado para separar partes do resultado. | `não declarado` | obrigatório |
| `valores` | Coleção de valores processada. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `juntar(separador, valores)`

**Origem da implementação:** `coral.stdlib.texto`

**Arquivo na release:** `coral/stdlib/texto.py`

:::

#### `substituir`

Trocar trecho.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valor` | Valor processado pela operação. | `não declarado` | obrigatório |
| `antigo` | Valor correspondente a antigo. | `não declarado` | obrigatório |
| `novo` | Valor correspondente a novo. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `substituir(valor, antigo, novo)`

**Origem da implementação:** `coral.stdlib.texto`

**Arquivo na release:** `coral/stdlib/texto.py`

:::

#### `comeca_com`

Indica se o texto começa com o trecho informado.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valor` | Valor processado pela operação. | `não declarado` | obrigatório |
| `prefixo` | Valor correspondente a prefixo. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `comeca_com(valor, prefixo)`

**Origem da implementação:** `coral.stdlib.texto`

**Arquivo na release:** `coral/stdlib/texto.py`

:::

#### `termina_com`

Indica se o texto termina com o trecho informado.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valor` | Valor processado pela operação. | `não declarado` | obrigatório |
| `sufixo` | Valor correspondente a sufixo. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `termina_com(valor, sufixo)`

**Origem da implementação:** `coral.stdlib.texto`

**Arquivo na release:** `coral/stdlib/texto.py`

:::

#### `localizar`

Buscar ocorrências.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valor` | Valor processado pela operação. | `não declarado` | obrigatório |
| `trecho` | Valor correspondente a trecho. | `não declarado` | obrigatório |
| `inicio` | Valor inicial do intervalo ou processo. | `não declarado` | `0` |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `localizar(valor, trecho, inicio = 0)`

**Origem da implementação:** `coral.stdlib.texto`

**Arquivo na release:** `coral/stdlib/texto.py`

:::

#### `contar`

Buscar ocorrências.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valor` | Valor processado pela operação. | `não declarado` | obrigatório |
| `trecho` | Valor correspondente a trecho. | `não declarado` | obrigatório |
| `inicio` | Valor inicial do intervalo ou processo. | `não declarado` | `0` |
| `fim` | Valor final do intervalo ou processo. | `não declarado` | `None` |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `contar(valor, trecho, inicio = 0, fim = None)`

**Origem da implementação:** `coral.stdlib.texto`

**Arquivo na release:** `coral/stdlib/texto.py`

:::

#### `normalizar_unicode`

Normalizar Unicode.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valor` | Valor processado pela operação. | `não declarado` | obrigatório |
| `forma` | Forma ou dimensões da estrutura a criar. | `não declarado` | `'NFC'` |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `normalizar_unicode(valor, forma = 'NFC')`

**Origem da implementação:** `coral.stdlib.texto`

**Arquivo na release:** `coral/stdlib/texto.py`

**Exceções diretamente observáveis no corpo:** `ValueError`

:::

#### `linhas`

Separar linhas.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valor` | Valor processado pela operação. | `não declarado` | obrigatório |
| `manter_quebras` | Valor correspondente a manter quebras. | `não declarado` | `False` |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `linhas(valor, *, manter_quebras = False)`

**Origem da implementação:** `coral.stdlib.texto`

**Arquivo na release:** `coral/stdlib/texto.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `valor` | posicional |
| `manter_quebras` | nomeado |

:::

#### `remover_prefixo`

Remove prefixo.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valor` | Valor processado pela operação. | `não declarado` | obrigatório |
| `prefixo` | Valor correspondente a prefixo. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `remover_prefixo(valor, prefixo)`

**Origem da implementação:** `coral.stdlib.texto`

**Arquivo na release:** `coral/stdlib/texto.py`

:::

#### `remover_sufixo`

Remove sufixo.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valor` | Valor processado pela operação. | `não declarado` | obrigatório |
| `sufixo` | Valor correspondente a sufixo. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `remover_sufixo(valor, sufixo)`

**Origem da implementação:** `coral.stdlib.texto`

**Arquivo na release:** `coral/stdlib/texto.py`

:::

#### `preencher`

Alinhar/preencher.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valor` | Valor processado pela operação. | `não declarado` | obrigatório |
| `largura` | Largura usada pela operação. | `não declarado` | obrigatório |
| `caractere` | Valor correspondente a caractere. | `não declarado` | `' '` |
| `alinhamento` | Valor correspondente a alinhamento. | `não declarado` | `'direita'` |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `preencher(valor, largura, caractere = ' ', alinhamento = 'direita')`

**Origem da implementação:** `coral.stdlib.texto`

**Arquivo na release:** `coral/stdlib/texto.py`

**Exceções diretamente observáveis no corpo:** `ValueError`

:::

#### `formatar`

Formata placeholders simples sem avaliar expressões ou atributos.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `modelo` | Valor correspondente a modelo. | `não declarado` | obrigatório |
| `valores` | Coleção de valores processada. | `não declarado` | `None` |
| `**campos` | Valor correspondente a campos. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `formatar(modelo, valores = None, **campos)`

**Origem da implementação:** `coral.stdlib.texto`

**Arquivo na release:** `coral/stdlib/texto.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `modelo` | posicional |
| `valores` | posicional |
| `**campos` | variádico nomeado |

**Exceções diretamente observáveis no corpo:** `TypeError`, `ValueError`, `KeyError`

:::

<!-- /AUTO:API -->
