# Métodos Numéricos — 2º GQ

Projeto desenvolvido para a disciplina de **Métodos Numéricos**.

## Problema 2: Investigação de Degradação de Desempenho em Servidores

Uma empresa de tecnologia realiza o monitoramento contínuo da temperatura dos processadores de três servidores (`SRV-01`, `SRV-02` e `SRV-03`) em seu data center. As medições foram coletadas em intervalos de 1 hora durante um período de 10 horas (das 14:00 às 23:00) e armazenadas no arquivo `data/temperaturas.csv`.

Durante o período, foram registrados três episódios de degradação de desempenho no arquivo `data/incidentes.log`:
* **15:30:00** ($t = 15.5\text{ h}$)
* **18:30:00** ($t = 18.5\text{ h}$)
* **21:30:00** ($t = 21.5\text{ h}$)

Como os incidentes ocorreram em horários intermediários nos quais não havia medição direta de temperatura, foram aplicados métodos numéricos de **interpolação polinomial** para estimar o comportamento térmico contínuo e verificar a violação do limite operacional de **80 °C**.

---

## Métodos Implementados

O pacote `metodos` contém implementações próprias desenvolvidas do zero (sem bibliotecas externas prontas de interpolação):

1. **Método de Interpolação de Lagrange (`src/metodos/lagrange.py`):**
   * Implementação clássica utilizando os polinômios base de Lagrange $L_i(t)$.
2. **Método de Interpolação de Newton (`src/metodos/newton.py`):**
   * Cálculo da tabela de diferenças divididas de forma *in-place* e avaliação eficiente pela forma aninhada de Horner em $O(n)$.

> **Unicidade do Polinômio Interpolador:**  
> Dados $n+1$ pontos com abscissas distintas, o polinômio interpolador é único. Portanto, $P_{\text{Lagrange}}(t) \equiv P_{\text{Newton}}(t)$, permitindo validação cruzada entre as duas implementações.

---

## Estrutura do Projeto

```text
projeto-MN/
├── data/
│   ├── incidentes.log          # Registro dos alertas de incidentes
│   └── temperaturas.csv        # Medições horárias de telemetria
├── notebook/
│   └── project.ipynb           # Notebook Jupyter com resolução completa, análises e gráficos
├── src/
│   └── metodos/
│       ├── __init__.py         # Módulo do pacote
│       ├── lagrange.py         # Interpolação de Lagrange
│       └── newton.py           # Interpolação de Newton
├── tests/
│   ├── test_dados_reais.py     # Teste com as medições reais de cada incidente
│   ├── test_lagrange.py        # Teste unitário do Método de Lagrange
│   └── test_newton.py          # Teste unitário do Método de Newton
├── pyproject.toml              # Configuração do pacote Python para instalação via pip
└── README.md                   # Documentação do projeto
```

---

## Requisitos

* Python 3.10 ou superior
* pip
* Jupyter Notebook / JupyterLab / VS Code
* Bibliotecas: `numpy`, `pandas`, `matplotlib`, `pytest`

---

## Instalação

Clone ou acesse o diretório do projeto:

```bash
cd projeto-MN
```

Instale o pacote em modo editável utilizando o `pip`:

```bash
pip install -e .
```

---

## Utilização

Após a instalação, as funções podem ser importadas normalmente:

```python
from metodos.newton import interpolacao_newton
from metodos.lagrange import interpolacao_lagrange

# Exemplo de interpolação com 3 pontos conhecidos
x = [14, 15, 16]
y = [58.99, 59.40, 63.77]
horario = 15.5

temp_newton = interpolacao_newton(x, y, horario)
temp_lagrange = interpolacao_lagrange(x, y, horario)

print(f"Temperatura Newton:   {temp_newton:.2f} °C")
print(f"Temperatura Lagrange: {temp_lagrange:.2f} °C")
```

---

## Execução dos Testes

Para executar os testes automatizados com o `pytest`:

```bash
pytest
```

Ou execute individualmente cada arquivo de teste:

```bash
python tests/test_newton.py
python tests/test_lagrange.py
python tests/test_dados_reais.py
```

---

## Notebook

O notebook presente no diretório `notebook/project.ipynb` reúne a análise completa:
* Carregamento e exploração tabular dos dados;
* Fundamentação teórica dos métodos de Newton e Lagrange;
* Execução e teste das implementações;
* Tabela comparativa e validação do Teorema da Unicidade;
* Representação gráfica *clean* e autoexplicativa;
* Resolução formal fundamentada dos itens **(a)**, **(b)**, **(c)** e **(d)**.

---

## Resumo dos Resultados

### (a) Temperatura estimada nos horários dos incidentes

| Servidor | Incidente 1 (15:30) | Incidente 2 (18:30) | Incidente 3 (21:30) |
| :--- | :---: | :---: | :---: |
| **SRV-01** | **49.11 °C** | **48.32 °C** | **49.30 °C** |
| **SRV-02** | **57.15 °C** | **61.30 °C** | **75.78 °C** |
| **SRV-03** | **61.09 °C** | **80.63 °C** | **61.22 °C** |

*(Lagrange e Newton produzem resultados numericamente equivalentes com diferença $\le 1.42 \times 10^{-14}\text{ °C}$).*

### (b) Servidores próximos ou superiores ao limite de 80 °C
1. **SRV-03:** Ultrapassou o limite operacional de 80 °C às **18:30:00**, atingindo estimativa de **80.63 °C**.
2. **SRV-02:** Apresentou temperatura próxima ao limite operacional às **21:30:00**, atingindo **75.78 °C**.
3. **SRV-01:** Operou em faixa segura em todo o período monitorado (entre **48.30 °C** e **51.37 °C**).

### (c) Representação Gráfica
Construída de forma limpa e objetiva no notebook, evidenciando as trajetórias térmicas, os pontos das medições horárias cheias, os pontos estimados nos incidentes e a linha crítica de 80 °C.

### (d) Diagnóstico dos Incidentes
* **15:30:00 (Causa Não-Térmica):** Temperaturas normais em todos os servidores. Degradação relacionada a causas externas (I/O, rede ou concorrência de software).
* **18:30:00 (Causa Térmica — `SRV-03`):** Superaquecimento crítico acima de 80 °C acionando proteção de *thermal throttling* (redução compulsória de clock).
* **21:30:00 (Causa Térmica — `SRV-02`):** Estresse térmico severo (~76 °C), levando a contenção e redução de desempenho.
