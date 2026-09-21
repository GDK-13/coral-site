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

A documentação desta página descreve a superfície detectada na **Coral 1.5.9**. O gerador do site atualiza automaticamente o inventário e a referência da API quando uma nova release é importada, mas o texto pedagógico desta seção permanece sob revisão humana.

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
