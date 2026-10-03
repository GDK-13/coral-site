# Instalação

A distribuição corrente usa o runtime **Coral 1.7.4**, a extensão **Coral Language 0.75.2** e preserva o **Livro Oficial 1.7.0**.

## Linux

Na raiz da distribuição extraída, o caminho mais direto para usar o runtime corrente é:

```bash
bash Instalacao/Coral_Setup.sh
python3 Instalacao/Runtime/coral-1.7.4.pyz --versao
```

O segundo comando deve informar `1.7.4`.

O pacote também preserva executáveis nativos Linux x86_64 e um pacote `.deb` identificados como `1.7.0`. Eles são artefatos nativos herdados; para executar exatamente o runtime desta edição, use `coral-1.7.4.pyz` ou o assistente da distribuição.

## Runtime portátil

O runtime portátil requer Python 3.10 ou superior e pode ser usado sem registrar uma instalação persistente:

```bash
python3 Instalacao/Runtime/coral-1.7.4.pyz programa.coral
```

Isso é suficiente para estudar e executar programas que não dependam de componentes opcionais ausentes no ambiente.

## Extensão do VS Code

A extensão oficial fica em `Instalacao/Extensao_VSCode/`. No VS Code, use **Extensions: Install from VSIX** e selecione:

```text
coral-language-0.75.2.vsix
```

Depois, execute **Developer: Reload Window** para reiniciar o host da extensão.

## Verificar a instalação

Use o próprio runtime para conferir o ambiente:

```bash
python3 Instalacao/Runtime/coral-1.7.4.pyz --self-check
python3 Instalacao/Runtime/coral-1.7.4.pyz --ambiente
```

Se estiver no VS Code, a visão **Ambiente Coral** também mostra runtime, projeto, LSP, DAP e componentes disponíveis.

## Componentes opcionais

Perfis de instalação podem reunir componentes para usos diferentes, como computação científica, jogos e hardware. O instalador mantém esses componentes separados do Python global do sistema quando usa o ambiente gerenciado da Coral.

## Disponibilidade de plataforma

A edição 1.7.4 é publicada com runtime portátil e extensão validados em Linux. Os artefatos nativos Linux preservados no pacote continuam identificados como 1.7.0. Windows não é declarado como plataforma nativa validada desta edição.

## Atualizar a Coral

Use uma distribuição oficial mais recente e execute novamente o assistente correspondente. Antes de atualizar um projeto importante, consulte **Notas de versão** para verificar compatibilidade, ferramentas e disponibilidade de plataforma.
