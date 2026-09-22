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

## Papel no ecossistema

É a camada de operações locais de sistema de arquivos. Ela concentra leitura, escrita, organização, metadados e recursos temporários para que o restante do programa não precise misturar lógica de domínio com detalhes de IO.

## Conceitos principais

### Texto e bytes

Use as famílias `ler_texto`/`escrever_texto` para dados textuais com codificação explícita e `ler_bytes`/`escrever_bytes` para conteúdo binário.

### Navegação e inspeção

`listar`, `listar_recursivo`, `existe`, `tamanho` e `metadados` cobrem descoberta e inspeção sem alterar o sistema de arquivos.

### Operações destrutivas

`remover`, `renomear`, `copiar` e `mover` alteram o estado local. Operações recursivas exigem intenção explícita.

### Arquivos temporários

`arquivo_temporario` e `pasta_temporaria` evitam nomes improvisados em testes, conversões e etapas intermediárias.

## Quando usar

Use este módulo quando o problema corresponder diretamente aos conceitos acima. Por ser um módulo complementar, ele normalmente entra em um programa para resolver uma responsabilidade específica e deve permanecer desacoplado da lógica central sempre que possível.

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

## API essencial

| Entrada | Papel |
|---|---|
| `ler_texto` / `escrever_texto` | IO textual |
| `ler_bytes` / `escrever_bytes` | IO binário |
| `listar` / `listar_recursivo` | descoberta de conteúdo |
| `copiar` / `mover` / `renomear` | organização |
| `remover` | remoção explícita |
| `metadados` / `tamanho` | inspeção |
| `arquivo_temporario` / `pasta_temporaria` | recursos temporários |

A seção **Referência da API** no fim desta página contém a superfície pública completa detectada na release, com assinaturas, parâmetros, retornos e docstrings quando presentes.

## Fluxos comuns

1. Normalize ou componha o caminho com `coral.caminhos` quando ele vier de múltiplas partes.
2. Escolha a operação de leitura adequada a texto ou bytes.
3. Valide existência e destino antes de uma mutação destrutiva quando isso fizer parte da regra do programa.
4. Converta o conteúdo com `coral.json`, `coral.formatos` ou outro módulo de dados somente depois de concluir o IO.

## Erros e casos de borda

Falhas de permissão, caminhos inexistentes, destinos ocupados e codificação inválida pertencem ao domínio de IO. O módulo não transforma toda falha do sistema em sucesso silencioso.

## Boas práticas

* Prefira `utf-8` para novos arquivos textuais.
* Não monte caminhos concatenando barras manualmente.
* Evite `remover(..., recursivo=True)` sem uma verificação anterior do alvo.
* Use temporários em testes em vez de escrever na árvore do projeto.

## Integração com outros módulos

`coral.caminhos` normaliza caminhos; `coral.json` e `coral.formatos` cuidam de representação; `coral.persistencia` deve ser preferido quando o objetivo é persistir objetos Coral segundo um contrato versionado.

## Testabilidade e previsibilidade

Testes devem trabalhar em pasta temporária e conferir efeitos observáveis: arquivo criado, conteúdo, tamanho, listagem e remoção. Isso evita depender do diretório pessoal da máquina.

## Compatibilidade e evolução

A documentação desta página descreve a superfície detectada na **Coral 1.5.12**. O gerador do site atualiza automaticamente o inventário e a referência da API quando uma nova release é importada, mas o texto pedagógico desta seção permanece sob revisão humana.

## Referência da API

<!-- AUTO:API -->

### Funções

#### `ler_texto`

Lê o conteúdo textual de um arquivo.

**Exemplo**

```coral
execute escrever_texto("mensagem.txt", "Olá, arquivo!")
defina conteudo como ler_texto("mensagem.txt")
mostre conteudo
```

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `caminho` | Caminho do arquivo ou diretório usado pela operação. | `não declarado` | obrigatório |
| `codificacao` | Codificação de texto usada na leitura ou escrita. | `não declarado` | `'utf-8'` |

**Retorno**

Retorna o texto lido.

:::details Detalhes técnicos

**Assinatura:** `ler_texto(caminho, codificacao = 'utf-8')`

**Origem da implementação:** `coral.stdlib.arquivos`

**Arquivo na release:** `coral/stdlib/arquivos.py`

:::

#### `escrever_texto`

Escreve texto em um arquivo, substituindo o conteúdo anterior.

**Exemplo**

```coral
mostre caminho_texto

execute escrever_texto("mensagem.txt", "Olá, arquivo!")
defina conteudo como ler_texto("mensagem.txt")
mostre conteudo
```

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `caminho` | Caminho do arquivo ou diretório usado pela operação. | `não declarado` | obrigatório |
| `texto` | Texto processado pela operação. | `não declarado` | obrigatório |
| `codificacao` | Codificação de texto usada na leitura ou escrita. | `não declarado` | `'utf-8'` |

**Retorno**

Não produz um valor de retorno útil; o efeito ocorre no estado ou recurso alvo.

:::details Detalhes técnicos

**Assinatura:** `escrever_texto(caminho, texto, codificacao = 'utf-8')`

**Origem da implementação:** `coral.stdlib.arquivos`

**Arquivo na release:** `coral/stdlib/arquivos.py`

:::

#### `adicionar_texto`

Acrescenta texto ao final de um arquivo.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `caminho` | Caminho do arquivo ou diretório usado pela operação. | `não declarado` | obrigatório |
| `texto` | Texto processado pela operação. | `não declarado` | obrigatório |
| `codificacao` | Codificação de texto usada na leitura ou escrita. | `não declarado` | `'utf-8'` |

**Retorno**

Não produz um valor de retorno útil; o efeito ocorre no estado ou recurso alvo.

:::details Detalhes técnicos

**Assinatura:** `adicionar_texto(caminho, texto, codificacao = 'utf-8')`

**Origem da implementação:** `coral.stdlib.arquivos`

**Arquivo na release:** `coral/stdlib/arquivos.py`

:::

#### `ler_bytes`

Lê o conteúdo binário de um arquivo.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `caminho` | Caminho do arquivo ou diretório usado pela operação. | `não declarado` | obrigatório |

**Retorno**

Retorna os bytes lidos.

:::details Detalhes técnicos

**Assinatura:** `ler_bytes(caminho) -> bytes`

**Origem da implementação:** `coral.stdlib.arquivos`

**Arquivo na release:** `coral/stdlib/arquivos.py`

:::

#### `escrever_bytes`

Escreve dados binários em um arquivo.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `caminho` | Caminho do arquivo ou diretório usado pela operação. | `não declarado` | obrigatório |
| `dados` | Dados processados pela operação. | `não declarado` | obrigatório |

**Retorno**

Não produz um valor de retorno útil; o efeito ocorre no estado ou recurso alvo.

:::details Detalhes técnicos

**Assinatura:** `escrever_bytes(caminho, dados) -> None`

**Origem da implementação:** `coral.stdlib.arquivos`

**Arquivo na release:** `coral/stdlib/arquivos.py`

**Exceções diretamente observáveis no corpo:** `TypeError`

:::

#### `existe`

Verifica se o caminho indicado existe.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `caminho` | Caminho do arquivo ou diretório usado pela operação. | `não declarado` | obrigatório |

**Retorno**

Retorna um valor lógico que indica o resultado da verificação.

:::details Detalhes técnicos

**Assinatura:** `existe(caminho)`

**Origem da implementação:** `coral.stdlib.arquivos`

**Arquivo na release:** `coral/stdlib/arquivos.py`

:::

#### `listar`

Lista os itens do diretório indicado.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `caminho` | Caminho do arquivo ou diretório usado pela operação. | `não declarado` | `'.'` |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `listar(caminho = '.')`

**Origem da implementação:** `coral.stdlib.arquivos`

**Arquivo na release:** `coral/stdlib/arquivos.py`

:::

#### `listar_recursivo`

Lista o conteúdo de um diretório incluindo subdiretórios.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `caminho` | Caminho do arquivo ou diretório usado pela operação. | `não declarado` | `'.'` |
| `profundidade` | Valor correspondente a profundidade. | `int \| None` | `None` |
| `incluir_pastas` | Controla se deve incluir pastas. | `bool` | `False` |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `listar_recursivo(caminho = '.', *, profundidade: int \| None = None, incluir_pastas: bool = False)`

**Origem da implementação:** `coral.stdlib.arquivos`

**Arquivo na release:** `coral/stdlib/arquivos.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `caminho` | posicional |
| `profundidade` | nomeado |
| `incluir_pastas` | nomeado |

**Exceções diretamente observáveis no corpo:** `ValueError`, `_erro_arquivo_em_portugues`

:::

#### `criar_pasta`

Cria pasta.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `caminho` | Caminho do arquivo ou diretório usado pela operação. | `não declarado` | obrigatório |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `criar_pasta(caminho)`

**Origem da implementação:** `coral.stdlib.arquivos`

**Arquivo na release:** `coral/stdlib/arquivos.py`

:::

#### `remover`

Remove o valor solicitado.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `caminho` | Caminho do arquivo ou diretório usado pela operação. | `não declarado` | obrigatório |
| `recursivo` | Valor correspondente a recursivo. | `bool` | `False` |

**Retorno**

Não produz um valor de retorno útil; o efeito ocorre no estado ou recurso alvo.

:::details Detalhes técnicos

**Assinatura:** `remover(caminho, *, recursivo: bool = False) -> None`

**Origem da implementação:** `coral.stdlib.arquivos`

**Arquivo na release:** `coral/stdlib/arquivos.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `caminho` | posicional |
| `recursivo` | nomeado |

:::

#### `renomear`

Renomeia o valor solicitado.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `caminho` | Caminho do arquivo ou diretório usado pela operação. | `não declarado` | obrigatório |
| `destino` | Destino que receberá o resultado da operação. | `não declarado` | obrigatório |

**Retorno**

Retorna um valor declarado como `Path`.

:::details Detalhes técnicos

**Assinatura:** `renomear(caminho, destino) -> Path`

**Origem da implementação:** `coral.stdlib.arquivos`

**Arquivo na release:** `coral/stdlib/arquivos.py`

:::

#### `copiar`

Copia o valor solicitado.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `caminho` | Caminho do arquivo ou diretório usado pela operação. | `não declarado` | obrigatório |
| `destino` | Destino que receberá o resultado da operação. | `não declarado` | obrigatório |
| `recursivo` | Valor correspondente a recursivo. | `bool` | `False` |

**Retorno**

Retorna um valor declarado como `Path`.

:::details Detalhes técnicos

**Assinatura:** `copiar(caminho, destino, *, recursivo: bool = False) -> Path`

**Origem da implementação:** `coral.stdlib.arquivos`

**Arquivo na release:** `coral/stdlib/arquivos.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `caminho` | posicional |
| `destino` | posicional |
| `recursivo` | nomeado |

**Exceções diretamente observáveis no corpo:** `IsADirectoryError`

:::

#### `mover`

Move o valor solicitado.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `caminho` | Caminho do arquivo ou diretório usado pela operação. | `não declarado` | obrigatório |
| `destino` | Destino que receberá o resultado da operação. | `não declarado` | obrigatório |

**Retorno**

Retorna um valor declarado como `Path`.

:::details Detalhes técnicos

**Assinatura:** `mover(caminho, destino) -> Path`

**Origem da implementação:** `coral.stdlib.arquivos`

**Arquivo na release:** `coral/stdlib/arquivos.py`

:::

#### `tamanho`

Obtém o tamanho do recurso indicado.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `caminho` | Caminho do arquivo ou diretório usado pela operação. | `não declarado` | obrigatório |

**Retorno**

Retorna um valor declarado como `int`.

:::details Detalhes técnicos

**Assinatura:** `tamanho(caminho) -> int`

**Origem da implementação:** `coral.stdlib.arquivos`

**Arquivo na release:** `coral/stdlib/arquivos.py`

:::

#### `metadados`

Obtém metadados do arquivo ou diretório indicado.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `caminho` | Caminho do arquivo ou diretório usado pela operação. | `não declarado` | obrigatório |

**Retorno**

Retorna um valor declarado como `dict[str, Any]`.

:::details Detalhes técnicos

**Assinatura:** `metadados(caminho) -> dict[str, Any]`

**Origem da implementação:** `coral.stdlib.arquivos`

**Arquivo na release:** `coral/stdlib/arquivos.py`

:::

#### `arquivo_temporario`

Cria um arquivo temporário e retorna seu caminho.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `prefixo` | Valor correspondente a prefixo. | `não declarado` | `'coral_'` |
| `sufixo` | Valor correspondente a sufixo. | `não declarado` | `''` |
| `pasta` | Valor correspondente a pasta. | `não declarado` | `None` |

**Retorno**

Retorna um valor declarado como `Path`.

:::details Detalhes técnicos

**Assinatura:** `arquivo_temporario(*, prefixo = 'coral_', sufixo = '', pasta = None) -> Path`

**Origem da implementação:** `coral.stdlib.arquivos`

**Arquivo na release:** `coral/stdlib/arquivos.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `prefixo` | nomeado |
| `sufixo` | nomeado |
| `pasta` | nomeado |

:::

#### `pasta_temporaria`

Cria uma pasta temporária e retorna seu caminho.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `prefixo` | Valor correspondente a prefixo. | `não declarado` | `'coral_'` |
| `pasta` | Valor correspondente a pasta. | `não declarado` | `None` |

**Retorno**

Retorna um valor declarado como `Path`.

:::details Detalhes técnicos

**Assinatura:** `pasta_temporaria(*, prefixo = 'coral_', pasta = None) -> Path`

**Origem da implementação:** `coral.stdlib.arquivos`

**Arquivo na release:** `coral/stdlib/arquivos.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `prefixo` | nomeado |
| `pasta` | nomeado |

:::

#### `nome`

Obtém o nome final do caminho.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `caminho` | Caminho do arquivo ou diretório usado pela operação. | `não declarado` | obrigatório |

**Retorno**

Retorna um valor declarado como `str`.

:::details Detalhes técnicos

**Assinatura:** `nome(caminho) -> str`

**Origem da implementação:** `coral.stdlib.arquivos`

**Arquivo na release:** `coral/stdlib/arquivos.py`

:::

#### `extensao`

Obtém a extensão do caminho.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `caminho` | Caminho do arquivo ou diretório usado pela operação. | `não declarado` | obrigatório |

**Retorno**

Retorna um valor declarado como `str`.

:::details Detalhes técnicos

**Assinatura:** `extensao(caminho) -> str`

**Origem da implementação:** `coral.stdlib.arquivos`

**Arquivo na release:** `coral/stdlib/arquivos.py`

:::

#### `pai`

Obtém pai.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `caminho` | Caminho do arquivo ou diretório usado pela operação. | `não declarado` | obrigatório |

**Retorno**

Retorna um valor declarado como `Path`.

:::details Detalhes técnicos

**Assinatura:** `pai(caminho) -> Path`

**Origem da implementação:** `coral.stdlib.arquivos`

**Arquivo na release:** `coral/stdlib/arquivos.py`

:::

#### `resolver`

Resolve o valor solicitado.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `caminho` | Caminho do arquivo ou diretório usado pela operação. | `não declarado` | obrigatório |
| `estrito` | Valor correspondente a estrito. | `bool` | `False` |

**Retorno**

Retorna um valor declarado como `Path`.

:::details Detalhes técnicos

**Assinatura:** `resolver(caminho, *, estrito: bool = False) -> Path`

**Origem da implementação:** `coral.stdlib.arquivos`

**Arquivo na release:** `coral/stdlib/arquivos.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `caminho` | posicional |
| `estrito` | nomeado |

:::

<!-- /AUTO:API -->
