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

O exemplo mostra saída, variável, alteração de valor e uma decisão condicional usando o português corrente consolidado na linha 1.5.19. As formas anteriores, como `adicione 5 a pontos` e o cabeçalho com `então`, continuam válidas.

## Executar

Com o runtime portátil:

```bash
python coral-1.6.0.pyz executar ola.coral
```

Se a instalação persistente já estiver registrada, você pode usar o comando Coral configurado pelo instalador.

## Verificar sem executar

Para validar o programa sem rodar seus efeitos:

```bash
python coral-1.6.0.pyz verificar ola.coral
```

Essa etapa é útil para detectar erros sintáticos e semânticos antes da execução.

## Próximo passo

Quando o programa começar a crescer, separe funções e módulos. A página **Projetos e módulos** mostra quando criar `coral.toml` e como organizar vários arquivos.
