import random

class EnvironmentSimulator:
    """
    Classe para simular o ambiente com base nas probabilidades de transição e recompensas.
    """
    def __init__(self, transition_probabilities, rewards):
        """
        Inicializa o simulador com probabilidades de transição e recompensas.

        Parâmetros:
            transition_probabilities (dict): Probabilidades de transição no formato {((c, s), a, (new_c, new_s)): prob}.
            rewards (dict): Recompensas no formato {((c, s), a, (new_c, new_s)): reward}.
        """
        self.transition_probabilities = transition_probabilities
        self.rewards = rewards

    def simulate(self, state, action):
        """
        Simula o ambiente retornando o próximo estado e a recompensa.

        Parâmetros:
            state (tuple): Estado atual no formato (c, s).
            action (int): Ação a ser tomada.

        Retorna:
            next_state (tuple): Próximo estado no formato (new_c, new_s).
            reward (float): Recompensa para a transição.
        """
        possible_transitions = [
            (next_state, prob) for ((current_state, a, next_state), prob) in self.transition_probabilities.items()
            if current_state == state and a == action
        ]

        if not possible_transitions:
            return state, 0  # Retorna o estado atual e recompensa zero se não houver transição

        next_states, probabilities = zip(*possible_transitions)
        next_state = random.choices(next_states, probabilities)[0]

        reward = self.rewards.get((state, action, next_state), 0)

        return next_state, reward

def q_learning(states, actions, simulator, alpha=0.1, gamma=0.9, epsilon=0.1, episodes=1000, max_steps=100):
    """
    Resolve o problema de decisão usando o algoritmo Q-Learning.

    Parâmetros:
        states (list): Lista de estados no formato [(c, s)].
        actions (list): Lista de ações.
        simulator (EnvironmentSimulator): Instância da classe de simulação do ambiente.
        alpha (float): Taxa de aprendizado.
        gamma (float): Fator de desconto.
        epsilon (float): Probabilidade de explorar ações aleatórias.
        episodes (int): Número de episódios de aprendizado.
        max_steps (int): Número máximo de passos por episódio.

    Retorna:
        policy (dict): Política ótima no formato {state: action}.
        V (dict): Função de valor calculada no formato {state: value}.
        delta_lista (list): Lista com as mudanças absolutas máximas em V(s) ao longo dos episódios.
    """
    # Inicializa a função Q arbitrariamente
    Q = {state: {action: 0 for action in actions} for state in states}
    V = {state: 0 for state in states}
    delta_lista = []

    for episode in range(episodes):
        # Escolhe um estado inicial aleatoriamente
        state = random.choice(states)
        steps = 0
        delta = 0

        while steps < max_steps:
            # Escolhe a ação usando a política epsilon-greedy
            if random.uniform(0, 1) < epsilon:
                action = random.choice(actions)  # Exploração
            else:
                action = max(Q[state], key=Q[state].get)  # Exploitação

            # Simula o ambiente para obter o próximo estado e a recompensa
            next_state, reward = simulator.simulate(state, action)

            # Atualiza a função Q usando a equação de aprendizado por diferença temporal (TD)
            max_next_q = max(Q[next_state].values()) if next_state in Q else 0
            Q[state][action] += alpha * (reward + gamma * max_next_q - Q[state][action])

            # Atualiza o estado atual
            state = next_state

            # Incrementa o contador de passos
            steps += 1

        # Calcula a função de valor V(s) = max_a Q(s, a) após cada episódio
        new_V = {state: max(Q[state].values()) for state in states}

        # Calcula a mudança absoluta máxima em V(s)
        delta = max(abs(new_V[s] - V[s]) for s in states)
        delta_lista.append(delta)

        # Atualiza V
        V = new_V

    # Deriva a política ótima a partir da função Q
    policy = {state: max(Q[state], key=Q[state].get) for state in states}

    return policy, V, delta_lista
