import numpy as np

# Função para visualizar o vetor de probabilidades
def visualizar_vetor(vetor):
    estados = [f"({i},{j})" for i in range(1, 5) for j in range(1, 5)]
    for i, probabilidade in enumerate(vetor):
        print(f"{estados[i]}: {probabilidade:.4f}")

# Matriz de transição de estados
P = np.array([
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

# Estado inicial
v0 = np.array([0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

# Probabilidade de transição após 20 passos
v20 = v0
for i in range(20):
    v20 = np.dot(v20, P)

print("Probabilidade de transição após 20 passos:")
visualizar_vetor(v20)

# Função para inicializar o vetor de probabilidade com um 1 aleatório, evitando estados proibidos
estados_proibidos = [(0, 0), (3, 0), (1, 1), (2, 3)]
def vetor_inicial_aleatorio(n):
    vetor = np.zeros(n)
    while True:
        posicao = np.random.randint(0, n)  # Posição aleatória entre 0 e n-1
        # Verificar se a posição é proibida
        if (posicao // 4, posicao % 4) not in estados_proibidos:
            vetor[posicao] = 1  # Definir a posição aleatória como 1
            break
    return vetor

# Função para calcular o estado estacionário
def estado_estacionario(P, tol=1e-6, max_iter=1000):
    n = P.shape[0]
    pi = vetor_inicial_aleatorio(n)
    print(f"pi: {pi}")
    for _ in range(max_iter):
        pi_novo = np.dot(pi, P)
        # Verifica a norma L2 da diferença
        if np.linalg.norm(pi_novo - pi) < tol:
            return pi_novo
        pi = pi_novo
    return pi

# Calcular o estado estacionário
pi = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0])
pi_estacionario = estado_estacionario(P)

print("Estado estacionário:")
visualizar_vetor(pi_estacionario)
print(f"Soma das probabilidades: {np.sum(pi_estacionario)}")
