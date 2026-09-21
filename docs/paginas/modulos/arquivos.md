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

A documentação desta página descreve a superfície detectada na **Coral 1.5.9**. O gerador do site atualiza automaticamente o inventário e a referência da API quando uma nova release é importada, mas o texto pedagógico desta seção permanece sob revisão humana.

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
