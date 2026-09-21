# coral.entrada

## Visão geral

`coral.entrada` oferece entrada interceptável e testável. Use quando a leitura de entrada precisa ser substituível em testes ou controlada por outra fonte.

<!-- AUTO:MODULO -->

**Importação:** `coral.entrada`  
**Categoria:** runtime  

entrada interceptável e testável

### Superfície pública detectada

`FonteEntrada`, `FonteEntradaFuncao`, `FonteEntradaSequencial`, `FimDeEntrada`, `ler_linha`, `usar_fonte_entrada`

<!-- /AUTO:MODULO -->

## Papel no ecossistema

Separa leitura de linha da origem física da entrada. O programa pode ler do terminal em produção e usar uma fonte determinística em testes, REPLs, debugger ou ferramentas.

## Conceitos principais

### Fonte explícita

`ler_linha(..., fonte=...)` permite escolher a origem para uma única leitura.

### Fonte contextual

`usar_fonte_entrada` instala temporariamente uma fonte no contexto corrente, evitando passar o leitor por toda a cadeia de chamadas.

### Fonte sequencial

`FonteEntradaSequencial` consome uma sequência conhecida de linhas e gera `FimDeEntrada` quando termina.

### Fim de entrada

EOF do terminal e fontes esgotadas convergem para `FimDeEntrada`, evitando dependência direta de `EOFError`.

## Quando usar

Use este módulo quando o problema corresponder diretamente aos conceitos acima. Por ser um módulo complementar, ele normalmente entra em um programa para resolver uma responsabilidade específica e deve permanecer desacoplado da lógica central sempre que possível.

## Começando

A release inclui um exemplo real em `Exemplos/Dados/01_entrada_conversoes_e_texto.coral`:

```coral
# Entrada, conversão explícita e composição de texto.
de coral.entrada importe ler_linha
de coral.conversoes importe inteiro, decimal
de coral.formatacao importe montar_texto

defina nome como ler_linha("Nome: ")
defina idade como inteiro(ler_linha("Idade: "))
defina altura como decimal(ler_linha("Altura em metros: "))
mostre montar_texto("Olá, ", nome, ". Idade: ", idade, ". Altura: ", altura)
```

## API essencial

| Entrada | Papel |
|---|---|
| `ler_linha` | ler uma linha |
| `usar_fonte_entrada` | instalar fonte contextual |
| `FonteEntradaSequencial` | entrada determinística |
| `FonteEntrada` | protocolo de fonte |
| `FimDeEntrada` | fim controlado da fonte |

A seção **Referência da API** no fim desta página contém a superfície pública completa detectada na release, com assinaturas, parâmetros, retornos e docstrings quando presentes.

## Fluxos comuns

1. Leia texto bruto por `ler_linha`.
2. Converta o valor com `coral.conversoes` na borda da aplicação.
3. Em testes, substitua terminal por `FonteEntradaSequencial` ou fonte função.
4. Trate `FimDeEntrada` quando terminar a fonte for um cenário esperado.

## Erros e casos de borda

Uma fonte pode terminar antes do esperado. `ler_linha` remove quebras finais de linha, mas não converte o conteúdo para número ou booleano automaticamente.

## Boas práticas

* Não misture leitura de terminal com lógica de domínio.
* Converta e valide imediatamente após ler.
* Use fonte determinística em testes e ferramentas.

## Integração com outros módulos

`coral.conversoes` transforma o texto lido; `coral.formatacao` monta prompts e mensagens; DAP, REPL e ferramentas podem injetar fontes sem modificar o programa.

## Testabilidade e previsibilidade

Com `FonteEntradaSequencial`, testes não precisam de stdin real. Isso torna prompts e fluxos de entrada repetíveis em CI.

## Compatibilidade e evolução

A documentação desta página descreve a superfície detectada na **Coral 1.5.9**. O gerador do site atualiza automaticamente o inventário e a referência da API quando uma nova release é importada, mas o texto pedagógico desta seção permanece sob revisão humana.

## Referência da API

<!-- AUTO:API -->

### Funções

#### `ler_linha(mensagem: str | None = None, *, fonte: FonteEntrada | FonteEntradaFuncao | None = None) -> str`

Lê uma linha usando a fonte explícita, contextual ou o terminal.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `mensagem` | `str \| None` | `None` | posicional |
| `fonte` | `FonteEntrada \| FonteEntradaFuncao \| None` | `None` | nomeado |

**Retorno:** `str`

**Exceções observáveis no corpo:** `FimDeEntrada`

#### `usar_fonte_entrada(fonte: FonteEntrada | FonteEntradaFuncao)`

Instala temporariamente uma fonte de entrada no contexto corrente.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `fonte` | `FonteEntrada \| FonteEntradaFuncao` | obrigatório | posicional |

**Retorno:** `não declarado`

### Classes e protocolos

#### `FonteEntrada(...)`

Entrada pública `FonteEntrada` da superfície `coral.entrada`.

**Métodos e propriedades públicas**

| Nome | Tipo | Assinatura | Retorno | Descrição |
|---|---|---|---|---|
| `ler_linha` | método | `ler_linha(mensagem: str = '') -> str` | `str` | Sem docstring própria na release. |

#### `FonteEntradaSequencial(linhas: Iterable[str])`

Fonte determinística útil em testes, REPLs e ferramentas.

**Atributos declarados**

| Nome | Tipo | Padrão |
|---|---|---|
| `linhas` | `Iterable[str]` | obrigatório |

**Métodos e propriedades públicas**

| Nome | Tipo | Assinatura | Retorno | Descrição |
|---|---|---|---|---|
| `ler_linha` | método | `ler_linha(mensagem: str = '') -> str` | `str` | Sem docstring própria na release. |

### Exceções

#### `FimDeEntrada(...)`

A fonte de entrada terminou antes de produzir outra linha.

**Implementação:** `coral.erros`

### Constantes e aliases

#### `FonteEntradaFuncao`

Alias público de tipo ou valor.

**Valor declarado:** `Callable[[str], str]`

<!-- /AUTO:API -->
