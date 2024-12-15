def value_iteration(states, actions, transition_probabilities, rewards, gamma=0.9, theta=1e-6):
    """
    Resolve o problema de decisão usando o algoritmo Value Iteration.

    Parâmetros:
        states (list): Lista de estados no formato [(c, s)].
        actions (list): Lista de ações.
        transition_probabilities (dict): Probabilidades de transição no formato {((c, s), a, (new_c, new_s)): prob}.
        rewards (dict): Recompensas no formato {((c, s), a, (new_c, new_s)): reward}.
        gamma (float): Fator de desconto.
        theta (float): Limiar para a convergência.

    Retorna:
        policy (dict): Política ótima no formato {state: action}.
        V (dict): Função de valor ótima no formato {state: value}.
    """
    # Inicializa os valores de todos os estados com 0
    V = {state: 0 for state in states}

    while True:
        delta = 0
        for state in states:
            v = V[state]
            # Calcula o valor esperado para cada ação
            action_values = []
            for a in actions:
                expected_value = sum(
                    prob * (rewards.get((state, a, next_state), 0) + gamma * V.get(next_state, 0))
                    for (current_state, a_current, next_state), prob in transition_probabilities.items()
                    if current_state == state and a_current == a
                )
                action_values.append(expected_value)

            # Atualiza o valor do estado com o máximo valor esperado
            print(action_values)
            V[state] = max(action_values)
            delta = max(delta, abs(v - V[state]))

        # Verifica convergência
        if delta < theta:
            break

    # Determina a política ótima
    policy = {}
    for state in states:
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

    return policy, V
