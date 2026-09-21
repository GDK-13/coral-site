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

## Quando usar

Use para consultar e testar categorias de valor quando a lógica realmente depende do tipo em tempo de execução.

Entre as entradas públicas detectadas estão `tipo_de`, `nome_tipo`, `e_tipo`.

## Começando

Uma importação seletiva começa assim:

```coral
de coral.tipos importe tipo_de, nome_tipo, e_tipo
```

Depois da importação, use o hover e o preenchimento do VS Code para consultar a assinatura exata disponível na release.

## Cuidados

Prefira código orientado ao comportamento quando não for necessário ramificar por categoria de valor.

## Relações com outros módulos

Na mesma área, veja também `coral.assincrono`, `coral.comum`, `coral.conversoes`, `coral.entrada`.

## Referência da API

<!-- AUTO:API -->

### Funções

#### `traduzir_tipo(tipo: str) -> str`

Entrada pública `traduzir_tipo` da superfície `coral.tipos`.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `tipo` | `str` | obrigatório | posicional |

**Retorno:** `str`

#### `tipo_de(valor: Any) -> TipoCoral`

Entrada pública `tipo_de` da superfície `coral.tipos`.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `valor` | `Any` | obrigatório | posicional |

**Retorno:** `TipoCoral`

#### `nome_tipo(valor: Any) -> str`

Entrada pública `nome_tipo` da superfície `coral.tipos`.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `valor` | `Any` | obrigatório | posicional |

**Retorno:** `str`

#### `e_tipo(valor: Any, esperado: str | type | TipoCoral) -> bool`

Entrada pública `e_tipo` da superfície `coral.tipos`.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `valor` | `Any` | obrigatório | posicional |
| `esperado` | `str \| type \| TipoCoral` | obrigatório | posicional |

**Retorno:** `bool`

### Classes e protocolos

#### `TipoCoral(nome: str, tipos_python: tuple[type, ...] = (), aliases: tuple[str, ...] = ())`

Entrada pública `TipoCoral` da superfície `coral.tipos`.

**Atributos declarados**

| Nome | Tipo | Padrão |
|---|---|---|
| `nome` | `str` | obrigatório |
| `tipos_python` | `tuple[type, ...]` | `()` |
| `aliases` | `tuple[str, ...]` | `()` |

**Métodos e propriedades públicas**

| Nome | Tipo | Assinatura | Retorno | Descrição |
|---|---|---|---|---|
| `aceita` | método | `aceita(valor: Any) -> bool` | `bool` | Sem docstring própria na release. |

### Constantes e aliases

#### `TIPOS_CORAL`

Constante pública do módulo.

**Valor declarado:** `{'inteiro': 'int', 'decimal': 'float', 'número': 'float', 'numero': 'float', 'texto': 'str', 'booleano': 'bool', 'lógico': 'bool', 'logico': 'bool', 'lista': 'list', 'dicionário': 'dict', 'dicionario': 'dict', 'conjunto': 'set', 'tupla': 't`

<!-- /AUTO:API -->
