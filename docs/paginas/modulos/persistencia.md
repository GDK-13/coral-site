# coral.persistencia

## Visão geral

`coral.persistencia` oferece persistência portátil, versionada e canônica. Use quando os dados precisam ser salvos de forma portátil, versionada e canônica.

<!-- AUTO:MODULO -->

**Importação:** `coral.persistencia`  
**Categoria:** dados  

persistência portátil, versionada e canônica

### Superfície pública detectada

`CONTRATO`, `VERSAO_ESQUEMA`, `VERSOES_LEITURA`, `VERSAO_ESCRITA`, `politica_persistencia`, `ErroPersistencia`, `registrar_adaptador`, `registrar_extensao_persistente`, `extensoes_para_dados`, `aplicar_extensoes_persistentes`, `valor_portatil`, `para_dados`, `de_dados`, `texto_canonico`, `serializar_canonico`, `salvar`, `carregar`, `carregar_como`

<!-- /AUTO:MODULO -->

## Papel no ecossistema

É o contrato de persistência portátil e versionada da Coral. Em vez de serializar objetos arbitrários do runtime, grava somente dados semânticos reconstruíveis e rejeita estado que não é seguro ou portátil salvar.

## Conceitos principais

### Contrato versionado

`CONTRATO` e `VERSAO_ESQUEMA` identificam o formato persistente. Na 1.6.0, `VERSOES_LEITURA` e `VERSAO_ESCRITA` tornam explícitas as versões que o runtime aceita ler e a versão que ele grava.

### Política executável

`politica_persistencia()` apresenta a política corrente como dados consultáveis. Ela informa contrato, versões de leitura e escrita, estratégia de migração e compatibilidade declarada, evitando que ferramentas precisem duplicar essas regras em texto ou tabelas paralelas.

### Conversão para dados

`para_dados` e `de_dados` transformam entre objeto suportado e documento persistente.

### Representação portátil

`valor_portatil` normaliza valores; `texto_canonico` e `serializar_canonico` geram representação determinística útil para hash, cache e equivalência.

### Arquivo

`salvar`, `carregar` e `carregar_como` operam sobre o formato persistente.

### Extensão

Adaptadores e extensões persistentes permitem que outros domínios participem do contrato sem acoplamento rígido ao módulo central.

## Quando usar

Use este módulo quando o problema corresponder diretamente aos conceitos acima. Por ser um módulo complementar, ele normalmente entra em um programa para resolver uma responsabilidade específica e deve permanecer desacoplado da lógica central sempre que possível.

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

## API essencial

| Entrada | Papel |
|---|---|
| `VERSOES_LEITURA` / `VERSAO_ESCRITA` | declarar compatibilidade de esquema |
| `politica_persistencia` | consultar a política executável do formato |
| `valor_portatil` | normalizar valor |
| `para_dados` / `de_dados` | converter documento |
| `texto_canonico` / `serializar_canonico` | representação determinística |
| `salvar` / `carregar` | persistir arquivo |
| `carregar_como` | validar tipo esperado |
| `registrar_adaptador` | ensinar novo tipo |
| `registrar_extensao_persistente` | anexar dados de domínio |

A seção **Referência da API** no fim desta página contém a superfície pública completa detectada na release, com assinaturas, parâmetros, retornos e docstrings quando presentes.

## Fluxos comuns

1. Converta estado de domínio para dados persistíveis.
2. Use a serialização canônica quando precisar de identidade de conteúdo ou comparação determinística.
3. Salve com o contrato versionado.
4. Ao carregar, valide a estrutura e reconstrua somente tipos registrados ou suportados.

## Erros e casos de borda

Handles, recursos externos, estado de execução e objetos arbitrários são deliberadamente recusados. Persistir tudo que existe na memória não é o objetivo do módulo.

## Boas práticas

* Persista estado semântico, não detalhes efêmeros do runtime.
* Mantenha adaptadores pequenos e versionáveis.
* Use `carregar_como` quando o tipo esperado é parte do contrato do chamador.
* Não edite manualmente o documento canônico esperando estabilidade de campos internos não documentados.

## Integração com outros módulos

Módulos como `coral.mundo` podem registrar extensões de domínio; `coral.arquivos` fornece operações genéricas de IO, enquanto `coral.persistencia` define o significado do formato salvo.

## Testabilidade e previsibilidade

Teste round trip objeto → dados → objeto, compatibilidade de versão e rejeição de valores não portáteis. A saída canônica deve ser determinística para o mesmo conteúdo.

## Compatibilidade e evolução

Na **Coral 1.6.0**, a persistência continua no contrato `coral.persistencia/1` e no esquema de escrita `1`. A novidade pública é a política explícita e consultável: `VERSOES_LEITURA`, `VERSAO_ESCRITA` e `politica_persistencia()` documentam no próprio runtime o que pode ser lido, o que será escrito e como um esquema desconhecido é tratado. O gerador do site continua atualizando automaticamente o inventário e a referência da API, enquanto esta explicação pedagógica permanece sob revisão humana.

## Referência da API

<!-- AUTO:API -->

### Funções

#### `politica_persistencia`

Descreve a política executável do formato persistente corrente.

**Retorno**

Retorna um valor declarado como `dict[str, Any]`.

:::details Detalhes técnicos

**Assinatura:** `politica_persistencia() -> dict[str, Any]`

**Origem da implementação:** `coral.persistencia`

**Arquivo na release:** `coral/persistencia.py`

:::

#### `registrar_adaptador`

Ensinar novo tipo.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `tipo_python` | Valor correspondente a tipo python. | `type` | obrigatório |
| `identificador` | Valor correspondente a identificador. | `str` | obrigatório |
| `para_dados` | Valor correspondente a para dados. | `Callable[[Any], dict[str, Any]]` | obrigatório |
| `de_dados` | Valor correspondente a de dados. | `Callable[[dict[str, Any]], Any]` | obrigatório |

**Retorno**

Não produz um valor de retorno útil; o efeito ocorre no estado ou recurso alvo.

:::details Detalhes técnicos

**Assinatura:** `registrar_adaptador(tipo_python: type, identificador: str, para_dados: Callable[[Any], dict[str, Any]], de_dados: Callable[[dict[str, Any]], Any]) -> None`

**Origem da implementação:** `coral.persistencia`

**Arquivo na release:** `coral/persistencia.py`

**Exceções diretamente observáveis no corpo:** `ValueError`

:::

#### `registrar_extensao_persistente`

Registra uma extensão de domínio sem acoplar o tipo hospedeiro ao módulo dono.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `tipo_python` | Valor correspondente a tipo python. | `type` | obrigatório |
| `identificador` | Valor correspondente a identificador. | `str` | obrigatório |
| `para_dados` | Valor correspondente a para dados. | `Callable[[Any], Any]` | obrigatório |
| `aplicar_dados` | Valor correspondente a aplicar dados. | `Callable[[Any, Any], None]` | obrigatório |

**Retorno**

Não produz um valor de retorno útil; o efeito ocorre no estado ou recurso alvo.

:::details Detalhes técnicos

**Assinatura:** `registrar_extensao_persistente(tipo_python: type, identificador: str, para_dados: Callable[[Any], Any], aplicar_dados: Callable[[Any, Any], None]) -> None`

**Origem da implementação:** `coral.persistencia`

**Arquivo na release:** `coral/persistencia.py`

**Exceções diretamente observáveis no corpo:** `ValueError`

:::

#### `extensoes_para_dados`

Converte extensões persistentes registradas para dados portáteis.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `objeto` | Objeto processado pela operação. | `Any` | obrigatório |

**Retorno**

Retorna um valor declarado como `dict[str, Any]`.

:::details Detalhes técnicos

**Assinatura:** `extensoes_para_dados(objeto: Any) -> dict[str, Any]`

**Origem da implementação:** `coral.persistencia`

**Arquivo na release:** `coral/persistencia.py`

:::

#### `aplicar_extensoes_persistentes`

Aplica ao objeto as extensões persistentes presentes nos dados carregados.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `objeto` | Objeto processado pela operação. | `Any` | obrigatório |
| `extensoes` | Valor correspondente a extensoes. | `Any` | obrigatório |

**Retorno**

Não produz um valor de retorno útil; o efeito ocorre no estado ou recurso alvo.

:::details Detalhes técnicos

**Assinatura:** `aplicar_extensoes_persistentes(objeto: Any, extensoes: Any) -> None`

**Origem da implementação:** `coral.persistencia`

**Arquivo na release:** `coral/persistencia.py`

**Exceções diretamente observáveis no corpo:** `ErroPersistencia`

:::

#### `valor_portatil`

Normaliza um valor isolado segundo o contrato portátil da Coral.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valor` | Valor processado pela operação. | `Any` | obrigatório |

**Retorno**

Retorna um valor declarado como `Any`.

:::details Detalhes técnicos

**Assinatura:** `valor_portatil(valor: Any) -> Any`

**Origem da implementação:** `coral.persistencia`

**Arquivo na release:** `coral/persistencia.py`

:::

#### `para_dados`

Converter documento.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `objeto` | Objeto processado pela operação. | `Any` | obrigatório |

**Retorno**

Retorna um valor declarado como `dict[str, Any]`.

:::details Detalhes técnicos

**Assinatura:** `para_dados(objeto: Any) -> dict[str, Any]`

**Origem da implementação:** `coral.persistencia`

**Arquivo na release:** `coral/persistencia.py`

:::

#### `de_dados`

Converter documento.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `documento` | Valor correspondente a documento. | `dict[str, Any]` | obrigatório |

**Retorno**

Retorna um valor declarado como `Any`.

:::details Detalhes técnicos

**Assinatura:** `de_dados(documento: dict[str, Any]) -> Any`

**Origem da implementação:** `coral.persistencia`

**Arquivo na release:** `coral/persistencia.py`

**Exceções diretamente observáveis no corpo:** `ErroPersistencia`

:::

#### `texto_canonico`

Serialização JSON canônica para hash, cache, replay e equivalência.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valor` | Valor processado pela operação. | `Any` | obrigatório |

**Retorno**

Retorna um valor declarado como `str`.

:::details Detalhes técnicos

**Assinatura:** `texto_canonico(valor: Any) -> str`

**Origem da implementação:** `coral.persistencia`

**Arquivo na release:** `coral/persistencia.py`

:::

#### `serializar_canonico`

Versão UTF 8 explícita da serialização canônica.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valor` | Valor processado pela operação. | `Any` | obrigatório |

**Retorno**

Retorna um valor declarado como `bytes`.

:::details Detalhes técnicos

**Assinatura:** `serializar_canonico(valor: Any) -> bytes`

**Origem da implementação:** `coral.persistencia`

**Arquivo na release:** `coral/persistencia.py`

:::

#### `salvar`

Persistir arquivo.

**Exemplo**

```coral
defina dados como {"ponto": (3, 4), "tags": {"a", "b"}}
execute salvar(dados, "exemplo.coraldata")
```

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `objeto` | Objeto processado pela operação. | `Any` | obrigatório |
| `caminho` | Caminho do arquivo ou diretório usado pela operação. | `str \| Path` | obrigatório |

**Retorno**

Retorna um valor declarado como `Path`.

:::details Detalhes técnicos

**Assinatura:** `salvar(objeto: Any, caminho: str \| Path) -> Path`

**Origem da implementação:** `coral.persistencia`

**Arquivo na release:** `coral/persistencia.py`

**Exceções diretamente observáveis no corpo:** `ErroPersistencia`

:::

#### `carregar`

Persistir arquivo.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `caminho` | Caminho do arquivo ou diretório usado pela operação. | `str \| Path` | obrigatório |

**Retorno**

Retorna um valor declarado como `Any`.

:::details Detalhes técnicos

**Assinatura:** `carregar(caminho: str \| Path) -> Any`

**Origem da implementação:** `coral.persistencia`

**Arquivo na release:** `coral/persistencia.py`

**Exceções diretamente observáveis no corpo:** `ErroPersistencia`

:::

#### `carregar_como`

Validar tipo esperado.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `caminho` | Caminho do arquivo ou diretório usado pela operação. | `str \| Path` | obrigatório |
| `tipo_esperado` | Valor correspondente a tipo esperado. | `type` | obrigatório |
| `nome_tipo` | Valor correspondente a nome tipo. | `str \| None` | `None` |

**Retorno**

Retorna um valor declarado como `Any`.

:::details Detalhes técnicos

**Assinatura:** `carregar_como(caminho: str \| Path, tipo_esperado: type, nome_tipo: str \| None = None) -> Any`

**Origem da implementação:** `coral.persistencia`

**Arquivo na release:** `coral/persistencia.py`

**Exceções diretamente observáveis no corpo:** `ErroPersistencia`

:::

### Exceções

#### `ErroPersistencia`

Falha de validação, codificação ou reconstrução persistente.

:::details Detalhes técnicos

**Assinatura:** `ErroPersistencia(...)`

**Origem da implementação:** `coral.persistencia`

**Arquivo na release:** `coral/persistencia.py`

:::

### Constantes e aliases

#### `CONTRATO`

Expõe a constante pública `CONTRATO`.

:::details Detalhes técnicos

**Assinatura:** `CONTRATO`

**Origem da implementação:** `coral.persistencia`

**Arquivo na release:** `coral/persistencia.py`

**Valor declarado:** `'coral.persistencia/1'`

:::

#### `VERSAO_ESQUEMA`

Expõe a constante pública `VERSAO_ESQUEMA`.

:::details Detalhes técnicos

**Assinatura:** `VERSAO_ESQUEMA`

**Origem da implementação:** `coral.persistencia`

**Arquivo na release:** `coral/persistencia.py`

**Valor declarado:** `1`

:::

#### `VERSOES_LEITURA`

Expõe a constante pública `VERSOES_LEITURA`.

:::details Detalhes técnicos

**Assinatura:** `VERSOES_LEITURA`

**Origem da implementação:** `coral.persistencia`

**Arquivo na release:** `coral/persistencia.py`

**Valor declarado:** `(1,)`

:::

#### `VERSAO_ESCRITA`

Expõe a constante pública `VERSAO_ESCRITA`.

:::details Detalhes técnicos

**Assinatura:** `VERSAO_ESCRITA`

**Origem da implementação:** `coral.persistencia`

**Arquivo na release:** `coral/persistencia.py`

**Valor declarado:** `1`

:::

<!-- /AUTO:API -->
