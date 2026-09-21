# coral.formatos

## Visão geral

`coral.formatos` oferece CSV, hexadecimal e Base64. Use para codificação e formatos auxiliares como CSV, hexadecimal e Base64.

<!-- AUTO:MODULO -->

**Importação:** `coral.formatos`  
**Categoria:** formatos  

CSV, hexadecimal e Base64

> Aviso: Hexadecimal e Base64 são codificações, não mecanismos de segurança.

### Superfície pública detectada

`para_hex`, `de_hex`, `para_base64`, `de_base64`, `para_csv`, `de_csv`

<!-- /AUTO:MODULO -->

## Quando usar

Use para codificação e formatos auxiliares como CSV, hexadecimal e Base64.

Entre as entradas públicas detectadas estão `para_hex`, `de_hex`, `para_base64`, `de_base64`, `para_csv`, `de_csv`.

## Começando

A release inclui um exemplo real em `Exemplos/Dados/04_criptografia_basica.coral`:

```coral
# Codificação, hash, token seguro e autenticação. Nenhum destes recursos cifra dados.
de coral.formatos importe para_base64
de coral.criptografia importe resumir, verificar_resumo, gerar_token_seguro, autenticar, verificar_autenticacao

defina mensagem como "Coral"
defina codificado como para_base64(mensagem.encode("utf-8"))
defina resumo como resumir(mensagem, "sha256")
defina token como gerar_token_seguro(16, "hex")
defina chave como "chave de exemplo"
defina etiqueta como autenticar(mensagem, chave, "sha256")
```

## Cuidados

Base64 e hexadecimal são codificações, não mecanismos de segurança.

## Relações com outros módulos

Na mesma área, veja também `coral.json`.

## Referência da API

<!-- AUTO:API -->

### Funções

#### `para_hex(dados, *, maiusculas = False) -> str`

Entrada pública `para_hex` da superfície `coral.formatos`.

**Implementação:** `coral.stdlib.formatos`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `dados` | `não declarado` | obrigatório | posicional |
| `maiusculas` | `não declarado` | `False` | nomeado |

**Retorno:** `str`

**Exceções observáveis no corpo:** `TypeError`

#### `de_hex(texto) -> bytes`

Entrada pública `de_hex` da superfície `coral.formatos`.

**Implementação:** `coral.stdlib.formatos`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `texto` | `não declarado` | obrigatório | posicional |

**Retorno:** `bytes`

**Exceções observáveis no corpo:** `ValueError`

#### `para_base64(dados, *, url = False, sem_padding = False) -> str`

Entrada pública `para_base64` da superfície `coral.formatos`.

**Implementação:** `coral.stdlib.formatos`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `dados` | `não declarado` | obrigatório | posicional |
| `url` | `não declarado` | `False` | nomeado |
| `sem_padding` | `não declarado` | `False` | nomeado |

**Retorno:** `str`

**Exceções observáveis no corpo:** `TypeError`

#### `de_base64(texto, *, url = False) -> bytes`

Entrada pública `de_base64` da superfície `coral.formatos`.

**Implementação:** `coral.stdlib.formatos`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `texto` | `não declarado` | obrigatório | posicional |
| `url` | `não declarado` | `False` | nomeado |

**Retorno:** `bytes`

**Exceções observáveis no corpo:** `ValueError`

#### `para_csv(linhas: Iterable[Mapping[str, Any] | Iterable[Any]], *, colunas = None, delimitador = ',') -> str`

Entrada pública `para_csv` da superfície `coral.formatos`.

**Implementação:** `coral.stdlib.formatos`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `linhas` | `Iterable[Mapping[str, Any] \| Iterable[Any]]` | obrigatório | posicional |
| `colunas` | `não declarado` | `None` | nomeado |
| `delimitador` | `não declarado` | `','` | nomeado |

**Retorno:** `str`

#### `de_csv(texto, *, cabecalho = True, delimitador = ',')`

Entrada pública `de_csv` da superfície `coral.formatos`.

**Implementação:** `coral.stdlib.formatos`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `texto` | `não declarado` | obrigatório | posicional |
| `cabecalho` | `não declarado` | `True` | nomeado |
| `delimitador` | `não declarado` | `','` | nomeado |

**Retorno:** `não declarado`

<!-- /AUTO:API -->
