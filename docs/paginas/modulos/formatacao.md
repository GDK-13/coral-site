# coral.formatacao

## Visão geral

`coral.formatacao` oferece montagem explícita de texto. Use para montar textos e formatar valores de modo explícito e reutilizável.

<!-- AUTO:MODULO -->

**Importação:** `coral.formatacao`  
**Categoria:** texto  

montagem explícita de texto

### Superfície pública detectada

`formatar_valor`, `montar_texto`, `ErroFormato`

<!-- /AUTO:MODULO -->

## Papel no ecossistema

Fornece montagem textual explícita e previsível. É intencionalmente pequeno para não criar um segundo sistema de interpolação fora do parser e da AST da Coral.

## Conceitos principais

### Representação de valor

`formatar_valor` usa as convenções textuais da Coral, incluindo `nulo`, `verdadeiro` e `falso`.

### Composição

`montar_texto` converte cada parte, junta com separador opcional e acrescenta um final opcional.

### Sem interpolação oculta

O módulo não interpreta placeholders ou expressões dentro de strings; isso evita sintaxe paralela à linguagem.

## Quando usar

Use este módulo quando o problema corresponder diretamente aos conceitos acima. Por ser um módulo complementar, ele normalmente entra em um programa para resolver uma responsabilidade específica e deve permanecer desacoplado da lógica central sempre que possível.

## Começando

A release inclui um exemplo real em `Exemplos/Dados/01_entrada_conversoes_e_texto.coral`:

```coral
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
| `formatar_valor` | representar um valor |
| `montar_texto` | montar texto por partes |
| `ErroFormato` | falha controlada de formatação |

A seção **Referência da API** no fim desta página contém a superfície pública completa detectada na release, com assinaturas, parâmetros, retornos e docstrings quando presentes.

## Fluxos comuns

1. Converta valores do domínio apenas no momento de apresentar.
2. Use `montar_texto` quando a mensagem combina partes heterogêneas e um separador claro.
3. Para transformações de texto, use `coral.texto`; para formatos de dados, use `coral.formatos` ou `coral.json`.

## Erros e casos de borda

Separador e final precisam ser representáveis como texto. O módulo não tenta executar código escrito dentro de uma string.

## Boas práticas

* Mantenha lógica de cálculo fora da formatação.
* Use `montar_texto` quando a composição é simples e explícita.
* Não confunda apresentação humana com serialização de dados.

## Integração com outros módulos

`coral.conversoes.texto` sustenta a representação básica; `coral.texto` cuida de transformação textual; módulos de dados devem usar formatos próprios para persistência e intercâmbio.

## Testabilidade e previsibilidade

Teste valores especiais como `nulo`, booleanos e separadores. Como não há interpolação implícita, os resultados são fáceis de comparar exatamente.

## Compatibilidade e evolução

A documentação desta página descreve a superfície detectada na **Coral 1.5.9**. O gerador do site atualiza automaticamente o inventário e a referência da API quando uma nova release é importada, mas o texto pedagógico desta seção permanece sob revisão humana.

## Referência da API

<!-- AUTO:API -->

### Funções

#### `formatar_valor(valor: Any) -> str`

Representação textual básica usando convenções de literais Coral.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `valor` | `Any` | obrigatório | posicional |

**Retorno:** `str`

#### `montar_texto(*partes: Any, separador: str = '', final: str = '') -> str`

Monta texto convertendo as partes de modo explícito e previsível.

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `*partes` | `Any` | obrigatório | variádico |
| `separador` | `str` | `''` | nomeado |
| `final` | `str` | `''` | nomeado |

**Retorno:** `str`

**Exceções observáveis no corpo:** `ErroFormato`

### Exceções

#### `ErroFormato(...)`

Dados ou texto não obedecem ao formato esperado.

**Implementação:** `coral.erros`

<!-- /AUTO:API -->
