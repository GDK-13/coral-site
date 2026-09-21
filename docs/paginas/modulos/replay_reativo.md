# coral.replay_reativo

## Visão geral

`coral.replay_reativo` oferece gravação e reprodução determinística de eventos e mudanças. Use para gravar e reproduzir eventos e mudanças de forma determinística.

<!-- AUTO:MODULO -->

**Importação:** `coral.replay_reativo`  
**Categoria:** reativo  

gravação e reprodução determinística de eventos e mudanças

### Superfície pública detectada

`RegistroReplay`, `ResultadoReplay`, `GravadorReplay`, `ReplayReativo`

<!-- /AUTO:MODULO -->

## Quando usar

Use para gravar e reproduzir eventos e mudanças de forma determinística.

Entre as entradas públicas detectadas estão `RegistroReplay`, `ResultadoReplay`, `GravadorReplay`, `ReplayReativo`.

## Começando

Uma importação seletiva começa assim:

```coral
de coral.replay_reativo importe RegistroReplay, ResultadoReplay, GravadorReplay
```

Depois da importação, use o hover e o preenchimento do VS Code para consultar a assinatura exata disponível na release.

## Cuidados

Replay depende de entradas reproduzíveis. Efeitos externos precisam ser controlados ou registrados.

## Relações com outros módulos

Na mesma área, veja também `coral.observadores_reativos`, `coral.rastreamento_reativo`, `coral.sequencias_reativas`.

## Referência da API

<!-- AUTO:API -->

### Classes e protocolos

#### `RegistroReplay(tipo: str, dados: dict[str, Any])`

Entrada pública `RegistroReplay` da superfície `coral.replay_reativo`.

**Atributos declarados**

| Nome | Tipo | Padrão |
|---|---|---|
| `tipo` | `str` | obrigatório |
| `dados` | `dict[str, Any]` | obrigatório |

#### `ResultadoReplay(tipo: str, instante: float, processados: tuple[str, ...] = ())`

Entrada pública `ResultadoReplay` da superfície `coral.replay_reativo`.

**Atributos declarados**

| Nome | Tipo | Padrão |
|---|---|---|
| `tipo` | `str` | obrigatório |
| `instante` | `float` | obrigatório |
| `processados` | `tuple[str, ...]` | `()` |

#### `GravadorReplay() -> None`

Entrada pública `GravadorReplay` da superfície `coral.replay_reativo`.

**Métodos e propriedades públicas**

| Nome | Tipo | Assinatura | Retorno | Descrição |
|---|---|---|---|---|
| `registros` | propriedade | `registros() -> tuple[RegistroReplay, ...]` | `tuple[RegistroReplay, ...]` | Sem docstring própria na release. |
| `evento` | método | `evento(nome: str, *args: Any, origem: str \| None = None, **kwargs: Any) -> RegistroReplay` | `RegistroReplay` | Sem docstring própria na release. |
| `mudanca_mapa` | método | `mudanca_mapa(mudanca: Any) -> RegistroReplay` | `RegistroReplay` | Registra uma mudança aplicada para reconstrução determinística posterior. |
| `avancar` | método | `avancar(segundos: Any) -> RegistroReplay` | `RegistroReplay` | Sem docstring própria na release. |
| `como_json` | método | `como_json() -> str` | `str` | Sem docstring própria na release. |

#### `ReplayReativo(registros: Iterable[RegistroReplay | dict[str, Any]]) -> None`

Entrada pública `ReplayReativo` da superfície `coral.replay_reativo`.

**Métodos e propriedades públicas**

| Nome | Tipo | Assinatura | Retorno | Descrição |
|---|---|---|---|---|
| `reproduzir` | método | `reproduzir(motor: MotorRegras, relogio: RelogioSimulado, contexto: Any = None) -> tuple[ResultadoReplay, ...]` | `tuple[ResultadoReplay, ...]` | Sem docstring própria na release. |

<!-- /AUTO:API -->
