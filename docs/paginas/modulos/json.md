# coral.json

## Visão geral

`coral.json` oferece ler e escrever JSON. Use para serializar dados estruturados em JSON e carregar arquivos ou textos JSON de volta para valores Coral.

<!-- AUTO:MODULO -->

**Importação:** `coral.json`  
**Categoria:** formatos  

ler e escrever JSON

### Superfície pública detectada

`para_json`, `de_json`, `ler_json`, `escrever_json`

<!-- /AUTO:MODULO -->

## Quando usar

Use para serializar dados estruturados em JSON e carregar arquivos ou textos JSON de volta para valores Coral.

Entre as entradas públicas detectadas estão `para_json`, `de_json`, `ler_json`, `escrever_json`.

## Começando

A release inclui um exemplo real em `Exemplos/Dados/02_arquivos_json_e_caminhos.coral`:

```coral
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

JSON é ótimo para interoperabilidade, mas não preserva automaticamente qualquer tipo específico da aplicação.

## Relações com outros módulos

Na mesma área, veja também `coral.formatos`.

## Referência da API

<!-- AUTO:API -->

### Funções

#### `para_json(valor, identar = 2)`

Entrada pública `para_json` da superfície `coral.json`.

**Implementação:** `coral.stdlib.json`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `valor` | `não declarado` | obrigatório | posicional |
| `identar` | `não declarado` | `2` | posicional |

**Retorno:** `não declarado`

#### `de_json(texto)`

Entrada pública `de_json` da superfície `coral.json`.

**Implementação:** `coral.stdlib.json`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `texto` | `não declarado` | obrigatório | posicional |

**Retorno:** `não declarado`

**Exceções observáveis no corpo:** `_json.JSONDecodeError`

#### `ler_json(caminho)`

Entrada pública `ler_json` da superfície `coral.json`.

**Implementação:** `coral.stdlib.json`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `caminho` | `não declarado` | obrigatório | posicional |

**Retorno:** `não declarado`

#### `escrever_json(caminho, valor, identar = 2)`

Entrada pública `escrever_json` da superfície `coral.json`.

**Implementação:** `coral.stdlib.json`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `caminho` | `não declarado` | obrigatório | posicional |
| `valor` | `não declarado` | obrigatório | posicional |
| `identar` | `não declarado` | `2` | posicional |

**Retorno:** `não declarado`

<!-- /AUTO:API -->
