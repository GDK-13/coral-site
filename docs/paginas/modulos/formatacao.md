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

## Quando usar

Use para montar textos e formatar valores de modo explícito e reutilizável.

Entre as entradas públicas detectadas estão `montar_texto`, `formatar_valor`.

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

## Cuidados

Mantenha regras de apresentação próximas da camada de saída quando elas não fizerem parte do domínio.

## Relações com outros módulos

Na mesma área, veja também `coral.texto`.

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
