import numpy as np

# Definindo a matriz
matriz = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0.75, 0.25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0.25, 0.25, 0.25, 0, 0, 0.25, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0.25, 0.5, 0, 0, 0, 0.25, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0.75, 0, 0, 0, 0.25, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0.25, 0, 0, 0, 0.25, 0.25, 0, 0, 0.25, 0, 0, 0, 0, 0],
    [0, 0, 0, 0.25, 0, 0, 0.25, 0.5, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0.25, 0, 0, 0, 0.5, 0.25, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0.25, 0.25, 0.25, 0, 0, 0.25, 0, 0],
    [0, 0, 0, 0, 0, 0, 0.25, 0, 0, 0.25, 0.25, 0, 0, 0, 0.25, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0.25, 0, 0, 0, 0.5, 0.25, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.25, 0, 0, 0.25, 0.25, 0.25],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.25, 0.75]
])

# Verificação se a soma de cada linha é igual a 1
somas = np.sum(matriz, axis=1)
linhas_validadas = somas == 1

# Exibe resultado
print("Soma de cada linha:", somas)
print("Linhas com soma igual a 1:", linhas_validadas)