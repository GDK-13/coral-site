# coral.procedural

## Visão geral

sementes derivadas, geração determinística, ruído, campos e distribuição procedural

<!-- AUTO:MODULO -->

**Importação:** `coral.procedural`  
**Categoria:** simulacao  

sementes derivadas, geração determinística, campos, amostragem, receitas e pontes explícitas para jogos e pesquisa

### Superfície pública detectada

`CONTRATO`, `Semente`, `semente`, `derivar_semente`, `GeradorProcedural`, `SequenciaProcedural`, `CampoProcedural`, `campo_constante`, `campo_ruido`, `distribuir_pontos`, `amostrar_campo`, `matriz_campo`, `anotar_pontos`, `proveniencia_procedural`, `CONTRATO_RECEITA`, `ReceitaProcedural`, `receita_procedural`, `diagnosticar_custo_receita`, `reconstruir_receita`

<!-- /AUTO:MODULO -->

## Papel no ecossistema

`coral.procedural` fornece geração determinística por semente sem exigir interface gráfica. O mesmo conjunto de primitivas pode servir a jogos, simulações, ecologia, logística, geração de dados, mapas, cenários de teste e qualquer domínio que precise produzir variação reproduzível.

## Conceitos principais

### Sementes derivadas

`Semente` normaliza uma raiz e permite derivar novas sementes por rótulos. Subsementes independentes evitam que adicionar uma nova consulta em uma parte do programa altere resultados de outra parte que usa outra chave.

### Gerador por chave

`GeradorProcedural` é orientado por chave ou contexto. Consultar o mesmo método com a mesma semente, namespace e chaves produz o mesmo resultado, sem depender da ordem das consultas anteriores.

### Sequências indexadas

`SequenciaProcedural` associa cada índice diretamente a um valor. Consultar a posição 20 antes da posição 3 não muda nenhuma delas.

### Campos

`CampoProcedural` representa uma função numérica sobre coordenadas. Campos podem ser transformados, limitados, normalizados, somados, multiplicados e convertidos em máscaras.

### Ruído e distribuição espacial

`campo_ruido` produz ruído de valor suave em uma, duas ou três dimensões. `distribuir_pontos` cria posições 2D determinísticas com margem, distância mínima e uma restrição opcional.

## Quando usar

Use este módulo quando o programa precisa de resultados variados que continuem reproduzíveis. É especialmente útil para geração de mapas, parâmetros ambientais, distribuição de objetos, séries de demanda, dados sintéticos e testes que precisam repetir exatamente o mesmo cenário.

## Começando

A release inclui uma forma natural para geração por semente:

```coral
crie um gerador chamado clima com semente 42
gere um decimal com clima para "chuva" como amostra
crie um campo de ruido chamado relevo com semente 42 e escala 20
consulte o campo relevo em [10, 15] como altura
mostre amostra
mostre altura
```

Subsementes podem isolar subsistemas:

```coral
crie um gerador chamado mundo com semente 42
derive do gerador mundo a chave "temperatura" como temperatura
derive do gerador mundo a chave "vegetacao" como vegetacao
gere um decimal com temperatura para "setor-1" como calor
gere um decimal com vegetacao para "setor-1" como plantas
```

## API essencial

| Entrada | Papel |
|---|---|
| `Semente` / `semente` | raiz estável e normalizada para geração |
| `derivar_semente` | cria uma subsemente a partir de rótulos portáteis |
| `GeradorProcedural` | gera valores determinísticos por chave |
| `SequenciaProcedural` | série indexada independente da ordem de consulta |
| `CampoProcedural` | campo numérico componível por coordenadas |
| `campo_ruido` | ruído suave de uma a três dimensões |
| `campo_constante` | campo com valor fixo |
| `distribuir_pontos` | distribuição 2D com restrições simples |

## Fluxos comuns

1. Escolha uma semente raiz para o cenário.
2. Derive namespaces ou subsementes para separar partes independentes do sistema.
3. Use chaves estáveis ligadas ao domínio em vez de depender de ordem de chamada.
4. Componha campos quando precisar de mapas contínuos ou máscaras.
5. Materialize o resultado apenas quando o domínio realmente exigir uma grade armazenada.

## Erros e casos de borda

Sementes e rótulos aceitam apenas valores portáteis e determinísticos. Ruído exige escala e lacunaridade positivas, persistência não negativa e uma quantidade positiva de oitavas. `distribuir_pontos` pode gerar `RuntimeError` quando as restrições espaciais tornam impossível alcançar a quantidade solicitada dentro do limite de tentativas.

## Boas práticas

* Derive uma semente separada por subsistema para evitar acoplamento acidental de resultados.
* Use chaves com significado de domínio, como identificador, coordenada ou período.
* Prefira consultar campos sob demanda quando não houver necessidade de armazenar uma grade completa.
* Ao usar distribuição com distância mínima, escolha área e quantidade compatíveis para evitar tentativas impossíveis.

## Integração com outros módulos

`coral.simulacao` usa campos procedurais como base para `CampoAmbiental`. `coral.mundo` pode receber campos materializados em camadas de mapa. `coral.aleatorio` continua útil para aleatoriedade sequencial tradicional, enquanto `coral.procedural` é preferível quando independência por chave e reprodutibilidade estrutural são requisitos centrais.

## Testabilidade e previsibilidade

Testes devem fixar a semente e comparar resultados por chave ou coordenada. Uma propriedade importante é a independência da ordem: consultar outra chave antes não deve alterar um valor já definido pelo mesmo contexto.

## Compatibilidade e integração

A superfície procedural corrente trabalha com sementes derivadas, geração determinística, campos, distribuição de pontos, proveniência e receitas. Jogos e Laboratório consomem essa base por pontes explícitas, sem transformar Procedural em dependência de interface ou experimento.

## Referência da API

<!-- AUTO:API -->

### Funções

#### `semente`

Executa a operação `semente` disponibilizada por `coral.procedural`.

**Exemplo**

```coral
crie um gerador chamado clima com semente 42
gere um decimal com clima para "chuva" como amostra
crie um campo de ruido chamado relevo com semente 42 e escala 20
consulte o campo relevo em [10, 15] como altura
mostre amostra
mostre altura
```

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valor` | Valor processado pela operação. | `Any` | `0` |

**Retorno**

Retorna um valor declarado como `Semente`.

:::details Detalhes técnicos

**Assinatura:** `semente(valor: Any = 0) -> Semente`

**Origem da implementação:** `coral.procedural`

**Arquivo na release:** `coral/procedural.py`

:::

#### `derivar_semente`

Executa a operação `derivar_semente` disponibilizada por `coral.procedural`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valor` | Valor processado pela operação. | `Any` | obrigatório |
| `*rotulos` | Valor correspondente a rotulos. | `Any` | obrigatório |

**Retorno**

Retorna um valor declarado como `Semente`.

:::details Detalhes técnicos

**Assinatura:** `derivar_semente(valor: Any, *rotulos: Any) -> Semente`

**Origem da implementação:** `coral.procedural`

**Arquivo na release:** `coral/procedural.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `valor` | posicional |
| `*rotulos` | variádico |

:::

#### `campo_constante`

Executa a operação `campo_constante` disponibilizada por `coral.procedural`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valor` | Valor processado pela operação. | `float` | obrigatório |
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | `'constante'` |

**Retorno**

Retorna um valor declarado como `CampoProcedural`.

:::details Detalhes técnicos

**Assinatura:** `campo_constante(valor: float, *, nome: str = 'constante') -> CampoProcedural`

**Origem da implementação:** `coral.procedural`

**Arquivo na release:** `coral/procedural.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `valor` | posicional |
| `nome` | nomeado |

:::

#### `campo_ruido`

Cria ruído de valor suave para 1D, 2D ou 3D sem dependências externas.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `semente_raiz` | Valor correspondente a semente raiz. | `Any` | `0` |
| `escala` | Valor correspondente a escala. | `float` | `1.0` |
| `oitavas` | Valor correspondente a oitavas. | `int` | `1` |
| `persistencia` | Valor correspondente a persistencia. | `float` | `0.5` |
| `lacunaridade` | Valor correspondente a lacunaridade. | `float` | `2.0` |
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | `'ruido'` |

**Retorno**

Retorna um valor declarado como `CampoProcedural`.

:::details Detalhes técnicos

**Assinatura:** `campo_ruido(semente_raiz: Any = 0, *, escala: float = 1.0, oitavas: int = 1, persistencia: float = 0.5, lacunaridade: float = 2.0, nome: str = 'ruido') -> CampoProcedural`

**Origem da implementação:** `coral.procedural`

**Arquivo na release:** `coral/procedural.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `semente_raiz` | posicional |
| `escala` | nomeado |
| `oitavas` | nomeado |
| `persistencia` | nomeado |
| `lacunaridade` | nomeado |
| `nome` | nomeado |

**Exceções diretamente observáveis no corpo:** `ValueError`

:::

#### `distribuir_pontos`

Distribui pontos 2D determinísticos sob limites finitos de trabalho.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `largura` | Largura usada pela operação. | `float` | obrigatório |
| `altura` | Altura usada pela operação. | `float` | obrigatório |
| `quantidade` | Quantidade de itens solicitada. | `int` | obrigatório |
| `semente_raiz` | Valor correspondente a semente raiz. | `Any` | `0` |
| `margem` | Valor correspondente a margem. | `float` | `0.0` |
| `distancia_minima` | Valor correspondente a distancia minima. | `float` | `0.0` |
| `restricao` | Valor correspondente a restricao. | `Callable[[float, float], bool] \| None` | `None` |
| `max_tentativas_por_ponto` | Valor correspondente a max tentativas por ponto. | `int` | `200` |
| `limite_tentativas_total` | Valor correspondente a limite tentativas total. | `int` | `1000000` |

**Retorno**

Retorna um valor declarado como `tuple[tuple[float, float], ...]`.

:::details Detalhes técnicos

**Assinatura:** `distribuir_pontos(largura: float, altura: float, quantidade: int, *, semente_raiz: Any = 0, margem: float = 0.0, distancia_minima: float = 0.0, restricao: Callable[[float, float], bool] \| None = None, max_tentativas_por_ponto: int = 200, limite_tentativas_total: int = 1000000) -> tuple[tuple[float, float], ...]`

**Origem da implementação:** `coral.procedural`

**Arquivo na release:** `coral/procedural.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `largura` | posicional |
| `altura` | posicional |
| `quantidade` | posicional |
| `semente_raiz` | nomeado |
| `margem` | nomeado |
| `distancia_minima` | nomeado |
| `restricao` | nomeado |
| `max_tentativas_por_ponto` | nomeado |
| `limite_tentativas_total` | nomeado |

**Exceções diretamente observáveis no corpo:** `ValueError`, `TypeError`, `RuntimeError`

:::

#### `amostrar_campo`

Materializa amostras portáteis de um campo sem depender de Numérico ou Laboratório.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `campo` | Valor correspondente a campo. | `CampoProcedural` | obrigatório |
| `coordenadas` | Valor correspondente a coordenadas. | `Iterable[Sequence[float]]` | obrigatório |
| `nomes_eixos` | Valor correspondente a nomes eixos. | `Sequence[str] \| None` | `None` |
| `nome_valor` | Valor correspondente a nome valor. | `str` | `'valor'` |
| `limite_amostras` | Valor correspondente a limite amostras. | `int` | `100000` |

**Retorno**

Retorna um valor declarado como `tuple[dict[str, Any], ...]`.

:::details Detalhes técnicos

**Assinatura:** `amostrar_campo(campo: CampoProcedural, coordenadas: Iterable[Sequence[float]], *, nomes_eixos: Sequence[str] \| None = None, nome_valor: str = 'valor', limite_amostras: int = 100000) -> tuple[dict[str, Any], ...]`

**Origem da implementação:** `coral.procedural`

**Arquivo na release:** `coral/procedural.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `campo` | posicional |
| `coordenadas` | posicional |
| `nomes_eixos` | nomeado |
| `nome_valor` | nomeado |
| `limite_amostras` | nomeado |

**Exceções diretamente observáveis no corpo:** `TypeError`, `ValueError`

:::

#### `matriz_campo`

Amostra um campo 2D como matriz, pronta para mapas, jogos e mapas de calor.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `campo` | Valor correspondente a campo. | `CampoProcedural` | obrigatório |
| `colunas` | Valor correspondente a colunas. | `int` | obrigatório |
| `linhas` | Linhas usadas para construir ou processar a estrutura. | `int` | obrigatório |
| `origem` | Origem usada pela operação. | `Sequence[float]` | `(0.0, 0.0)` |
| `passo` | Incremento aplicado entre valores sucessivos. | `Sequence[float]` | `(1.0, 1.0)` |
| `limite_celulas` | Valor correspondente a limite celulas. | `int` | `1000000` |

**Retorno**

Retorna um valor declarado como `tuple[tuple[float, ...], ...]`.

:::details Detalhes técnicos

**Assinatura:** `matriz_campo(campo: CampoProcedural, colunas: int, linhas: int, *, origem: Sequence[float] = (0.0, 0.0), passo: Sequence[float] = (1.0, 1.0), limite_celulas: int = 1000000) -> tuple[tuple[float, ...], ...]`

**Origem da implementação:** `coral.procedural`

**Arquivo na release:** `coral/procedural.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `campo` | posicional |
| `colunas` | posicional |
| `linhas` | posicional |
| `origem` | nomeado |
| `passo` | nomeado |
| `limite_celulas` | nomeado |

**Exceções diretamente observáveis no corpo:** `TypeError`, `ValueError`

:::

#### `anotar_pontos`

Anexa valores de campos a pontos 2D em registros gerais e portáteis.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `pontos` | Valor correspondente a pontos. | `Iterable[Sequence[float]]` | obrigatório |
| `campos` | Valor correspondente a campos. | `Mapping[str, CampoProcedural]` | obrigatório |
| `limite_pontos` | Valor correspondente a limite pontos. | `int` | `100000` |

**Retorno**

Retorna um valor declarado como `tuple[dict[str, Any], ...]`.

:::details Detalhes técnicos

**Assinatura:** `anotar_pontos(pontos: Iterable[Sequence[float]], campos: Mapping[str, CampoProcedural], *, limite_pontos: int = 100000) -> tuple[dict[str, Any], ...]`

**Origem da implementação:** `coral.procedural`

**Arquivo na release:** `coral/procedural.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `pontos` | posicional |
| `campos` | posicional |
| `limite_pontos` | nomeado |

**Exceções diretamente observáveis no corpo:** `ValueError`, `TypeError`

:::

#### `proveniencia_procedural`

Descreve origem procedural sem importar domínios consumidores.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `objeto` | Objeto processado pela operação. | `Any` | obrigatório |

**Retorno**

Retorna um valor declarado como `dict[str, Any]`.

:::details Detalhes técnicos

**Assinatura:** `proveniencia_procedural(objeto: Any) -> dict[str, Any]`

**Origem da implementação:** `coral.procedural`

**Arquivo na release:** `coral/procedural.py`

**Exceções diretamente observáveis no corpo:** `TypeError`

:::

#### `receita_procedural`

Cria uma receita portátil para um dos algoritmos declarativos suportados.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `algoritmo` | Valor correspondente a algoritmo. | `str` | obrigatório |
| `semente_raiz` | Valor correspondente a semente raiz. | `Any` | `0` |
| `**parametros` | Valor correspondente a parametros. | `Any` | obrigatório |

**Retorno**

Retorna um valor declarado como `ReceitaProcedural`.

:::details Detalhes técnicos

**Assinatura:** `receita_procedural(algoritmo: str, *, semente_raiz: Any = 0, **parametros: Any) -> ReceitaProcedural`

**Origem da implementação:** `coral.procedural`

**Arquivo na release:** `coral/procedural.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `algoritmo` | posicional |
| `semente_raiz` | nomeado |
| `**parametros` | variádico nomeado |

:::

#### `diagnosticar_custo_receita`

Estima o trabalho máximo conhecido antes de reconstruir a receita.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `receita` | Valor correspondente a receita. | `ReceitaProcedural \| Mapping[str, Any]` | obrigatório |

**Retorno**

Retorna um valor declarado como `dict[str, Any]`.

:::details Detalhes técnicos

**Assinatura:** `diagnosticar_custo_receita(receita: ReceitaProcedural \| Mapping[str, Any]) -> dict[str, Any]`

**Origem da implementação:** `coral.procedural`

**Arquivo na release:** `coral/procedural.py`

:::

#### `reconstruir_receita`

Reconstrói uma receita após validar versão e orçamento explícito.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `receita` | Valor correspondente a receita. | `ReceitaProcedural \| Mapping[str, Any]` | obrigatório |
| `limite_custo` | Valor correspondente a limite custo. | `int` | `LIMITE_CUSTO_PADRAO` |

**Retorno**

Retorna um valor declarado como `Any`.

:::details Detalhes técnicos

**Assinatura:** `reconstruir_receita(receita: ReceitaProcedural \| Mapping[str, Any], *, limite_custo: int = LIMITE_CUSTO_PADRAO) -> Any`

**Origem da implementação:** `coral.procedural`

**Arquivo na release:** `coral/procedural.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `receita` | posicional |
| `limite_custo` | nomeado |

**Exceções diretamente observáveis no corpo:** `ValueError`

:::

### Classes e protocolos

#### `Semente`

Semente estável capaz de derivar sub sementes independentes.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valor` | Valor processado pela operação. | `Any` | `0` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `valor` | Valor processado pela operação. | `Any` | `0` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `inteiro` | Sorteia um número inteiro entre os limites informados. | `int` |
| `hexadecimal` | Executa a operação `hexadecimal` disponibilizada por `coral.procedural`. | `str` |
| `derivar` | Executa a operação `derivar` disponibilizada por `coral.procedural`. | `'Semente'` |
| `fonte` | Cria uma fonte de aleatoriedade, opcionalmente reproduzível por semente. | `FonteAleatoria` |

:::details Detalhes técnicos

**Assinatura:** `Semente(valor: Any = 0)`

**Origem da implementação:** `coral.procedural`

**Arquivo na release:** `coral/procedural.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `inteiro` | propriedade | `inteiro() -> int` |
| `hexadecimal` | propriedade | `hexadecimal() -> str` |
| `derivar` | método | `derivar(*rotulos: Any) -> 'Semente'` |
| `fonte` | método | `fonte(*rotulos: Any) -> FonteAleatoria` |

:::

#### `GeradorProcedural`

Gerador sem estado para consultas determinísticas por chave ou contexto.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `semente_raiz` | Valor correspondente a semente raiz. | `Any` | `0` |
| `namespace` | Valor correspondente a namespace. | `str` | `'gerador'` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `derivar` | Executa a operação `derivar` disponibilizada por `coral.procedural`. | `'GeradorProcedural'` |
| `fonte` | Cria uma fonte de aleatoriedade, opcionalmente reproduzível por semente. | `FonteAleatoria` |
| `decimal` | Sorteia um número decimal dentro do intervalo informado. | `float` |
| `inteiro` | Sorteia um número inteiro entre os limites informados. | `int` |
| `escolher` | Escolhe o valor solicitado. | `Any` |
| `escolha_ponderada` | Escolhe um valor considerando os pesos fornecidos. | `Any` |
| `amostra` | Seleciona uma amostra de valores da coleção fornecida. | `list[Any]` |
| `normal` | Executa a operação `normal` disponibilizada por `coral.procedural`. | `float` |
| `triangular` | Executa a operação `triangular` disponibilizada por `coral.procedural`. | `float` |

:::details Detalhes técnicos

**Assinatura:** `GeradorProcedural(semente_raiz: Any = 0, *, namespace: str = 'gerador') -> None`

**Origem da implementação:** `coral.procedural`

**Arquivo na release:** `coral/procedural.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `semente_raiz` | posicional |
| `namespace` | nomeado |

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `derivar` | método | `derivar(rotulo: Any) -> 'GeradorProcedural'` |
| `fonte` | método | `fonte(*chaves: Any) -> FonteAleatoria` |
| `decimal` | método | `decimal(*chaves: Any, minimo: float = 0.0, maximo: float = 1.0) -> float` |
| `inteiro` | método | `inteiro(minimo: int, maximo: int, *chaves: Any) -> int` |
| `escolher` | método | `escolher(valores: Iterable[Any], *chaves: Any) -> Any` |
| `escolha_ponderada` | método | `escolha_ponderada(valores: Iterable[Any], pesos: Iterable[float], *chaves: Any) -> Any` |
| `amostra` | método | `amostra(valores: Iterable[Any], quantidade: int, *chaves: Any) -> list[Any]` |
| `normal` | método | `normal(*chaves: Any, media: float = 0.0, desvio: float = 1.0) -> float` |
| `triangular` | método | `triangular(*chaves: Any, minimo: float = 0.0, maximo: float = 1.0, moda: float \| None = None) -> float` |

:::

#### `SequenciaProcedural`

Sequência indexada cuja posição não depende das consultas anteriores.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `semente_raiz` | Valor correspondente a semente raiz. | `Any` | `0` |
| `gerador` | Valor correspondente a gerador. | `Callable[[GeradorProcedural, int], Any] \| None` | `None` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `obter` | Executa a operação `obter` disponibilizada por `coral.procedural`. | `Any` |
| `trecho` | Executa a operação `trecho` disponibilizada por `coral.procedural`. | `tuple[Any, ...]` |

:::details Detalhes técnicos

**Assinatura:** `SequenciaProcedural(semente_raiz: Any = 0, gerador: Callable[[GeradorProcedural, int], Any] \| None = None)`

**Origem da implementação:** `coral.procedural`

**Arquivo na release:** `coral/procedural.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `obter` | método | `obter(indice: int) -> Any` |
| `trecho` | método | `trecho(inicio: int, quantidade: int, *, limite_itens: int = LIMITE_TRECHO_PADRAO) -> tuple[Any, ...]` |

:::

#### `CampoProcedural`

Campo numérico consultável por coordenadas e combinável por composição.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `funcao` | Função fornecida para executar a operação. | `Callable[..., float]` | obrigatório |
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | `'campo'` |
| `metadados` | Valor correspondente a metadados. | `Mapping[str, Any] \| None` | `None` |
| `dimensoes_min` | Valor correspondente a dimensoes min. | `int` | `1` |
| `dimensoes_max` | Valor correspondente a dimensoes max. | `int \| None` | `None` |
| `intervalo` | Valor correspondente a intervalo. | `tuple[float, float] \| None` | `None` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `valor` | Obtém valor. | `float` |
| `transformar` | Executa a operação `transformar` disponibilizada por `coral.procedural`. | `'CampoProcedural'` |
| `limitar` | Executa a operação `limitar` disponibilizada por `coral.procedural`. | `'CampoProcedural'` |
| `normalizar` | Normaliza o valor solicitado. | `'CampoProcedural'` |
| `somar` | Executa a operação `somar` disponibilizada por `coral.procedural`. | `'CampoProcedural'` |
| `multiplicar` | Executa a operação `multiplicar` disponibilizada por `coral.procedural`. | `'CampoProcedural'` |
| `mascara` | Executa a operação `mascara` disponibilizada por `coral.procedural`. | `'CampoProcedural'` |

:::details Detalhes técnicos

**Assinatura:** `CampoProcedural(funcao: Callable[..., float], *, nome: str = 'campo', metadados: Mapping[str, Any] \| None = None, dimensoes_min: int = 1, dimensoes_max: int \| None = None, intervalo: tuple[float, float] \| None = None)`

**Origem da implementação:** `coral.procedural`

**Arquivo na release:** `coral/procedural.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `funcao` | posicional |
| `nome` | nomeado |
| `metadados` | nomeado |
| `dimensoes_min` | nomeado |
| `dimensoes_max` | nomeado |
| `intervalo` | nomeado |

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `valor` | método | `valor(*coordenadas: float) -> float` |
| `transformar` | método | `transformar(funcao: Callable[[float], float], *, nome: str \| None = None, intervalo: tuple[float, float] \| None = None, operacao: str = 'transformar') -> 'CampoProcedural'` |
| `limitar` | método | `limitar(minimo: float, maximo: float) -> 'CampoProcedural'` |
| `normalizar` | método | `normalizar(origem_min: float, origem_max: float, destino_min: float = 0.0, destino_max: float = 1.0) -> 'CampoProcedural'` |
| `somar` | método | `somar(outro: 'CampoProcedural \| float') -> 'CampoProcedural'` |
| `multiplicar` | método | `multiplicar(outro: 'CampoProcedural \| float') -> 'CampoProcedural'` |
| `mascara` | método | `mascara(*, minimo: float \| None = None, maximo: float \| None = None, dentro: float = 1.0, fora: float = 0.0) -> 'CampoProcedural'` |

:::

#### `ReceitaProcedural`

Descrição portátil e reconstruível de uma operação procedural suportada.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `algoritmo` | Valor correspondente a algoritmo. | `str` | obrigatório |
| `semente_raiz` | Valor correspondente a semente raiz. | `Any` | `0` |
| `parametros` | Valor correspondente a parametros. | `Mapping[str, Any] \| None` | `None` |
| `versao_algoritmo` | Valor correspondente a versao algoritmo. | `int` | `VERSAO_RECEITA` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `contrato` | Executa a operação `contrato` disponibilizada por `coral.procedural`. | `str` |
| `parametros` | Executa a operação `parametros` disponibilizada por `coral.procedural`. | `dict[str, Any]` |
| `para_dados` | Converte o valor para dados. | `dict[str, Any]` |
| `para_json` | Converte o valor para JSON. | `str` |
| `de_dados` | Interpreta ou reconstrói um valor a partir de dados. | `'ReceitaProcedural'` |
| `de_json` | Interpreta ou reconstrói um valor a partir de JSON. | `'ReceitaProcedural'` |

:::details Detalhes técnicos

**Assinatura:** `ReceitaProcedural(algoritmo: str, *, semente_raiz: Any = 0, parametros: Mapping[str, Any] \| None = None, versao_algoritmo: int = VERSAO_RECEITA) -> None`

**Origem da implementação:** `coral.procedural`

**Arquivo na release:** `coral/procedural.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `algoritmo` | posicional |
| `semente_raiz` | nomeado |
| `parametros` | nomeado |
| `versao_algoritmo` | nomeado |

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `contrato` | propriedade | `contrato() -> str` |
| `parametros` | propriedade | `parametros() -> dict[str, Any]` |
| `para_dados` | método | `para_dados() -> dict[str, Any]` |
| `para_json` | método | `para_json(*, identar: int \| None = None) -> str` |
| `de_dados` | método | `de_dados(dados: Mapping[str, Any]) -> 'ReceitaProcedural'` |
| `de_json` | método | `de_json(texto: str) -> 'ReceitaProcedural'` |

:::

### Constantes e aliases

#### `CONTRATO`

Expõe a constante pública `CONTRATO`.

:::details Detalhes técnicos

**Assinatura:** `CONTRATO`

**Origem da implementação:** `coral.procedural`

**Arquivo na release:** `coral/procedural.py`

**Valor declarado:** `'coral.procedural/1'`

:::

#### `CONTRATO_RECEITA`

Expõe a constante pública `CONTRATO_RECEITA`.

:::details Detalhes técnicos

**Assinatura:** `CONTRATO_RECEITA`

**Origem da implementação:** `coral.procedural`

**Arquivo na release:** `coral/procedural.py`

**Valor declarado:** `'coral.procedural.receita/1'`

:::

<!-- /AUTO:API -->
