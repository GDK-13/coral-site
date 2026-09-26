# Roadmap de QoL e Didática do Site Coral

**Base atual:** Site Coral 1.6.0  
**Objetivo:** melhorar a experiência de consulta, aprendizagem e descoberta da documentação sem redesenhar o site por completo.  
**Estado:** a Fase 1 de prioridade muito alta foi concluída na base 1.5.20 e permanece ativa na 1.6.0.  
**Princípio:** preservar a identidade visual, o gerador atual, a documentação em Markdown, a busca existente e a arquitetura estática sempre que possível.

---

## 1. Direção geral

O site atual já possui uma base sólida de qualidade de vida: busca global, histórico de páginas, cópia de código, âncoras, temas claro e escuro, índice da página, breadcrumbs, navegação anterior e próxima, funcionamento offline e detalhes técnicos recolhíveis.

A próxima evolução deve concentrar se em **arquitetura da informação e didática**, principalmente em páginas extensas e módulos complexos.

A meta não é transformar o site em uma plataforma pesada. A meta é fazer com que ele responda melhor a duas perguntas diferentes:

1. **“Quero aprender a usar isso.”**
2. **“Já sei o que quero e preciso consultar rapidamente.”**

---

# 2. Escopo ativo imediato

Nesta etapa serão implementados **somente os itens classificados como prioridade muito alta**.

## 2.1. Modo Aprender e Modo Referência

### Objetivo

Permitir que a mesma documentação atenda bem iniciantes, estudantes intermediários e usuários que já conhecem a linguagem.

### Modo Aprender

Deve priorizar:

- explicação em linguagem natural;
- exemplos progressivos;
- resultado esperado;
- erros comuns;
- observações pedagógicas;
- relação com outros conceitos;
- próximos passos;
- referência técnica recolhida ou secundária.

### Modo Referência

Deve priorizar:

- assinatura;
- parâmetros;
- retorno;
- exceções;
- formas aceitas;
- membros e operações públicas;
- origem do símbolo;
- consulta rápida.

### Requisitos de QoL

- alternância visível entre os dois modos;
- preferência armazenada localmente;
- sem necessidade de conta;
- sem backend;
- funcionamento offline;
- mudança de modo sem recarregar a navegação;
- acessibilidade por teclado;
- nenhuma informação técnica deve ser perdida em qualquer modo.

### Estratégia recomendada

Usar `localStorage` para guardar a preferência do usuário.

A estrutura editorial pode continuar sendo gerada a partir do mesmo Markdown, com blocos ou classes indicando:

- conteúdo comum;
- conteúdo pedagógico;
- conteúdo de referência.

---

## 2.2. Guias por objetivo

### Objetivo

Permitir que o usuário encontre conteúdo pelo problema que quer resolver, e não apenas pelo nome do módulo.

### Problema atual

Um iniciante pensa:

- “quero ler um arquivo”;
- “quero salvar progresso”;
- “quero mover um personagem”;
- “quero fazer uma câmera seguir algo”;

e não necessariamente:

- `coral.arquivos`;
- `coral.jogos`;
- `coral.sistema`.

### Nova área sugerida

Criar uma página:

`O que você quer fazer?`

ou rota equivalente dentro da documentação.

### Primeiras categorias

#### Entrada e dados

- receber dados do usuário;
- converter valores;
- validar entradas;
- trabalhar com texto;
- trabalhar com números.

#### Arquivos e persistência

- ler um arquivo;
- escrever um arquivo;
- salvar progresso;
- carregar dados;
- trabalhar com JSON ou formatos equivalentes disponíveis.

#### Jogos

- criar uma janela;
- carregar uma imagem;
- mover um sprite;
- animar um sprite;
- detectar colisão;
- usar câmera;
- usar HUD;
- usar camadas;
- criar transições.

#### RPG e regras

- criar personagem;
- representar atributos;
- criar regras;
- trabalhar com turnos;
- organizar estados e ações.

#### Simulação e geração

- criar eventos;
- trabalhar com agentes;
- gerar conteúdo por semente;
- usar geração procedural;
- simular sistemas.

### Formato de cada guia

Cada item deve ter:

1. objetivo em linguagem natural;
2. exemplo mínimo;
3. resultado esperado;
4. módulo relacionado;
5. link para a explicação completa;
6. nível aproximado.

### Regra editorial

Os guias não substituem a documentação do módulo.

Eles funcionam como **porta de entrada**.

---

## 2.3. Resumo rápido no início de cada módulo

### Objetivo

Permitir que o usuário entenda em poucos segundos:

- para que o módulo serve;
- quando usar;
- quando provavelmente não usar;
- qual é o menor exemplo útil;
- com quais módulos ele se relaciona.

### Estrutura proposta

Cada página de módulo deve começar com um cartão ou bloco semelhante a:

#### Serve para

Descrição curta e objetiva.

#### Use quando

Situações típicas em que o módulo resolve um problema.

#### Talvez você não precise dele quando

Situações em que outro módulo ou recurso é mais apropriado.

#### Exemplo mínimo

Trecho pequeno e funcional.

#### Relaciona se com

Links para módulos relacionados.

### Exemplo conceitual

Para `coral.jogos`:

**Serve para:** criar aplicações interativas, jogos 2D e experiências gráficas.

**Use quando:** precisar de janela, sprites, mapas, câmera, animação, colisão, HUD ou transições.

**Talvez você não precise dele quando:** o programa for apenas textual, de terminal ou manipulação de dados.

**Relaciona se com:** `coral.mundo`, `coral.rpg`, `coral.regras`, `coral.procedural`.

### Requisitos

- conteúdo curto;
- leitura rápida;
- visualmente distinto;
- gerado de forma consistente;
- não repetir grandes trechos da introdução;
- não transformar a página em uma lista de slogans.

---

## 2.4. Exemplos com saída esperada

### Objetivo

Eliminar a dúvida:

**“Executei corretamente?”**

Cada exemplo didático relevante deve poder mostrar o resultado que o usuário deveria observar.

### Tipos de resultado

#### Terminal

Mostrar a saída textual esperada.

#### Dados

Mostrar o valor final ou a estrutura resultante.

#### Arquivos

Mostrar uma amostra do conteúdo criado.

#### Jogos e interface

Mostrar uma descrição objetiva do resultado visual.

Quando houver material adequado, poderá ser usada uma pequena imagem ou captura.

### Estrutura sugerida

Após o código:

`Resultado esperado`

O conteúdo pode ficar recolhível para não aumentar demais o comprimento da página.

### Regras

- não inventar uma saída exata quando ela depender de aleatoriedade;
- em exemplos aleatórios, explicar o padrão esperado;
- quando o resultado depender do ambiente, deixar isso explícito;
- manter o exemplo principal legível;
- preservar o botão de copiar código já existente.

---

# 3. Ordem de implementação desta etapa

A implementação deve seguir esta ordem:

## Bloco A — Fundação

1. definir componentes editoriais e classes para os dois modos;
2. adicionar preferência local;
3. criar alternância Aprender / Referência;
4. garantir que o renderer não remova conteúdo.

## Bloco B — Estrutura de módulo

1. criar componente de resumo rápido;
2. aplicar primeiro a módulos representativos;
3. validar em módulos simples e complexos;
4. expandir para todos os módulos.

## Bloco C — Resultado esperado

1. criar sintaxe editorial para resultado;
2. adicionar renderer;
3. aplicar aos exemplos mais importantes;
4. validar terminal, dados e exemplos visuais.

## Bloco D — Guias por objetivo

1. criar página principal;
2. criar taxonomia inicial;
3. conectar os guias à busca;
4. ligar cada guia à documentação existente.

---

# 4. Critérios de aceite da fase atual

A etapa de prioridade muito alta só deve ser considerada concluída quando:

- o modo Aprender funcionar;
- o modo Referência funcionar;
- a preferência sobreviver ao fechamento do navegador;
- o site continuar funcionando offline;
- nenhum conteúdo técnico ficar inacessível;
- todos os módulos tiverem resumo rápido;
- os principais exemplos didáticos tiverem resultado esperado;
- existir uma página funcional de guias por objetivo;
- os guias apontarem para documentação real;
- a busca continuar funcionando;
- links, âncoras e IDs continuarem válidos;
- o layout responsivo continuar funcionando;
- os temas claro e escuro continuarem funcionando;
- o site continuar sem exigir backend.

---

# 5. Backlog futuro

Os itens abaixo **não fazem parte da implementação atual**.

Eles ficam registrados para fases posteriores.

## Prioridade alta

### 5.1. Receitas práticas

Criar uma área de soluções pequenas e diretas:

- ler JSON;
- salvar progresso;
- sortear sem repetir;
- mover sprite;
- detectar colisão;
- criar turno;
- criar evento periódico;
- usar semente procedural.

Cada receita deve resolver um problema específico antes de aprofundar a teoria.

---

### 5.2. Índice de erros e soluções

Criar uma área dedicada a mensagens de erro e problemas comuns.

Cada entrada deve explicar:

- o que significa;
- causas comuns;
- solução mínima;
- como diagnosticar;
- links relacionados.

---

### 5.3. Busca com filtros

Expandir a busca atual com filtros como:

- Tudo;
- Guias;
- API;
- Exemplos;
- Receitas;
- Erros;
- Módulos.

Também poderão existir filtros por nível:

- Iniciante;
- Intermediário;
- Avançado.

---

### 5.4. Marcadores de nível e pré requisitos

Adicionar informações como:

- nível;
- tempo aproximado de leitura;
- conhecimentos recomendados;
- páginas sugeridas antes desta.

Especialmente útil para:

- `coral.mundo`;
- `coral.regras`;
- `coral.simulacao`;
- `coral.agentes`;
- `coral.procedural`;
- `coral.jogos`.

---

# 6. Backlog de prioridade média

## 6.1. Progresso local de aprendizado

Permitir que o usuário marque páginas ou etapas como concluídas.

Requisitos:

- apenas armazenamento local;
- sem conta;
- sem servidor;
- opção de limpar progresso.

---

## 6.2. Favoritos locais

Permitir marcar:

- módulos;
- páginas;
- receitas;
- APIs.

Os favoritos devem permanecer apenas no navegador.

---

## 6.3. Comparação entre formas do português corrente

Criar blocos didáticos mostrando:

- ideia conceitual;
- forma Coral;
- forma equivalente aceita;
- efeito semântico.

Exemplo conceitual:

**Ideia:** aumentar uma variável em cinco unidades.

**Em Coral:**

```coral
aumente pontos em 5
```

**O que acontece:** o valor de `pontos` é incrementado em cinco unidades.

O objetivo é explicar a linguagem, e não apenas listar palavras chave.

---

## 6.4. Histórico de introdução de API

Adicionar marcadores discretos, quando úteis:

- Desde 1.5.11;
- Ampliado em 1.5.13;
- Forma natural adicionada em 1.5.19.

Evitar aplicar a informação indiscriminadamente.

---

# 7. Melhorias futuras de didática

Estas ideias ficam registradas para etapas posteriores.

## 7.1. Trilhas curtas de aprendizagem

Possíveis trilhas:

- Primeiros 30 minutos;
- Primeiro programa útil;
- Primeiro jogo;
- Mundo e RPG;
- Simulação;
- Automação e sistema.

Cada trilha pode ter entre cinco e oito etapas.

---

## 7.2. Micro exercícios

Após conceitos importantes:

- propor uma pequena alteração;
- esconder a solução;
- permitir comparar posteriormente.

Não exige backend.

---

## 7.3. Componente “Em Coral”

Criar um padrão editorial específico para relacionar conceitos de programação à linguagem Coral.

Estrutura:

1. ideia;
2. forma Coral;
3. explicação;
4. formas equivalentes aceitas;
5. observações importantes.

Esse componente deve reforçar a proposta de português corrente sem transformar a documentação em mera tradução de palavras chave.

---

# 8. Arquitetura para módulos muito grandes

Páginas extensas, especialmente módulos como `coral.jogos`, devem evoluir para uma organização em portal.

Exemplo:

- Começar;
- Sprites;
- Animação;
- Câmera;
- Mapas;
- HUD e texto;
- Transições;
- Colisão;
- Depuração;
- Referência completa.

A referência técnica pode continuar concentrada, mas o usuário não deve precisar navegar por uma página gigantesca apenas para aprender uma funcionalidade específica.

Esta mudança não faz parte obrigatória da primeira implementação, mas deve orientar a arquitetura atual para evitar retrabalho.

---

# 9. O que não fazer agora

Nesta fase, evitar:

- redesenho completo do site;
- migração para framework pesado sem necessidade;
- contas de usuário;
- backend apenas para progresso;
- editor Coral executável no navegador;
- gamificação complexa;
- sistema de comentários;
- fóruns;
- banco de dados;
- fragmentação excessiva da documentação;
- substituição da busca atual sem necessidade.

---

# 10. Possível fase futura: execução no navegador

Um editor Coral executável diretamente no site pode ser valioso no futuro, mas não é apenas uma melhoria de QoL.

Ele exigirá decidir:

- como executar o runtime Coral no navegador;
- sandbox de execução;
- limites de recursos;
- suporte a módulos;
- suporte gráfico;
- segurança;
- compatibilidade;
- distribuição do runtime.

Portanto, deve ser tratado como projeto arquitetural separado.

---

# 11. Estado consolidado

## Implementar agora

1. **Modo Aprender e Modo Referência**
2. **Guias por objetivo**
3. **Resumo rápido no início de cada módulo**
4. **Exemplos com saída esperada**

## Guardar para depois

- Receitas práticas;
- índice de erros;
- filtros de busca;
- níveis e pré requisitos;
- progresso local;
- favoritos;
- comparação de português corrente;
- histórico de API;
- trilhas;
- micro exercícios;
- componente “Em Coral”;
- reorganização profunda de módulos gigantes;
- execução Coral no navegador.

---

# 12. Meta da primeira entrega

Ao final desta etapa, o site deve continuar reconhecível como o Site Coral atual, porém com uma diferença clara:

**quem está aprendendo deve conseguir descobrir o que fazer a seguir, enquanto quem já conhece a Coral deve continuar chegando rapidamente à referência técnica.**

A melhoria deve vir da organização e da didática, não do aumento desnecessário de complexidade técnica.
