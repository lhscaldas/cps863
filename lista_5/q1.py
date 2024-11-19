import numpy as np

class HMM:
    def __init__(self, A, B, pi):
        """
        Inicializa o modelo HMM.
        
        :param A: Matriz de transição de estados (N x N)
        :param B: Matriz de emissão de observações (N x M)
        :param pi: Vetor de probabilidades iniciais (1 x N)
        """
        self.A = A  # Matriz de transição
        self.B = B  # Matriz de emissão
        self.pi = pi  # Probabilidades iniciais

    def forward(self, O):
        """
        Calcula o alpha para todos os estados e tempos para uma sequência O.

        :param O: Sequência de observações (lista de índices das observações)
        :return: Matriz alpha (T x N)
        """
        N = len(self.pi)  # Número de estados
        T = len(O)  # Comprimento da sequência de observações

        # Inicialização
        alpha = np.zeros((T, N))
        alpha[0, :] = self.pi * self.B[:, O[0]]

        # Recursão
        for t in range(1, T):
            for j in range(N):
                alpha[t, j] = np.sum(alpha[t - 1, :] * self.A[:, j]) * self.B[j, O[t]]

        return alpha
    
    def P_obs(self, alpha):
        """
        Calcula a probabilidade da sequência de observações, dado o modelo.
        
        :param alpha: Matriz alpha (T x N) calculada pelo método forward
        :return: Probabilidade da sequência de observações
        """
        return np.sum(alpha[-1, :])
    
    def backward(self, O):
        """
        Calcula o beta para todos os estados e tempos para uma sequência O.

        :param O: Sequência de observações (lista de índices das observações)
        :return: Matriz beta (T x N)
        """
        N = len(self.pi)
        T = len(O)

        # Inicialização
        beta = np.zeros((T, N))
        beta[-1, :] = 1

        # Recursão
        for t in range(T - 2, -1, -1):
            for i in range(N):
                beta[t, i] = np.sum(self.A[i, :] * self.B[:, O[t + 1]] * beta[t + 1, :])

        return beta
    
    def gamma(self, alpha, beta):
        """
        Calcula a matriz gamma para todos os estados e tempos para uma sequência O.
        
        :param alpha: Matriz alpha (T x N) calculada pelo método forward
        :param beta: Matriz beta (T x N) calculada pelo método backward
        :return: Matriz gamma (T x N)
        """
        return alpha * beta / np.sum(alpha * beta, axis=1).reshape(-1, 1)

    def end_state(self, gamma):
            """
            Calcula o estado mais provável na última observação.
            
            :param gamma: Matriz gamma (T x N) calculada pelo método gamma
            :return: Estado mais provável na última observação
            """
            end_state = np.argmax(gamma[-1, :])
            P_end_state = gamma[-1, end_state]
            state_map = {0: 'S1', 1: 'S2', 2: 'S3', 3: 'S4', 4: 'S5', 5: 'S6', 6: 'S7', 7: 'S8', 8: 'S9', 9: 'S10', 10: 'S11', 11: 'S12', 12: 'S13', 13: 'S14', 14: 'S15', 15: 'S16'}
            return state_map[end_state], P_end_state
    
    def viterbi(self, O):
        # inicialização
        N = len(self.pi)
        T = len(O)
        delta = np.zeros((T, N))
        psi = np.zeros((T, N), dtype=int)
        delta[0, :] = self.pi * self.B[:, O[0]]
        psi[0, :] = 0

        # recursão
        for t in range(1, T):
            for j in range(N):
                delta[t, j] = np.max(delta[t - 1, :] * self.A[:, j]) * self.B[j, O[t]]
                psi[t, j] = np.argmax(delta[t - 1, :] * self.A[:, j])
        
        # finalização
        P_star = np.max(delta[-1, :])
        q_star = np.argmax(delta[-1, :])

        # reconstrução do caminho
        path = [q_star]
        for t in range(T - 1, 0, -1):
            q_star = psi[t, q_star]
            path.insert(0, q_star)

        state_map = {0: 'S1', 1: 'S2', 2: 'S3', 3: 'S4', 4: 'S5', 5: 'S6', 6: 'S7', 7: 'S8', 8: 'S9', 9: 'S10', 10: 'S11', 11: 'S12', 12: 'S13', 13: 'S14', 14: 'S15', 15: 'S16'}
        path = [state_map[state] for state in path]
        return path, P_star

# Exemplo de uso:
if __name__ == "__main__":
    # Matriz de transição A
    A = np.array([
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0.75, 0.25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0.25, 0.25, 0.25, 0, 0, 0.25, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0.25, 0.50, 0, 0, 0, 0.25, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0.75, 0, 0, 0, 0.25, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0.25, 0, 0, 0, 0.25, 0.25, 0, 0, 0.25, 0, 0, 0, 0, 0],
        [0, 0, 0, 0.25, 0, 0, 0.25, 0.50, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0.25, 0, 0, 0, 0.50, 0.25, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0.25, 0.25, 0.25, 0, 0, 0.25, 0, 0],
        [0, 0, 0, 0, 0, 0, 0.25, 0, 0, 0.25, 0.25, 0, 0, 0, 0.25, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0.25, 0, 0, 0, 0.50, 0.25, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.25, 0, 0, 0.25, 0.25, 0.25],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.25, 0.75],
    ])
    # verificação se a matriz de transição está normalizada
    # print("Somas das linhas de A:", A.sum(axis=1))

    # Matriz de emissão B
    B = np.array([
        [0, 0, 0, 0],
        [0.0333, 0.0333, 0.0333, 0.9000],
        [0.0333, 0.0333, 0.9000, 0.0333],
        [0.0333, 0.9000, 0.0333, 0.0333],
        [0.9000, 0.0333, 0.0333, 0.0333],
        [0, 0, 0, 0],
        [0.0333, 0.0333, 0.0333, 0.9000],
        [0.0333, 0.0333, 0.9000, 0.0333],
        [0.0333, 0.9000, 0.0333, 0.0333],
        [0.0333, 0.0333, 0.0333, 0.9000],
        [0.0333, 0.9000, 0.0333, 0.0333],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0.9000, 0.0333, 0.0333, 0.0333],
        [0.0333, 0.0333, 0.9000, 0.0333],
        [0.0333, 0.9000, 0.0333, 0.0333],
    ])
    # verificação se a matriz de emissão está normalizada
    # print("Somas das linhas de B:", B.sum(axis=1))

    # Vetor de probabilidades iniciais (pi)
    pi = np.zeros(16)
    pi[4] = 1  # Estado inicial é S5

    # Sequência de observações 
    O_letras_1 = "r r y r y r b g b r y y g b".split() # sequência 1
    O_letras_2 = "r b y r g r b g b r y y g b".split() # sequencia 2
    color_map = {'r': 0, 'b': 1, 'y': 2, 'g': 3} # (índices das observações)
    O_1 = [color_map[obs] for obs in O_letras_1] # Transforma as observações em índices
    O_2 = [color_map[obs] for obs in O_letras_2] # Transforma as observações em índices

    # Instanciação do HMM e cálculo
    hmm = HMM(A, B, pi)
    alpha_1 = hmm.forward(O_1)
    P_O_1 = hmm.P_obs(alpha_1)
    print("Probabilidade de se observar a sequência P(O | λ):", P_O_1)
    alpha_2 = hmm.forward(O_2)
    P_O_2 = hmm.P_obs(alpha_2)
    print("Probabilidade de se observar a sequência P(O | λ):", P_O_2)

    # Estado mais provável na última observação
    beta_1 = hmm.backward(O_1)
    gamma_1 = hmm.gamma(alpha_1, beta_1)
    end_state_1, P_end_state_1 = hmm.end_state(gamma_1)
    print("Estado mais provável na última observação da sequência 1:", end_state_1)
    print("Probabilidade do estado mais provável:", P_end_state_1)
    beta_2 = hmm.backward(O_2)
    gamma_2 = hmm.gamma(alpha_2, beta_2)
    end_state_2, P_end_state_2 = hmm.end_state(gamma_2)
    print("Estado mais provável na última observação da sequência 2:", end_state_2)
    print("Probabilidade do estado mais provável:", P_end_state_2)

    # Caminho mais provável
    path_1, P_star_1 = hmm.viterbi(O_1)
    print("Caminho mais provável da sequência 1:", path_1)
    print("Probabilidade do caminho mais provável:", P_star_1)
    path_2, P_star_2 = hmm.viterbi(O_2)
    print("Caminho mais provável da sequência 2:", path_2)
    print("Probabilidade do caminho mais provável:", P_star_2)
    
