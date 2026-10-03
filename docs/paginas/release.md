# Notas de versão

Esta página reúne mudanças de compatibilidade, sintaxe, ferramentas e distribuição relevantes para quem usa a Coral. O histórico interno de desenvolvimento não faz parte do site público.

## Versão atual

<!-- AUTO:VERSAO_NOTAS -->

**Coral:** `1.7.4`  
**Coral Language:** `0.75.2`  
**Livro Oficial:** `1.7.0`

<!-- /AUTO:VERSAO_NOTAS -->

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
