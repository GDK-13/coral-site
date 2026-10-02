# Notas de versão

Esta página reúne mudanças de compatibilidade, sintaxe, ferramentas e distribuição relevantes para quem usa a Coral. O histórico interno de desenvolvimento não faz parte do site público.

## Versão atual

<!-- AUTO:VERSAO_NOTAS -->

**Coral:** `1.7.2`  
**Coral Language:** `0.74.0`  
**Livro Oficial:** `1.7.0`

<!-- /AUTO:VERSAO_NOTAS -->

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
