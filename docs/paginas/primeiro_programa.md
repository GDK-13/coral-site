# Seu primeiro programa

O primeiro programa pode ser um único arquivo. Crie `ola.coral` e coloque o conteúdo abaixo.

## Escrever

```coral
mostre "Olá, Coral!"

defina pontos como 10
adicione 5 a pontos

se pontos for maior ou igual a 15 então
    mostre "Meta alcançada"
senão
    mostre "Continue tentando"
fim
```

O exemplo mostra saída, variável, alteração de valor e uma decisão condicional.

## Executar

Com o runtime portátil:

```bash
python coral-1.5.9.pyz executar ola.coral
```

Se a instalação persistente já estiver registrada, você pode usar o comando Coral configurado pelo instalador.

## Verificar sem executar

Para validar o programa sem rodar seus efeitos:

```bash
python coral-1.5.9.pyz verificar ola.coral
```

Essa etapa é útil para detectar erros sintáticos e semânticos antes da execução.

## Próximo passo

Quando o programa começar a crescer, separe funções e módulos. A página **Projetos e módulos** mostra quando criar `coral.toml` e como organizar vários arquivos.
