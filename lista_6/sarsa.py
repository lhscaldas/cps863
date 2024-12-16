import random

def sarsa(states, actions, simulator, alpha=0.1, gamma=0.9, epsilon=0.1, episodes=1000, max_steps=100):
    """
    Resolve o problema de decisão usando o algoritmo SARSA.

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

        # Escolhe a primeira ação usando epsilon-greedy
        if random.uniform(0, 1) < epsilon:
            action = random.choice(actions)  # Exploração
        else:
            action = max(Q[state], key=Q[state].get)  # Exploitação

        while steps < max_steps:
            # Simula o ambiente para obter o próximo estado e a recompensa
            next_state, reward = simulator.simulate(state, action)

            # Escolhe a próxima ação usando epsilon-greedy
            if random.uniform(0, 1) < epsilon:
                next_action = random.choice(actions)  # Exploração
            else:
                next_action = max(Q[next_state], key=Q[next_state].get)  # Exploitação

            # Atualiza a função Q usando a equação de aprendizado SARSA
            Q[state][action] += alpha * (reward + gamma * Q[next_state][next_action] - Q[state][action])

            # Atualiza o estado e a ação atuais
            state = next_state
            action = next_action

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
