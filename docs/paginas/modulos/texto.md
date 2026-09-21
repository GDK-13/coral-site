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

A documentação desta página descreve a superfície detectada na **Coral 1.5.9**. O gerador do site atualiza automaticamente o inventário e a referência da API quando uma nova release é importada, mas o texto pedagógico desta seção permanece sob revisão humana.

## Referência da API

<!-- AUTO:API -->

### Funções

#### `maiusculas(valor)`

Entrada pública `maiusculas` da superfície `coral.texto`.

**Implementação:** `coral.stdlib.texto`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `valor` | `não declarado` | obrigatório | posicional |

**Retorno:** `não declarado`

#### `minusculas(valor)`

Entrada pública `minusculas` da superfície `coral.texto`.

**Implementação:** `coral.stdlib.texto`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `valor` | `não declarado` | obrigatório | posicional |

**Retorno:** `não declarado`

#### `aparar(valor)`

Entrada pública `aparar` da superfície `coral.texto`.

**Implementação:** `coral.stdlib.texto`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `valor` | `não declarado` | obrigatório | posicional |

**Retorno:** `não declarado`

#### `dividir(valor, separador = None)`

Entrada pública `dividir` da superfície `coral.texto`.

**Implementação:** `coral.stdlib.texto`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `valor` | `não declarado` | obrigatório | posicional |
| `separador` | `não declarado` | `None` | posicional |

**Retorno:** `não declarado`

#### `juntar(separador, valores)`

Entrada pública `juntar` da superfície `coral.texto`.

**Implementação:** `coral.stdlib.texto`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `separador` | `não declarado` | obrigatório | posicional |
| `valores` | `não declarado` | obrigatório | posicional |

**Retorno:** `não declarado`

#### `substituir(valor, antigo, novo)`

Entrada pública `substituir` da superfície `coral.texto`.

**Implementação:** `coral.stdlib.texto`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `valor` | `não declarado` | obrigatório | posicional |
| `antigo` | `não declarado` | obrigatório | posicional |
| `novo` | `não declarado` | obrigatório | posicional |

**Retorno:** `não declarado`

#### `comeca_com(valor, prefixo)`

Entrada pública `comeca_com` da superfície `coral.texto`.

**Implementação:** `coral.stdlib.texto`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `valor` | `não declarado` | obrigatório | posicional |
| `prefixo` | `não declarado` | obrigatório | posicional |

**Retorno:** `não declarado`

#### `termina_com(valor, sufixo)`

Entrada pública `termina_com` da superfície `coral.texto`.

**Implementação:** `coral.stdlib.texto`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `valor` | `não declarado` | obrigatório | posicional |
| `sufixo` | `não declarado` | obrigatório | posicional |

**Retorno:** `não declarado`

#### `localizar(valor, trecho, inicio = 0)`

Entrada pública `localizar` da superfície `coral.texto`.

**Implementação:** `coral.stdlib.texto`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `valor` | `não declarado` | obrigatório | posicional |
| `trecho` | `não declarado` | obrigatório | posicional |
| `inicio` | `não declarado` | `0` | posicional |

**Retorno:** `não declarado`

#### `contar(valor, trecho, inicio = 0, fim = None)`

Entrada pública `contar` da superfície `coral.texto`.

**Implementação:** `coral.stdlib.texto`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `valor` | `não declarado` | obrigatório | posicional |
| `trecho` | `não declarado` | obrigatório | posicional |
| `inicio` | `não declarado` | `0` | posicional |
| `fim` | `não declarado` | `None` | posicional |

**Retorno:** `não declarado`

#### `normalizar_unicode(valor, forma = 'NFC')`

Entrada pública `normalizar_unicode` da superfície `coral.texto`.

**Implementação:** `coral.stdlib.texto`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `valor` | `não declarado` | obrigatório | posicional |
| `forma` | `não declarado` | `'NFC'` | posicional |

**Retorno:** `não declarado`

**Exceções observáveis no corpo:** `ValueError`

#### `linhas(valor, *, manter_quebras = False)`

Entrada pública `linhas` da superfície `coral.texto`.

**Implementação:** `coral.stdlib.texto`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `valor` | `não declarado` | obrigatório | posicional |
| `manter_quebras` | `não declarado` | `False` | nomeado |

**Retorno:** `não declarado`

#### `remover_prefixo(valor, prefixo)`

Entrada pública `remover_prefixo` da superfície `coral.texto`.

**Implementação:** `coral.stdlib.texto`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `valor` | `não declarado` | obrigatório | posicional |
| `prefixo` | `não declarado` | obrigatório | posicional |

**Retorno:** `não declarado`

#### `remover_sufixo(valor, sufixo)`

Entrada pública `remover_sufixo` da superfície `coral.texto`.

**Implementação:** `coral.stdlib.texto`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `valor` | `não declarado` | obrigatório | posicional |
| `sufixo` | `não declarado` | obrigatório | posicional |

**Retorno:** `não declarado`

#### `preencher(valor, largura, caractere = ' ', alinhamento = 'direita')`

Entrada pública `preencher` da superfície `coral.texto`.

**Implementação:** `coral.stdlib.texto`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `valor` | `não declarado` | obrigatório | posicional |
| `largura` | `não declarado` | obrigatório | posicional |
| `caractere` | `não declarado` | `' '` | posicional |
| `alinhamento` | `não declarado` | `'direita'` | posicional |

**Retorno:** `não declarado`

**Exceções observáveis no corpo:** `ValueError`

#### `formatar(modelo, valores = None, **campos)`

Formata placeholders simples sem avaliar expressões ou atributos.

**Implementação:** `coral.stdlib.texto`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `modelo` | `não declarado` | obrigatório | posicional |
| `valores` | `não declarado` | `None` | posicional |
| `**campos` | `não declarado` | obrigatório | variádico nomeado |

**Retorno:** `não declarado`

**Exceções observáveis no corpo:** `TypeError`, `ValueError`, `KeyError`

<!-- /AUTO:API -->
