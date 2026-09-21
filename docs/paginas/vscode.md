# VS Code

A extensão Coral Language integra o editor ao runtime por LSP e DAP. O objetivo é que editar, navegar, testar e depurar Coral não dependa de serviços externos nem de listas paralelas mantidas em JavaScript.

## Recursos principais

| Área | O que oferece |
|---|---|
| IntelliSense | conclusão contextual, hover, assinatura, definição, referências e rename |
| Coloração | TextMate como fallback e semantic tokens do LSP como camada contextual |
| Diagnósticos | erros e avisos com contexto de projeto e ações rápidas quando seguras |
| Execução | arquivo, projeto e REPL integrados |
| Debug | F5, breakpoints, pilha, evaluate e passos entre módulos |
| Testes | integração com runner e Test Explorer |
| Projetos | `coral.toml`, multiroot, Project Explorer e Ambiente Coral |

## Coloração e tema

A extensão não impõe uma paleta própria ao código. TextMate garante realce léxico enquanto o LSP não está disponível e semantic tokens refinam o papel real de símbolos quando há contexto suficiente. O tema do usuário continua soberano.

## Linha longa

O limite editorial corrente é de 150 caracteres. Quando uma linha ultrapassa esse tamanho, o editor pode oferecer uma prévia de quebra antes de aplicar a alteração.

## Ambiente Coral

A visão Ambiente Coral reúne runtime selecionado, versão, projeto atual, estado do LSP e do DAP, confiança do workspace, componentes e problemas relevantes.

## Recuperação de falhas

Quando o LSP falha, a extensão deve deixar o estado degradado explícito e oferecer reinício e acesso ao log. O fallback local continua disponível apenas para o que pode ser feito com segurança sem semântica de projeto.

<!-- AUTO:VERSAO -->

**Extensão corrente:** Coral Language `0.41.0` para Coral `1.5.9`.

<!-- /AUTO:VERSAO -->
