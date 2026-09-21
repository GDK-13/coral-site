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

## Papel no ecossistema

É o contrato de persistência portátil e versionada da Coral. Em vez de serializar objetos arbitrários do runtime, grava somente dados semânticos reconstruíveis e rejeita estado que não é seguro ou portátil salvar.

## Conceitos principais

### Contrato versionado

`CONTRATO` e `VERSAO_ESQUEMA` identificam o formato persistente.

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

A documentação desta página descreve a superfície detectada na **Coral 1.5.9**. O gerador do site atualiza automaticamente o inventário e a referência da API quando uma nova release é importada, mas o texto pedagógico desta seção permanece sob revisão humana.

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
