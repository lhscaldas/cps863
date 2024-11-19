import numpy as np

# Matriz Q (12x12)
Q = np.array([
    [0.75, 0.25, 0,    0,    0,    0,    0,    0,    0,    0,    0,    0   ],
    [0.25, 0.25, 0.25, 0,    0.25, 0,    0,    0,    0,    0,    0,    0   ],
    [0,    0.25, 0.5,  0,    0,    0.25, 0,    0,    0,    0,    0,    0   ],
    [0,    0,    0,    0.75, 0,    0,    0.25, 0,    0,    0,    0,    0   ],
    [0,    0.25, 0,    0,    0.25, 0.25, 0,    0,    0.25, 0,    0,    0   ],
    [0,    0,    0.25, 0,    0.25, 0.25,  0,    0,    0,    0.25, 0,    0   ],
    [0,    0,    0,    0.25, 0,    0,    0.5,  0.25, 0,    0,    0,    0   ],
    [0,    0,    0,    0,    0,    0,    0.25, 0.25, 0.25, 0,    0.25, 0   ],
    [0,    0,    0,    0,    0.25, 0,    0,    0.25, 0.25, 0,    0,    0.25],
    [0,    0,    0,    0,    0,    0.25, 0,    0,    0.25, 0.25, 0,    0   ],
    [0,    0,    0,    0,    0,    0,    0,    0.25, 0,    0,    0.5,  0.25],
    [0,    0,    0,    0,    0,    0,    0,    0,    0.25, 0,    0.25, 0.25],
])
# print("Somas das linhas de Q:", Q.sum(axis=1))

# Vetor b (custos totais por transição)
b = np.array([
    41, 11, 6, 31, 41, 11, 41, 6, 31, 31, 31, 11
])

# Identidade para o cálculo de N
I = np.eye(len(Q))
# det_I_minus_Q = np.linalg.det(I - Q)
# print("Determinante de (I - Q):", det_I_minus_Q)

# Cálculo da matriz fundamental N
N = np.linalg.inv(I - Q)

# Cálculo do custo total esperado E_c
E_c = np.dot(N, b)

# Exibe os resultados
print("Matriz Fundamental (N):")
print(N)
print("\nCusto Total Esperado (E_c) com o robô iniciando em cada estado transitório:")
print(E_c)
print("\nCusto Total Esperado (E_c) com o robô iniciando no estado s5:"),
print(E_c[4])

# Calculo do valor recebido
E_r = 100 - E_c[4]
print("\nValor recebido: R$ %.2f" % E_r)
