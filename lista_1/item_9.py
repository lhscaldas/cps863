import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

# Definindo os parâmetros
M = 200
TPR = 0.9  # True Positive Rate (P[L = 1 | ha])
FPR = 0.1  # False Positive Rate (P[L = 1 | hb])

# Valores de V (de 0 a M)
V_values = np.arange(0, M+1)

# Calculando as PMFs para P(V | ha) e P(V | hb)
P_V_given_ha = binom.pmf(V_values, M, TPR)  # Quando há ataque
P_V_given_hb = binom.pmf(V_values, M, FPR)  # Quando não há ataque

# Plotando as curvas
plt.figure(figsize=(10, 6))
plt.plot(V_values, P_V_given_ha, label='P(V | $h_a$) - Ataque', color='blue', linewidth=2)
plt.plot(V_values, P_V_given_hb, label='P(V | $h_b$) - Não Ataque', color='red', linewidth=2)
plt.xlabel('Número de roteadores que alarmam ($V$)')
plt.ylabel('Probabilidade')
plt.title('Distribuição do número de roteadores que alarmam ($V$)')
plt.legend(loc='best')
plt.grid(True)
plt.show()  # Para visualizar o gráfico, descomente esta linha
