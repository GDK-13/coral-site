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

## Papel no ecossistema

É a superfície direta para JSON em memória e em arquivo. Separa serialização JSON de persistência Coral versionada, que possui outro contrato.

## Conceitos principais

### Em memória

`para_json` e `de_json` convertem entre valor compatível e texto JSON.

### Arquivo

`ler_json` e `escrever_json` combinam IO de arquivo com a serialização JSON.

### Indentação

`para_json` e `escrever_json` aceitam controle de indentação para legibilidade.

## Quando usar

Use este módulo quando o problema corresponder diretamente aos conceitos acima. Por ser um módulo complementar, ele normalmente entra em um programa para resolver uma responsabilidade específica e deve permanecer desacoplado da lógica central sempre que possível.

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

## API essencial

| Entrada | Papel |
|---|---|
| `para_json` | serializar valor |
| `de_json` | interpretar texto JSON |
| `ler_json` | ler JSON de arquivo |
| `escrever_json` | gravar JSON em arquivo |

A seção **Referência da API** no fim desta página contém a superfície pública completa detectada na release, com assinaturas, parâmetros, retornos e docstrings quando presentes.

## Fluxos comuns

1. Use `para_json`/`de_json` quando o texto já está em memória.
2. Use as funções de arquivo quando JSON é diretamente o formato externo desejado.
3. Use `coral.persistencia` quando o objetivo é salvar objetos segundo o contrato portátil e versionado da Coral.

## Erros e casos de borda

Nem todo objeto Coral é automaticamente representável em JSON. JSON também não preserva todos os tipos ricos da linguagem sem uma convenção adicional.

## Boas práticas

* Use JSON para interoperabilidade com outros sistemas.
* Não dependa da formatação textual exata quando o consumidor só precisa dos dados.
* Mantenha a fronteira entre JSON externo e modelo interno explícita.

## Integração com outros módulos

`coral.arquivos` fornece IO genérico; `coral.caminhos` ajuda a construir o caminho; `coral.persistencia` é a alternativa quando portabilidade Coral e versionamento são requisitos.

## Testabilidade e previsibilidade

Round trip é o teste principal: serializar e desserializar deve preservar os valores compatíveis esperados. Teste também JSON inválido quando a entrada vem de fora.

## Compatibilidade e evolução

A documentação desta página descreve a superfície detectada na **Coral 1.6.0**. O gerador do site atualiza automaticamente o inventário e a referência da API quando uma nova release é importada, mas o texto pedagógico desta seção permanece sob revisão humana.

## Referência da API

<!-- AUTO:API -->

### Funções

#### `para_json`

Serializar valor.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valor` | Valor processado pela operação. | `não declarado` | obrigatório |
| `identar` | Valor correspondente a identar. | `não declarado` | `2` |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `para_json(valor, identar = 2)`

**Origem da implementação:** `coral.stdlib.json`

**Arquivo na release:** `coral/stdlib/json.py`

:::

#### `de_json`

Interpretar texto JSON.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `texto` | Texto processado pela operação. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `de_json(texto)`

**Origem da implementação:** `coral.stdlib.json`

**Arquivo na release:** `coral/stdlib/json.py`

**Exceções diretamente observáveis no corpo:** `_json.JSONDecodeError`

:::

#### `ler_json`

Ler JSON de arquivo.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `caminho` | Caminho do arquivo ou diretório usado pela operação. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `ler_json(caminho)`

**Origem da implementação:** `coral.stdlib.json`

**Arquivo na release:** `coral/stdlib/json.py`

:::

#### `escrever_json`

Gravar JSON em arquivo.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `caminho` | Caminho do arquivo ou diretório usado pela operação. | `não declarado` | obrigatório |
| `valor` | Valor processado pela operação. | `não declarado` | obrigatório |
| `identar` | Valor correspondente a identar. | `não declarado` | `2` |

**Retorno**

Não produz um valor de retorno útil; o efeito ocorre no estado ou recurso alvo.

:::details Detalhes técnicos

**Assinatura:** `escrever_json(caminho, valor, identar = 2)`

**Origem da implementação:** `coral.stdlib.json`

**Arquivo na release:** `coral/stdlib/json.py`

:::

<!-- /AUTO:API -->
