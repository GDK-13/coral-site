# coral.caminhos

## Visão geral

`coral.caminhos` oferece normalização explícita de caminhos locais e portáteis. Use para juntar e normalizar caminhos de forma explícita e mais portátil entre sistemas.

<!-- AUTO:MODULO -->

**Importação:** `coral.caminhos`  
**Categoria:** sistema  

normalização explícita de caminhos locais e portáteis

### Superfície pública detectada

`CaminhoAceito`, `normalizar_caminho`, `juntar_caminho`, `estilo_caminho`, `estilo_nativo`, `caminho_portatil`

<!-- /AUTO:MODULO -->

## Quando usar

Use para juntar e normalizar caminhos de forma explícita e mais portátil entre sistemas.

Entre as entradas públicas detectadas estão `normalizar_caminho`, `juntar_caminho`.

## Começando

A release inclui um exemplo real em `Exemplos/Dados/02_arquivos_json_e_caminhos.coral`:

```coral
de coral.json importe para_json, de_json
de coral.caminhos importe juntar_caminho

defina caminho_texto como juntar_caminho("dados", "mensagem.txt")
mostre caminho_texto

execute escrever_texto("mensagem.txt", "Olá, arquivo!")
defina conteudo como ler_texto("mensagem.txt")
mostre conteudo

defina original como {"nome": "Ana", "nota": 9}
```

## Cuidados

Evite montar caminhos manualmente por concatenação de barras.

## Relações com outros módulos

Na mesma área, veja também `coral.arquivos`, `coral.sistema`.

## Referência da API

<!-- AUTO:API -->

### Funções

#### `normalizar_caminho(valor: CaminhoAceito, *, expandir_usuario: bool = False, resolver: bool = False) -> Path`

Converte uma entrada para ``Path`` nativo com regras explícitas.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `valor` | `CaminhoAceito` | obrigatório | posicional |
| `expandir_usuario` | `bool` | `False` | nomeado |
| `resolver` | `bool` | `False` | nomeado |

**Retorno:** `Path`

**Exceções observáveis no corpo:** `ValueError`, `TypeError`

#### `juntar_caminho(*partes: Any, expandir_usuario: bool = True) -> Path`

Entrada pública `juntar_caminho` da superfície `coral.caminhos`.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `*partes` | `Any` | obrigatório | variádico |
| `expandir_usuario` | `bool` | `True` | nomeado |

**Retorno:** `Path`

#### `estilo_caminho(valor: PurePath) -> str`

Entrada pública `estilo_caminho` da superfície `coral.caminhos`.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `valor` | `PurePath` | obrigatório | posicional |

**Retorno:** `str`

#### `estilo_nativo() -> str`

Entrada pública `estilo_nativo` da superfície `coral.caminhos`.

**Retorno:** `str`

#### `caminho_portatil(texto: str, estilo: str, *, concreto: bool = True) -> PurePath`

Reconstrói a categoria caminho sem fingir compatibilidade entre SOs.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `texto` | `str` | obrigatório | posicional |
| `estilo` | `str` | obrigatório | posicional |
| `concreto` | `bool` | `True` | nomeado |

**Retorno:** `PurePath`

**Exceções observáveis no corpo:** `ValueError`

### Constantes e aliases

#### `CaminhoAceito`

Alias público de tipo ou valor.

**Valor declarado:** `str | os.PathLike[str]`

<!-- /AUTO:API -->
