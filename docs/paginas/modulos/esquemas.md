# coral.esquemas

## Visão geral

`coral.esquemas` valida registros externos sem alterar os dados. Ele é útil quando CSV, JSON, formulários ou integrações entregam estruturas que precisam ser conferidas antes de entrar na lógica do programa.

<!-- AUTO:MODULO -->

**Importação:** `coral.esquemas`  
**Categoria:** dados  

validar registros externos sem coerção, distinguindo ausente e nulo

### Superfície pública detectada

`campo`, `esquema`, `validar_registro`, `validar_registros`

<!-- /AUTO:MODULO -->

## Conceitos principais

### Campo ausente não é o mesmo que nulo

Um campo está **ausente** quando a chave não existe. Um campo é **nulo** quando a chave existe com o valor `nulo`. As duas regras são configuradas separadamente por `obrigatorio` e `anulavel`.

Isso permite declarar um campo opcional que pode faltar mas não pode ser nulo, ou um campo obrigatório cuja chave deve existir mesmo quando o valor `nulo` é aceito.

### Validação não converte

O módulo aceita ou relata os valores recebidos. Ele não converte texto em número, não preenche valores padrão e não modifica o registro original. Quando a fonte contém números em texto, converta explicitamente antes da validação.

```coral
de coral.esquemas importe campo, esquema, validar_registro
de coral.conversoes importe inteiro

defina cadastro como esquema({"idade": campo("inteiro", minimo=0), "apelido": campo("texto", obrigatorio=falso)}, permitir_extras=falso)
defina bruto como {"idade": "18"}

mostre validar_registro(bruto, cadastro)["erros"][0]["regra"]

defina convertido como {"idade": inteiro(bruto["idade"])}
mostre validar_registro(convertido, cadastro)["valido"]
```

:::resultado
O primeiro resultado é `tipo`, porque `"18"` continua sendo texto. Depois da conversão explícita, o registro é válido.
:::

### Restrições de campo

`campo` pode combinar tipo, obrigatoriedade, nulidade, limites numéricos, limites de tamanho e uma coleção de valores permitidos. Limites numéricos são inclusivos. Inteiro recusa booleanos; decimal aceita números finitos e também recusa booleanos.

## Validar um registro

`validar_registro` retorna um relatório estruturado. Dados incompatíveis aparecem em `erros`; o valor original não é reescrito para tentar fazer a validação passar.

```coral
de coral.esquemas importe campo, esquema, validar_registro

defina pessoa como esquema({
    "nome": campo("texto", tamanho_minimo=1),
    "idade": campo("inteiro", minimo=0),
    "grupo": campo("texto", permitidos=["controle", "ensaio"])
}, permitir_extras=falso)

defina resultado como validar_registro({"nome": "Ana", "idade": 20, "grupo": "ensaio"}, pessoa)
mostre resultado["valido"]
```

:::resultado
O relatório informa verdadeiro em `valido` e não contém erros de campo.
:::

## Validar vários registros

`validar_registros` percorre um iterável em passagem única e guarda os erros encontrados, não uma cópia dos registros. `modo="primeiro"` interrompe no primeiro erro; `modo="coletar"` continua até o limite configurado.

O retorno informa `valido`, `erros`, `verificados` e `interrompido`. Cada erro pode registrar `campo`, `regra`, `mensagem`, índice do registro, linha lógica e origem fornecida pelo chamador.

A função não fecha iteradores de terceiros. Quando a entrada vem de `ler_csv` ou `ler_lotes_csv`, o bloco `com` continua pertencendo ao chamador.

## Quando usar

Use esquemas na fronteira entre dados externos e a lógica do programa: importadores, cadastros, configurações, pesquisas e inventários são casos típicos. Para dados já controlados internamente, tipos e invariantes do próprio domínio costumam ser mais diretos.

## API essencial

| Entrada | Papel |
|---|---|
| `campo` | descreve o contrato de um campo |
| `esquema` | reúne campos e define a política de chaves extras |
| `validar_registro` | valida um registro e produz relatório |
| `validar_registros` | valida uma sequência em passagem única |

## Erros comuns

* Esperar coerção automática de texto para número. Converta antes.
* Tratar campo ausente e `nulo` como a mesma situação.
* Confundir índice lógico de registro com linha física de um CSV que possui campos multilinha.
* Esquecer que limitar erros pode interromper o consumo antes do fim da entrada.
* Fechar no validador um leitor que pertence ao chamador. O ownership continua externo.

## Integração

`coral.esquemas` combina especialmente bem com `coral.arquivos`, `coral.conversoes` e `coral.json`. O projeto `Exemplos/Projetos/Importador_Validado/` mostra o fluxo completo: ler CSV, converter campos explicitamente, validar os registros e salvar um relatório JSON.

## Referência da API

<!-- AUTO:API -->

### Funções

#### `campo`

Define um campo: ausente depende de obrigatorio; nulo depende de anulavel.

**Exemplo**

```coral
de coral.esquemas importe campo, esquema, validar_registro
de coral.conversoes importe inteiro

defina cadastro como esquema({"idade": campo("inteiro", minimo=0), "apelido": campo("texto", obrigatorio=falso)}, permitir_extras=falso)
defina bruto como {"idade": "18"}

mostre validar_registro(bruto, cadastro)["erros"][0]["regra"]

defina convertido como {"idade": inteiro(bruto["idade"])}
mostre validar_registro(convertido, cadastro)["valido"]
```

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `tipo` | Tipo solicitado para o resultado, quando o módulo oferece essa escolha. | `str` | obrigatório |
| `obrigatorio` | Valor correspondente a obrigatorio. | `bool` | `True` |
| `anulavel` | Valor correspondente a anulavel. | `bool` | `False` |
| `minimo` | Limite mínimo considerado pela operação. | `int \| float \| None` | `None` |
| `maximo` | Limite máximo considerado pela operação. | `int \| float \| None` | `None` |
| `tamanho_minimo` | Valor correspondente a tamanho minimo. | `int \| None` | `None` |
| `tamanho_maximo` | Valor correspondente a tamanho maximo. | `int \| None` | `None` |
| `permitidos` | Valor correspondente a permitidos. | `Iterable \| None` | `None` |

**Retorno**

Retorna um valor declarado como `dict`.

:::details Detalhes técnicos

**Assinatura:** `campo(tipo: str, *, obrigatorio: bool = True, anulavel: bool = False, minimo: int \| float \| None = None, maximo: int \| float \| None = None, tamanho_minimo: int \| None = None, tamanho_maximo: int \| None = None, permitidos: Iterable \| None = None) -> dict`

**Origem da implementação:** `coral.stdlib.esquemas`

**Arquivo na release:** `coral/stdlib/esquemas.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `tipo` | posicional |
| `obrigatorio` | nomeado |
| `anulavel` | nomeado |
| `minimo` | nomeado |
| `maximo` | nomeado |
| `tamanho_minimo` | nomeado |
| `tamanho_maximo` | nomeado |
| `permitidos` | nomeado |

**Exceções diretamente observáveis no corpo:** `TypeError`, `ValueError`

:::

#### `esquema`

Copia campos declarados em ordem; extras são permitidos por padrão.

**Exemplo**

```coral
de coral.esquemas importe campo, esquema, validar_registro
de coral.conversoes importe inteiro

defina cadastro como esquema({"idade": campo("inteiro", minimo=0), "apelido": campo("texto", obrigatorio=falso)}, permitir_extras=falso)
defina bruto como {"idade": "18"}

mostre validar_registro(bruto, cadastro)["erros"][0]["regra"]

defina convertido como {"idade": inteiro(bruto["idade"])}
mostre validar_registro(convertido, cadastro)["valido"]
```

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `campos` | Valor correspondente a campos. | `Mapping[str, dict]` | obrigatório |
| `permitir_extras` | Controla se deve permitir extras. | `bool` | `True` |

**Retorno**

Retorna um valor declarado como `dict`.

:::details Detalhes técnicos

**Assinatura:** `esquema(campos: Mapping[str, dict], *, permitir_extras: bool = True) -> dict`

**Origem da implementação:** `coral.stdlib.esquemas`

**Arquivo na release:** `coral/stdlib/esquemas.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `campos` | posicional |
| `permitir_extras` | nomeado |

**Exceções diretamente observáveis no corpo:** `TypeError`, `ValueError`

:::

#### `validar_registro`

Valida sem converter: ausente e nulo têm regras diferentes.

**Exemplo**

```coral
de coral.esquemas importe campo, esquema, validar_registro
de coral.conversoes importe inteiro

defina cadastro como esquema({"idade": campo("inteiro", minimo=0), "apelido": campo("texto", obrigatorio=falso)}, permitir_extras=falso)
defina bruto como {"idade": "18"}

mostre validar_registro(bruto, cadastro)["erros"][0]["regra"]

defina convertido como {"idade": inteiro(bruto["idade"])}
mostre validar_registro(convertido, cadastro)["valido"]
```

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `registro` | Valor correspondente a registro. | `Mapping` | obrigatório |
| `esquema` | Valor correspondente a esquema. | `Mapping` | obrigatório |
| `indice` | Valor correspondente a indice. | `int` | `1` |
| `linha` | Valor correspondente a linha. | `int \| None` | `None` |
| `origem` | Origem usada pela operação. | `str \| None` | `None` |
| `modo` | Valor correspondente a modo. | `str` | `'coletar'` |
| `limite_erros` | Valor correspondente a limite erros. | `int` | `100` |

**Retorno**

Retorna um valor declarado como `dict`.

:::details Detalhes técnicos

**Assinatura:** `validar_registro(registro: Mapping, esquema: Mapping, *, indice: int = 1, linha: int \| None = None, origem: str \| None = None, modo: str = 'coletar', limite_erros: int = 100) -> dict`

**Origem da implementação:** `coral.stdlib.esquemas`

**Arquivo na release:** `coral/stdlib/esquemas.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `registro` | posicional |
| `esquema` | posicional |
| `indice` | nomeado |
| `linha` | nomeado |
| `origem` | nomeado |
| `modo` | nomeado |
| `limite_erros` | nomeado |

:::

#### `validar_registros`

Valida uma passagem, sem reter registros nem fechar o iterador do chamador.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `registros` | Valor correspondente a registros. | `Iterable[Mapping]` | obrigatório |
| `esquema` | Valor correspondente a esquema. | `Mapping` | obrigatório |
| `modo` | Valor correspondente a modo. | `str` | `'coletar'` |
| `limite_erros` | Valor correspondente a limite erros. | `int` | `100` |
| `linha_inicial` | Valor correspondente a linha inicial. | `int \| None` | `None` |
| `origem` | Origem usada pela operação. | `str \| None` | `None` |

**Retorno**

Retorna um valor declarado como `dict`.

:::details Detalhes técnicos

**Assinatura:** `validar_registros(registros: Iterable[Mapping], esquema: Mapping, *, modo: str = 'coletar', limite_erros: int = 100, linha_inicial: int \| None = None, origem: str \| None = None) -> dict`

**Origem da implementação:** `coral.stdlib.esquemas`

**Arquivo na release:** `coral/stdlib/esquemas.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `registros` | posicional |
| `esquema` | posicional |
| `modo` | nomeado |
| `limite_erros` | nomeado |
| `linha_inicial` | nomeado |
| `origem` | nomeado |

:::

<!-- /AUTO:API -->
