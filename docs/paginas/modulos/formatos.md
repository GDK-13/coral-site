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

## Papel no ecossistema

Agrupa codificações e formatos de intercâmbio pequenos: hexadecimal, Base64 e CSV. O módulo transforma representação; ele não adiciona segurança ao conteúdo.

## Conceitos principais

### Hexadecimal

`para_hex` e `de_hex` convertem entre bytes e representação hexadecimal.

### Base64

`para_base64` e `de_base64` suportam variante normal ou URL e opções de padding na codificação.

### CSV

`para_csv` serializa linhas tabulares e `de_csv` reconstrói dados, com cabeçalho e delimitador configuráveis.

## Quando usar

Use este módulo quando o problema corresponder diretamente aos conceitos acima. Por ser um módulo complementar, ele normalmente entra em um programa para resolver uma responsabilidade específica e deve permanecer desacoplado da lógica central sempre que possível.

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

## API essencial

| Entrada | Papel |
|---|---|
| `para_hex` / `de_hex` | hexadecimal |
| `para_base64` / `de_base64` | Base64 |
| `para_csv` | gerar CSV |
| `de_csv` | ler CSV |

A seção **Referência da API** no fim desta página contém a superfície pública completa detectada na release, com assinaturas, parâmetros, retornos e docstrings quando presentes.

## Fluxos comuns

1. Escolha o formato de acordo com o consumidor externo.
2. Converta bytes para hex ou Base64 quando precisar de uma forma textual.
3. Para dados tabulares, defina deliberadamente cabeçalho e delimitador.
4. Para objetos estruturados hierárquicos, considere `coral.json` em vez de CSV.

## Erros e casos de borda

Base64 e hexadecimal são codificações reversíveis, não criptografia. CSV pode ser ambíguo se o produtor e o consumidor não concordarem sobre delimitador e cabeçalho.

## Boas práticas

* Documente variante Base64 e política de padding em protocolos.
* Defina colunas explicitamente quando a ordem importa.
* Não use Base64 para “proteger” segredos.

## Integração com outros módulos

`coral.criptografia` produz bytes, hashes e tokens seguros; `coral.arquivos` lê e escreve conteúdo; `coral.json` cobre estruturas hierárquicas.

## Testabilidade e previsibilidade

Teste round trips: valor → formato → valor. Para CSV, inclua células com delimitador, aspas e quebras quando esse caso fizer parte do uso.

## Compatibilidade e evolução

A documentação desta página descreve a superfície detectada na **Coral 1.5.12**. O gerador do site atualiza automaticamente o inventário e a referência da API quando uma nova release é importada, mas o texto pedagógico desta seção permanece sob revisão humana.

## Referência da API

<!-- AUTO:API -->

### Funções

#### `para_hex`

Converte o valor para hex.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `dados` | Dados processados pela operação. | `não declarado` | obrigatório |
| `maiusculas` | Valor correspondente a maiusculas. | `não declarado` | `False` |

**Retorno**

Retorna um valor declarado como `str`.

:::details Detalhes técnicos

**Assinatura:** `para_hex(dados, *, maiusculas = False) -> str`

**Origem da implementação:** `coral.stdlib.formatos`

**Arquivo na release:** `coral/stdlib/formatos.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `dados` | posicional |
| `maiusculas` | nomeado |

**Exceções diretamente observáveis no corpo:** `TypeError`

:::

#### `de_hex`

Interpreta ou reconstrói um valor a partir de hex.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `texto` | Texto processado pela operação. | `não declarado` | obrigatório |

**Retorno**

Retorna um valor declarado como `bytes`.

:::details Detalhes técnicos

**Assinatura:** `de_hex(texto) -> bytes`

**Origem da implementação:** `coral.stdlib.formatos`

**Arquivo na release:** `coral/stdlib/formatos.py`

**Exceções diretamente observáveis no corpo:** `ValueError`

:::

#### `para_base64`

Converte o valor para base64.

**Exemplo**

```coral
defina mensagem como "Coral"
defina codificado como para_base64(mensagem.encode("utf-8"))
defina resumo como resumir(mensagem, "sha256")
defina token como gerar_token_seguro(16, "hex")
defina chave como "chave de exemplo"
```

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `dados` | Dados processados pela operação. | `não declarado` | obrigatório |
| `url` | Valor correspondente a url. | `não declarado` | `False` |
| `sem_padding` | Valor correspondente a sem padding. | `não declarado` | `False` |

**Retorno**

Retorna um valor declarado como `str`.

:::details Detalhes técnicos

**Assinatura:** `para_base64(dados, *, url = False, sem_padding = False) -> str`

**Origem da implementação:** `coral.stdlib.formatos`

**Arquivo na release:** `coral/stdlib/formatos.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `dados` | posicional |
| `url` | nomeado |
| `sem_padding` | nomeado |

**Exceções diretamente observáveis no corpo:** `TypeError`

:::

#### `de_base64`

Interpreta ou reconstrói um valor a partir de base64.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `texto` | Texto processado pela operação. | `não declarado` | obrigatório |
| `url` | Valor correspondente a url. | `não declarado` | `False` |

**Retorno**

Retorna um valor declarado como `bytes`.

:::details Detalhes técnicos

**Assinatura:** `de_base64(texto, *, url = False) -> bytes`

**Origem da implementação:** `coral.stdlib.formatos`

**Arquivo na release:** `coral/stdlib/formatos.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `texto` | posicional |
| `url` | nomeado |

**Exceções diretamente observáveis no corpo:** `ValueError`

:::

#### `para_csv`

Gerar CSV.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `linhas` | Linhas usadas para construir ou processar a estrutura. | `Iterable[Mapping[str, Any] \| Iterable[Any]]` | obrigatório |
| `colunas` | Valor correspondente a colunas. | `não declarado` | `None` |
| `delimitador` | Valor correspondente a delimitador. | `não declarado` | `','` |

**Retorno**

Retorna um valor declarado como `str`.

:::details Detalhes técnicos

**Assinatura:** `para_csv(linhas: Iterable[Mapping[str, Any] \| Iterable[Any]], *, colunas = None, delimitador = ',') -> str`

**Origem da implementação:** `coral.stdlib.formatos`

**Arquivo na release:** `coral/stdlib/formatos.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `linhas` | posicional |
| `colunas` | nomeado |
| `delimitador` | nomeado |

:::

#### `de_csv`

Ler CSV.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `texto` | Texto processado pela operação. | `não declarado` | obrigatório |
| `cabecalho` | Valor correspondente a cabecalho. | `não declarado` | `True` |
| `delimitador` | Valor correspondente a delimitador. | `não declarado` | `','` |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `de_csv(texto, *, cabecalho = True, delimitador = ',')`

**Origem da implementação:** `coral.stdlib.formatos`

**Arquivo na release:** `coral/stdlib/formatos.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `texto` | posicional |
| `cabecalho` | nomeado |
| `delimitador` | nomeado |

:::

<!-- /AUTO:API -->
