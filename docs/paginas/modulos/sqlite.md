# coral.sqlite

## Visão geral

persistência local SQLite com consultas parametrizadas e transações explícitas

<!-- AUTO:MODULO -->

**Importação:** `coral.sqlite`  
**Categoria:** dados  

persistência local SQLite com consultas parametrizadas e transações explícitas

### Superfície pública detectada

`ErroSQLite`, `ErroOperacionalSQLite`, `Conexao`, `abrir`

<!-- /AUTO:MODULO -->

## Quando usar

Use `coral.sqlite` quando o programa precisar guardar dados localmente e consultá los depois sem depender de um servidor de banco de dados. É adequado para catálogos, configurações estruturadas, pequenos aplicativos locais, protótipos e ferramentas que precisam de persistência relacional em um único arquivo.

SQLite não é um formato Coral nem um ORM. O SQL continua explícito, e os valores devem ser enviados separadamente da consulta por parâmetros.

## Começo rápido

```coral
de coral.sqlite importe abrir

defina banco como abrir(":memoria:")
execute banco.executar(
    "CREATE TABLE itens (id INTEGER PRIMARY KEY, nome TEXT NOT NULL)"
)
execute banco.executar(
    "INSERT INTO itens(nome) VALUES (?)",
    ["Caderno"]
)
execute banco.confirmar()

defina itens como banco.consultar("SELECT id, nome FROM itens")
mostre itens
execute banco.fechar()
```

:::resultado
A consulta devolve uma lista de registros em forma de dicionário. O banco `:memoria:` existe somente durante a conexão.
:::

## Consultas longas com texto multilinha

A 1.7.9 permite organizar SQL extenso com textos multilinha gerais da linguagem. O conteúdo continua sendo texto comum: a Coral não interpreta nem reescreve SQL.

```coral
defina consulta como """
    SELECT id, nome
    FROM itens
    WHERE id > ?
    ORDER BY id
"""

defina itens como banco.consultar(consulta, [0])
```

Quando o conteúdo começa na linha seguinte ao delimitador, a primeira quebra é estrutural. O recuo comum do corpo é removido, e uma quebra final usada apenas para posicionar o delimitador de fechamento também não entra no valor.

## Parâmetros e segurança

Passe valores como parâmetros da consulta. Não monte valores recebidos do usuário concatenando texto SQL.

```coral
execute banco.executar(
    "INSERT INTO itens(nome, quantidade) VALUES (?, ?)",
    [nome, quantidade]
)
```

Os parâmetros representam **valores**. Eles não substituem nomes de tabelas, nomes de colunas ou fragmentos arbitrários de SQL.

## Transações

`confirmar()` conserva alterações pendentes. `reverter()` desfaz alterações ainda não confirmadas. `transacao()` oferece um contexto explícito que confirma ao sair normalmente e reverte quando o bloco falha. Transações contextuais aninhadas são recusadas em vez de criar savepoints implícitos.

## API essencial

| Entrada | Papel |
|---|---|
| `abrir` | Abre um banco em arquivo ou em memória e devolve uma conexão Coral. |
| `Conexao` | Representa a conexão e concentra execução, consulta, transação e fechamento. |
| `ErroSQLite` | Erro base da camada SQLite Coral. |
| `ErroOperacionalSQLite` | Falha operacional, como bloqueio, caminho inválido ou SQL recusado pelo SQLite. |

## Limites

A API não introduz ORM, migrações automáticas gerais, MySQL, PostgreSQL ou sincronização em nuvem. Para esses casos, escolha uma camada apropriada ao projeto em vez de tratar `coral.sqlite` como abstração universal de banco de dados.

## Referência da API

<!-- AUTO:API -->

### Funções

#### `abrir`

Abre uma conexão SQLite. ``:memoria:`` cria banco somente em memória.

**Exemplo**

```coral
de coral.sqlite importe abrir

defina banco como abrir(":memoria:")
execute banco.executar(
    "CREATE TABLE itens (id INTEGER PRIMARY KEY, nome TEXT NOT NULL)"
)
execute banco.executar(
    "INSERT INTO itens(nome) VALUES (?)",
    ["Caderno"]
)
execute banco.confirmar()

defina itens como banco.consultar("SELECT id, nome FROM itens")
mostre itens
execute banco.fechar()
```

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `caminho` | Caminho do arquivo ou diretório usado pela operação. | `str \| Path` | obrigatório |
| `timeout` | Valor correspondente a timeout. | `float` | `5.0` |

**Retorno**

Retorna um valor declarado como `Conexao`.

:::details Detalhes técnicos

**Assinatura:** `abrir(caminho: str \| Path, *, timeout: float = 5.0) -> Conexao`

**Origem da implementação:** `coral.sqlite`

**Arquivo na release:** `coral/sqlite.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `caminho` | posicional |
| `timeout` | nomeado |

:::

### Classes e protocolos

#### `Conexao`

Conexão SQLite com resultados em dicionários e transações explícitas.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `caminho` | Caminho do arquivo ou diretório usado pela operação. | `str \| Path` | obrigatório |
| `timeout` | Valor correspondente a timeout. | `float` | `5.0` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `fechada` | Executa a operação `fechada` disponibilizada por `coral.sqlite`. | `bool` |
| `em_transacao` | Executa a operação `em_transacao` disponibilizada por `coral.sqlite`. | `bool` |
| `executar` | Executa um comando e devolve linhas_afetadas e ultimo_id. | `dict[str, int \| None]` |
| `executar_muitos` | Executa muitos. | `dict[str, int \| None]` |
| `consultar` | Executa consulta e materializa as linhas em dicionários. | `list[dict[str, Any]]` |
| `consultar_um` | Executa a operação `consultar_um` disponibilizada por `coral.sqlite`. | `dict[str, Any] \| None` |
| `confirmar` | Executa a operação `confirmar` disponibilizada por `coral.sqlite`. | `None` |
| `reverter` | Executa a operação `reverter` disponibilizada por `coral.sqlite`. | `None` |
| `fechar` | Fecha o valor solicitado. | `None` |
| `transacao` | Confirma ao sair normalmente e reverte quando o bloco falha. | `Iterator['Conexao']` |

:::details Detalhes técnicos

**Assinatura:** `Conexao(caminho: str \| Path, *, timeout: float = 5.0)`

**Origem da implementação:** `coral.sqlite`

**Arquivo na release:** `coral/sqlite.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `caminho` | posicional |
| `timeout` | nomeado |

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `fechada` | propriedade | `fechada() -> bool` |
| `em_transacao` | propriedade | `em_transacao() -> bool` |
| `executar` | método | `executar(sql: str, parametros = ()) -> dict[str, int \| None]` |
| `executar_muitos` | método | `executar_muitos(sql: str, parametros) -> dict[str, int \| None]` |
| `consultar` | método | `consultar(sql: str, parametros = ()) -> list[dict[str, Any]]` |
| `consultar_um` | método | `consultar_um(sql: str, parametros = ()) -> dict[str, Any] \| None` |
| `confirmar` | método | `confirmar() -> None` |
| `reverter` | método | `reverter() -> None` |
| `fechar` | método | `fechar() -> None` |
| `transacao` | método | `transacao() -> Iterator['Conexao']` |

:::

### Exceções

#### `ErroSQLite`

Erro de uso ou execução da camada SQLite Coral.

:::details Detalhes técnicos

**Assinatura:** `ErroSQLite(...)`

**Origem da implementação:** `coral.sqlite`

**Arquivo na release:** `coral/sqlite.py`

:::

#### `ErroOperacionalSQLite`

Erro operacional do SQLite, como bloqueio, caminho ou SQL inválido.

:::details Detalhes técnicos

**Assinatura:** `ErroOperacionalSQLite(...)`

**Origem da implementação:** `coral.sqlite`

**Arquivo na release:** `coral/sqlite.py`

:::

<!-- /AUTO:API -->
