# Missão Aurora Siger

## Sistema Inteligente de Análise e Decisão da Colônia Marciana

O Aurora Siger é um sistema computacional autônomo desenvolvido para monitorar, analisar e otimizar os sistemas críticos de sobrevivência de uma colônia em Marte.

Projetado para operar em um ambiente hostil e com alta latência de comunicação com a Terra, o sistema utiliza:

- Programação Orientada a Objetos (POO)
- Lógica condicional para tomada de decisão
- Machine Learning com regressão linear
- Monitoramento energético em tempo real
- Protocolos automáticos de contingência

O objetivo principal é garantir a estabilidade energética e priorizar o suporte à vida em cenários extremos.

---

# Arquitetura do Sistema

A aplicação foi estruturada em torno da classe `GerenciadorHabitat`, responsável por centralizar o estado operacional da colônia e coordenar as decisões automatizadas.

O fluxo do sistema é dividido em três etapas principais:

---

## 1. Coleta de Dados (Entrada)

O sistema monitora continuamente informações ambientais e operacionais, incluindo:

- Velocidade do vento
- Temperatura externa
- Geração fotovoltaica
- Consumo energético das unidades
- Nível do banco de baterias

Todos os dados são organizados em uma estrutura centralizada:

```python
self.estado
```

Isso permite atualizações dinâmicas e análise em tempo real.

---

## 2. Processamento Inteligente

### Modelagem Preditiva com Machine Learning

A função `executar_modelo_preditivo()` utiliza dados históricos de telemetria para treinar um modelo de Regressão Linear com `scikit-learn`.

O modelo é capaz de prever:

- geração energética futura
- eficiência da rede
- comportamento da fonte aerodinâmica

Exemplo:

> Estimar a geração eólica com base na velocidade atual do vento.

---

### Avaliação de Segurança Energética

O método `avaliar_seguranca_rede()` compara:

- suprimento total de energia
- demanda agregada da colônia
- capacidade restante das baterias

Com base nessas informações, o sistema classifica o estado da rede como:

| Estado | Condição |
|---|---|
| Nominal | Operação estável |
| Alerta | Déficit energético controlado |
| Emergência | Risco crítico ao suporte vital |

---

## 3. Resposta Automatizada

Quando uma condição crítica é detectada, o protocolo de contingência é acionado automaticamente.

### Critérios de Emergência

O sistema entra em modo crítico quando:

```text
Bateria < 50%
AND
Demanda > Suprimento
AND
Previsão de Tempo Ruim = True
```

### Ações Executadas

- Desligamento de módulos não essenciais
- Redução automática do consumo energético
- Priorização total do suporte à vida
- Mitigação do déficit energético

Módulos desativados automaticamente:

- Laboratório de Pesquisa
- Unidade de Extração

---

# Simulações Executadas

## Cenário 1 — Déficit Energético Controlado

### Configuração

| Variável | Valor |
|---|---|
| Velocidade do vento | 11.0 m/s |
| Baterias | 85% |
| Tempo ruim | False |

### Resultado

O modelo preditivo estima:

```text
Potência aerodinâmica ≈ 27.50 kW
```

Apesar da demanda total superar a geração disponível, o sistema mantém estabilidade operacional e emite apenas um alerta preventivo.

---

## Cenário 2 — Tempestade de Poeira e Contingência Crítica

### Configuração

| Variável | Valor |
|---|---|
| Geração solar | 2.0 kW |
| Baterias | 42% |
| Tempo ruim | True |

### Resultado

O sistema detecta uma condição crítica e:

- altera o estado da rede para `emergencia`
- desliga módulos secundários
- reduz o consumo total para `30.0 kW`
- prioriza exclusivamente os sistemas vitais

---

# Tecnologias Utilizadas

- Python 3
- NumPy
- Scikit-learn
- Programação Orientada a Objetos
- Machine Learning
- Regressão Linear

---

# Instalação

## Pré-requisitos

- Python 3.10+
- pip instalado

---

## Instale as dependências

```bash
pip install numpy scikit-learn
```

---

# Execução

Salve o arquivo principal como:

```bash
sistema_aurora.py
```

Execute no terminal:

```bash
python sistema_aurora.py
```

---

# Estrutura do Projeto

```text
aurora-siger/
├── sistema_aurora.py
└── README.md
```

---

# Componentes Principais

## `GerenciadorHabitat`

Classe principal responsável por:

- armazenar o estado da colônia
- avaliar segurança energética
- executar respostas automáticas

---

## `executar_modelo_preditivo()`

Função responsável por:

- treinar o modelo de regressão linear
- calcular métricas de desempenho
- gerar previsões energéticas

Métricas analisadas:

- R² Score
- MSE (Mean Squared Error)

---

## `main`

Bloco principal responsável por:

- executar os cenários simulados
- orquestrar eventos climáticos
- imprimir auditorias operacionais

---

# Objetivo Acadêmico

Este projeto foi desenvolvido com foco em:

- simulação de sistemas autônomos
- modelagem preditiva
- automação de decisões energéticas
- engenharia de software orientada a objetos

---