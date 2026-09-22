# Instalação

A distribuição oficial da Coral inclui runtime portátil, assistentes de instalação e a extensão Coral Language. Você pode usar o runtime diretamente ou registrar uma instalação persistente no sistema.

## Antes de instalar

Tenha Python disponível no sistema. A Coral usa o runtime portátil distribuído como arquivo `.pyz`, então não é necessário montar manualmente o ambiente interno da linguagem para começar.

## Linux

Na raiz da distribuição extraída:

```bash
bash Instalacao/Coral_Setup.sh
python Instalacao/Runtime/coral-1.5.12.pyz --versao
```

O segundo comando deve informar a versão corrente da Coral.

## Windows

Na raiz da distribuição extraída:

```text
Instalacao\Coral_Setup.cmd
python Instalacao\Runtime\coral-1.5.12.pyz --versao
```

## Instalar a extensão do VS Code

A extensão oficial fica em `Instalacao/Extensao_VSCode/`. No VS Code, use **Extensions: Install from VSIX** e selecione o arquivo `coral-language-0.43.0.vsix`.

Depois, execute **Developer: Reload Window** para reiniciar o host da extensão.

## Verificar a instalação

Use o próprio runtime para conferir o ambiente:

```bash
python Instalacao/Runtime/coral-1.5.12.pyz --self-check
python Instalacao/Runtime/coral-1.5.12.pyz --ambiente
```

Se estiver no VS Code, a visão **Ambiente Coral** também mostra runtime, projeto, LSP, DAP e componentes disponíveis.

## Atualizar para uma nova release

Cada release completa é autocontida. Para atualizar, extraia a nova distribuição e execute novamente o assistente de instalação. A documentação do site é atualizada a partir do ZIP oficial da release, então versões exibidas aqui acompanham o pacote publicado.
