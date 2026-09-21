# coral.hardware

## Visão geral

`coral.hardware` expõe informações de CPU, memória, discos, bateria e comunicação serial por uma superfície que pode funcionar com capacidades opcionais e backends simulados.

<!-- AUTO:MODULO -->

**Importação:** `coral.hardware`  
**Categoria:** hardware  

CPU, memória, discos, bateria e comunicação serial

### Superfície pública detectada

`DependenciaHardwareAusente`, `CPU`, `Memoria`, `Disco`, `Bateria`, `psutil_disponivel`, `serial_disponivel`, `cpu`, `memoria`, `discos`, `bateria`, `diagnosticar_hardware`, `auditar_hardware`, `ErroSerial`, `DependenciaSerialAusente`, `ErroConfiguracaoSerial`, `ConexaoSerialFechada`, `DesconexaoSerial`, `BackendSerial`, `BackendSerialReal`, `BackendSerialSimulado`, `usar_backend_serial`, `ConexaoSerial`, `PortaSerial`, `portas_seriais`, `conectar_serial`

<!-- /AUTO:MODULO -->

## Papel no ecossistema

O módulo trata hardware como capacidade do ambiente, não como pressuposto. Um programa pode descobrir se `psutil` ou serial estão disponíveis e escolher entre backend real, simulação ou degradação explícita.

## Conceitos principais

### Inventário do host

`CPU`, `Memoria`, `Disco` e `Bateria` são estruturas de dados. As funções `cpu`, `memoria`, `discos` e `bateria` produzem esses retratos.

### Dependências opcionais

`psutil_disponivel()` e `serial_disponivel()` permitem consultar capacidades. `diagnosticar_hardware()` e `auditar_hardware()` ajudam a explicar por que um recurso não está disponível.

### Serial real e simulada

`BackendSerialReal` usa a dependência serial quando instalada. `BackendSerialSimulado` mantém portas e buffers em memória, permitindo testar protocolo, conexão e desconexão sem hardware físico.

### Conexão serial

`ConexaoSerial` concentra envio, leitura, leitura de linha e fechamento. `conectar_serial` é o atalho funcional para abrir uma sessão.

## Quando usar

Use quando o programa precisa inspecionar a máquina, reagir à presença de bateria ou disco, conversar com microcontroladores ou testar uma integração serial.

Evite tornar a lógica de domínio dependente de hardware real quando ela puder receber dados simulados. Isso melhora testes e permite executar o programa em servidores ou CI.

## Começando

O exemplo abaixo foi validado com o runtime 1.5.9:

```coral
de coral.hardware importe cpu, memoria, discos, psutil_disponivel

se psutil_disponivel() então
    defina processador como cpu()
    defina ram como memoria()
    defina unidades como discos()
    mostre processador.nucleos_logicos
    mostre ram.total_bytes
    mostre quantidade de unidades
fim
```

## API essencial

| Entrada | Papel | Assinatura |
|---|---|---|
| `psutil_disponivel` | detectar inventário avançado | `psutil_disponivel() -> bool` |
| `serial_disponivel` | detectar backend serial real | `serial_disponivel() -> bool` |
| `cpu` | consultar CPU | `cpu() -> CPU` |
| `memoria` | consultar RAM | `memoria() -> Memoria` |
| `discos` | listar discos | `discos() -> tuple[Disco, ...]` |
| `bateria` | consultar bateria | `bateria() -> Bateria \| None` |
| `diagnosticar_hardware` | diagnóstico estruturado | `diagnosticar_hardware() -> dict[str, Any]` |
| `BackendSerialSimulado` | simular portas em memória | `BackendSerialSimulado() -> None` |
| `ConexaoSerial` | sessão serial | `ConexaoSerial(porta: str, velocidade: int = 115200, timeout: float \| None = 1.0, *, codificacao: str = 'utf-8', backend: BackendSerial \| None = None)` |
| `conectar_serial` | abrir conexão serial | `conectar_serial(porta: str, velocidade: int = 115200, timeout: float \| None = 1.0, *, codificacao: str = 'utf-8', backend: BackendSerial \| None = None) -> ConexaoSerial` |

## Testando serial sem dispositivo físico

`BackendSerialSimulado` pode registrar portas, injetar bytes recebidos, registrar o que foi enviado, simular desconexão e reconexão e abrir transportes sem esperar tempo real. Use essa rota como padrão para testes automatizados.

## Erros e diagnóstico

`DependenciaHardwareAusente` informa ausência de capacidade de inventário. A camada serial separa falta da dependência, configuração inválida, conexão fechada e desconexão durante a sessão.

Antes de concluir que há defeito no programa, consulte `diagnosticar_hardware()` e a disponibilidade das capacidades usadas.

## Segurança e robustez

* Trate dados vindos de serial como entrada externa.
* Defina timeout apropriado para dispositivos que podem parar de responder.
* Feche conexões explicitamente quando o ciclo de vida terminar.
* Não presuma que bateria ou determinada porta existe.
* Prefira o backend simulado em testes de lógica.

## Integração com outros módulos

`coral.sistema` descreve o host de forma geral. `coral.laboratorio` pode medir experimentos dependentes de hardware. `coral.tempo_eventos` ajuda a controlar polling e timeouts em fluxos mais amplos.

## Referência da API

<!-- AUTO:API -->

### Funções

#### `psutil_disponivel() -> bool`

Entrada pública `psutil_disponivel` da superfície `coral.hardware`.

**Retorno:** `bool`

#### `serial_disponivel() -> bool`

Entrada pública `serial_disponivel` da superfície `coral.hardware`.

**Retorno:** `bool`

#### `cpu() -> CPU`

Entrada pública `cpu` da superfície `coral.hardware`.

**Retorno:** `CPU`

#### `memoria() -> Memoria`

Entrada pública `memoria` da superfície `coral.hardware`.

**Retorno:** `Memoria`

#### `discos() -> tuple[Disco, ...]`

Entrada pública `discos` da superfície `coral.hardware`.

**Retorno:** `tuple[Disco, ...]`

#### `bateria() -> Bateria | None`

Entrada pública `bateria` da superfície `coral.hardware`.

**Retorno:** `Bateria | None`

#### `diagnosticar_hardware() -> dict[str, Any]`

Entrada pública `diagnosticar_hardware` da superfície `coral.hardware`.

**Retorno:** `dict[str, Any]`

#### `auditar_hardware() -> dict[str, Any]`

Inventário observável e estado dos gates de coesão de Hardware 1.4.9.

**Retorno:** `dict[str, Any]`

#### `usar_backend_serial(backend: BackendSerial)`

Usa temporariamente um backend serial como padrão do contexto atual.

**Implementação:** `coral.hardware.serial`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `backend` | `BackendSerial` | obrigatório | posicional |

**Retorno:** `não declarado`

#### `portas_seriais(*, backend: BackendSerial | None = None) -> tuple[PortaSerial, ...]`

Entrada pública `portas_seriais` da superfície `coral.hardware`.

**Implementação:** `coral.hardware.serial`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `backend` | `BackendSerial \| None` | `None` | nomeado |

**Retorno:** `tuple[PortaSerial, ...]`

#### `conectar_serial(porta: str, velocidade: int = 115200, timeout: float | None = 1.0, *, codificacao: str = 'utf-8', backend: BackendSerial | None = None) -> ConexaoSerial`

Entrada pública `conectar_serial` da superfície `coral.hardware`.

**Implementação:** `coral.hardware.serial`

**Parâmetros**

| Nome | Tipo | Padrão | Modo |
|---|---|---|---|
| `porta` | `str` | obrigatório | posicional |
| `velocidade` | `int` | `115200` | posicional |
| `timeout` | `float \| None` | `1.0` | posicional |
| `codificacao` | `str` | `'utf-8'` | nomeado |
| `backend` | `BackendSerial \| None` | `None` | nomeado |

**Retorno:** `ConexaoSerial`

### Classes e protocolos

#### `CPU(nome: str, nucleos_logicos: int | None, nucleos_fisicos: int | None, frequencia_mhz: float | None)`

Entrada pública `CPU` da superfície `coral.hardware`.

**Atributos declarados**

| Nome | Tipo | Padrão |
|---|---|---|
| `nome` | `str` | obrigatório |
| `nucleos_logicos` | `int \| None` | obrigatório |
| `nucleos_fisicos` | `int \| None` | obrigatório |
| `frequencia_mhz` | `float \| None` | obrigatório |

#### `Memoria(total_bytes: int | None, disponivel_bytes: int | None, percentual_usado: float | None)`

Entrada pública `Memoria` da superfície `coral.hardware`.

**Atributos declarados**

| Nome | Tipo | Padrão |
|---|---|---|
| `total_bytes` | `int \| None` | obrigatório |
| `disponivel_bytes` | `int \| None` | obrigatório |
| `percentual_usado` | `float \| None` | obrigatório |

#### `Disco(dispositivo: str, ponto_montagem: str, sistema_arquivos: str, total_bytes: int | None = None, livre_bytes: int | None = None)`

Entrada pública `Disco` da superfície `coral.hardware`.

**Atributos declarados**

| Nome | Tipo | Padrão |
|---|---|---|
| `dispositivo` | `str` | obrigatório |
| `ponto_montagem` | `str` | obrigatório |
| `sistema_arquivos` | `str` | obrigatório |
| `total_bytes` | `int \| None` | `None` |
| `livre_bytes` | `int \| None` | `None` |

#### `Bateria(percentual: float | None, conectada: bool | None, segundos_restantes: int | None)`

Entrada pública `Bateria` da superfície `coral.hardware`.

**Atributos declarados**

| Nome | Tipo | Padrão |
|---|---|---|
| `percentual` | `float \| None` | obrigatório |
| `conectada` | `bool \| None` | obrigatório |
| `segundos_restantes` | `int \| None` | obrigatório |

#### `ConexaoSerialFechada(...)`

Uma operação foi solicitada depois do fechamento da conexão.

**Implementação:** `coral.hardware.serial`

#### `DesconexaoSerial(...)`

A porta deixou de estar conectada durante a sessão.

**Implementação:** `coral.hardware.serial`

#### `BackendSerial(...)`

Contrato mínimo de backend serial usado por ``ConexaoSerial``.

**Implementação:** `coral.hardware.serial`

**Métodos e propriedades públicas**

| Nome | Tipo | Assinatura | Retorno | Descrição |
|---|---|---|---|---|
| `abrir` | método | `abrir(porta: str, velocidade: int, timeout: float \| None) -> TransporteSerial` | `TransporteSerial` | Sem docstring própria na release. |
| `listar_portas` | método | `listar_portas() -> tuple[PortaSerial, ...]` | `tuple[PortaSerial, ...]` | Sem docstring própria na release. |

#### `BackendSerialReal(...)`

Adaptador do pyserial, carregado apenas quando realmente necessário.

**Implementação:** `coral.hardware.serial`

**Métodos e propriedades públicas**

| Nome | Tipo | Assinatura | Retorno | Descrição |
|---|---|---|---|---|
| `abrir` | método | `abrir(porta: str, velocidade: int, timeout: float \| None) -> TransporteSerial` | `TransporteSerial` | Sem docstring própria na release. |
| `listar_portas` | método | `listar_portas() -> tuple[PortaSerial, ...]` | `tuple[PortaSerial, ...]` | Sem docstring própria na release. |

#### `BackendSerialSimulado() -> None`

Backend serial em memória, sem espera real e sem dependências externas.

**Implementação:** `coral.hardware.serial`

**Métodos e propriedades públicas**

| Nome | Tipo | Assinatura | Retorno | Descrição |
|---|---|---|---|---|
| `registrar_porta` | método | `registrar_porta(dispositivo: str = 'SIM0', *, descricao: str = 'Porta serial simulada', fabricante: str \| None = 'Coral', vid: int \| None = None, pid: int \| None = None) -> PortaSerial` | `PortaSerial` | Sem docstring própria na release. |
| `remover_porta` | método | `remover_porta(dispositivo: str) -> None` | `None` | Sem docstring própria na release. |
| `desconectar` | método | `desconectar(dispositivo: str) -> None` | `None` | Sem docstring própria na release. |
| `reconectar` | método | `reconectar(dispositivo: str) -> None` | `None` | Sem docstring própria na release. |
| `injetar_recebimento` | método | `injetar_recebimento(dispositivo: str, dados: bytes \| bytearray \| str, *, codificacao: str = 'utf-8') -> int` | `int` | Sem docstring própria na release. |
| `dados_enviados` | método | `dados_enviados(dispositivo: str, *, limpar: bool = False) -> bytes` | `bytes` | Sem docstring própria na release. |
| `limpar` | método | `limpar(dispositivo: str \| None = None) -> None` | `None` | Sem docstring própria na release. |
| `listar_portas` | método | `listar_portas() -> tuple[PortaSerial, ...]` | `tuple[PortaSerial, ...]` | Sem docstring própria na release. |
| `abrir` | método | `abrir(porta: str, velocidade: int, timeout: float \| None) -> TransporteSerial` | `TransporteSerial` | Sem docstring própria na release. |

#### `ConexaoSerial(porta: str, velocidade: int = 115200, timeout: float | None = 1.0, *, codificacao: str = 'utf-8', backend: BackendSerial | None = None)`

Entrada pública `ConexaoSerial` da superfície `coral.hardware`.

**Implementação:** `coral.hardware.serial`

**Métodos e propriedades públicas**

| Nome | Tipo | Assinatura | Retorno | Descrição |
|---|---|---|---|---|
| `aberta` | propriedade | `aberta() -> bool` | `bool` | Sem docstring própria na release. |
| `enviar_bytes` | método | `enviar_bytes(dados: bytes \| bytearray) -> int` | `int` | Sem docstring própria na release. |
| `enviar` | método | `enviar(texto: Any, *, terminar_linha: bool = False) -> int` | `int` | Sem docstring própria na release. |
| `ler` | método | `ler(quantidade: int = 1) -> bytes` | `bytes` | Sem docstring própria na release. |
| `ler_linha` | método | `ler_linha() -> str` | `str` | Sem docstring própria na release. |
| `fechar` | método | `fechar() -> None` | `None` | Sem docstring própria na release. |

#### `PortaSerial(dispositivo: str, descricao: str = '', fabricante: str | None = None, vid: int | None = None, pid: int | None = None)`

Entrada pública `PortaSerial` da superfície `coral.hardware`.

**Implementação:** `coral.hardware.serial`

**Atributos declarados**

| Nome | Tipo | Padrão |
|---|---|---|
| `dispositivo` | `str` | obrigatório |
| `descricao` | `str` | `''` |
| `fabricante` | `str \| None` | `None` |
| `vid` | `int \| None` | `None` |
| `pid` | `int \| None` | `None` |

### Exceções

#### `DependenciaHardwareAusente(...)`

Entrada pública `DependenciaHardwareAusente` da superfície `coral.hardware`.

#### `ErroSerial(...)`

Erro público base da camada serial Coral.

**Implementação:** `coral.hardware.serial`

#### `DependenciaSerialAusente(...)`

pyserial não está disponível para o backend real.

**Implementação:** `coral.hardware.serial`

#### `ErroConfiguracaoSerial(...)`

Parâmetro serial inválido antes da abertura da porta.

**Implementação:** `coral.hardware.serial`

<!-- /AUTO:API -->

## Compatibilidade e dependências

`psutil` e `pyserial` são opcionais. A importação do módulo permanece possível sem elas; a capacidade específica informa a ausência quando necessária. Informações disponíveis também variam por sistema operacional e máquina.
