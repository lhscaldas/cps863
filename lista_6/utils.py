import matplotlib.pyplot as plt

def plot_policy_and_values(states, policy, V):
    """
    Plota um grid com os estados, mostrando a política ótima e a função de valor em cada estado.

    Parâmetros:
        states (list): Lista de estados no formato (C, S).
        policy (dict): Política ótima no formato {s: a}.
        V (dict): Função de valor ótima no formato {s: value}.
    """
    # Define o tamanho do grid com base nos estados
    max_clients = max(s[0] for s in states)
    max_servers = max(s[1] for s in states)

    # Cria o grid
    fig, ax = plt.subplots(figsize=(max_servers + 2, max_clients + 2))
    ax.set_xlim(-0.5, max_servers + 0.5)
    ax.set_ylim(-0.5, max_clients + 0.5)
    ax.set_xticks(range(1, max_servers + 1))
    ax.set_yticks(range(0, max_clients + 1))
    ax.set_xlabel("Número de Servidores (S)")
    ax.set_ylabel("Número de Clientes (C)")
    ax.grid(True)

    # Plota cada estado
    for (c, s) in states:
        action = policy.get((c, s), "N/A")
        value = V.get((c, s), 0)
        ax.text(
            s, c, f"{action}\n{value:.2f}", 
            ha='center', va='center',
            bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="white")
        )

    plt.title("Política Ótima e Função de Valor")
    plt.gca().invert_yaxis()  # Inverte o eixo y para alinhar com a convenção (0, 0) no canto inferior
    plt.show()

def debug_transition_probabilities(transition_probabilities):
    """
    Função para debugar e entender os elementos de transition_probabilities.

    Parâmetros:
        transition_probabilities (dict): Dicionário de probabilidades de transição no formato {((c, s), a, (new_c, new_s)): prob}.
    """
    print("Debugging Transition Probabilities:\n")

    if not transition_probabilities:
        print("transition_probabilities está vazio. Verifique a lógica de preenchimento.\n")
        return

    # Itera por todas as transições
    for ((c, s), action, (new_c, new_s)), prob in transition_probabilities.items():
        print(f"Estado Atual: (C={c}, S={s}), Ação: {action}, Próximo Estado: (C'={new_c}, S'={new_s}), Probabilidade: {prob:.2f}")
        print("-" * 50)


def debug_rewards(rewards):
    """
    Função para debugar e entender os elementos da variável de recompensas.

    Parâmetros:
        rewards (dict): Dicionário de recompensas no formato {((c, s), a, (new_c, new_s)): reward}.
    """
    print("Debugging Rewards:\n")

    if not rewards:
        print("A variável rewards está vazia. Verifique a lógica de preenchimento.\n")
        return

    # Itera por todas as recompensas
    for ((c, s), action, (new_c, new_s)), reward in rewards.items():
        print(f"Estado Atual: (C={c}, S={s}), Ação: {action}, Próximo Estado: (C'={new_c}, S'={new_s}), Recompensa: {reward}")
        print("-" * 50)




