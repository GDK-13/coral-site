# coral.aleatorio

## Visão geral

`coral.aleatorio` oferece aleatoriedade reproduzível e simulação. Use quando um programa precisa de sorteios, amostras ou simulações reproduzíveis. Uma fonte com semente fixa é especialmente útil em testes.

<!-- AUTO:MODULO -->

**Importação:** `coral.aleatorio`  
**Categoria:** simulacao  

aleatoriedade reproduzível e simulação

> Aviso: Não usar para senhas, chaves, tokens ou outros segredos.

### Superfície pública detectada

`FonteAleatoria`, `fonte`, `inteiro`, `decimal`, `escolher`, `amostra`, `escolha_ponderada`, `embaralhar`

<!-- /AUTO:MODULO -->

## Papel no ecossistema

É a fonte comum de aleatoriedade da biblioteca padrão. A separação entre funções de conveniência e `FonteAleatoria` permite escolher entre uso rápido e controle explícito do estado pseudoaleatório.

## Conceitos principais

### Fonte reproduzível

`fonte(semente)` cria um gerador independente. Com a mesma semente e a mesma sequência de chamadas, ele é apropriado para testes, simulações e geração procedural reproduzível.

### Sorteio, amostra e embaralhamento

`escolher` seleciona um elemento, `amostra` seleciona vários, `embaralhar` reorganiza valores e `escolha_ponderada` permite pesos explícitos.

### Aleatoriedade numérica

`inteiro` trabalha com limites inteiros e `decimal` produz valores em intervalo decimal. As mesmas operações também existem como métodos de `FonteAleatoria`.

## Quando usar

Use este módulo quando o problema corresponder diretamente aos conceitos acima. Por ser um módulo complementar, ele normalmente entra em um programa para resolver uma responsabilidade específica e deve permanecer desacoplado da lógica central sempre que possível.

## Começando

A release inclui um exemplo real em `Exemplos/Dados/03_aleatorio_e_persistencia.coral`:

```coral
# Aleatoriedade reproduzível e persistência portátil.
de coral.aleatorio importe fonte
de coral.persistencia importe salvar, carregar

defina gerador_a como fonte(42)
defina gerador_b como fonte(42)
defina primeiro como gerador_a.inteiro(1, 100)
defina segundo como gerador_b.inteiro(1, 100)
garanta que primeiro for igual a segundo

defina dados como {"ponto": (3, 4), "tags": {"a", "b"}}
```

## API essencial

| Entrada | Papel |
|---|---|
| `fonte` | criar uma fonte reproduzível |
| `inteiro` | sortear inteiro em intervalo |
| `decimal` | sortear decimal em intervalo |
| `escolher` | escolher um elemento |
| `amostra` | selecionar vários elementos |
| `escolha_ponderada` | sortear com pesos |
| `embaralhar` | reordenar valores |

A seção **Referência da API** no fim desta página contém a superfície pública completa detectada na release, com assinaturas, parâmetros, retornos e docstrings quando presentes.

## Fluxos comuns

1. Para testes, crie a fonte com semente fixa e passe a mesma fonte às operações relacionadas.
2. Para geração procedural, mantenha a fonte junto do estado da simulação para evitar sorteios escondidos em pontos diferentes do programa.
3. Para sorteios com chances diferentes, valide se valores e pesos representam a mesma população antes de chamar `escolha_ponderada`.

## Erros e casos de borda

Uma população vazia, uma quantidade de amostra incompatível ou pesos inválidos podem produzir erro operacional. A referência automática abaixo registra exceções diretamente observáveis no corpo das funções quando a release as expõe.

## Boas práticas

* Use sementes explícitas em testes.
* Compartilhe uma `FonteAleatoria` quando várias decisões pertencem à mesma sequência pseudoaleatória.
* Não use este módulo para segredos, tokens ou material criptográfico.

## Integração com outros módulos

`coral.persistencia` pode guardar dados produzidos por simulações; `coral.mundo` e `coral.rpg` podem usar a fonte para geração procedural; `coral.criptografia` é a escolha apropriada quando a aleatoriedade precisa ser segura.

## Testabilidade e previsibilidade

Reprodutibilidade é a principal ferramenta de teste deste módulo. Um caso que falha com uma semente conhecida deve poder ser repetido com a mesma semente.

## Compatibilidade e evolução

A documentação desta página descreve a superfície detectada na **Coral 1.5.12**. O gerador do site atualiza automaticamente o inventário e a referência da API quando uma nova release é importada, mas o texto pedagógico desta seção permanece sob revisão humana.

## Referência da API

<!-- AUTO:API -->

### Funções

#### `fonte`

Criar uma fonte reproduzível.

**Exemplo**

```coral
de coral.persistencia importe salvar, carregar

defina gerador_a como fonte(42)
defina gerador_b como fonte(42)
defina primeiro como gerador_a.inteiro(1, 100)
defina segundo como gerador_b.inteiro(1, 100)
```

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `semente` | Semente usada para tornar a sequência reproduzível. | `não declarado` | `None` |

**Retorno**

Retorna a fonte de aleatoriedade criada.

:::details Detalhes técnicos

**Assinatura:** `fonte(semente = None) -> FonteAleatoria`

**Origem da implementação:** `coral.stdlib.aleatorio`

**Arquivo na release:** `coral/stdlib/aleatorio.py`

:::

#### `inteiro`

Sortear inteiro em intervalo.

**Exemplo**

```coral
defina gerador_a como fonte(42)
defina gerador_b como fonte(42)
defina primeiro como gerador_a.inteiro(1, 100)
defina segundo como gerador_b.inteiro(1, 100)
garanta que primeiro for igual a segundo
```

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `minimo` | Limite mínimo considerado pela operação. | `não declarado` | obrigatório |
| `maximo` | Limite máximo considerado pela operação. | `não declarado` | obrigatório |
| `fonte` | Fonte explícita usada pela operação; quando omitida, vale o comportamento padrão do módulo. | `FonteAleatoria \| None` | `None` |

**Retorno**

Retorna o número inteiro sorteado.

:::details Detalhes técnicos

**Assinatura:** `inteiro(minimo, maximo, *, fonte: FonteAleatoria \| None = None)`

**Origem da implementação:** `coral.stdlib.aleatorio`

**Arquivo na release:** `coral/stdlib/aleatorio.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `minimo` | posicional |
| `maximo` | posicional |
| `fonte` | nomeado |

:::

#### `decimal`

Sortear decimal em intervalo.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `minimo` | Limite mínimo considerado pela operação. | `não declarado` | `0.0` |
| `maximo` | Limite máximo considerado pela operação. | `não declarado` | `1.0` |
| `fonte` | Fonte explícita usada pela operação; quando omitida, vale o comportamento padrão do módulo. | `FonteAleatoria \| None` | `None` |

**Retorno**

Retorna o número decimal sorteado.

:::details Detalhes técnicos

**Assinatura:** `decimal(minimo = 0.0, maximo = 1.0, *, fonte: FonteAleatoria \| None = None)`

**Origem da implementação:** `coral.stdlib.aleatorio`

**Arquivo na release:** `coral/stdlib/aleatorio.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `minimo` | posicional |
| `maximo` | posicional |
| `fonte` | nomeado |

:::

#### `escolher`

Escolher um elemento.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valores` | Coleção de valores processada. | `não declarado` | obrigatório |
| `fonte` | Fonte explícita usada pela operação; quando omitida, vale o comportamento padrão do módulo. | `FonteAleatoria \| None` | `None` |

**Retorno**

Retorna um dos valores fornecidos.

:::details Detalhes técnicos

**Assinatura:** `escolher(valores, *, fonte: FonteAleatoria \| None = None)`

**Origem da implementação:** `coral.stdlib.aleatorio`

**Arquivo na release:** `coral/stdlib/aleatorio.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `valores` | posicional |
| `fonte` | nomeado |

:::

#### `amostra`

Selecionar vários elementos.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valores` | Coleção de valores processada. | `não declarado` | obrigatório |
| `quantidade` | Quantidade de itens solicitada. | `não declarado` | obrigatório |
| `fonte` | Fonte explícita usada pela operação; quando omitida, vale o comportamento padrão do módulo. | `FonteAleatoria \| None` | `None` |

**Retorno**

Retorna a amostra selecionada.

:::details Detalhes técnicos

**Assinatura:** `amostra(valores, quantidade, *, fonte: FonteAleatoria \| None = None)`

**Origem da implementação:** `coral.stdlib.aleatorio`

**Arquivo na release:** `coral/stdlib/aleatorio.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `valores` | posicional |
| `quantidade` | posicional |
| `fonte` | nomeado |

:::

#### `escolha_ponderada`

Sortear com pesos.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valores` | Coleção de valores processada. | `não declarado` | obrigatório |
| `pesos` | Pesos associados aos valores usados na escolha. | `não declarado` | obrigatório |
| `fonte` | Fonte explícita usada pela operação; quando omitida, vale o comportamento padrão do módulo. | `FonteAleatoria \| None` | `None` |

**Retorno**

Retorna o valor escolhido segundo os pesos.

:::details Detalhes técnicos

**Assinatura:** `escolha_ponderada(valores, pesos, *, fonte: FonteAleatoria \| None = None)`

**Origem da implementação:** `coral.stdlib.aleatorio`

**Arquivo na release:** `coral/stdlib/aleatorio.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `valores` | posicional |
| `pesos` | posicional |
| `fonte` | nomeado |

**Exceções diretamente observáveis no corpo:** `ValueError`

:::

#### `embaralhar`

Reordenar valores.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `valores` | Coleção de valores processada. | `não declarado` | obrigatório |
| `fonte` | Fonte explícita usada pela operação; quando omitida, vale o comportamento padrão do módulo. | `FonteAleatoria \| None` | `None` |

**Retorno**

Retorna o resultado produzido pela operação; o tipo não é declarado pela release.

:::details Detalhes técnicos

**Assinatura:** `embaralhar(valores, *, fonte: FonteAleatoria \| None = None)`

**Origem da implementação:** `coral.stdlib.aleatorio`

**Arquivo na release:** `coral/stdlib/aleatorio.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `valores` | posicional |
| `fonte` | nomeado |

:::

### Classes e protocolos

#### `FonteAleatoria`

Fonte reproduzível quando criada com semente explícita.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `semente` | Semente usada para tornar a sequência reproduzível. | `Any` | `None` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `semente` | Semente usada para tornar a sequência reproduzível. | `Any` | `None` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `inteiro` | Sortear inteiro em intervalo. | `não declarado` |
| `decimal` | Sortear decimal em intervalo. | `não declarado` |
| `escolher` | Escolher um elemento. | `não declarado` |
| `amostra` | Selecionar vários elementos. | `não declarado` |
| `escolha_ponderada` | Sortear com pesos. | `não declarado` |
| `embaralhar` | Reordenar valores. | `não declarado` |

:::details Detalhes técnicos

**Assinatura:** `FonteAleatoria(semente: Any = None)`

**Origem da implementação:** `coral.stdlib.aleatorio`

**Arquivo na release:** `coral/stdlib/aleatorio.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `inteiro` | método | `inteiro(minimo, maximo)` |
| `decimal` | método | `decimal(minimo = 0.0, maximo = 1.0)` |
| `escolher` | método | `escolher(valores)` |
| `amostra` | método | `amostra(valores, quantidade)` |
| `escolha_ponderada` | método | `escolha_ponderada(valores, pesos)` |
| `embaralhar` | método | `embaralhar(valores)` |

:::

<!-- /AUTO:API -->
