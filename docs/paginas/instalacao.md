# Instalação

A distribuição oficial da Coral inclui runtime portátil, assistentes de instalação, a extensão Coral Language e artefatos nativos quando a plataforma é suportada pela edição corrente.

## Linux x86_64

Linux x86_64 é a plataforma nativa autoritativa da Coral 1.7.0.

Na raiz da distribuição extraída:

```bash
bash Instalacao/Coral_Setup.sh
python Instalacao/Runtime/coral-1.7.0.pyz --versao
```

O segundo comando deve informar `1.7.0`.

A distribuição também contém artefatos nativos Linux e um pacote `.deb`. Todos usam a mesma lógica de instalação e perfis da Coral.

## Runtime portátil

Se você não quiser registrar uma instalação persistente, pode executar o runtime diretamente:

```bash
python Instalacao/Runtime/coral-1.7.0.pyz programa.coral
```

Isso é suficiente para estudar e executar programas que não dependam de componentes opcionais ausentes no ambiente.

## Windows

A Coral 1.7.0 não declara Windows x86_64 como plataforma nativa validada desta edição. A distribuição ainda preserva ferramentas portáteis e assistentes relacionados, mas eles não devem ser apresentados como instalador nativo oficial da 1.7.0.

## Instalar a extensão do VS Code

A extensão oficial fica em `Instalacao/Extensao_VSCode/`. No VS Code, use **Extensions: Install from VSIX** e selecione `coral-language-0.72.0.vsix`.

Depois, execute **Developer: Reload Window** para reiniciar o host da extensão.

## Verificar a instalação

Use o próprio runtime para conferir o ambiente:

```bash
python Instalacao/Runtime/coral-1.7.0.pyz --self-check
python Instalacao/Runtime/coral-1.7.0.pyz --ambiente
```

Se estiver no VS Code, a visão **Ambiente Coral** também mostra runtime, projeto, LSP, DAP e componentes disponíveis.

## Componentes opcionais

Perfis de instalação podem reunir componentes para usos diferentes, como computação científica e desenvolvimento. O instalador mantém esses componentes separados do Python global do sistema.

## Atualizar a Coral

Use uma distribuição oficial mais recente e execute novamente o assistente correspondente. Antes de atualizar um projeto importante, consulte **Notas de versão** para verificar disponibilidade de plataforma e mudanças relevantes para quem usa a linguagem.
