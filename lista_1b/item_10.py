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

# Função para calcular P(V | h_a)
def P_V_given_ha(V, M, TPR, FPR, FNR, TNR, P_inf, P_not_inf):
    prob_alarm = (TPR * P_inf) + (FPR * P_not_inf)
    prob_no_alarm = (TNR * P_not_inf) + (FNR * P_inf)
    return comb(M, V) * (prob_alarm ** V) * (prob_no_alarm ** (M - V))

# Função para calcular P(V | h_b)
def P_V_given_hb(V, M, FPR, TNR, P_inf, P_not_inf):
    prob_alarm = (FPR * P_inf) + (FPR * P_not_inf)
    prob_no_alarm = (TNR * P_not_inf) + (TNR * P_inf)
    return comb(M, V) * (prob_alarm ** V) * (prob_no_alarm ** (M - V))

# Função para calcular TPR e FPR para diferentes limiares
def calculate_roc(M, TPR, FPR, P_inf, P_not_inf):
    thresholds = np.arange(0, M + 1)  # Possíveis limiares
    tpr_list = []
    fpr_list = []

    for threshold in thresholds:
        # Calcula TPR e FPR para cada limiar
        true_positives = sum(P_V_given_ha(v, M, TPR, FPR, FNR, TNR, P_inf, P_not_inf) for v in range(threshold, M + 1))
        false_positives = sum(P_V_given_hb(v, M, FPR, TNR, P_inf, P_not_inf) for v in range(threshold, M + 1))
        
        # Estimando as taxas
        tpr = true_positives / sum(P_V_given_ha(v, M, TPR, FPR, FNR, TNR, P_inf, P_not_inf) for v in range(M + 1))
        fpr = false_positives / sum(P_V_given_hb(v, M, FPR, TNR, P_inf, P_not_inf) for v in range(M + 1))

        tpr_list.append(tpr)
        fpr_list.append(fpr)

    return np.array(tpr_list), np.array(fpr_list)


# Função para plotar a curva ROC
def plot_roc():
    tpr_list, fpr_list = calculate_roc(M, TPR, FPR, P_inf, P_not_inf)

    plt.figure(figsize=(10, 6))
    plt.plot(fpr_list, tpr_list, color='blue', lw=2)
    plt.plot([0, 1], [0, 1], color='red', linestyle='--')  # Linha de referência
    plt.xlabel('Taxa de Falsos Positivos (FPR)')
    plt.ylabel('Taxa de Verdadeiros Positivos (TPR)')
    plt.title('Curva ROC')
    # plt.xlim([0.0, 1.0])
    # plt.ylim([0.0, 1.0])
    plt.grid(True)
    plt.show()

# Chamada para plotar a curva ROC
plot_roc()
