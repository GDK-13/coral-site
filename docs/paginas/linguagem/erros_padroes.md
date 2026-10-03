# Erros e padrões

A linguagem possui construções para tratar falhas esperadas e selecionar valores por padrões estruturados.

## Tratar uma exceção

```coral
tente
    defina resultado como 10 dividido por 0
se der erro do tipo ZeroDivisionError
    mostre "Não é possível dividir por zero"
finalmente
    mostre "Operação encerrada"
fim
```

:::resultado
A divisão gera uma exceção, o ramo correspondente mostra a mensagem e `finalmente` executa ao sair do bloco.
:::

Capture o tipo de erro que o programa realmente sabe tratar. Uma captura ampla demais pode esconder defeitos que deveriam ser corrigidos.

## Criar e lançar um erro próprio

```coral
crie a exceção SaldoInsuficiente
fim

crie a função sacar com saldo e valor
    se valor for maior que saldo então
        lance um erro do tipo SaldoInsuficiente com "saldo insuficiente"
    fim
    retorne saldo menos valor
fim
```

O exemplo declara uma exceção própria e a lança quando a operação não pode continuar.

## Selecionar por padrão

```coral
defina comando como "iniciar"

combinar comando
    caso "iniciar"
        mostre "Começando"
    caso "sair" ou "parar"
        mostre "Encerrando"
    caso padrão
        mostre "Comando desconhecido"
fim
```

:::resultado
Como `comando` vale `iniciar`, o primeiro caso é executado.
:::

## Diagnósticos de execução

Erros do runtime também recebem códigos e sugestões quando a Coral consegue classificá los. A página [Diagnósticos](../diagnosticos.html) explica categorias como conversão, arquivos, aritmética, tipos, acesso e nomes.
