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

## Realce semântico por papel

A coloração semântica usa o significado que o LSP consegue comprovar no contexto do arquivo. O tema continua decidindo as cores; a extensão fornece categorias e modificadores, não uma paleta fixa.

No exemplo abaixo, as ocorrências de `dieta` não exercem o mesmo papel:

```coral
crie a classe Dieta
fim

crie a classe Animal
    ao criar um Animal com dieta do tipo Dieta
        defina seu dieta como dieta
    fim
fim
```

O primeiro `dieta` no construtor é um **parâmetro**, `Dieta` é uma **classe**, `seu dieta` é uma **propriedade** e a última ocorrência volta a ser o parâmetro. Funções, métodos, variáveis, módulos e símbolos importados também recebem categorias próprias quando a identidade pode ser resolvida.

Quando o código está incompleto ou um símbolo ainda não foi resolvido, o editor preserva o realce lexical do TextMate em vez de inventar uma classificação.

## Análise entre módulos

Projetos usam interfaces públicas dos módulos para transportar assinaturas, retornos, classes, membros, imports, aliases e reexportações sem executar o código do usuário. Isso permite que hover, completion, navegação e diagnósticos mantenham a mesma identidade ao atravessar uma fachada de módulo.

A análise permanece conservadora. Membros qualificados e relações de herança que não possam ser comprovados com segurança podem permanecer sem refinamento semântico.

## Fluxo conservador de tipos

O editor mantém uma evidência de tipo somente enquanto ela continua válida. Condições, laços e atribuições que podem alterar um valor invalidam certezas antigas quando o fluxo não permite provar o tipo resultante. Expressões lógicas como `verdadeiro e falso` são tratadas como lógica e não recebem o diagnóstico aritmético `T204`.

## `coral.toml` no editor

Ao abrir um `coral.toml` vazio, a extensão pode sugerir **Estrutura básica Coral**. O comando **Coral: Inserir estrutura básica do coral.toml** oferece a mesma criação de forma explícita.

A inserção é conservadora: um manifesto já preenchido não é sobrescrito e uma resposta deixa de ser aplicada se o arquivo tiver sido alterado enquanto a operação aguardava conclusão. Completion, hover e diagnósticos continuam disponíveis para as chaves do manifesto.

## Linha longa

O limite editorial corrente é de 150 caracteres. Quando uma linha ultrapassa esse tamanho, o editor pode oferecer uma prévia de quebra antes de aplicar a alteração.

## Ambiente Coral

A visão Ambiente Coral reúne runtime selecionado, versão, projeto atual, estado do LSP e do DAP, confiança do workspace, componentes e problemas relevantes.

## Recuperação de falhas

Quando o LSP falha, a extensão deve deixar o estado degradado explícito e oferecer reinício e acesso ao log. O fallback local continua disponível apenas para o que pode ser feito com segurança sem semântica de projeto.

<!-- AUTO:VERSAO -->

**Extensão corrente:** Coral Language `0.75.2` para Coral `1.7.4`.

<!-- /AUTO:VERSAO -->
