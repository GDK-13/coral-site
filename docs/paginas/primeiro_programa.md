# Seu primeiro programa

O primeiro programa pode ser um único arquivo. Crie `ola.coral` e coloque o conteúdo abaixo.

## Escrever

```coral
mostre "Olá, Coral!"

defina pontos como 10
aumente pontos em 5

se pontos é maior que 14
    mostre "Meta alcançada"
senão
    mostre "Continue tentando"
fim
```

:::resultado
A saída é:

```saida
Olá, Coral!
Meta alcançada
```
:::

O exemplo mostra saída, variável, alteração de valor e uma decisão condicional usando o português corrente da linguagem.

## Executar

Com o runtime portátil:

```bash
python coral-1.7.4.pyz executar ola.coral
```

Se a instalação persistente já estiver registrada, você pode usar o comando Coral configurado pelo instalador.

## Verificar sem executar

Para validar o programa sem rodar seus efeitos:

```bash
python coral-1.7.4.pyz verificar ola.coral
```

Essa etapa é útil para detectar erros sintáticos e semânticos antes da execução.

## Organizar uma aplicação com entrada explícita

Quando o arquivo representa uma aplicação maior, você pode usar uma entrada principal sem deixar de declarar funções e classes no mesmo módulo.

```coral
programa principal
    chame saudar com "Ana"
fim

crie a função saudar com nome
    mostre "Olá, " mais nome
fim
```

:::resultado
Ao executar o arquivo diretamente, o módulo é inicializado e `programa principal` roda uma única vez. Se o arquivo for importado como módulo, essa entrada não é iniciada.
:::

Leia [**Programa principal**](linguagem/programa_principal.html) para os limites e as diferenças entre `chame`, `execute` e uma entrada de aplicação.

## Quando algo der errado

Erros de execução trazem código, categoria, mensagem e sugestão. Abra [**Diagnósticos**](diagnosticos.html) para entender códigos como `R102` para conversão, `R110` para arquivo ausente e `R203` para incompatibilidade de tipo.

## Próximo passo

Antes de partir para bibliotecas maiores, abra [**Fundamentos da linguagem**](linguagem/index.html) para aprender variáveis, operadores, controle de fluxo, funções, classes, tipos, coleções e erros. Quando o programa começar a crescer em vários arquivos, a página **Projetos e módulos** mostra quando criar `coral.toml`.
