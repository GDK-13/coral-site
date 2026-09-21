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

## Formas naturais importadas

Funções públicas podem declarar uma forma natural. Quando a função é importada seletivamente, essa forma também pode ser reconhecida no arquivo consumidor.

```coral
crie a função dobro com numero chamada como "dobre {numero}"
    retorne numero vezes 2
fim

mostre dobre 21
```

A forma natural não é uma substituição textual solta. Ela participa do parser e das interfaces de módulo.

## Validar e construir

A CLI oferece comandos para validar, construir e executar projetos. O VS Code expõe as mesmas operações pela interface para evitar que o terminal seja obrigatório no uso cotidiano.
