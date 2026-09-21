# coral.criptografia

## Visão geral

`coral.criptografia` oferece fundação introdutória para hash, HMAC e aleatoriedade segura. Use para aprender e aplicar primitivas introdutórias de resumo, autenticação e aleatoriedade segura.

<!-- AUTO:MODULO -->

**Importação:** `coral.criptografia`  
**Categoria:** seguranca  

fundação introdutória para hash, HMAC e aleatoriedade segura

> Aviso: Primitivas isoladas não formam automaticamente um protocolo seguro.

### Superfície pública detectada

`resumir`, `verificar_resumo`, `autenticar`, `verificar_autenticacao`, `gerar_bytes_seguros`, `gerar_token_seguro`, `comparar_com_seguranca`, `listar_algoritmos`, `explicar_algoritmo`

<!-- /AUTO:MODULO -->

## Quando usar

Use para aprender e aplicar primitivas introdutórias de resumo, autenticação e aleatoriedade segura.

Entre as entradas públicas detectadas estão `resumir`, `verificar_resumo`, `autenticar`, `verificar_autenticacao`, `gerar_bytes_seguros`, `gerar_token_seguro`.

## Começando

A release inclui um exemplo real em `Exemplos/Dados/04_criptografia_basica.coral`:

```coral
de coral.formatos importe para_base64
de coral.criptografia importe resumir, verificar_resumo, gerar_token_seguro, autenticar, verificar_autenticacao

defina mensagem como "Coral"
defina codificado como para_base64(mensagem.encode("utf-8"))
defina resumo como resumir(mensagem, "sha256")
defina token como gerar_token_seguro(16, "hex")
defina chave como "chave de exemplo"
defina etiqueta como autenticar(mensagem, chave, "sha256")

garanta que verificar_resumo(mensagem, resumo)
```

## Cuidados

Hash e HMAC não são cifragem. Primitivas isoladas não formam automaticamente um protocolo seguro. Este módulo ainda não faz parte da edição 1.5.8 do Livro.

## Relações com outros módulos

Consulte a navegação lateral para módulos que fornecem dados, sistema, texto ou runtime complementar.

## Referência da API

<!-- AUTO:API -->

### Funções

#### `resumir(dados, algoritmo = 'sha256', formato = 'hex')`

Entrada pública `resumir` da superfície `coral.criptografia`.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `dados` | `não declarado` | obrigatório | posicional |
| `algoritmo` | `não declarado` | `'sha256'` | posicional |
| `formato` | `não declarado` | `'hex'` | posicional |

**Retorno:** `não declarado`

#### `verificar_resumo(dados, esperado, algoritmo = 'sha256', formato = 'hex') -> bool`

Entrada pública `verificar_resumo` da superfície `coral.criptografia`.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `dados` | `não declarado` | obrigatório | posicional |
| `esperado` | `não declarado` | obrigatório | posicional |
| `algoritmo` | `não declarado` | `'sha256'` | posicional |
| `formato` | `não declarado` | `'hex'` | posicional |

**Retorno:** `bool`

#### `autenticar(dados, chave, algoritmo = 'sha256', formato = 'hex')`

Entrada pública `autenticar` da superfície `coral.criptografia`.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `dados` | `não declarado` | obrigatório | posicional |
| `chave` | `não declarado` | obrigatório | posicional |
| `algoritmo` | `não declarado` | `'sha256'` | posicional |
| `formato` | `não declarado` | `'hex'` | posicional |

**Retorno:** `não declarado`

**Exceções observáveis no corpo:** `ErroValor`

#### `verificar_autenticacao(dados, chave, esperado, algoritmo = 'sha256', formato = 'hex') -> bool`

Entrada pública `verificar_autenticacao` da superfície `coral.criptografia`.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `dados` | `não declarado` | obrigatório | posicional |
| `chave` | `não declarado` | obrigatório | posicional |
| `esperado` | `não declarado` | obrigatório | posicional |
| `algoritmo` | `não declarado` | `'sha256'` | posicional |
| `formato` | `não declarado` | `'hex'` | posicional |

**Retorno:** `bool`

**Exceções observáveis no corpo:** `ErroValor`

#### `gerar_bytes_seguros(quantidade = 32) -> bytes`

Entrada pública `gerar_bytes_seguros` da superfície `coral.criptografia`.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `quantidade` | `não declarado` | `32` | posicional |

**Retorno:** `bytes`

**Exceções observáveis no corpo:** `ErroValor`

#### `gerar_token_seguro(bytes_de_entropia = 32, formato = 'url')`

Entrada pública `gerar_token_seguro` da superfície `coral.criptografia`.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `bytes_de_entropia` | `não declarado` | `32` | posicional |
| `formato` | `não declarado` | `'url'` | posicional |

**Retorno:** `não declarado`

**Exceções observáveis no corpo:** `ErroFormato`, `ErroValor`

#### `comparar_com_seguranca(primeiro, segundo) -> bool`

Entrada pública `comparar_com_seguranca` da superfície `coral.criptografia`.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `primeiro` | `não declarado` | obrigatório | posicional |
| `segundo` | `não declarado` | obrigatório | posicional |

**Retorno:** `bool`

#### `listar_algoritmos() -> list[str]`

Entrada pública `listar_algoritmos` da superfície `coral.criptografia`.

**Retorno:** `list[str]`

#### `explicar_algoritmo(nome) -> dict[str, Any]`

Entrada pública `explicar_algoritmo` da superfície `coral.criptografia`.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `nome` | `não declarado` | obrigatório | posicional |

**Retorno:** `dict[str, Any]`

**Exceções observáveis no corpo:** `ErroValor`

<!-- /AUTO:API -->
