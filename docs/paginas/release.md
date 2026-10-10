# Notas de versão

Esta página reúne mudanças de compatibilidade, sintaxe, ferramentas e distribuição relevantes para quem usa a Coral. O histórico interno de desenvolvimento não faz parte do site público.

## Versão atual

<!-- AUTO:VERSAO_NOTAS -->

**Coral:** `1.8.0`  
**Coral Language:** `0.83.0`  
**Livro Oficial:** `1.8.0`

<!-- /AUTO:VERSAO_NOTAS -->

## Coral 1.8.0

### Guia canônico de escrita

A 1.8.0 promove o guia de escrita da Coral. Ele recomenda nomes que indiquem intenção, imports públicos explícitos, quatro espaços por nível, `fim` alinhado com a construção correspondente e escolha consciente entre formas compactas e multilinha. Essas recomendações orientam legibilidade e manutenção; não são uma nova sintaxe.

A documentação do site ganhou a página **Estilo e legibilidade**, e a coleção do Livro 1.8.0 incorpora as mesmas orientações.

### Referência e aplicações

A coleção do Livro 1.8.0 amplia a referência das funções e classes públicas e mantém exemplos verificados contra o runtime corrente. A distribuição também consolida três aplicações de referência: catálogo SQLite validado, análise de CSV com estatística e automação de arquivos com concorrência controlada.

### Distribuição

* Runtime portátil: `coral-1.8.0.pyz`.
* Extensão: `coral-language-0.83.0.vsix`.
* Livro Oficial: coleção `1.8.0` em dois volumes.
* A integração opcional do desktop Linux pode ser administrada pelo subcomando `coral desktop`.

## Coral 1.7.11

### Integração opcional do desktop Linux

A 1.7.11 adiciona `coral desktop instalar`, `status` e `remover`. A integração registra `*.coral` e o nome exato `coral.toml` com tipos MIME e ícones da Coral, sem escolher aplicativo padrão e sem associar todos os arquivos TOML.

A remoção é conservadora: arquivos de terceiros ou arquivos modificados depois da instalação são preservados.

### Aplicações integradas

Três projetos em `Exemplos/Projetos` mostram composição de recursos públicos: catálogo SQLite, análise de CSV e automação de arquivos. Eles separam núcleo reutilizável da entrada da aplicação e documentam entradas, saídas e dependências opcionais.

## Coral 1.7.10

### Concorrência controlada

`coral.assincrono` passa a oferecer `FilaTarefas`, `ResultadoTarefa`, `ProgressoTarefas`, `RelatorioTarefas`, `executar_bloqueante` e `executar_fila`. A fila limita simultaneidade e capacidade, permite políticas de falha, timeout por tarefa ou por grupo, cancelamento cooperativo e acompanhamento de progresso.

`grupo_tarefas`, `aguardar_com_timeout` e `cancelar_tarefa` permanecem disponíveis. O novo fluxo é indicado quando o programa precisa de sucesso parcial, limite explícito de tarefas ativas ou relatório estruturado.

## Coral 1.7.9

### SQLite local

A 1.7.9 adiciona `coral.sqlite` para persistência local com SQL explícito. `abrir` cria uma `Conexao`, consultas devolvem registros como dicionários e as alterações podem ser confirmadas ou revertidas explicitamente. A API também oferece transação contextual, sem criar aninhamento ou savepoints implícitos.

Valores devem ser enviados separadamente do SQL por parâmetros. Parâmetros representam valores e não substituem nomes de tabelas, colunas ou fragmentos arbitrários de consulta.

### Textos multilinha

Textos podem ser delimitados por três aspas duplas ou três aspas simples. Quando o corpo começa na linha seguinte, a quebra inicial é estrutural e o recuo comum é removido. O recurso é geral e não interpreta automaticamente SQL, HTML, Markdown ou qualquer outro conteúdo incorporado.

### Editor e distribuição

Coral Language `0.80.0` reconhece o novo literal como string opaca e preserva os mapas de linha. O Livro Oficial 1.7.9 incorpora SQLite e textos multilinha nos dois volumes.

* Runtime portátil: `coral-1.7.9.pyz`.
* Extensão: `coral-language-0.80.0.vsix`.
* Livro Oficial: coleção `1.7.9` em dois volumes.

## Coral 1.7.8

### Validação declarativa de dados externos

A 1.7.8 adiciona `coral.esquemas`, uma API explícita para validar registros sem converter ou preencher valores automaticamente. `campo` descreve restrições, `esquema` reúne os campos e `validar_registro` ou `validar_registros` produzem relatórios estruturados.

A validação distingue **campo ausente** de **campo presente com `nulo`**. Isso permite declarar, por exemplo, um campo opcional que ainda assim recusa `nulo`, ou um campo obrigatório que aceita `nulo` quando estiver presente. Limites numéricos são inclusivos e valores inválidos são relatados sem alterar a entrada.

O projeto `Exemplos/Projetos/Importador_Validado/` combina CSV gradual, conversão explícita e esquemas para gerar um relatório JSON com origem, índice lógico, regra e mensagem de cada problema.

### Distribuição

* Runtime portátil: `coral-1.7.8.pyz`.
* Extensão: `coral-language-0.79.0.vsix`.
* Livro Oficial: coleção `1.7.8` em dois volumes.
* Linux permanece como plataforma autoritativa desta distribuição.

## Coral 1.7.7

### Leitura e escrita graduais

`coral.arquivos` passa a oferecer `ler_linhas`, `ler_csv`, `ler_lotes_csv`, `escrever_linhas` e `escrever_csv`. Essas operações trabalham gradualmente com os dados, evitando materializar um arquivo inteiro quando o programa só precisa percorrê lo ou transformá lo em sequência.

Os leitores são de passagem única e fecham o arquivo ao chegar ao fim ou diante de erro. Quando o programa interrompe a leitura antes do fim, use `com` ou feche o leitor explicitamente. O CSV é estrito: cabeçalhos precisam ser coerentes, registros precisam manter a largura esperada e a biblioteca não converte campos silenciosamente.

O projeto `Exemplos/Projetos/Importador_Gradual/` demonstra leitura em lotes, filtro e escrita CSV preservando o benefício de memória limitada.

### Distribuição

* Runtime portátil: `coral-1.7.7.pyz`.
* Extensão: `coral-language-0.78.0.vsix`.
* A coleção do Livro foi atualizada para acompanhar a edição.

## Coral 1.7.6

### Cabeçalhos multilinha

Declarações longas podem distribuir parâmetros de função, imports e bases de herança em várias linhas. A estrutura continua explícita: `fim com` encerra a lista de parâmetros e `fim herança` encerra a lista de bases.

```coral
crie a função somar com
    primeiro do tipo inteiro
    segundo do tipo inteiro opcional 2
fim com retornando inteiro
    retorne primeiro mais segundo
fim
```

Imports também podem listar um símbolo por linha, inclusive com aliases, e herança múltipla pode listar uma base por linha.

### Ambientes de projeto reproduzíveis

Projetos podem declarar requisitos de Python e dependências em `coral.toml`, resolver versões para um `coral.lock` e preparar uma geração isolada em `.coral/ambientes`. A resolução é offline por padrão, aceita wheels e não instala dependências no Python global.

A execução de projeto usa o ambiente associado ao lock quando o projeto adota esse fluxo. Se o ambiente estiver ausente ou incompatível, a Coral informa o problema em vez de continuar silenciosamente com outro ambiente.

`Exemplos/Projetos/Ambiente_Reproduzivel/` demonstra o fluxo completo sem depender de um registro remoto.

### Distribuição

* Runtime portátil: `coral-1.7.6.pyz`.
* Extensão: `coral-language-0.77.0.vsix`.
* Linux é a plataforma qualificada para esse fluxo.

## Coral 1.7.5

### Consultas naturais de classe

`valor for do tipo Classe` passa a consultar diretamente classes definidas pelo programa, incluindo ancestrais por herança simples ou múltipla. A forma negativa `valor não for do tipo Classe` segue o mesmo contrato, e `e_tipo(valor, Classe)` continua disponível para código existente e usos dinâmicos.

Imports, aliases e referências qualificadas como `modelos.Animal` obedecem ao escopo normal. O editor completa classes depois de `do tipo`, e os diagnósticos `T206` e `T207` ajudam a distinguir um nome que não é tipo de um tipo inexistente.

### Chamadas explícitas multilinha

Chamadas longas podem usar `com` no fim da linha, um argumento completo por linha e `fim` para encerrar a chamada. Chamadas aninhadas possuem seu próprio fechamento. Comentários e linhas vazias são ignorados como argumentos, enquanto argumentos nomeados e expansões preservam seus contratos.

```coral
defina celula como chame Celula com
    chame Onivoro
fim
```

O formatador e a ajuda de assinatura do VS Code acompanham a nova forma.

### Editor e projetos

Coral Language `0.76.0` separa o estado dos documentos abertos, snapshots de análise e o índice seletivo do projeto. A fonte aberta no editor prevalece sobre o disco, versões obsoletas são ignoradas e mudanças de interface atualizam os consumidores afetados sem exigir reanalisar indiscriminadamente todo o workspace.

### Livro Oficial

O Livro Oficial 1.7.5 passa a ser uma coleção em dois volumes. O **Volume I — Linguagem e Desenvolvimento** é voltado à aprendizagem e ao uso prático; o **Volume II — Referência e Arquitetura** concentra consulta técnica e arquitetura. Ambos estão disponíveis em PDF e em leitura HTML local.

### Exemplos e distribuição

A distribuição acrescenta `Exemplos/Analise_1_7_5/Ecossistema/`, com classes, herança múltipla, consultas naturais de classe, chamada explícita multilinha e testes.

* Runtime portátil: `coral-1.7.5.pyz`.
* Extensão: `coral-language-0.76.0.vsix`.
* Livro Oficial: coleção `1.7.5` em dois volumes.
* Linux permanece como plataforma autoritativa desta distribuição.

## Coral 1.7.4

### Editor semântico

Coral Language `0.75.2` amplia a identificação contextual dos símbolos. Classes, tipos nativos, funções, métodos, parâmetros, propriedades, variáveis e módulos podem receber categorias semânticas diferentes quando o papel da ocorrência é comprovado. O tema do VS Code continua responsável pelas cores.

TextMate permanece como fallback quando o LSP ainda não possui contexto suficiente ou o documento está incompleto.

### Análise entre módulos

Interfaces públicas de módulo passam a carregar assinaturas, retornos, classes, membros, imports e aliases de forma mais rica. O verificador e o editor conseguem reutilizar esses contratos para acompanhar argumentos, retornos e identidades nominais entre arquivos sem executar os módulos do usuário.

Aliases e reexportações preservam a origem do símbolo e possuem proteção contra ciclos. Casos que não podem ser comprovados permanecem conservadores, em vez de receber um tipo inventado.

### Fluxo de tipos e diagnóstico lógico

A análise conserva uma informação de tipo somente enquanto o fluxo permite justificá la. Condições, laços e atribuições potencialmente mutáveis invalidam evidências antigas quando necessário.

Expressões lógicas como `verdadeiro e falso` deixam de receber o diagnóstico aritmético `T204`.

### `coral.toml`

Um manifesto vazio pode receber a sugestão **Estrutura básica Coral** ou ser inicializado pelo comando **Coral: Inserir estrutura básica do coral.toml**. O editor não sobrescreve um arquivo já preenchido e evita aplicar uma resposta obsoleta quando o documento muda durante a operação.

### Exemplos e distribuição

A distribuição acrescenta `Exemplos/Analise_1_7_4/Cadastro/`, um projeto pequeno com classes, parâmetros tipados, fachada de módulo, aliases, testes e `programa principal`.

* Runtime portátil: `coral-1.7.4.pyz`.
* Extensão: `coral-language-0.75.2.vsix`.
* Livro Oficial preservado na edição `1.7.0`.
* Linux permanece como plataforma autoritativa desta distribuição.

## Coral 1.7.3

### Tipagem opcional estrutural

As anotações opcionais agora podem descrever a estrutura das coleções com formas como `lista de T`, `conjunto de T`, `dicionário de K para V` e `tupla de (T, U)`. Tipos podem ser aninhados, e `T ou nulo` descreve valores opcionais sem introduzir uniões gerais entre tipos arbitrários.

```coral
defina notas do tipo lista de decimal como [8, 9.5]
defina ficha do tipo tupla de (texto, inteiro) como ("Ana", 19)
defina apelido do tipo texto ou nulo como nulo
mostre notas
mostre ficha
mostre apelido
```

A análise é conservadora. Anotações não convertem valores e coleções mutáveis não ganham compatibilidades implícitas apenas pela relação entre os tipos dos elementos.

### Herança múltipla e cooperação

Classes podem declarar mais de uma base. A ordem de resolução segue C3, e `chame o método pai` continua a cadeia cooperativa dentro de métodos. Construtores podem cooperar com `inicialize a classe pai`.

Bases repetidas, ciclos, bases conhecidas que não são classes e hierarquias comprovadamente inconsistentes recebem diagnóstico antes da execução.

### Programa principal

`programa principal` oferece uma entrada opcional para aplicações. Ao executar o arquivo diretamente, o módulo é inicializado e a entrada roda uma vez. Ao importar o mesmo arquivo, a entrada não é iniciada. Scripts lineares continuam válidos.

```coral
programa principal
    chame apresentar com "Coral"
fim

crie a função apresentar com nome
    mostre nome
fim
```

### Editor e ferramentas

Coral Language `0.74.4` acompanha os tipos compostos, múltiplas bases, membros herdados pela ordem de resolução e `programa principal` no outline, hover, dobramento e indentação.

### Distribuição

* Runtime portátil: `coral-1.7.3.pyz`.
* Extensão: `coral-language-0.74.4.vsix`.
* Livro Oficial preservado na edição `1.7.0`; os recursos posteriores são complementados pela documentação Web.
* Os artefatos nativos Linux preservados na distribuição continuam identificados como `1.7.0`.
* A qualificação publicada desta edição cobre o runtime portátil e a extensão em Linux.

## Coral 1.7.2

### Português corrente e biblioteca base

A 1.7.2 amplia as formas naturais da biblioteca base sem remover as APIs explícitas. Entre as novas expressões estão consultas e testes de tipo, leitura de entrada, operações de arquivos e texto, operações de coleção, JSON e conversões.

Exemplos:

```coral
mostre o nome do tipo de valor
se valor for do tipo inteiro então
    mostre converta valor para texto
fim

defina linha como leia uma linha com "Valor: "
defina numero como tente converter linha para inteiro, senão nulo
```

Chamadas explícitas continuam sendo a forma indicada quando você precisa de argumentos opcionais, codificação, ordenação reversa ou tipos definidos pelo próprio programa.

### Contratos de tipo e conversão

* Booleano não é tratado como inteiro pelo teste de tipo Coral.
* Decimal corresponde ao valor decimal do runtime; o alias `número` conserva o contrato já existente e não passa a incluir inteiros.
* Tipos definidos pelo programa continuam usando `e_tipo` explicitamente.
* A forma curta `valor for inteiro` não é aceita; use `valor for do tipo inteiro`.
* Conversões naturais aceitam `inteiro`, `decimal`, `texto` e `booleano` e preservam o contrato de erro de `coral.conversoes`.

### Diagnósticos de execução

Erros de execução passam a ser classificados com código e categoria, mantendo a mensagem original e acrescentando sugestão. Terminal e depurador usam a mesma classificação. O diagnóstico estruturado também conserva origem, linha técnica e cadeia de causas quando disponíveis.

A documentação possui uma página própria de [**Diagnósticos**](diagnosticos.html) com a tabela de códigos `R100` a `R205` e o fallback `R001`.

### Editor

Coral Language `0.74.0` conhece as formas naturais da biblioteca base no LSP e nos snippets. A formatação preserva a escrita escolhida pelo programa, e as ferramentas de ensino podem explicar os contratos sem executar a expressão.

### Distribuição

* Runtime portátil: `coral-1.7.2.pyz`.
* Extensão: `coral-language-0.74.0.vsix`.
* Livro Oficial preservado na edição `1.7.0`; as formas novas da 1.7.2 são complementadas pela documentação Web.
* Os executáveis nativos Linux e o pacote `.deb` preservados na distribuição continuam identificados como `1.7.0`.
* Windows não é declarado como plataforma nativa validada desta edição.

## Coral 1.7.1

A 1.7.1 preservou gramática e APIs públicas. Para quem usa a linguagem, as mudanças visíveis foram a promoção do runtime para `1.7.1`, Coral Language para `0.73.0` e a correção da derivação da versão mínima padrão em pacotes locais.

O Livro Oficial permaneceu na edição `1.7.0`.

## Coral 1.7.0

A 1.7.0 consolidou a distribuição pública da linguagem, biblioteca padrão, ferramentas e Livro Oficial. O runtime portátil é `coral-1.7.0.pyz`, Coral Language é `0.72.0` e o Livro Oficial é `1.7.0`.

Linux x86_64 é a plataforma dos artefatos nativos dessa edição. A documentação inclui computação científica, gráficos 2D e 3D, Web local, cliente HTTP, servidor HTTP local, geração procedural, criptografia, jogos, simulação, sistema e hardware.

## Como ler estas notas

Use esta página para descobrir o que mudou ao atualizar a Coral. Para aprender sintaxe, módulos e APIs, use a documentação normal ou o Livro Oficial.
