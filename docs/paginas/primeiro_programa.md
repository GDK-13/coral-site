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
python coral-1.7.2.pyz executar ola.coral
```

Se a instalação persistente já estiver registrada, você pode usar o comando Coral configurado pelo instalador.

## Verificar sem executar

Para validar o programa sem rodar seus efeitos:

```bash
python coral-1.7.2.pyz verificar ola.coral
```

Essa etapa é útil para detectar erros sintáticos e semânticos antes da execução.

## Quando algo der errado

Erros de execução da 1.7.2 trazem código, categoria, mensagem e sugestão. Abra [**Diagnósticos**](diagnosticos.html) para entender códigos como `R102` para conversão, `R110` para arquivo ausente e `R203` para incompatibilidade de tipo.

## Próximo passo

Quando o programa começar a crescer, separe funções e módulos. A página **Projetos e módulos** mostra quando criar `coral.toml` e como organizar vários arquivos.
