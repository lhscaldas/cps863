import numpy as np
import matplotlib.pyplot as plt

# Definindo os parâmetros
M = 200
P_h_a = 0.1
P_h_b = 0.9
TPR = 0.24  # True Positive Rate (P[L = 1 | ha])
FPR = 0.1   # False Positive Rate (P[L = 1 | hb])

# Funções para P[ha|D] e P[hb|D] em função de V
def P_ha_given_D(V, M, TPR, FPR, P_h_a, P_h_b):
    P_D_given_ha = (TPR**V) * ((1 - TPR)**(M - V))
    P_D_given_hb = (FPR**V) * ((1 - FPR)**(M - V))
    return (P_D_given_ha * P_h_a) / (P_D_given_ha * P_h_a + P_D_given_hb * P_h_b)

def P_hb_given_D(V, M, TPR, FPR, P_h_a, P_h_b):
    P_D_given_ha = (TPR**V) * ((1 - TPR)**(M - V))
    P_D_given_hb = (FPR**V) * ((1 - FPR)**(M - V))
    return (P_D_given_hb * P_h_b) / (P_D_given_ha * P_h_a + P_D_given_hb * P_h_b)

# Valores de V (de 0 a M)
V_values = np.arange(0, M + 1)

# Calculando as probabilidades para cada V
P_ha_values = [P_ha_given_D(V, M, TPR, FPR, P_h_a, P_h_b) for V in V_values]
P_hb_values = [P_hb_given_D(V, M, TPR, FPR, P_h_a, P_h_b) for V in V_values]

# Plotando as curvas
plt.figure(figsize=(10, 6))
plt.plot(V_values, P_ha_values, label='$P[h_a|D]$', color='blue', linewidth=2)
plt.plot(V_values, P_hb_values, label='$P[h_b|D]$', color='red', linewidth=2)
plt.xlabel('Número de roteadores que sinalizam um ataque ($V$)')
plt.ylabel('Probabilidade posterior')
plt.title('Curvas de $P[h_a|D]$ e $P[h_b|D]$ em função de $V$')
plt.legend(loc='best')
plt.grid(True)
plt.show()  
