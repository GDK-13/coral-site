# coral.tipos

## Visão geral

`coral.tipos` oferece consulta e teste de categorias de valor. Use para consultar e testar categorias de valor quando a lógica realmente depende do tipo em tempo de execução.

<!-- AUTO:MODULO -->

**Importação:** `coral.tipos`  
**Categoria:** runtime  

consulta e teste de categorias de valor

### Superfície pública detectada

`TIPOS_CORAL`, `traduzir_tipo`, `TipoCoral`, `tipo_de`, `nome_tipo`, `e_tipo`

<!-- /AUTO:MODULO -->

## Papel no ecossistema

Expõe a visão de categorias de valor do runtime Coral. É útil para introspecção, validação e ferramentas, mas não deve substituir um desenho orientado ao comportamento quando o tipo concreto não importa.

## Conceitos principais

### Descritor

`TipoCoral` contém nome, tipos Python associados e aliases.

### Descoberta

`tipo_de` produz o descritor e `nome_tipo` retorna o nome textual da categoria.

### Teste

`e_tipo` aceita nome Coral, classe ou `TipoCoral` como expectativa.

### Tradução

`traduzir_tipo` converte nomes da sintaxe Coral para o nome técnico correspondente quando existe no mapa.

### Mapa público

`TIPOS_CORAL` expõe aliases básicos reconhecidos pela camada de tradução.

## Quando usar

Use este módulo quando o problema corresponder diretamente aos conceitos acima. Por ser um módulo complementar, ele normalmente entra em um programa para resolver uma responsabilidade específica e deve permanecer desacoplado da lógica central sempre que possível.

## Começando

```coral
de coral.tipos importe tipo_de, nome_tipo, e_tipo

defina valor como 42
mostre tipo_de(valor)
mostre nome_tipo(valor)
garanta que e_tipo(valor, "inteiro") for igual a verdadeiro
```

## API essencial

| Entrada | Papel |
|---|---|
| `tipo_de` | descobrir categoria |
| `nome_tipo` | obter nome Coral |
| `e_tipo` | testar categoria |
| `traduzir_tipo` | traduzir nome |
| `TipoCoral` | descritor |
| `TIPOS_CORAL` | mapa de aliases |

A seção **Referência da API** no fim desta página contém a superfície pública completa detectada na release, com assinaturas, parâmetros, retornos e docstrings quando presentes.

## Fluxos comuns

1. Use introspecção na borda de ferramentas, serialização ou APIs genéricas.
2. Quando o programa conhece a expectativa, prefira `e_tipo` a comparar strings de nome manualmente.
3. Depois da validação, deixe a lógica trabalhar com comportamento ou dados já normalizados.

## Erros e casos de borda

Booleano é tratado separadamente de inteiro apesar da herança do host. Datas, data e hora, duração e caminho também possuem categorias próprias no runtime.

## Boas práticas

* Não ramifique todo o domínio por `nome_tipo` se polimorfismo ou funções separadas forem mais claros.
* Use aliases Coral aceitos em vez de nomes Python quando a interface é voltada ao usuário.
* Considere `coral.conversoes` quando a intenção é transformar, não apenas inspecionar.

## Integração com outros módulos

`coral.conversoes` transforma valores; `coral.persistencia` consulta categorias para valores portáteis; ferramentas e diagnósticos podem exibir nomes Coral ao usuário.

## Testabilidade e previsibilidade

Teste diferenças intencionais como booleano versus inteiro, data versus data e hora, além de aliases acentuados e não acentuados.

## Compatibilidade e evolução

A documentação desta página descreve a superfície detectada na **Coral 1.5.12**. O gerador do site atualiza automaticamente o inventário e a referência da API quando uma nova release é importada, mas o texto pedagógico desta seção permanece sob revisão humana.

## Referência da API

<!-- AUTO:API -->

### Funções

#### `traduzir_tipo`

Traduzir nome.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `tipo` | Tipo solicitado para o resultado, quando o módulo oferece essa escolha. | `str` | obrigatório |

**Retorno**

Retorna um valor declarado como `str`.

:::details Detalhes técnicos

**Assinatura:** `traduzir_tipo(tipo: str) -> str`

**Origem da implementação:** `coral.tipos`

**Arquivo na release:** `coral/tipos.py`

:::

#### `tipo_de`

Descobrir categoria.

**Exemplo**

```coral
de coral.tipos importe tipo_de, nome_tipo, e_tipo

defina valor como 42
mostre tipo_de(valor)
mostre nome_tipo(valor)
garanta que e_tipo(valor, "inteiro") for igual a verdadeiro
```

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valor` | Valor processado pela operação. | `Any` | obrigatório |

**Retorno**

Retorna um valor declarado como `TipoCoral`.

:::details Detalhes técnicos

**Assinatura:** `tipo_de(valor: Any) -> TipoCoral`

**Origem da implementação:** `coral.tipos`

**Arquivo na release:** `coral/tipos.py`

:::

#### `nome_tipo`

Obter nome Coral.

**Exemplo**

```coral
de coral.tipos importe tipo_de, nome_tipo, e_tipo

defina valor como 42
mostre tipo_de(valor)
mostre nome_tipo(valor)
garanta que e_tipo(valor, "inteiro") for igual a verdadeiro
```

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valor` | Valor processado pela operação. | `Any` | obrigatório |

**Retorno**

Retorna um valor declarado como `str`.

:::details Detalhes técnicos

**Assinatura:** `nome_tipo(valor: Any) -> str`

**Origem da implementação:** `coral.tipos`

**Arquivo na release:** `coral/tipos.py`

:::

#### `e_tipo`

Testar categoria.

**Exemplo**

```coral
de coral.tipos importe tipo_de, nome_tipo, e_tipo

defina valor como 42
mostre tipo_de(valor)
mostre nome_tipo(valor)
garanta que e_tipo(valor, "inteiro") for igual a verdadeiro
```

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valor` | Valor processado pela operação. | `Any` | obrigatório |
| `esperado` | Valor correspondente a esperado. | `str \| type \| TipoCoral` | obrigatório |

**Retorno**

Retorna um valor declarado como `bool`.

:::details Detalhes técnicos

**Assinatura:** `e_tipo(valor: Any, esperado: str \| type \| TipoCoral) -> bool`

**Origem da implementação:** `coral.tipos`

**Arquivo na release:** `coral/tipos.py`

:::

### Classes e protocolos

#### `TipoCoral`

Representa descritor.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | obrigatório |
| `tipos_python` | Valor correspondente a tipos python. | `tuple[type, ...]` | `()` |
| `aliases` | Valor correspondente a aliases. | `tuple[str, ...]` | `()` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | obrigatório |
| `tipos_python` | Valor correspondente a tipos python. | `tuple[type, ...]` | `()` |
| `aliases` | Valor correspondente a aliases. | `tuple[str, ...]` | `()` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `aceita` | Executa a operação `aceita` disponibilizada por `coral.tipos`. | `bool` |

:::details Detalhes técnicos

**Assinatura:** `TipoCoral(nome: str, tipos_python: tuple[type, ...] = (), aliases: tuple[str, ...] = ())`

**Origem da implementação:** `coral.tipos`

**Arquivo na release:** `coral/tipos.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `aceita` | método | `aceita(valor: Any) -> bool` |

:::

### Constantes e aliases

#### `TIPOS_CORAL`

Expõe a constante pública `TIPOS_CORAL`.

:::details Detalhes técnicos

**Assinatura:** `TIPOS_CORAL`

**Origem da implementação:** `coral.tipos`

**Arquivo na release:** `coral/tipos.py`

**Valor declarado:** `{'inteiro': 'int', 'decimal': 'float', 'número': 'float', 'numero': 'float', 'texto': 'str', 'booleano': 'bool', 'lógico': 'bool', 'logico': 'bool', 'lista': 'list', 'dicionário': 'dict', 'dicionario': 'dict', 'conjunto': 'set', 'tupla': 't`

:::

<!-- /AUTO:API -->
