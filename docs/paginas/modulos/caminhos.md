# coral.caminhos

## Visão geral

`coral.caminhos` oferece normalização explícita de caminhos locais e portáteis. Use para juntar e normalizar caminhos de forma explícita e mais portátil entre sistemas.

<!-- AUTO:MODULO -->

**Importação:** `coral.caminhos`  
**Categoria:** sistema  

normalização explícita de caminhos locais e portáteis

### Superfície pública detectada

`CaminhoAceito`, `normalizar_caminho`, `juntar_caminho`, `estilo_caminho`, `estilo_nativo`, `caminho_portatil`

<!-- /AUTO:MODULO -->

## Papel no ecossistema

Define um contrato único para representar caminhos locais e portáteis. A intenção é impedir que texto, caminhos Windows e caminhos POSIX sejam misturados silenciosamente como se tivessem a mesma semântica.

## Conceitos principais

### Caminho local

`normalizar_caminho` produz um `Path` nativo e permite decidir explicitamente se `~` será expandido e se o caminho será resolvido.

### Composição

`juntar_caminho` reúne partes sem depender de barras escritas à mão.

### Estilo de caminho

`estilo_caminho` e `estilo_nativo` ajudam a distinguir representação Windows, POSIX e o estilo do sistema corrente.

### Reconstrução portátil

`caminho_portatil` reconstrói um caminho a partir de texto e estilo informado, sem fingir que ele já é necessariamente utilizável como caminho local.

## Quando usar

Use este módulo quando o problema corresponder diretamente aos conceitos acima. Por ser um módulo complementar, ele normalmente entra em um programa para resolver uma responsabilidade específica e deve permanecer desacoplado da lógica central sempre que possível.

## Começando

A release inclui um exemplo real em `Exemplos/Dados/02_arquivos_json_e_caminhos.coral`:

```coral
de coral.json importe para_json, de_json
de coral.caminhos importe juntar_caminho

defina caminho_texto como juntar_caminho("dados", "mensagem.txt")
mostre caminho_texto

execute escrever_texto("mensagem.txt", "Olá, arquivo!")
defina conteudo como ler_texto("mensagem.txt")
mostre conteudo

defina original como {"nome": "Ana", "nota": 9}
```

## API essencial

| Entrada | Papel |
|---|---|
| `normalizar_caminho` | normalizar entrada local |
| `juntar_caminho` | compor partes |
| `estilo_caminho` | identificar estilo |
| `estilo_nativo` | consultar estilo local |
| `caminho_portatil` | reconstruir caminho por estilo |

A seção **Referência da API** no fim desta página contém a superfície pública completa detectada na release, com assinaturas, parâmetros, retornos e docstrings quando presentes.

## Fluxos comuns

1. Receba texto ou objeto de caminho na borda da aplicação.
2. Normalize somente quando a operação realmente será local.
3. Preserve a informação de estilo quando um caminho será transportado entre sistemas.
4. Passe o caminho normalizado a `coral.arquivos` apenas no momento do IO.

## Erros e casos de borda

Resolver um caminho e expandir usuário são decisões diferentes. Também não é seguro assumir que um caminho portátil de outro sistema existe na máquina atual.

## Boas práticas

* Não concatene `"/"` ou `"\"` manualmente.
* Não converta cedo demais um caminho de outro estilo para `Path` nativo.
* Guarde caminhos relativos quando isso melhorar a portabilidade de projetos movidos.

## Integração com outros módulos

É parceiro direto de `coral.arquivos`; também aparece em persistência, assets e recursos de projeto onde um valor precisa continuar portátil.

## Testabilidade e previsibilidade

Testes de caminho devem cobrir componentes, estilos e normalização sem depender de uma pasta real sempre que possível. IO real fica para testes de `coral.arquivos`.

## Compatibilidade e evolução

A documentação desta página descreve a superfície detectada na **Coral 1.5.9**. O gerador do site atualiza automaticamente o inventário e a referência da API quando uma nova release é importada, mas o texto pedagógico desta seção permanece sob revisão humana.

## Referência da API

<!-- AUTO:API -->

### Funções

#### `normalizar_caminho(valor: CaminhoAceito, *, expandir_usuario: bool = False, resolver: bool = False) -> Path`

Converte uma entrada para ``Path`` nativo com regras explícitas.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `valor` | `CaminhoAceito` | obrigatório | posicional |
| `expandir_usuario` | `bool` | `False` | nomeado |
| `resolver` | `bool` | `False` | nomeado |

**Retorno:** `Path`

**Exceções observáveis no corpo:** `ValueError`, `TypeError`

#### `juntar_caminho(*partes: Any, expandir_usuario: bool = True) -> Path`

Entrada pública `juntar_caminho` da superfície `coral.caminhos`.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `*partes` | `Any` | obrigatório | variádico |
| `expandir_usuario` | `bool` | `True` | nomeado |

**Retorno:** `Path`

#### `estilo_caminho(valor: PurePath) -> str`

Entrada pública `estilo_caminho` da superfície `coral.caminhos`.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `valor` | `PurePath` | obrigatório | posicional |

**Retorno:** `str`

#### `estilo_nativo() -> str`

Entrada pública `estilo_nativo` da superfície `coral.caminhos`.

**Retorno:** `str`

#### `caminho_portatil(texto: str, estilo: str, *, concreto: bool = True) -> PurePath`

Reconstrói a categoria caminho sem fingir compatibilidade entre SOs.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `texto` | `str` | obrigatório | posicional |
| `estilo` | `str` | obrigatório | posicional |
| `concreto` | `bool` | `True` | nomeado |

**Retorno:** `PurePath`

**Exceções observáveis no corpo:** `ValueError`

### Constantes e aliases

#### `CaminhoAceito`

Alias público de tipo ou valor.

**Valor declarado:** `str | os.PathLike[str]`

<!-- /AUTO:API -->
