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

#### `psutil_disponivel`

Detectar inventário avançado.

**Exemplo**

```coral
de coral.hardware importe cpu, memoria, discos, psutil_disponivel

se psutil_disponivel() então
    defina processador como cpu()
    defina ram como memoria()
    defina unidades como discos()
```

**Retorno**

Retorna um valor lógico que indica o resultado da verificação.

:::details Detalhes técnicos

**Assinatura:** `psutil_disponivel() -> bool`

**Origem da implementação:** `coral.hardware`

**Arquivo na release:** `coral/hardware/__init__.py`

:::

#### `serial_disponivel`

Detectar backend serial real.

**Retorno**

Retorna um valor lógico que indica o resultado da verificação.

:::details Detalhes técnicos

**Assinatura:** `serial_disponivel() -> bool`

**Origem da implementação:** `coral.hardware`

**Arquivo na release:** `coral/hardware/__init__.py`

:::

#### `cpu`

Consultar CPU.

**Exemplo**

```coral
se psutil_disponivel() então
    defina processador como cpu()
    defina ram como memoria()
    defina unidades como discos()
    mostre processador.nucleos_logicos
```

**Retorno**

Retorna um valor declarado como `CPU`.

:::details Detalhes técnicos

**Assinatura:** `cpu() -> CPU`

**Origem da implementação:** `coral.hardware`

**Arquivo na release:** `coral/hardware/__init__.py`

:::

#### `memoria`

Consultar RAM.

**Exemplo**

```coral
se psutil_disponivel() então
    defina processador como cpu()
    defina ram como memoria()
    defina unidades como discos()
    mostre processador.nucleos_logicos
    mostre ram.total_bytes
```

**Retorno**

Retorna um valor declarado como `Memoria`.

:::details Detalhes técnicos

**Assinatura:** `memoria() -> Memoria`

**Origem da implementação:** `coral.hardware`

**Arquivo na release:** `coral/hardware/__init__.py`

:::

#### `discos`

Listar discos.

**Exemplo**

```coral
defina processador como cpu()
    defina ram como memoria()
    defina unidades como discos()
    mostre processador.nucleos_logicos
    mostre ram.total_bytes
    mostre quantidade de unidades
```

**Retorno**

Retorna um valor declarado como `tuple[Disco, ...]`.

:::details Detalhes técnicos

**Assinatura:** `discos() -> tuple[Disco, ...]`

**Origem da implementação:** `coral.hardware`

**Arquivo na release:** `coral/hardware/__init__.py`

:::

#### `bateria`

Consultar bateria.

**Retorno**

Retorna um valor declarado como `Bateria | None`.

:::details Detalhes técnicos

**Assinatura:** `bateria() -> Bateria \| None`

**Origem da implementação:** `coral.hardware`

**Arquivo na release:** `coral/hardware/__init__.py`

:::

#### `diagnosticar_hardware`

Produz informações de diagnóstico para hardware.

**Retorno**

Retorna um valor declarado como `dict[str, Any]`.

:::details Detalhes técnicos

**Assinatura:** `diagnosticar_hardware() -> dict[str, Any]`

**Origem da implementação:** `coral.hardware`

**Arquivo na release:** `coral/hardware/__init__.py`

:::

#### `auditar_hardware`

Inventário observável e estado dos gates de coesão de Hardware 1.4.9.

**Retorno**

Retorna um valor declarado como `dict[str, Any]`.

:::details Detalhes técnicos

**Assinatura:** `auditar_hardware() -> dict[str, Any]`

**Origem da implementação:** `coral.hardware`

**Arquivo na release:** `coral/hardware/__init__.py`

:::

#### `usar_backend_serial`

Usa temporariamente um backend serial como padrão do contexto atual.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `backend` | Backend usado para executar a operação. | `BackendSerial` | obrigatório |

**Retorno**

Não produz um valor de retorno útil; o efeito ocorre no estado ou recurso alvo.

:::details Detalhes técnicos

**Assinatura:** `usar_backend_serial(backend: BackendSerial)`

**Origem da implementação:** `coral.hardware.serial`

**Arquivo na release:** `coral/hardware/serial.py`

:::

#### `portas_seriais`

Obtém portas seriais.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `backend` | Backend usado para executar a operação. | `BackendSerial \| None` | `None` |

**Retorno**

Retorna um valor declarado como `tuple[PortaSerial, ...]`.

:::details Detalhes técnicos

**Assinatura:** `portas_seriais(*, backend: BackendSerial \| None = None) -> tuple[PortaSerial, ...]`

**Origem da implementação:** `coral.hardware.serial`

**Arquivo na release:** `coral/hardware/serial.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `backend` | nomeado |

:::

#### `conectar_serial`

Abrir conexão serial.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `porta` | Valor correspondente a porta. | `str` | obrigatório |
| `velocidade` | Valor correspondente a velocidade. | `int` | `115200` |
| `timeout` | Valor correspondente a timeout. | `float \| None` | `1.0` |
| `codificacao` | Codificação de texto usada na leitura ou escrita. | `str` | `'utf-8'` |
| `backend` | Backend usado para executar a operação. | `BackendSerial \| None` | `None` |

**Retorno**

Retorna um valor declarado como `ConexaoSerial`.

:::details Detalhes técnicos

**Assinatura:** `conectar_serial(porta: str, velocidade: int = 115200, timeout: float \| None = 1.0, *, codificacao: str = 'utf-8', backend: BackendSerial \| None = None) -> ConexaoSerial`

**Origem da implementação:** `coral.hardware.serial`

**Arquivo na release:** `coral/hardware/serial.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `porta` | posicional |
| `velocidade` | posicional |
| `timeout` | posicional |
| `codificacao` | nomeado |
| `backend` | nomeado |

:::

### Classes e protocolos

#### `CPU`

Representa CPU na API de `coral.hardware`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | obrigatório |
| `nucleos_logicos` | Valor correspondente a nucleos logicos. | `int \| None` | obrigatório |
| `nucleos_fisicos` | Valor correspondente a nucleos fisicos. | `int \| None` | obrigatório |
| `frequencia_mhz` | Valor correspondente a frequencia mhz. | `float \| None` | obrigatório |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `nome` | Nome usado para identificar o objeto criado ou consultado. | `str` | obrigatório |
| `nucleos_logicos` | Valor correspondente a nucleos logicos. | `int \| None` | obrigatório |
| `nucleos_fisicos` | Valor correspondente a nucleos fisicos. | `int \| None` | obrigatório |
| `frequencia_mhz` | Valor correspondente a frequencia mhz. | `float \| None` | obrigatório |

:::details Detalhes técnicos

**Assinatura:** `CPU(nome: str, nucleos_logicos: int \| None, nucleos_fisicos: int \| None, frequencia_mhz: float \| None)`

**Origem da implementação:** `coral.hardware`

**Arquivo na release:** `coral/hardware/__init__.py`

:::

#### `Memoria`

Representa Memoria na API de `coral.hardware`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `total_bytes` | Valor correspondente a total bytes. | `int \| None` | obrigatório |
| `disponivel_bytes` | Valor correspondente a disponivel bytes. | `int \| None` | obrigatório |
| `percentual_usado` | Valor correspondente a percentual usado. | `float \| None` | obrigatório |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `total_bytes` | Valor correspondente a total bytes. | `int \| None` | obrigatório |
| `disponivel_bytes` | Valor correspondente a disponivel bytes. | `int \| None` | obrigatório |
| `percentual_usado` | Valor correspondente a percentual usado. | `float \| None` | obrigatório |

:::details Detalhes técnicos

**Assinatura:** `Memoria(total_bytes: int \| None, disponivel_bytes: int \| None, percentual_usado: float \| None)`

**Origem da implementação:** `coral.hardware`

**Arquivo na release:** `coral/hardware/__init__.py`

:::

#### `Disco`

Representa Disco na API de `coral.hardware`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `dispositivo` | Valor correspondente a dispositivo. | `str` | obrigatório |
| `ponto_montagem` | Valor correspondente a ponto montagem. | `str` | obrigatório |
| `sistema_arquivos` | Valor correspondente a sistema arquivos. | `str` | obrigatório |
| `total_bytes` | Valor correspondente a total bytes. | `int \| None` | `None` |
| `livre_bytes` | Valor correspondente a livre bytes. | `int \| None` | `None` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `dispositivo` | Valor correspondente a dispositivo. | `str` | obrigatório |
| `ponto_montagem` | Valor correspondente a ponto montagem. | `str` | obrigatório |
| `sistema_arquivos` | Valor correspondente a sistema arquivos. | `str` | obrigatório |
| `total_bytes` | Valor correspondente a total bytes. | `int \| None` | `None` |
| `livre_bytes` | Valor correspondente a livre bytes. | `int \| None` | `None` |

:::details Detalhes técnicos

**Assinatura:** `Disco(dispositivo: str, ponto_montagem: str, sistema_arquivos: str, total_bytes: int \| None = None, livre_bytes: int \| None = None)`

**Origem da implementação:** `coral.hardware`

**Arquivo na release:** `coral/hardware/__init__.py`

:::

#### `Bateria`

Representa Bateria na API de `coral.hardware`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `percentual` | Valor correspondente a percentual. | `float \| None` | obrigatório |
| `conectada` | Valor correspondente a conectada. | `bool \| None` | obrigatório |
| `segundos_restantes` | Valor correspondente a segundos restantes. | `int \| None` | obrigatório |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `percentual` | Valor correspondente a percentual. | `float \| None` | obrigatório |
| `conectada` | Valor correspondente a conectada. | `bool \| None` | obrigatório |
| `segundos_restantes` | Valor correspondente a segundos restantes. | `int \| None` | obrigatório |

:::details Detalhes técnicos

**Assinatura:** `Bateria(percentual: float \| None, conectada: bool \| None, segundos_restantes: int \| None)`

**Origem da implementação:** `coral.hardware`

**Arquivo na release:** `coral/hardware/__init__.py`

:::

#### `ConexaoSerialFechada`

Uma operação foi solicitada depois do fechamento da conexão.

:::details Detalhes técnicos

**Assinatura:** `ConexaoSerialFechada(...)`

**Origem da implementação:** `coral.hardware.serial`

**Arquivo na release:** `coral/hardware/serial.py`

:::

#### `DesconexaoSerial`

A porta deixou de estar conectada durante a sessão.

:::details Detalhes técnicos

**Assinatura:** `DesconexaoSerial(...)`

**Origem da implementação:** `coral.hardware.serial`

**Arquivo na release:** `coral/hardware/serial.py`

:::

#### `BackendSerial`

Contrato mínimo de backend serial usado por ``ConexaoSerial``.

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `abrir` | Abre o valor solicitado. | `TransporteSerial` |
| `listar_portas` | Lista portas. | `tuple[PortaSerial, ...]` |

:::details Detalhes técnicos

**Assinatura:** `BackendSerial(...)`

**Origem da implementação:** `coral.hardware.serial`

**Arquivo na release:** `coral/hardware/serial.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `abrir` | método | `abrir(porta: str, velocidade: int, timeout: float \| None) -> TransporteSerial` |
| `listar_portas` | método | `listar_portas() -> tuple[PortaSerial, ...]` |

:::

#### `BackendSerialReal`

Adaptador do pyserial, carregado apenas quando realmente necessário.

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `abrir` | Abre o valor solicitado. | `TransporteSerial` |
| `listar_portas` | Lista portas. | `tuple[PortaSerial, ...]` |

:::details Detalhes técnicos

**Assinatura:** `BackendSerialReal(...)`

**Origem da implementação:** `coral.hardware.serial`

**Arquivo na release:** `coral/hardware/serial.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `abrir` | método | `abrir(porta: str, velocidade: int, timeout: float \| None) -> TransporteSerial` |
| `listar_portas` | método | `listar_portas() -> tuple[PortaSerial, ...]` |

:::

#### `BackendSerialSimulado`

Backend serial em memória, sem espera real e sem dependências externas.

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `registrar_porta` | Registra porta. | `PortaSerial` |
| `remover_porta` | Remove porta. | `None` |
| `desconectar` | Executa a operação `desconectar` disponibilizada por `coral.hardware`. | `None` |
| `reconectar` | Executa a operação `reconectar` disponibilizada por `coral.hardware`. | `None` |
| `injetar_recebimento` | Executa a operação `injetar_recebimento` disponibilizada por `coral.hardware`. | `int` |
| `dados_enviados` | Obtém dados enviados. | `bytes` |
| `limpar` | Limpa o valor solicitado. | `None` |
| `listar_portas` | Lista portas. | `tuple[PortaSerial, ...]` |
| `abrir` | Abre o valor solicitado. | `TransporteSerial` |

:::details Detalhes técnicos

**Assinatura:** `BackendSerialSimulado() -> None`

**Origem da implementação:** `coral.hardware.serial`

**Arquivo na release:** `coral/hardware/serial.py`

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `registrar_porta` | método | `registrar_porta(dispositivo: str = 'SIM0', *, descricao: str = 'Porta serial simulada', fabricante: str \| None = 'Coral', vid: int \| None = None, pid: int \| None = None) -> PortaSerial` |
| `remover_porta` | método | `remover_porta(dispositivo: str) -> None` |
| `desconectar` | método | `desconectar(dispositivo: str) -> None` |
| `reconectar` | método | `reconectar(dispositivo: str) -> None` |
| `injetar_recebimento` | método | `injetar_recebimento(dispositivo: str, dados: bytes \| bytearray \| str, *, codificacao: str = 'utf-8') -> int` |
| `dados_enviados` | método | `dados_enviados(dispositivo: str, *, limpar: bool = False) -> bytes` |
| `limpar` | método | `limpar(dispositivo: str \| None = None) -> None` |
| `listar_portas` | método | `listar_portas() -> tuple[PortaSerial, ...]` |
| `abrir` | método | `abrir(porta: str, velocidade: int, timeout: float \| None) -> TransporteSerial` |

:::

#### `ConexaoSerial`

Representa sessão serial.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `porta` | Valor correspondente a porta. | `str` | obrigatório |
| `velocidade` | Valor correspondente a velocidade. | `int` | `115200` |
| `timeout` | Valor correspondente a timeout. | `float \| None` | `1.0` |
| `codificacao` | Codificação de texto usada na leitura ou escrita. | `str` | `'utf-8'` |
| `backend` | Backend usado para executar a operação. | `BackendSerial \| None` | `None` |

**Operações públicas da classe**

| Nome | O que faz | Retorno |
|---|---|---|
| `aberta` | Indica o estado de aberta. | `bool` |
| `enviar_bytes` | Executa a operação `enviar_bytes` disponibilizada por `coral.hardware`. | `int` |
| `enviar` | Executa a operação `enviar` disponibilizada por `coral.hardware`. | `int` |
| `ler` | Lê o valor solicitado. | `bytes` |
| `ler_linha` | Lê linha. | `str` |
| `fechar` | Fecha o valor solicitado. | `None` |

:::details Detalhes técnicos

**Assinatura:** `ConexaoSerial(porta: str, velocidade: int = 115200, timeout: float \| None = 1.0, *, codificacao: str = 'utf-8', backend: BackendSerial \| None = None)`

**Origem da implementação:** `coral.hardware.serial`

**Arquivo na release:** `coral/hardware/serial.py`

**Modo dos parâmetros**

| Parâmetro | Modo |
|---|---|
| `porta` | posicional |
| `velocidade` | posicional |
| `timeout` | posicional |
| `codificacao` | nomeado |
| `backend` | nomeado |

**Assinaturas de métodos e propriedades**

| Nome | Tipo | Assinatura |
|---|---|---|
| `aberta` | propriedade | `aberta() -> bool` |
| `enviar_bytes` | método | `enviar_bytes(dados: bytes \| bytearray) -> int` |
| `enviar` | método | `enviar(texto: Any, *, terminar_linha: bool = False) -> int` |
| `ler` | método | `ler(quantidade: int = 1) -> bytes` |
| `ler_linha` | método | `ler_linha() -> str` |
| `fechar` | método | `fechar() -> None` |

:::

#### `PortaSerial`

Representa PortaSerial na API de `coral.hardware`.

**Parâmetros**

| Parâmetro | Significado | Tipo | Padrão |
|---|---|---|---|
| `dispositivo` | Valor correspondente a dispositivo. | `str` | obrigatório |
| `descricao` | Valor correspondente a descricao. | `str` | `''` |
| `fabricante` | Valor correspondente a fabricante. | `str \| None` | `None` |
| `vid` | Valor correspondente a vid. | `int \| None` | `None` |
| `pid` | Valor correspondente a pid. | `int \| None` | `None` |

**Atributos públicos**

| Nome | Significado | Tipo | Padrão |
|---|---|---|---|
| `dispositivo` | Valor correspondente a dispositivo. | `str` | obrigatório |
| `descricao` | Valor correspondente a descricao. | `str` | `''` |
| `fabricante` | Valor correspondente a fabricante. | `str \| None` | `None` |
| `vid` | Valor correspondente a vid. | `int \| None` | `None` |
| `pid` | Valor correspondente a pid. | `int \| None` | `None` |

:::details Detalhes técnicos

**Assinatura:** `PortaSerial(dispositivo: str, descricao: str = '', fabricante: str \| None = None, vid: int \| None = None, pid: int \| None = None)`

**Origem da implementação:** `coral.hardware.serial`

**Arquivo na release:** `coral/hardware/serial.py`

:::

### Exceções

#### `DependenciaHardwareAusente`

Representa a condição de erro DependenciaHardwareAusente.

:::details Detalhes técnicos

**Assinatura:** `DependenciaHardwareAusente(...)`

**Origem da implementação:** `coral.hardware`

**Arquivo na release:** `coral/hardware/__init__.py`

:::

#### `ErroSerial`

Erro público base da camada serial Coral.

:::details Detalhes técnicos

**Assinatura:** `ErroSerial(...)`

**Origem da implementação:** `coral.hardware.serial`

**Arquivo na release:** `coral/hardware/serial.py`

:::

#### `DependenciaSerialAusente`

pyserial não está disponível para o backend real.

:::details Detalhes técnicos

**Assinatura:** `DependenciaSerialAusente(...)`

**Origem da implementação:** `coral.hardware.serial`

**Arquivo na release:** `coral/hardware/serial.py`

:::

#### `ErroConfiguracaoSerial`

Parâmetro serial inválido antes da abertura da porta.

:::details Detalhes técnicos

**Assinatura:** `ErroConfiguracaoSerial(...)`

**Origem da implementação:** `coral.hardware.serial`

**Arquivo na release:** `coral/hardware/serial.py`

:::

<!-- /AUTO:API -->

## Compatibilidade e dependências

`psutil` e `pyserial` são opcionais. A importação do módulo permanece possível sem elas; a capacidade específica informa a ausência quando necessária. Informações disponíveis também variam por sistema operacional e máquina.
