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

## Diagnósticos de execução

Desde a 1.7.2, terminal e DAP compartilham a mesma classificação de falhas de execução. O editor pode mostrar código, categoria, mensagem, localização e sugestão sem descartar a causa original.

O detalhe estruturado adicional do DAP fica em `exceptionInfo.details.diagnostico`. Consulte [**Diagnósticos**](diagnosticos.html) para a tabela de códigos e categorias.


## Tipos, herança e entrada principal

A extensão corrente reconhece anotações compostas como `lista de inteiro`, `dicionário de texto para decimal` e `T ou nulo`. O hover preserva a forma estrutural, a hierarquia de tipos mostra todas as bases conhecidas e a conclusão local considera membros herdados pela ordem de resolução da classe.

`programa principal` também aparece no outline e participa de hover, dobramento, indentação e fechamento automático de bloco. A análise permanece conservadora quando o documento está incompleto durante a edição.

## Coloração e tema

A extensão não impõe uma paleta própria ao código. TextMate garante realce léxico enquanto o LSP não está disponível e semantic tokens refinam o papel real de símbolos quando há contexto suficiente. O tema do usuário continua soberano.

## Linha longa

O limite editorial corrente é de 150 caracteres. Quando uma linha ultrapassa esse tamanho, o editor pode oferecer uma prévia de quebra antes de aplicar a alteração.

## Ambiente Coral

A visão Ambiente Coral reúne runtime selecionado, versão, projeto atual, estado do LSP e do DAP, confiança do workspace, componentes e problemas relevantes.

## Recuperação de falhas

Quando o LSP falha, a extensão deve deixar o estado degradado explícito e oferecer reinício e acesso ao log. O fallback local continua disponível apenas para o que pode ser feito com segurança sem semântica de projeto.

<!-- AUTO:VERSAO -->

**Extensão corrente:** Coral Language `0.74.4` para Coral `1.7.3`.

<!-- /AUTO:VERSAO -->
