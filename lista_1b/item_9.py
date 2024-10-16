import numpy as np
import matplotlib.pyplot as plt
from math import comb

# Definindo os parâmetros
M = 200  # Número total de roteadores
TPR = 0.9  # Taxa de verdadeiros positivos
FPR = 0.1  # Taxa de falsos positivos
FNR = 1 - TPR  # Taxa de falsos negativos
TNR = 1 - FPR  # Taxa de verdadeiros negativos
P_inf = 0.2  # Probabilidade de uma residência estar infectada
P_not_inf = 1 - P_inf  # Probabilidade de uma residência não estar infectada

# Função para P(V | ha)
def P_V_given_ha(V, M, TPR, FPR, FNR, TNR, P_inf, P_not_inf):
    prob_alarm = (TPR * P_inf) + (FPR * P_not_inf)
    prob_no_alarm = (TNR * P_not_inf) + (FNR * P_inf)
    return comb(M, V) * (prob_alarm ** V) * (prob_no_alarm ** (M - V))

# Função para P(V | hb)
def P_V_given_hb(V, M, FPR, TNR, P_inf, P_not_inf):
    prob_alarm = (FPR * P_inf) + (FPR * P_not_inf)
    prob_no_alarm = (TNR * P_not_inf) + (TNR * P_inf)
    return comb(M, V) * (prob_alarm ** V) * (prob_no_alarm ** (M - V))

# Valores de V (de 0 a M)
V_values = np.arange(0, M+1)

# Calculando as PMFs para P(V | ha) e P(V | hb)
P_ha_values = [P_V_given_ha(V, M, TPR, FPR, FNR, TNR, P_inf, P_not_inf) for V in V_values]
P_hb_values = [P_V_given_hb(V, M, FPR, TNR, P_inf, P_not_inf) for V in V_values]

# Plotando as curvas
plt.figure(figsize=(10, 6))
plt.plot(V_values, P_ha_values, label='$P(V | h_a)$ - Ataque', color='blue', linewidth=2)
plt.plot(V_values, P_hb_values, label='$P(V | h_b)$ - Não Ataque', color='red', linewidth=2)
plt.xlabel('Número de roteadores que alarmam ($V$)')
plt.ylabel('Probabilidade')
plt.title('Distribuição do número de roteadores que alarmam ($V$)')
plt.legend(loc='best')
plt.grid(True)
plt.show()  # Para visualizar o gráfico, descomente esta linha

