# Projetos e módulos

Projetos Coral usam `coral.toml` como ponto central de configuração. O runtime, o LSP e o Project Explorer leem a mesma estrutura, evitando que o editor invente uma interpretação diferente da usada na execução.

## Quando criar um projeto

Use um projeto quando houver mais de um arquivo, testes, recursos, caminhos de módulo ou configuração compartilhada. Para scripts pequenos, um arquivo isolado continua válido.

## Estrutura mínima

Uma estrutura comum é:

```text
meu_projeto/
├── coral.toml
├── principal.coral
├── modulos/
└── testes/
```

O `coral.toml` declara a entrada e os caminhos usados pelo projeto. A extensão do VS Code usa isso para montar a árvore semântica do Project Explorer.

## Importar funções

A forma seletiva deixa explícito o que entra no escopo do arquivo:

```coral
de calculos importe dobro
mostre dobro(21)
```

## Imports multilinha

Quando uma importação seletiva ficaria longa, os símbolos podem ser listados um por linha. Aliases continuam explícitos.

```coral
de math importe
    sqrt como raiz
    floor
fim

mostre raiz(9)
mostre floor(2.8)
```

O `fim` pertence à lista de imports. Essa forma é útil principalmente quando a interface consumida possui vários nomes e você quer manter cada dependência visível.

## Formas naturais importadas

Funções públicas podem declarar uma forma natural. Quando a função é importada seletivamente, essa forma também pode ser reconhecida no arquivo consumidor.

```coral
crie a função dobro com numero chamada como "dobre {numero}"
    retorne numero vezes 2
fim

mostre dobre 21
```

A forma natural não é uma substituição textual solta. Ela participa do parser e das interfaces de módulo.

## Interfaces públicas entre módulos

A análise de projeto não precisa executar um módulo para descobrir sua superfície pública. A Coral registra contratos com funções, classes, assinaturas, retornos, membros, imports e aliases. O editor e o verificador reutilizam esses contratos para acompanhar símbolos entre arquivos.

O projeto oficial `Exemplos/Analise_1_7_4/Cadastro/` mostra essa organização. `modelos.coral` declara `Autor` e `Livro`, `fachada.coral` publica nomes usados pelo restante do projeto e `principal.coral` consome a fachada a partir de `programa principal`.

Esse mecanismo também protege cadeias de aliases e reexportações contra ciclos. Quando a análise não consegue comprovar um detalhe, ela preserva o estado desconhecido em vez de assumir um tipo ou membro.

## Projeto Ecossistema da 1.7.5

`Exemplos/Analise_1_7_5/Ecossistema/` mostra um projeto pequeno em que classes são importadas entre arquivos, consultas `for do tipo` respeitam herança e uma construção de objeto usa chamada explícita multilinha. É um bom exemplo para verificar navegação, hover e análise de projeto sem concentrar tudo em um único arquivo.

## Criar o manifesto no VS Code

Se você abrir um arquivo vazio chamado exatamente `coral.toml`, Coral Language pode oferecer a sugestão **Estrutura básica Coral**. Também existe o comando **Coral: Inserir estrutura básica do coral.toml**. O conteúdo existente é preservado; o editor não substitui silenciosamente um manifesto já preenchido.

## Ambientes reproduzíveis

Projetos que dependem de pacotes Python podem declarar requisitos no próprio `coral.toml` e fixar a resolução em `coral.lock`. O objetivo é reproduzir o ambiente sem modificar o Python global da máquina.

```toml
[projeto]
nome = "meu-projeto"

[coral]
versao = ">=1.7.6"

[dependencias]
python = ["numpy>=2.0,<3"]

[ambiente]
python = ">=3.10,<3.15"
```

O fluxo comum é:

```bash
coral manager ambiente resolver --projeto . --cache wheels --offline --json
coral manager ambiente preparar --projeto . --offline --aplicar --json
coral --projeto-executar
coral manager ambiente verificar --projeto . --json
```

`resolver` produz o lock; `preparar` confere ou cria uma geração isolada; `verificar` compara o ambiente ativo com o contrato do projeto. Sem `--permitir-rede`, a resolução não consulta registros remotos. `--simular` mostra o plano sem criar lock, cache ou ambiente.

O lock registra versões exatas, dependências transitivas, origem e hashes das wheels, além do alvo de Python e plataforma. Quando esses requisitos mudam, faça uma nova resolução em vez de editar o arquivo manualmente.

O exemplo `Exemplos/Projetos/Ambiente_Reproduzivel/` demonstra esse ciclo usando artefatos locais.

## Validar e construir

A CLI oferece comandos para validar, construir e executar projetos. O VS Code expõe as mesmas operações pela interface para evitar que o terminal seja obrigatório no uso cotidiano.
