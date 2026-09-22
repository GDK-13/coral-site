# REPL e CLI

A CLI é a interface de baixo nível para execução, verificação, projetos, testes, diagnóstico e ferramentas da Coral. O VS Code cobre o fluxo cotidiano, mas a CLI continua sendo a referência reproduzível para automação e manutenção.

## Uso cotidiano

```bash
python coral-1.5.12.pyz --versao
python coral-1.5.12.pyz --self-check
python coral-1.5.12.pyz --ambiente
```

## Executar e verificar arquivos

```bash
python coral-1.5.12.pyz executar programa.coral
python coral-1.5.12.pyz verificar programa.coral
```

## REPL

O REPL permite experimentar expressões e construções sem criar um arquivo novo.

```bash
python coral-1.5.12.pyz --repl
```

## Projetos

A CLI oferece operações de informação, validação, construção e execução de projetos. Essas ações usam `coral.toml` como fonte de configuração.

## Diagnóstico

Os comandos de ambiente, self check e diagnóstico ajudam a distinguir erros do programa de problemas de instalação, dependências opcionais ou seleção de runtime.

## Referência detectada

A lista abaixo é importada automaticamente do contrato gerado da release. Ela é mecânica e pode ser extensa, por isso fica ao fim desta página em vez de ocupar a navegação principal.

<!-- AUTO:CLI -->

### Opções detectadas

`--ambiente`, `--ambiente-json`, `--api-info`, `--ast-expressao`, `--ast-json`, `--ast-programa`, `--auditar-exemplos`, `--cache-info`, `--caso-teste`, `--checar-formatacao`, `--compilar`, `--conformidade`, `--conformidade-1-1`, `--conformidade-1-2`, `--conformidade-1-3`, `--contratos-1-3`, `--contratos-1-3-json`, `--contratos-stdlib`, `--corpus`, `--dap`, `--dependencias`, `--destino-projeto`, `--diagnostico-instalacao`, `--diagnostico-instalacao-json`, `--diagnosticos-json`, `--documentar`, `--explicar`, `--explicar-json`, `--filtro-teste`, `--formatar`, `--formatar-em-lugar`, `--gate-1-1`, `--gate-1-2`, `--gate-1-3`, `--gate-1-4`, `--gate-1-4-10`, `--gate-1-4-11`, `--gate-1-4-9`, `--gate-1-5`, `--gate-rc-1-1`, `--gate-vscode`, `--hardware-check`, `--hardware-check-json`, `--help`, `--jogos-check`, `--laboratorio-check`, `--limpar-cache`, `--lint`, `--listar-templates`, `--lsp`, `--mapa-linhas`, `--mostrar-python`, `--naturalidade`, `--naturalidade-json`, `--novo-projeto`, `--numerico-check`, `--projeto-construir`, `--projeto-executar`, `--projeto-info`, `--projeto-validar`, `--release-check-1-3`, `--release-check-1-3-json`, `--repl`, `--robustez`, `--robustez-intensa`, `--self-check`, `--sem-cache`, `--semantica`, `--simbolos`, `--sistema-info`, `--sistema-info-json`, `--template-projeto`, `--testar`, `--testes-json`, `--tokens-expressao`, `--validar-vsix`, `--verificar`, `--versao`, `--vscode-check`, `--vscode-check-json`, `-h`

### Subcomandos detectados

`repl`, `executar`, `verificar`, `lint`, `formatar`, `compilar`, `testar`, `testar-json`, `documentar`, `dependencias`, `projeto-info`, `projeto-validar`, `construir`, `diagnostico`, `explicar`, `naturalidade`, `templates`, `novo`

<!-- /AUTO:CLI -->
