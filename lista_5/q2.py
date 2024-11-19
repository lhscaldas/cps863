import numpy as np
import pandas as pd

def em_algorithm(data, num_classes, max_iters=1000, tol=1e-6):
    """
    Algoritmo EM otimizado com vetorização para lidar com dados faltantes.
    
    Args:
        data (pd.DataFrame): Dados de entrada (clientes x características), com NaN para valores faltantes.
        num_classes (int): Número de classes (clusters) no modelo.
        max_iters (int): Número máximo de iterações.
        tol (float): Tolerância para critério de convergência.
    
    Returns:
        dict: Parâmetros estimados (médias, covariâncias e probabilidades a priori).
        pd.DataFrame: Responsabilidades finais para cada cliente e classe.
    """
    n, d = data.shape
    np.random.seed(42)

    # Inicializar parâmetros
    means = np.random.rand(num_classes, d)  # Médias aleatórias
    covariances = [np.eye(d) for _ in range(num_classes)]  # Covariâncias como matrizes identidade
    priors = np.ones(num_classes) / num_classes  # Probabilidades a priori uniformes

    # Matriz de responsabilidades
    responsibilities = np.zeros((n, num_classes))

    # Converter o DataFrame em matriz NumPy para maior eficiência
    data_np = data.to_numpy()

    for iteration in range(max_iters):
        # --- E-step: Calcular responsabilidades ---
        for k in range(num_classes):
            mean_k = means[k]
            cov_k = covariances[k]
            prior_k = priors[k]

            for i in range(n):
                observed = ~np.isnan(data_np[i])  # Dimensões observadas
                x_obs = data_np[i, observed]
                mean_obs = mean_k[observed]
                cov_obs = cov_k[np.ix_(observed, observed)]
                
                if len(x_obs) > 0:
                    diff = x_obs - mean_obs
                    likelihood = (
                        np.exp(-0.5 * diff.T @ np.linalg.inv(cov_obs) @ diff) /
                        np.sqrt((2 * np.pi) ** len(x_obs) * np.linalg.det(cov_obs))
                    )
                else:
                    likelihood = 1e-6
                
                responsibilities[i, k] = prior_k * likelihood

        # Normalizar responsabilidades
        responsibilities /= responsibilities.sum(axis=1, keepdims=True)

        # --- M-step: Atualizar parâmetros ---
        Nk = responsibilities.sum(axis=0)  # Soma total de responsabilidades para cada classe

        # Atualizar médias
        for k in range(num_classes):
            weighted_sum = np.zeros(d)
            for j in range(d):
                observed = ~np.isnan(data_np[:, j])
                weighted_sum[j] = np.dot(responsibilities[observed, k], data_np[observed, j])
            means[k] = weighted_sum / Nk[k]

        # Atualizar covariâncias
        for k in range(num_classes):
            cov_k = np.zeros((d, d))
            for i in range(n):
                observed = ~np.isnan(data_np[i])
                x_obs = data_np[i, observed]
                mean_obs = means[k, observed]
                if len(x_obs) > 0:
                    diff = x_obs - mean_obs
                    cov_k[np.ix_(observed, observed)] += responsibilities[i, k] * np.outer(diff, diff)
            covariances[k] = cov_k / Nk[k]

        # Atualizar probabilidades a priori
        priors = Nk / n

        # Verificar convergência
        if iteration > 0 and np.abs(responsibilities - prev_responsibilities).max() < tol:
            break

        prev_responsibilities = responsibilities.copy()

    return {
        "means": means,
        "covariances": covariances,
        "priors": priors
    }, pd.DataFrame(responsibilities, columns=[f"Class_{k+1}" for k in range(num_classes)], index=data.index), iteration



if __name__ == "__main__":
    # Exemplo de uso
    data = pd.read_csv("lista_5/customer_ratings.csv")
    data = data.drop(columns=["Customer Class"])  # Remover coluna Customer Class
    params, resps, its = em_algorithm(data, num_classes=3)

    print(f"Convergência após {its+1} iterações.")
    print("Médias:")
    print(params["means"])
    print("\nCovariâncias:")
    print(params["covariances"])
    print("\nProbabilidades a priori:")
    print(params["priors"])

    # Determinar a classe para cada cliente
    class_assignments = resps.idxmax(axis=1)

    # Contar quantos clientes foram alocados para cada classe
    class_counts = class_assignments.value_counts()

    print("\nQuantidade de usuários por classe:")
    print(class_counts)

    # Calcular a probabilidade de um cliente específico ser de uma classe específica
    cliente_id = 0  # ID do cliente (linha no DataFrame original)
    classe_k = "Class_3"  # Nome da classe (coluna no DataFrame de responsabilidades)

    probabilidade = resps.loc[cliente_id, classe_k]

    print(f"A probabilidade do cliente {cliente_id+1} pertencer à classe {classe_k} é {probabilidade:.4f}")



