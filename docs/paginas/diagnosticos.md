# Diagnósticos

Desde a Coral 1.7.2, a linguagem usa uma classificação comum para erros de execução no terminal e no depurador. O objetivo é mostrar o problema em termos úteis para quem escreveu o programa sem apagar a mensagem nem a causa técnica original.

## O que um diagnóstico informa

Um diagnóstico de execução pode trazer:

* código estável, como `R102`;
* categoria, como `conversao`, `arquivo` ou `tipo`;
* mensagem original da exceção;
* fonte e linha Coral quando o mapa de linhas permite localizar o erro;
* sugestão curta para corrigir ou investigar o problema;
* detalhes técnicos, incluindo o tipo da exceção, linha Python e cadeia de causas.

## Códigos de execução

| Código | Categoria | Situação classificada | Sugestão principal |
|---|---|---|---|
| `R100` | entrada | erro de entrada | verificar a fonte e a mensagem de leitura |
| `R101` | entrada | fim da fonte de entrada | verificar se existe outra linha antes de ler novamente |
| `R102` | conversão | falha em `coral.conversoes` | conferir a representação ou fornecer padrão explícito |
| `R110` | arquivo | arquivo não encontrado | conferir caminho e existência |
| `R111` | arquivo | permissão negada | conferir permissões do arquivo e da pasta |
| `R112` | arquivo | outra falha de arquivo ou sistema | conferir caminho e operação solicitada |
| `R120` | formato | formato, JSON ou codificação inválida | conferir formato dos dados e codificação |
| `R130` | operação | recurso necessário indisponível ou operação Coral inválida | conferir os recursos exigidos pela operação |
| `R201` | aritmética | divisão por zero | conferir se o divisor é diferente de zero |
| `R202` | valor | valor não aceito | conferir os valores aceitos pela operação |
| `R203` | tipo | tipo ou argumentos incompatíveis | conferir tipos e argumentos |
| `R204` | acesso | índice ou chave ausente | conferir a coleção antes do acesso |
| `R205` | nome | nome não definido | definir ou importar o nome antes do uso |
| `R001` | execução | erro não classificado nas categorias acima | conferir a operação e consultar os detalhes técnicos |

## Exemplo com conversão

```coral
defina idade como converta "dezoito" para inteiro
```

:::resultado
A conversão inválida é classificada como `R102`, na categoria de conversão. A mensagem original é preservada e o diagnóstico sugere conferir a representação de inteiro ou usar um valor padrão quando isso fizer sentido.
:::

Uma alternativa explícita quando existe um padrão legítimo é:

```coral
defina idade como tente converter "dezoito" para inteiro, senão nulo
```

## Localização na fonte Coral

O runtime usa os mapas de linhas gerados pela compilação para relacionar a exceção ao código Coral. Frames de bibliotecas externas não recebem uma linha Coral apenas porque o número coincide. Em projetos, mapas persistidos permitem localizar o módulo Coral mais profundo envolvido na falha.

## Terminal e VS Code

A classificação é compartilhada entre terminal e depurador. No DAP, o diagnóstico estruturado adicional fica em `exceptionInfo.details.diagnostico`.

No uso cotidiano, leia primeiro código, categoria, mensagem e sugestão. Os detalhes técnicos são úteis quando você precisa investigar integração, extensão ou uma causa encadeada.

:::referencia

## Estrutura técnica

O diagnóstico de execução preserva os campos `codigo`, `linha_coral`, `tipo_erro`, `mensagem`, `linha_python`, `categoria`, `sugestao`, `fonte` e `causas`. O domínio é `runtime`.

As causas são coletadas sem repetir objetos já visitados e preservam tipo e mensagem de cada exceção encadeada.

:::
