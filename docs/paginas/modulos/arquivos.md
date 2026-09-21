# coral.arquivos

## Visão geral

`coral.arquivos` oferece ler, escrever e organizar arquivos e caminhos locais. Use para ler e escrever dados locais, criar pastas e organizar arquivos sem espalhar chamadas de sistema pelo programa.

<!-- AUTO:MODULO -->

**Importação:** `coral.arquivos`  
**Categoria:** sistema  

ler, escrever e organizar arquivos e caminhos locais

### Superfície pública detectada

`ler_texto`, `escrever_texto`, `adicionar_texto`, `ler_bytes`, `escrever_bytes`, `existe`, `listar`, `listar_recursivo`, `criar_pasta`, `remover`, `renomear`, `copiar`, `mover`, `tamanho`, `metadados`, `arquivo_temporario`, `pasta_temporaria`, `nome`, `extensao`, `pai`, `resolver`

<!-- /AUTO:MODULO -->

## Quando usar

Use para ler e escrever dados locais, criar pastas e organizar arquivos sem espalhar chamadas de sistema pelo programa.

Entre as entradas públicas detectadas estão `ler_texto`, `escrever_texto`, `adicionar_texto`, `ler_bytes`, `escrever_bytes`, `existe`.

## Começando

A release inclui um exemplo real em `Exemplos/Dados/02_arquivos_json_e_caminhos.coral`:

```coral
# Arquivos, JSON, caminhos e contexto de leitura.
de coral.arquivos importe escrever_texto, ler_texto
de coral.json importe para_json, de_json
de coral.caminhos importe juntar_caminho

defina caminho_texto como juntar_caminho("dados", "mensagem.txt")
mostre caminho_texto

execute escrever_texto("mensagem.txt", "Olá, arquivo!")
defina conteudo como ler_texto("mensagem.txt")
mostre conteudo
```

## Cuidados

Operações de escrita, remoção e movimento alteram o sistema de arquivos. Valide caminhos e trate falhas operacionais.

## Relações com outros módulos

Na mesma área, veja também `coral.caminhos`, `coral.sistema`.

## Referência da API

<!-- AUTO:API -->

### Funções

#### `ler_texto(caminho, codificacao = 'utf-8')`

Entrada pública `ler_texto` da superfície `coral.arquivos`.

**Implementação:** `coral.stdlib.arquivos`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `caminho` | `não declarado` | obrigatório | posicional |
| `codificacao` | `não declarado` | `'utf-8'` | posicional |

**Retorno:** `não declarado`

#### `escrever_texto(caminho, texto, codificacao = 'utf-8')`

Entrada pública `escrever_texto` da superfície `coral.arquivos`.

**Implementação:** `coral.stdlib.arquivos`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `caminho` | `não declarado` | obrigatório | posicional |
| `texto` | `não declarado` | obrigatório | posicional |
| `codificacao` | `não declarado` | `'utf-8'` | posicional |

**Retorno:** `não declarado`

#### `adicionar_texto(caminho, texto, codificacao = 'utf-8')`

Entrada pública `adicionar_texto` da superfície `coral.arquivos`.

**Implementação:** `coral.stdlib.arquivos`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `caminho` | `não declarado` | obrigatório | posicional |
| `texto` | `não declarado` | obrigatório | posicional |
| `codificacao` | `não declarado` | `'utf-8'` | posicional |

**Retorno:** `não declarado`

#### `ler_bytes(caminho) -> bytes`

Entrada pública `ler_bytes` da superfície `coral.arquivos`.

**Implementação:** `coral.stdlib.arquivos`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `caminho` | `não declarado` | obrigatório | posicional |

**Retorno:** `bytes`

#### `escrever_bytes(caminho, dados) -> None`

Entrada pública `escrever_bytes` da superfície `coral.arquivos`.

**Implementação:** `coral.stdlib.arquivos`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `caminho` | `não declarado` | obrigatório | posicional |
| `dados` | `não declarado` | obrigatório | posicional |

**Retorno:** `None`

**Exceções observáveis no corpo:** `TypeError`

#### `existe(caminho)`

Entrada pública `existe` da superfície `coral.arquivos`.

**Implementação:** `coral.stdlib.arquivos`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `caminho` | `não declarado` | obrigatório | posicional |

**Retorno:** `não declarado`

#### `listar(caminho = '.')`

Entrada pública `listar` da superfície `coral.arquivos`.

**Implementação:** `coral.stdlib.arquivos`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `caminho` | `não declarado` | `'.'` | posicional |

**Retorno:** `não declarado`

#### `listar_recursivo(caminho = '.', *, profundidade: int | None = None, incluir_pastas: bool = False)`

Entrada pública `listar_recursivo` da superfície `coral.arquivos`.

**Implementação:** `coral.stdlib.arquivos`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `caminho` | `não declarado` | `'.'` | posicional |
| `profundidade` | `int \| None` | `None` | nomeado |
| `incluir_pastas` | `bool` | `False` | nomeado |

**Retorno:** `não declarado`

**Exceções observáveis no corpo:** `ValueError`, `_erro_arquivo_em_portugues`

#### `criar_pasta(caminho)`

Entrada pública `criar_pasta` da superfície `coral.arquivos`.

**Implementação:** `coral.stdlib.arquivos`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `caminho` | `não declarado` | obrigatório | posicional |

**Retorno:** `não declarado`

#### `remover(caminho, *, recursivo: bool = False) -> None`

Entrada pública `remover` da superfície `coral.arquivos`.

**Implementação:** `coral.stdlib.arquivos`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `caminho` | `não declarado` | obrigatório | posicional |
| `recursivo` | `bool` | `False` | nomeado |

**Retorno:** `None`

#### `renomear(caminho, destino) -> Path`

Entrada pública `renomear` da superfície `coral.arquivos`.

**Implementação:** `coral.stdlib.arquivos`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `caminho` | `não declarado` | obrigatório | posicional |
| `destino` | `não declarado` | obrigatório | posicional |

**Retorno:** `Path`

#### `copiar(caminho, destino, *, recursivo: bool = False) -> Path`

Entrada pública `copiar` da superfície `coral.arquivos`.

**Implementação:** `coral.stdlib.arquivos`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `caminho` | `não declarado` | obrigatório | posicional |
| `destino` | `não declarado` | obrigatório | posicional |
| `recursivo` | `bool` | `False` | nomeado |

**Retorno:** `Path`

**Exceções observáveis no corpo:** `IsADirectoryError`

#### `mover(caminho, destino) -> Path`

Entrada pública `mover` da superfície `coral.arquivos`.

**Implementação:** `coral.stdlib.arquivos`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `caminho` | `não declarado` | obrigatório | posicional |
| `destino` | `não declarado` | obrigatório | posicional |

**Retorno:** `Path`

#### `tamanho(caminho) -> int`

Entrada pública `tamanho` da superfície `coral.arquivos`.

**Implementação:** `coral.stdlib.arquivos`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `caminho` | `não declarado` | obrigatório | posicional |

**Retorno:** `int`

#### `metadados(caminho) -> dict[str, Any]`

Entrada pública `metadados` da superfície `coral.arquivos`.

**Implementação:** `coral.stdlib.arquivos`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `caminho` | `não declarado` | obrigatório | posicional |

**Retorno:** `dict[str, Any]`

#### `arquivo_temporario(*, prefixo = 'coral_', sufixo = '', pasta = None) -> Path`

Entrada pública `arquivo_temporario` da superfície `coral.arquivos`.

**Implementação:** `coral.stdlib.arquivos`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `prefixo` | `não declarado` | `'coral_'` | nomeado |
| `sufixo` | `não declarado` | `''` | nomeado |
| `pasta` | `não declarado` | `None` | nomeado |

**Retorno:** `Path`

#### `pasta_temporaria(*, prefixo = 'coral_', pasta = None) -> Path`

Entrada pública `pasta_temporaria` da superfície `coral.arquivos`.

**Implementação:** `coral.stdlib.arquivos`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `prefixo` | `não declarado` | `'coral_'` | nomeado |
| `pasta` | `não declarado` | `None` | nomeado |

**Retorno:** `Path`

#### `nome(caminho) -> str`

Entrada pública `nome` da superfície `coral.arquivos`.

**Implementação:** `coral.stdlib.arquivos`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `caminho` | `não declarado` | obrigatório | posicional |

**Retorno:** `str`

#### `extensao(caminho) -> str`

Entrada pública `extensao` da superfície `coral.arquivos`.

**Implementação:** `coral.stdlib.arquivos`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `caminho` | `não declarado` | obrigatório | posicional |

**Retorno:** `str`

#### `pai(caminho) -> Path`

Entrada pública `pai` da superfície `coral.arquivos`.

**Implementação:** `coral.stdlib.arquivos`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `caminho` | `não declarado` | obrigatório | posicional |

**Retorno:** `Path`

#### `resolver(caminho, *, estrito: bool = False) -> Path`

Entrada pública `resolver` da superfície `coral.arquivos`.

**Implementação:** `coral.stdlib.arquivos`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `caminho` | `não declarado` | obrigatório | posicional |
| `estrito` | `bool` | `False` | nomeado |

**Retorno:** `Path`

<!-- /AUTO:API -->
