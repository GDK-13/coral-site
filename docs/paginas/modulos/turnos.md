# coral.turnos

## Visão geral

filas reutilizáveis de turnos, atendimento, produção e escalonamento

<!-- AUTO:MODULO -->

**Importação:** `coral.turnos`  
**Categoria:** agentes  

filas reutilizáveis de turnos, atendimento, produção e escalonamento

### Superfície pública detectada

`FilaTurnos`

<!-- /AUTO:MODULO -->

## Papel no ecossistema

`coral.turnos` fornece uma fila circular genérica e persistível. Ela não conhece combate nem personagens: os participantes podem representar pessoas em atendimento, máquinas em produção, tarefas, unidades de jogo ou qualquer objeto que precise alternar execução em uma ordem controlada.

## Conceitos principais

### Participantes e ordem

A fila mantém a lista de participantes e uma ordem efetiva separada. A ordem pode seguir a inserção original, ser fornecida explicitamente ou ser calculada a partir de prioridades.

### Rodadas

Quando o índice retorna ao início da ordem, `rodada` avança. Isso permite acompanhar ciclos completos sem impor significado específico ao domínio.

### Pausa e filtro de avanço

Uma fila pode ser pausada e retomada. `avancar` também pode receber um filtro que ignora participantes temporariamente indisponíveis.

### Histórico

Mudanças de estrutura e avanço são registradas em um histórico simples, útil para inspeção e persistência.

## Quando usar

Use `FilaTurnos` sempre que houver uma sequência circular de participantes e o domínio precisar controlar quem é o atual, qual a rodada e como a ordem é montada. Para combate, ela pode ser combinada com `coral.rpg`, mas o módulo também serve a atendimento, filas de produção e escalonamento.

## Começando

A release inclui `Exemplos/Agentes/02_habilidades_e_fila.coral`:

```coral
crie um mundo chamado oficina
crie um agente chamado robo_a no mundo oficina
crie um agente chamado robo_b no mundo oficina

crie uma fila chamada manutencao com robo_a e robo_b
inicie a fila manutencao
garanta que manutencao.atual for igual a robo_a
avance a fila manutencao
garanta que manutencao.atual for igual a robo_b
mostre manutencao.rodada
```

## API essencial

| Entrada | Papel |
|---|---|
| `FilaTurnos` | fila circular com ordem, índice, rodada, pausa e histórico |
| `iniciar` | define a ordem inicial por lista explícita ou prioridades |
| `atual` | informa o participante corrente |
| `avancar` | move para o próximo participante aceito |
| `adicionar` / `remover` | altera a composição da fila |
| `pausar` / `retomar` | controla o avanço sem destruir o estado |

## Fluxos comuns

1. Crie a fila com os participantes conhecidos.
2. Inicie usando a ordem original, uma ordem explícita ou prioridades.
3. Consulte `atual` antes de executar a ação do participante.
4. Chame `avancar` quando a etapa terminar.
5. Persista a fila quando precisar continuar o mesmo ciclo em outra execução.

## Erros e casos de borda

Não é permitido informar ordem explícita e prioridades ao mesmo tempo. Uma ordem explícita só pode conter participantes já registrados e não pode repetir o mesmo objeto. Remover o participante atual reajusta o índice para manter a fila consistente.

## Boas práticas

* Deixe a fila cuidar apenas da ordem e mantenha as regras de ação no domínio correspondente.
* Use prioridades somente para construir a ordem inicial; se a prioridade mudar continuamente, decida explicitamente quando reiniciar a fila.
* Use o filtro de `avancar` para indisponibilidade temporária em vez de remover e adicionar participantes repetidamente.

## Integração com outros módulos

`coral.agentes` fornece participantes ricos sem criar dependência obrigatória. `coral.rpg` pode usar a mesma fila em combate. A persistência Coral registra o estado da fila e preserva ordem, índice, rodada e histórico.

## Testabilidade e previsibilidade

Para uma mesma lista e prioridades, a ordem é determinística e desempates preservam a ordem original. Testes devem verificar ordem, participante atual, avanço de rodada, pausa e restauração persistente.

## Compatibilidade e evolução

A fila genérica foi introduzida na linha 1.5.10 e permanece publicada na **Coral 1.5.12** sem depender de RPG ou Jogos.

## Referência da API

<!-- AUTO:API -->

### Classes e protocolos

#### `FilaTurnos`

Fila circular persistível sem conhecimento de RPG ou combate.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `participantes` | Valor correspondente a participantes. | `Iterable[Any]` | `()` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `identidade` | Executa a operação `identidade` disponibilizada por `coral.turnos`. | `str` |
| `adicionar` | Adiciona o valor solicitado. | `Any` |
| `remover` | Remove o valor solicitado. | `bool` |
| `iniciar` | Inicia o valor solicitado. | `tuple[Any, ...]` |
| `atual` | Obtém atual. | `Any \| None` |
| `avancar` | Avança o valor solicitado. | `Any \| None` |
| `pausar` | Pausa o valor solicitado. | `None` |
| `retomar` | Retoma o valor solicitado. | `None` |
| `limpar_historico` | Limpa historico. | `None` |

:::details Detalhes técnicos

**Assinatura:** `FilaTurnos(participantes: Iterable[Any] = ()) -> None`

**Origem da implementação:** `coral.turnos`

**Arquivo na release:** `coral/turnos.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `identidade` | método | `identidade(participante: Any) -> str` |
| `adicionar` | método | `adicionar(participante: Any) -> Any` |
| `remover` | método | `remover(participante: Any) -> bool` |
| `iniciar` | método | `iniciar(*, ordem: Iterable[Any] \| None = None, prioridades: Mapping[Any, float] \| Callable[[Any], float] \| None = None) -> tuple[Any, ...]` |
| `atual` | propriedade | `atual() -> Any \| None` |
| `avancar` | método | `avancar(*, aceitar: Callable[[Any], bool] \| None = None) -> Any \| None` |
| `pausar` | método | `pausar() -> None` |
| `retomar` | método | `retomar() -> None` |
| `limpar_historico` | método | `limpar_historico() -> None` |

:::

<!-- /AUTO:API -->
