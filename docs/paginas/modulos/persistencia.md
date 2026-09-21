# coral.persistencia

## Visão geral

`coral.persistencia` oferece persistência portátil, versionada e canônica. Use quando os dados precisam ser salvos de forma portátil, versionada e canônica.

<!-- AUTO:MODULO -->

**Importação:** `coral.persistencia`  
**Categoria:** dados  

persistência portátil, versionada e canônica

### Superfície pública detectada

`CONTRATO`, `VERSAO_ESQUEMA`, `ErroPersistencia`, `registrar_adaptador`, `registrar_extensao_persistente`, `extensoes_para_dados`, `aplicar_extensoes_persistentes`, `valor_portatil`, `para_dados`, `de_dados`, `texto_canonico`, `serializar_canonico`, `salvar`, `carregar`, `carregar_como`

<!-- /AUTO:MODULO -->

## Quando usar

Use quando os dados precisam ser salvos de forma portátil, versionada e canônica.

Entre as entradas públicas detectadas estão `salvar`, `carregar`, `valor_portatil`, `para_dados`, `de_dados`, `texto_canonico`.

## Começando

A release inclui um exemplo real em `Exemplos/Dados/03_aleatorio_e_persistencia.coral`:

```coral
de coral.aleatorio importe fonte
de coral.persistencia importe salvar, carregar

defina gerador_a como fonte(42)
defina gerador_b como fonte(42)
defina primeiro como gerador_a.inteiro(1, 100)
defina segundo como gerador_b.inteiro(1, 100)
garanta que primeiro for igual a segundo

defina dados como {"ponto": (3, 4), "tags": {"a", "b"}}
execute salvar(dados, "exemplo.coraldata")
```

## Cuidados

Versione o formato persistido quando ele fizer parte de um projeto que continuará evoluindo.

## Relações com outros módulos

Na mesma área, veja também `coral.colecoes`.

## Referência da API

<!-- AUTO:API -->

### Funções

#### `registrar_adaptador(tipo_python: type, identificador: str, para_dados: Callable[[Any], dict[str, Any]], de_dados: Callable[[dict[str, Any]], Any]) -> None`

Entrada pública `registrar_adaptador` da superfície `coral.persistencia`.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `tipo_python` | `type` | obrigatório | posicional |
| `identificador` | `str` | obrigatório | posicional |
| `para_dados` | `Callable[[Any], dict[str, Any]]` | obrigatório | posicional |
| `de_dados` | `Callable[[dict[str, Any]], Any]` | obrigatório | posicional |

**Retorno:** `None`

**Exceções observáveis no corpo:** `ValueError`

#### `registrar_extensao_persistente(tipo_python: type, identificador: str, para_dados: Callable[[Any], Any], aplicar_dados: Callable[[Any, Any], None]) -> None`

Registra uma extensão de domínio sem acoplar o tipo hospedeiro ao módulo dono.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `tipo_python` | `type` | obrigatório | posicional |
| `identificador` | `str` | obrigatório | posicional |
| `para_dados` | `Callable[[Any], Any]` | obrigatório | posicional |
| `aplicar_dados` | `Callable[[Any, Any], None]` | obrigatório | posicional |

**Retorno:** `None`

**Exceções observáveis no corpo:** `ValueError`

#### `extensoes_para_dados(objeto: Any) -> dict[str, Any]`

Entrada pública `extensoes_para_dados` da superfície `coral.persistencia`.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `objeto` | `Any` | obrigatório | posicional |

**Retorno:** `dict[str, Any]`

#### `aplicar_extensoes_persistentes(objeto: Any, extensoes: Any) -> None`

Entrada pública `aplicar_extensoes_persistentes` da superfície `coral.persistencia`.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `objeto` | `Any` | obrigatório | posicional |
| `extensoes` | `Any` | obrigatório | posicional |

**Retorno:** `None`

**Exceções observáveis no corpo:** `ErroPersistencia`

#### `valor_portatil(valor: Any) -> Any`

Normaliza um valor isolado segundo o contrato portátil da Coral.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `valor` | `Any` | obrigatório | posicional |

**Retorno:** `Any`

#### `para_dados(objeto: Any) -> dict[str, Any]`

Entrada pública `para_dados` da superfície `coral.persistencia`.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `objeto` | `Any` | obrigatório | posicional |

**Retorno:** `dict[str, Any]`

#### `de_dados(documento: dict[str, Any]) -> Any`

Entrada pública `de_dados` da superfície `coral.persistencia`.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `documento` | `dict[str, Any]` | obrigatório | posicional |

**Retorno:** `Any`

**Exceções observáveis no corpo:** `ErroPersistencia`

#### `texto_canonico(valor: Any) -> str`

Serialização JSON canônica para hash, cache, replay e equivalência.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `valor` | `Any` | obrigatório | posicional |

**Retorno:** `str`

#### `serializar_canonico(valor: Any) -> bytes`

Versão UTF 8 explícita da serialização canônica.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `valor` | `Any` | obrigatório | posicional |

**Retorno:** `bytes`

#### `salvar(objeto: Any, caminho: str | Path) -> Path`

Entrada pública `salvar` da superfície `coral.persistencia`.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `objeto` | `Any` | obrigatório | posicional |
| `caminho` | `str \| Path` | obrigatório | posicional |

**Retorno:** `Path`

**Exceções observáveis no corpo:** `ErroPersistencia`

#### `carregar(caminho: str | Path) -> Any`

Entrada pública `carregar` da superfície `coral.persistencia`.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `caminho` | `str \| Path` | obrigatório | posicional |

**Retorno:** `Any`

**Exceções observáveis no corpo:** `ErroPersistencia`

#### `carregar_como(caminho: str | Path, tipo_esperado: type, nome_tipo: str | None = None) -> Any`

Entrada pública `carregar_como` da superfície `coral.persistencia`.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `caminho` | `str \| Path` | obrigatório | posicional |
| `tipo_esperado` | `type` | obrigatório | posicional |
| `nome_tipo` | `str \| None` | `None` | posicional |

**Retorno:** `Any`

**Exceções observáveis no corpo:** `ErroPersistencia`

### Exceções

#### `ErroPersistencia(...)`

Falha de validação, codificação ou reconstrução persistente.

### Constantes e aliases

#### `CONTRATO`

Constante pública do módulo.

**Valor declarado:** `'coral.persistencia/1'`

#### `VERSAO_ESQUEMA`

Constante pública do módulo.

**Valor declarado:** `1`

<!-- /AUTO:API -->
