def policy_iteration(states, actions, transition_probabilities, rewards, gamma=0.9, theta=1e-6):
    """
    Resolve o problema de decisão usando o algoritmo Policy Iteration.

    Parâmetros:
        states (list): Lista de estados no formato [(c, s)].
        actions (list): Lista de ações.
        transition_probabilities (dict): Probabilidades de transição no formato {((c, s), a, (new_c, new_s)): prob}.
        rewards (dict): Recompensas no formato {((c, s), a, (new_c, new_s)): reward}.
        gamma (float): Fator de desconto.
        theta (float): Limiar para a convergência na avaliação da política.

    Retorna:
        policy (dict): Política ótima no formato {state: action}.
        V (dict): Função de valor ótima no formato {state: value}.
    """
    # Inicializa uma política arbitrária
    policy = {state: actions[0] for state in states}
    
    # Inicializa a função de valor V com zeros
    V = {state: 0 for state in states}

    delta_list = []
    while True:
        # Etapa 1: Avaliação da Política
        while True:
            delta = 0
            for state in states:
                v = V[state]
                action = policy[state]
                V[state] = sum(
                    prob * (rewards.get((state, action, next_state), 0) + gamma * V.get(next_state, 0))
                    for (current_state, a_current, next_state), prob in transition_probabilities.items()
                    if current_state == state and a_current == action
                )
                delta = max(delta, abs(v - V[state]))
                delta_list.append(delta)
            if delta < theta:
                break

        # Etapa 2: Melhoria da Política
        policy_stable = True
        for state in states:
            old_action = policy[state]
            best_action = None
            best_value = float('-inf')
            for a in actions:
                expected_value = sum(
                    prob * (rewards.get((state, a, next_state), 0) + gamma * V.get(next_state, 0))
                    for (current_state, a_current, next_state), prob in transition_probabilities.items()
                    if current_state == state and a_current == a
                )
                if expected_value > best_value:
                    best_value = expected_value
                    best_action = a
            policy[state] = best_action
            if old_action != best_action:
                policy_stable = False

        # Verifica se a política é estável
        if policy_stable:
            break

    return policy, V, delta_list
