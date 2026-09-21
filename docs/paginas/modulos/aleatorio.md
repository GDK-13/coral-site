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

A documentação desta página descreve a superfície detectada na **Coral 1.5.9**. O gerador do site atualiza automaticamente o inventário e a referência da API quando uma nova release é importada, mas o texto pedagógico desta seção permanece sob revisão humana.

## Referência da API

<!-- AUTO:API -->

### Funções

#### `fonte(semente = None) -> FonteAleatoria`

Entrada pública `fonte` da superfície `coral.aleatorio`.

**Implementação:** `coral.stdlib.aleatorio`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `semente` | `não declarado` | `None` | posicional |

**Retorno:** `FonteAleatoria`

#### `inteiro(minimo, maximo, *, fonte: FonteAleatoria | None = None)`

Entrada pública `inteiro` da superfície `coral.aleatorio`.

**Implementação:** `coral.stdlib.aleatorio`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `minimo` | `não declarado` | obrigatório | posicional |
| `maximo` | `não declarado` | obrigatório | posicional |
| `fonte` | `FonteAleatoria \| None` | `None` | nomeado |

**Retorno:** `não declarado`

#### `decimal(minimo = 0.0, maximo = 1.0, *, fonte: FonteAleatoria | None = None)`

Entrada pública `decimal` da superfície `coral.aleatorio`.

**Implementação:** `coral.stdlib.aleatorio`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `minimo` | `não declarado` | `0.0` | posicional |
| `maximo` | `não declarado` | `1.0` | posicional |
| `fonte` | `FonteAleatoria \| None` | `None` | nomeado |

**Retorno:** `não declarado`

#### `escolher(valores, *, fonte: FonteAleatoria | None = None)`

Entrada pública `escolher` da superfície `coral.aleatorio`.

**Implementação:** `coral.stdlib.aleatorio`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `valores` | `não declarado` | obrigatório | posicional |
| `fonte` | `FonteAleatoria \| None` | `None` | nomeado |

**Retorno:** `não declarado`

#### `amostra(valores, quantidade, *, fonte: FonteAleatoria | None = None)`

Entrada pública `amostra` da superfície `coral.aleatorio`.

**Implementação:** `coral.stdlib.aleatorio`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `valores` | `não declarado` | obrigatório | posicional |
| `quantidade` | `não declarado` | obrigatório | posicional |
| `fonte` | `FonteAleatoria \| None` | `None` | nomeado |

**Retorno:** `não declarado`

#### `escolha_ponderada(valores, pesos, *, fonte: FonteAleatoria | None = None)`

Entrada pública `escolha_ponderada` da superfície `coral.aleatorio`.

**Implementação:** `coral.stdlib.aleatorio`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `valores` | `não declarado` | obrigatório | posicional |
| `pesos` | `não declarado` | obrigatório | posicional |
| `fonte` | `FonteAleatoria \| None` | `None` | nomeado |

**Retorno:** `não declarado`

**Exceções observáveis no corpo:** `ValueError`

#### `embaralhar(valores, *, fonte: FonteAleatoria | None = None)`

Entrada pública `embaralhar` da superfície `coral.aleatorio`.

**Implementação:** `coral.stdlib.aleatorio`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `valores` | `não declarado` | obrigatório | posicional |
| `fonte` | `FonteAleatoria \| None` | `None` | nomeado |

**Retorno:** `não declarado`

### Classes e protocolos

#### `FonteAleatoria(semente: Any = None)`

Fonte reproduzível quando criada com semente explícita.

**Implementação:** `coral.stdlib.aleatorio`

**Atributos declarados**

| Nome | Tipo | Padrão |
|---|---|---|
| `semente` | `Any` | `None` |

**Métodos e propriedades públicas**

| Nome | Tipo | Assinatura | Retorno | Descrição |
|---|---|---|---|---|
| `inteiro` | método | `inteiro(minimo, maximo)` | `não declarado` | Sem docstring própria na release. |
| `decimal` | método | `decimal(minimo = 0.0, maximo = 1.0)` | `não declarado` | Sem docstring própria na release. |
| `escolher` | método | `escolher(valores)` | `não declarado` | Sem docstring própria na release. |
| `amostra` | método | `amostra(valores, quantidade)` | `não declarado` | Sem docstring própria na release. |
| `escolha_ponderada` | método | `escolha_ponderada(valores, pesos)` | `não declarado` | Sem docstring própria na release. |
| `embaralhar` | método | `embaralhar(valores)` | `não declarado` | Sem docstring própria na release. |

<!-- /AUTO:API -->
