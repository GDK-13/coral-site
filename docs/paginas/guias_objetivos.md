# O que você quer fazer?

Esta página parte do problema que você quer resolver e aponta para a parte certa da Coral. Use estes guias como porta de entrada. Quando precisar de assinaturas, parâmetros e detalhes completos, siga o link do módulo relacionado.

## Entrada e dados

### Receber uma linha digitada pelo usuário

**Nível:** iniciante  
**Módulo:** [`coral.entrada`](modulos/entrada.html)

```coral
de coral.entrada importe ler_linha

defina nome como ler_linha("Seu nome: ")
mostre nome
```

:::resultado
O programa pede uma linha e depois mostra exatamente o texto recebido. A origem da entrada também pode ser substituída em testes.
:::

### Converter texto para um valor explícito

**Nível:** iniciante  
**Módulo:** [`coral.conversoes`](modulos/conversoes.html)

```coral
de coral.conversoes importe inteiro

defina quantidade como inteiro("12")
mostre quantidade
```

:::resultado
`quantidade` passa a representar o inteiro `12`. Entradas incompatíveis seguem o contrato de erro de conversão do módulo.
:::

### Limpar e transformar texto

**Nível:** iniciante  
**Módulo:** [`coral.texto`](modulos/texto.html)

```coral
de coral.texto importe aparar, maiusculas

defina nome como aparar("  coral  ")
mostre maiusculas(nome)
```

:::resultado
A saída textual é `CORAL`.
:::

## Arquivos e persistência

### Ler um arquivo de texto

**Nível:** iniciante  
**Módulo:** [`coral.arquivos`](modulos/arquivos.html)

```coral
de coral.arquivos importe ler_texto

defina conteudo como ler_texto("notas.txt")
mostre conteudo
```

:::resultado
`conteudo` recebe o texto armazenado em `notas.txt`. O caminho precisa existir e estar acessível ao programa.
:::

### Escrever dados em JSON

**Nível:** iniciante  
**Módulo:** [`coral.json`](modulos/json.html)

```coral
de coral.json importe escrever_json

defina perfil como {"nome": "Lia", "nivel": 3}
escrever_json("perfil.json", perfil)
```

:::resultado
O arquivo `perfil.json` é criado ou atualizado com uma representação JSON do valor informado.
:::

### Salvar estado portável

**Nível:** intermediário  
**Módulo:** [`coral.persistencia`](modulos/persistencia.html)

```coral
de coral.persistencia importe salvar

defina estado como {"fase": 4, "pontos": 180}
salvar(estado, "estado.coral.json")
```

:::resultado
O estado é convertido para a representação persistente suportada pelo módulo e gravado no caminho indicado.
:::

### Consultar a política do formato persistente

**Nível:** intermediário  
**Módulo:** [`coral.persistencia`](modulos/persistencia.html)

```coral
de coral.persistencia importe politica_persistencia

defina politica como politica_persistencia()
mostre politica
```

:::resultado
A política informa o contrato persistente corrente, as versões que podem ser lidas, a versão usada para escrita e a estratégia declarada para esquemas desconhecidos. Na Coral 1.6.0, a escrita usa o esquema `1` e a leitura aceita o esquema `1`.
:::

## Aleatoriedade e geração

### Sortear um item

**Nível:** iniciante  
**Módulo:** [`coral.aleatorio`](modulos/aleatorio.html)

```coral
de coral.aleatorio importe escolher

defina premio como escolher(["moeda", "poção", "mapa"])
mostre premio
```

:::resultado
A saída será um dos três valores da coleção. Quando você precisar repetir o mesmo resultado, use uma fonte aleatória com semente controlada.
:::

### Gerar conteúdo de forma reproduzível

**Nível:** intermediário  
**Módulo:** [`coral.procedural`](modulos/procedural.html)

```coral
de coral.procedural importe GeradorProcedural

defina gerador como GeradorProcedural(42)
```

:::resultado
O gerador é criado a partir da semente `42`. Usar a mesma semente e o mesmo fluxo de operações permite reproduzir a geração.
:::

## Mundo, regras e RPG

### Criar um mundo com entidades relacionadas

**Nível:** intermediário  
**Módulo:** [`coral.mundo`](modulos/mundo.html)

```coral
crie um mundo chamado campanha com nome "Campanha"
crie uma entidade chamada vila no mundo campanha
crie uma entidade chamada bosque no mundo campanha
relacione vila com bosque como "estrada" no mundo campanha
```

:::resultado
O mundo `campanha` passa a conter as entidades `vila` e `bosque`, ligadas pela relação `estrada`.
:::

### Criar um personagem de RPG

**Nível:** iniciante  
**Módulo:** [`coral.rpg`](modulos/rpg.html)

```coral
crie um mundo chamado campanha com nome "Campanha"
crie um personagem chamado heroina no mundo campanha com 12 de vida
```

:::resultado
O mundo recebe uma personagem chamada `heroina` com vida inicial `12`.
:::

### Reagir a uma condição com uma regra

**Nível:** intermediário  
**Módulo:** [`coral.regras`](modulos/regras.html)

```coral
defina vida como 10
defina estado como "normal"

regra "ferido" quando vida for menor ou igual a 5 então
    defina estado como "ferido"
fim
```

:::resultado
Quando a regra for avaliada com `vida` menor ou igual a `5`, o estado passa a ser `ferido`.
:::

## Jogos e apresentação

### Criar um jogo testável sem abrir janela

**Nível:** intermediário  
**Módulo:** [`coral.jogos`](modulos/jogos.html)

```coral
de coral.jogos importe criar_jogo, BackendNulo

defina jogo como criar_jogo("Teste", backend=BackendNulo())
```

:::resultado
O objeto de jogo usa um backend sem janela, adequado para lógica e testes automatizados de apresentação e entrada.
:::

### Fazer uma câmera seguir um alvo

**Nível:** intermediário  
**Módulo:** [`coral.jogos`](modulos/jogos.html#camera-e-efeitos-temporarios)

```coral
de coral.jogos importe Camera, Sprite

defina camera como Camera(0, 0, 320, 180)
defina heroi como Sprite(100, 80, 16, 16)
execute camera.seguir(heroi, constante_tempo=0.25)
```

:::resultado
A câmera passa a usar `heroi` como alvo de seguimento e aplica a suavização configurada durante as atualizações.
:::

## Simulação

### Criar uma simulação independente da interface

**Nível:** intermediário  
**Módulo:** [`coral.simulacao`](modulos/simulacao.html)

```coral
de coral.simulacao importe criar_simulacao

defina simulacao como criar_simulacao()
```

:::resultado
Uma instância de simulação é criada para coordenar tempo e sistemas sem exigir uma interface gráfica.
:::

## Como continuar

Se o guia resolveu sua dúvida inicial, abra o módulo relacionado e use o **Modo Aprender** para entender os conceitos ou o **Modo Referência** para consultar diretamente a API. A busca global continua sendo a melhor opção quando você já conhece o nome de uma função, classe ou conceito.
