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

## Classes e chamadas na 1.7.5

Coral Language 0.76.0 entende consultas como `objeto for do tipo Animal`. Depois de `do tipo`, a conclusão pode oferecer tipos nativos e classes comprovadas no escopo. Classes permitem definição, hover com declaração e bases e realce semântico. Um nome local que encobre um import continua apontando para o vínculo local, sem navegar por engano para a classe externa.

As chamadas multilinha também participam da experiência do editor. O formatador mantém a indentação e os fechamentos, o fechamento automático respeita a configuração do usuário e a ajuda de assinatura acompanha o argumento atual mesmo em chamadas aninhadas.

## Documentos abertos e índice do projeto

A análise do projeto dá prioridade ao **documento aberto** no editor sobre a cópia salva em disco. Versões antigas do mesmo documento são ignoradas e, ao fechar o arquivo, o estado volta a refletir o conteúdo salvo.

O índice do projeto é seletivo: mudanças na interface pública de um módulo atualizam os consumidores afetados, enquanto alterações apenas no corpo podem preservar contratos já conhecidos. Eventos de arquivos e mudanças no manifesto atualizam somente o projeto correspondente. Isso reduz trabalho desnecessário sem misturar projetos diferentes.

## `coral.toml` no editor

Ao abrir um `coral.toml` vazio, a extensão pode sugerir **Estrutura básica Coral**. O comando **Coral: Inserir estrutura básica do coral.toml** oferece a mesma criação de forma explícita.

A inserção é conservadora: um manifesto já preenchido não é sobrescrito e uma resposta deixa de ser aplicada se o arquivo tiver sido alterado enquanto a operação aguardava conclusão. Completion, hover e diagnósticos continuam disponíveis para as chaves do manifesto.

## Cabeçalhos multilinha e projetos reproduzíveis

A extensão reconhece cabeçalhos multilinha de parâmetros, imports e herança como uma única estrutura. Isso permite manter indentação, navegação e análise sem exigir que declarações extensas sejam comprimidas em uma única linha.

Em projetos que usam `coral.lock`, o editor e a CLI compartilham a mesma identidade de projeto. A visão **Ambiente Coral** ajuda a distinguir o runtime selecionado, o projeto corrente e o ambiente gerenciado, evitando que a edição e a execução usem configurações divergentes.

## Textos multilinha na 1.7.9

Coral Language 0.80.0 reconhece literais delimitados por três aspas como uma única string, inclusive quando ocupam várias linhas físicas. O conteúdo é tratado como texto opaco: palavras que pareçam código Coral, SQL, HTML ou Markdown dentro do literal não recebem análise semântica como se fossem instruções do programa.

O formatador preserva o conteúdo textual e os mapas de linha continuam apontando para as linhas físicas corretas do arquivo. Isso permite usar consultas SQL, mensagens extensas e outros blocos textuais sem confundir o editor sobre onde a string termina.

## Guia de escrita e formatador

A Coral 1.8 possui um guia canônico de escrita, mas o editor não transforma preferência de estilo em erro de compilação. O formatador preserva a intenção entre formas compactas e multilinha e deve ser idempotente: formatar novamente não deve mudar o resultado da primeira formatação.

Use [**Estilo e legibilidade**](linguagem/estilo_legibilidade.html) para decidir quando quebrar uma declaração, como organizar imports e como separar definições da entrada da aplicação.

## Linha longa

O limite editorial corrente é de 150 caracteres. Quando uma linha ultrapassa esse tamanho, o editor pode oferecer uma prévia de quebra antes de aplicar a alteração.

## Ambiente Coral

A visão Ambiente Coral reúne runtime selecionado, versão, projeto atual, estado do LSP e do DAP, confiança do workspace, componentes e problemas relevantes.

## Recuperação de falhas

Quando o LSP falha, a extensão deve deixar o estado degradado explícito e oferecer reinício e acesso ao log. O fallback local continua disponível apenas para o que pode ser feito com segurança sem semântica de projeto.

<!-- AUTO:VERSAO -->

**Extensão corrente:** Coral Language `0.83.0` para Coral `1.8.0`.

<!-- /AUTO:VERSAO -->
