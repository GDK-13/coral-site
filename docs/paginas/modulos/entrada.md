# coral.entrada

## Visão geral

`coral.entrada` oferece entrada interceptável e testável. Use quando a leitura de entrada precisa ser substituível em testes ou controlada por outra fonte.

<!-- AUTO:MODULO -->

**Importação:** `coral.entrada`  
**Categoria:** runtime  

entrada interceptável e testável

### Superfície pública detectada

`FonteEntrada`, `FonteEntradaFuncao`, `FonteEntradaSequencial`, `FimDeEntrada`, `ler_linha`, `usar_fonte_entrada`

<!-- /AUTO:MODULO -->

## Quando usar

Use quando a leitura de entrada precisa ser substituível em testes ou controlada por outra fonte.

Entre as entradas públicas detectadas estão `ler_linha`, `usar_fonte_entrada`, `FonteEntradaSequencial`.

## Começando

A release inclui um exemplo real em `Exemplos/Dados/01_entrada_conversoes_e_texto.coral`:

```coral
# Entrada, conversão explícita e composição de texto.
de coral.entrada importe ler_linha
de coral.conversoes importe inteiro, decimal
de coral.formatacao importe montar_texto

defina nome como ler_linha("Nome: ")
defina idade como inteiro(ler_linha("Idade: "))
defina altura como decimal(ler_linha("Altura em metros: "))
mostre montar_texto("Olá, ", nome, ". Idade: ", idade, ". Altura: ", altura)
```

## Cuidados

Separar a fonte de entrada facilita testes determinísticos e evita depender do teclado real.

## Relações com outros módulos

Na mesma área, veja também `coral.assincrono`, `coral.comum`, `coral.conversoes`, `coral.tipos`.

## Referência da API

<!-- AUTO:API -->

### Funções

#### `ler_linha(mensagem: str | None = None, *, fonte: FonteEntrada | FonteEntradaFuncao | None = None) -> str`

Lê uma linha usando a fonte explícita, contextual ou o terminal.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `mensagem` | `str \| None` | `None` | posicional |
| `fonte` | `FonteEntrada \| FonteEntradaFuncao \| None` | `None` | nomeado |

**Retorno:** `str`

**Exceções observáveis no corpo:** `FimDeEntrada`

#### `usar_fonte_entrada(fonte: FonteEntrada | FonteEntradaFuncao)`

Instala temporariamente uma fonte de entrada no contexto corrente.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `fonte` | `FonteEntrada \| FonteEntradaFuncao` | obrigatório | posicional |

**Retorno:** `não declarado`

### Classes e protocolos

#### `FonteEntrada(...)`

Entrada pública `FonteEntrada` da superfície `coral.entrada`.

**Métodos e propriedades públicas**

| Nome | Tipo | Assinatura | Retorno | Descrição |
|---|---|---|---|---|
| `ler_linha` | método | `ler_linha(mensagem: str = '') -> str` | `str` | Sem docstring própria na release. |

#### `FonteEntradaSequencial(linhas: Iterable[str])`

Fonte determinística útil em testes, REPLs e ferramentas.

**Atributos declarados**

| Nome | Tipo | Padrão |
|---|---|---|
| `linhas` | `Iterable[str]` | obrigatório |

**Métodos e propriedades públicas**

| Nome | Tipo | Assinatura | Retorno | Descrição |
|---|---|---|---|---|
| `ler_linha` | método | `ler_linha(mensagem: str = '') -> str` | `str` | Sem docstring própria na release. |

### Exceções

#### `FimDeEntrada(...)`

A fonte de entrada terminou antes de produzir outra linha.

**Implementação:** `coral.erros`

### Constantes e aliases

#### `FonteEntradaFuncao`

Alias público de tipo ou valor.

**Valor declarado:** `Callable[[str], str]`

<!-- /AUTO:API -->
