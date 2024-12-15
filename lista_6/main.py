from value_iteration import value_iteration
from utils import plot_policy_and_values, debug_transition_probabilities, debug_rewards

# Configurações do problema
states = [(c, s) for c in range(9) for s in range(1, 4)]  # Estados: (C, S), onde C ∈ [0, 8] e S ∈ [1, 3]
actions = [-1, 0, 1]  # Ações: -1 (remover servidor), 0 (manter), 1 (adicionar servidor)

# Probabilidades de chegada de clientes
p_0, p_2, p_4 = 0.4, 0.2, 0.4
arrival_probs = {0: p_0, 2: p_2, 4: p_4}

# Probabilidades de transição
transition_probabilities = {}
rewards = {}

# Preenchendo as probabilidades de transição e recompensas
for (c, s) in states:
    for a in actions:
        new_s = s + a
        if 1 <= new_s <= 3:  # Garantir limites de servidores
            for arrivals, prob in arrival_probs.items():
                attended = min(s, c)  # Clientes atendidos
                remaining_clients = c - attended
                new_c = min(remaining_clients + arrivals, 8)  # Limita a capacidade a 8 clientes

                # Transição (estado atual, ação, próximo estado)
                transition_probabilities[((c, s), a, (new_c, new_s))] = prob

                # Recompensa
                gain = attended * 10  # Ganhos: T = 10 por cliente atendido
                server_cost = -5 * new_s  # Custo dos servidores: Rs = 5 por servidor
                queue_penalty = -10 * min(1, max(0, new_c - 4))  # Penalidade: Rq = 10 para clientes > 4
                idle_penalty = -2 * max(0, new_s - new_c)  # Penalidade: R0 = 2 para servidores ociosos

                rewards[((c, s), a, (new_c, new_s))] = gain + server_cost + queue_penalty + idle_penalty

# # salvar as transições em um arquivo
# with open('lista_6/transitions.txt', 'w') as f:
#     for key, value in transition_probabilities.items():
#         f.write(f'{key} : {value}\n')

# # salvar as recompensas em um arquivo
# with open('lista_6/rewards.txt', 'w') as f:
#     for key, value in rewards.items():
#         f.write(f'{key} : {value}\n')

# # Debugando as probabilidades de transição
# debug_transition_probabilities(transition_probabilities)

# # Debugando as recompensas  
# debug_rewards(rewards)

# Fator de desconto e limiar
gamma = 0.9
theta = 1e-6

# Resolve o problema com Value Iteration
policy, V = value_iteration(states, actions, transition_probabilities, rewards, gamma, theta)

# Resultados
print("Política Ótima:", policy)
print("Função de Valor Ótima:", V)

# Plota resultados
plot_policy_and_values(states, policy, V)


