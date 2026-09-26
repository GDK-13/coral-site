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

## Papel no ecossistema

Fornece uma fundação introdutória para hash, HMAC, comparação em tempo apropriado e aleatoriedade segura usando primitivas da biblioteca padrão. Ela ensina conceitos separados em vez de vender uma função genérica chamada “criptografar”.

## Conceitos principais

### Resumo criptográfico

`resumir` produz hash em algoritmo e formato escolhidos; `verificar_resumo` compara um resumo esperado.

### Autenticação com chave

`autenticar` e `verificar_autenticacao` implementam HMAC para autenticar dados com uma chave compartilhada.

### Aleatoriedade segura

`gerar_bytes_seguros` e `gerar_token_seguro` usam uma fonte apropriada para segredos, diferente de `coral.aleatorio`.

### Comparação segura

`comparar_com_seguranca` evita uma comparação ingênua quando o valor comparado é sensível.

### Descoberta

`listar_algoritmos` e `explicar_algoritmo` ajudam a conhecer o que a release expõe sem depender de nomes memorizados.

## Quando usar

Use este módulo quando o problema corresponder diretamente aos conceitos acima. Por ser um módulo complementar, ele normalmente entra em um programa para resolver uma responsabilidade específica e deve permanecer desacoplado da lógica central sempre que possível.

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

## API essencial

| Entrada | Papel |
|---|---|
| `resumir` | hash de dados |
| `verificar_resumo` | verificar hash |
| `autenticar` | HMAC |
| `verificar_autenticacao` | verificar HMAC |
| `gerar_bytes_seguros` | entropia em bytes |
| `gerar_token_seguro` | token textual seguro |
| `comparar_com_seguranca` | comparação sensível |

A seção **Referência da API** no fim desta página contém a superfície pública completa detectada na release, com assinaturas, parâmetros, retornos e docstrings quando presentes.

## Fluxos comuns

1. Escolha primeiro se o problema é integridade, autenticação ou geração de segredo.
2. Para integridade sem chave, use resumo; para autenticação com segredo compartilhado, use HMAC.
3. Use tokens seguros para identificadores secretos e nunca uma fonte pseudoaleatória comum.
4. Armazene algoritmo e formato junto do valor quando a verificação ocorrer em outro momento.

## Erros e casos de borda

Hash não cifra dados e Base64 não protege conteúdo. HMAC também não fornece confidencialidade. A própria release adverte que primitivas isoladas não formam automaticamente um protocolo seguro.

## Boas práticas

* Prefira algoritmos atuais expostos e documentados pela release.
* Nunca invente protocolo criptográfico combinando primitivas sem uma especificação externa confiável.
* Não reutilize `coral.aleatorio` para senhas, tokens ou chaves.

## Integração com outros módulos

`coral.formatos` pode codificar bytes, mas codificação não é segurança. `coral.persistencia` pode armazenar dados derivados, porém segredos exigem uma política própria de armazenamento.

## Testabilidade e previsibilidade

Vetores conhecidos e comparações de verificação são mais úteis que testes baseados em “parece aleatório”. Para tokens, teste formato e tamanho, não igualdade entre execuções.

## Compatibilidade e evolução

A documentação desta página descreve a superfície detectada na **Coral 1.6.0**. O gerador do site atualiza automaticamente o inventário e a referência da API quando uma nova release é importada, mas o texto pedagógico desta seção permanece sob revisão humana.

## Referência da API

<!-- AUTO:API -->

### Funções

#### `resumir`

Calcula um resumo criptográfico dos dados usando o algoritmo solicitado.

**Exemplo**

```coral
defina mensagem como "Coral"
defina codificado como para_base64(mensagem.encode("utf-8"))
defina resumo como resumir(mensagem, "sha256")
defina token como gerar_token_seguro(16, "hex")
defina chave como "chave de exemplo"
defina etiqueta como autenticar(mensagem, chave, "sha256")
```

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `dados` | Dados processados pela operação. | `não declarado` | obrigatório |
| `algoritmo` | Valor correspondente a algoritmo. | `não declarado` | `'sha256'` |
| `formato` | Formato usado para interpretar ou produzir o valor. | `não declarado` | `'hex'` |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `resumir(dados, algoritmo = 'sha256', formato = 'hex')`

**Origem da implementação:** `coral.criptografia`

**Arquivo na release:** `coral/criptografia/__init__.py`

:::

#### `verificar_resumo`

Verificar hash.

**Exemplo**

```coral
defina etiqueta como autenticar(mensagem, chave, "sha256")

garanta que verificar_resumo(mensagem, resumo)
```

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `dados` | Dados processados pela operação. | `não declarado` | obrigatório |
| `esperado` | Valor correspondente a esperado. | `não declarado` | obrigatório |
| `algoritmo` | Valor correspondente a algoritmo. | `não declarado` | `'sha256'` |
| `formato` | Formato usado para interpretar ou produzir o valor. | `não declarado` | `'hex'` |

**Retorno**

Retorna um valor declarado como `bool`.

:::details Detalhes técnicos

**Assinatura:** `verificar_resumo(dados, esperado, algoritmo = 'sha256', formato = 'hex') -> bool`

**Origem da implementação:** `coral.criptografia`

**Arquivo na release:** `coral/criptografia/__init__.py`

:::

#### `autenticar`

Calcula um código de autenticação para os dados usando uma chave.

**Exemplo**

```coral
defina token como gerar_token_seguro(16, "hex")
defina chave como "chave de exemplo"
defina etiqueta como autenticar(mensagem, chave, "sha256")

garanta que verificar_resumo(mensagem, resumo)
```

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `dados` | Dados processados pela operação. | `não declarado` | obrigatório |
| `chave` | Chave usada para localizar ou identificar um valor. | `não declarado` | obrigatório |
| `algoritmo` | Valor correspondente a algoritmo. | `não declarado` | `'sha256'` |
| `formato` | Formato usado para interpretar ou produzir o valor. | `não declarado` | `'hex'` |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `autenticar(dados, chave, algoritmo = 'sha256', formato = 'hex')`

**Origem da implementação:** `coral.criptografia`

**Arquivo na release:** `coral/criptografia/__init__.py`

**Exceções diretamente observáveis no corpo:** `ErroValor`

:::

#### `verificar_autenticacao`

Verificar HMAC.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `dados` | Dados processados pela operação. | `não declarado` | obrigatório |
| `chave` | Chave usada para localizar ou identificar um valor. | `não declarado` | obrigatório |
| `esperado` | Valor correspondente a esperado. | `não declarado` | obrigatório |
| `algoritmo` | Valor correspondente a algoritmo. | `não declarado` | `'sha256'` |
| `formato` | Formato usado para interpretar ou produzir o valor. | `não declarado` | `'hex'` |

**Retorno**

Retorna um valor declarado como `bool`.

:::details Detalhes técnicos

**Assinatura:** `verificar_autenticacao(dados, chave, esperado, algoritmo = 'sha256', formato = 'hex') -> bool`

**Origem da implementação:** `coral.criptografia`

**Arquivo na release:** `coral/criptografia/__init__.py`

**Exceções diretamente observáveis no corpo:** `ErroValor`

:::

#### `gerar_bytes_seguros`

Gera bytes aleatórios adequados a usos criptográficos.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `quantidade` | Quantidade de itens solicitada. | `não declarado` | `32` |

**Retorno**

Retorna um valor declarado como `bytes`.

:::details Detalhes técnicos

**Assinatura:** `gerar_bytes_seguros(quantidade = 32) -> bytes`

**Origem da implementação:** `coral.criptografia`

**Arquivo na release:** `coral/criptografia/__init__.py`

**Exceções diretamente observáveis no corpo:** `ErroValor`

:::

#### `gerar_token_seguro`

Gera um token textual aleatório adequado a usos criptográficos.

**Exemplo**

```coral
defina codificado como para_base64(mensagem.encode("utf-8"))
defina resumo como resumir(mensagem, "sha256")
defina token como gerar_token_seguro(16, "hex")
defina chave como "chave de exemplo"
defina etiqueta como autenticar(mensagem, chave, "sha256")
```

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `bytes_de_entropia` | Valor correspondente a bytes de entropia. | `não declarado` | `32` |
| `formato` | Formato usado para interpretar ou produzir o valor. | `não declarado` | `'url'` |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `gerar_token_seguro(bytes_de_entropia = 32, formato = 'url')`

**Origem da implementação:** `coral.criptografia`

**Arquivo na release:** `coral/criptografia/__init__.py`

**Exceções diretamente observáveis no corpo:** `ErroFormato`, `ErroValor`

:::

#### `comparar_com_seguranca`

Compara valores sensíveis usando uma comparação apropriada para material criptográfico.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `primeiro` | Valor correspondente a primeiro. | `não declarado` | obrigatório |
| `segundo` | Valor correspondente a segundo. | `não declarado` | obrigatório |

**Retorno**

Retorna um valor declarado como `bool`.

:::details Detalhes técnicos

**Assinatura:** `comparar_com_seguranca(primeiro, segundo) -> bool`

**Origem da implementação:** `coral.criptografia`

**Arquivo na release:** `coral/criptografia/__init__.py`

:::

#### `listar_algoritmos`

Lista algoritmos.

**Retorno**

Retorna um valor declarado como `list[str]`.

:::details Detalhes técnicos

**Assinatura:** `listar_algoritmos() -> list[str]`

**Origem da implementação:** `coral.criptografia`

**Arquivo na release:** `coral/criptografia/__init__.py`

:::

#### `explicar_algoritmo`

Retorna uma explicação do algoritmo criptográfico solicitado.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `não declarado` | obrigatório |

**Retorno**

Retorna um valor declarado como `dict[str, Any]`.

:::details Detalhes técnicos

**Assinatura:** `explicar_algoritmo(nome) -> dict[str, Any]`

**Origem da implementação:** `coral.criptografia`

**Arquivo na release:** `coral/criptografia/__init__.py`

**Exceções diretamente observáveis no corpo:** `ErroValor`

:::

<!-- /AUTO:API -->
