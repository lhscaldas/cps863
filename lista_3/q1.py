import numpy as np
import pandas as pd
from scipy.optimize import minimize
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, accuracy_score
import seaborn as sns
from sklearn.preprocessing import StandardScaler

# Função para calcular a média e covariância para cada classe
def calculate_gaussian_parameters(X_class):
    mean = np.mean(X_class, axis=0)
    cov = np.cov(X_class, rowvar=False)
    return mean, cov

# GaussI: Mistura de Gaussianas com Matriz Identidade
def calculate_gaussI_params(X_class1, X_class2, total_samples):
    mean1, _ = calculate_gaussian_parameters(X_class1)
    mean2, _ = calculate_gaussian_parameters(X_class2)
    pi1 = len(X_class1) / total_samples
    pi2 = len(X_class2) / total_samples
    cov_identity = np.identity(X_class1.shape[1])  # Covariância é a matriz identidade
    return mean1, mean2, cov_identity, pi1, pi2

# GaussX: Mistura de Gaussianas com Covariância Livre
def calculate_gaussX_params(X_class1, X_class2, total_samples):
    mean1, cov1 = calculate_gaussian_parameters(X_class1)
    mean2, cov2 = calculate_gaussian_parameters(X_class2)
    pi1 = len(X_class1) / total_samples
    pi2 = len(X_class2) / total_samples
    return mean1, cov1, mean2, cov2, pi1, pi2

# Função Sigmóide
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# Função de Log-Likelihood para Regressão Logística
def log_likelihood_logistic(params, X, y):
    w = params[:-1]
    b = params[-1]
    linear_model = X.dot(w) + b
    probabilities = sigmoid(linear_model)
    y_log_prob = y * np.log(probabilities + 1e-10) + (1 - y) * np.log(1 - probabilities + 1e-10)
    return -np.sum(y_log_prob)  # Retornamos o negativo pois vamos minimizar


# Função para otimizar a log-likelihood da regressão logística
def fit_logistic_regression(X, y):
    initial_params = np.zeros(X.shape[1] + 1)  # w (coeficientes) + b (intercepto)
    result = minimize(log_likelihood_logistic, initial_params, args=(X, y), method='BFGS')
    w_opt = result.x[:-1]
    b_opt = result.x[-1]
    return w_opt, b_opt

# Função para calcular a densidade de probabilidade de uma Gaussiana multivariada
def multivariate_gaussian_pdf(x, mean, cov):
    d = len(mean)
    det_cov = np.linalg.det(cov)
    inv_cov = np.linalg.inv(cov)
    term1 = 1 / ((2 * np.pi) ** (d / 2) * det_cov ** 0.5)
    term2 = np.exp(-0.5 * (x - mean).T @ inv_cov @ (x - mean))
    return term1 * term2

# Log-Likelihood para o modelo GaussI
def log_likelihood_gaussI(X_test, mean1, mean2, cov_identity, pi1, pi2):
    log_likelihood = 0
    for x in X_test:
        # Calcula a probabilidade de cada classe usando a mistura de Gaussianas
        p_x_given_class1 = multivariate_gaussian_pdf(x, mean1, cov_identity)
        p_x_given_class2 = multivariate_gaussian_pdf(x, mean2, cov_identity)
        # Calcula a probabilidade total considerando o peso da mistura
        p_x = pi1 * p_x_given_class1 + pi2 * p_x_given_class2
        log_likelihood += np.log(p_x)
    return log_likelihood

# Log-Likelihood para o modelo GaussX
def log_likelihood_gaussX(X_test, mean1, cov1, mean2, cov2, pi1, pi2):
    log_likelihood = 0
    for x in X_test:
        # Calcula a probabilidade de cada classe usando a mistura de Gaussianas com covariância livre
        p_x_given_class1 = multivariate_gaussian_pdf(x, mean1, cov1)
        p_x_given_class2 = multivariate_gaussian_pdf(x, mean2, cov2)
        # Calcula a probabilidade total considerando o peso da mistura
        p_x = pi1 * p_x_given_class1 + pi2 * p_x_given_class2
        log_likelihood += np.log(p_x)
    return log_likelihood

# Função para classificar uma amostra usando o modelo GaussI
def classify_gaussI(x, mean1, mean2, cov_identity, pi1, pi2):
    p_x_given_class1 = multivariate_gaussian_pdf(x, mean1, cov_identity)
    p_x_given_class2 = multivariate_gaussian_pdf(x, mean2, cov_identity)
    p_class1 = pi1 * p_x_given_class1
    p_class2 = pi2 * p_x_given_class2
    return 1 if p_class1 > p_class2 else 2

# Função para classificar um dataset usando o modelo GaussI
def predict_gaussI(X, mean1, mean2, cov_identity, pi1, pi2):
    return np.array([classify_gaussI(x, mean1, mean2, cov_identity, pi1, pi2) for x in X])

# Função para classificar uma amostra usando o modelo GaussX
def classify_gaussX(x, mean1, cov1, mean2, cov2, pi1, pi2):
    p_x_given_class1 = multivariate_gaussian_pdf(x, mean1, cov1)
    p_x_given_class2 = multivariate_gaussian_pdf(x, mean2, cov2)
    p_class1 = pi1 * p_x_given_class1
    p_class2 = pi2 * p_x_given_class2
    return 1 if p_class1 > p_class2 else 2

# Função para classificar um dataset usando o modelo GaussX
def predict_gaussX(X, mean1, cov1, mean2, cov2, pi1, pi2):
    return np.array([classify_gaussX(x, mean1, cov1, mean2, cov2, pi1, pi2) for x in X])

# Função para classificar uma amostra usando o modelo de Regressão Logística
def classify_logreg(x, w, b):
    linear_model = np.dot(w, x) + b
    p_y_given_x = sigmoid(linear_model)
    return 1 if p_y_given_x >= 0.5 else 0  # Retorna 1 ou 0 para consistência com y_logreg

# Função para classificar um dataset usando o modelo de Regressão Logística
def predict_logreg(X, w, b):
    predictions = np.array([classify_logreg(x, w, b) for x in X])
    return np.where(predictions == 0, 1, 2)  # Converte 0 para 1 e 1 para 2 para compatibilidade com y


def plot_confusion_matrix(y_true, models):
    for model_name, y_pred in models.items():
        acc = accuracy_score(y_true, y_pred)
        cm = confusion_matrix(y_true, y_pred)
        plt.figure()
        sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", cbar=False, xticklabels=[1, 2], yticklabels=[1, 2],annot_kws={"size": 24})
        plt.title(f"Matriz de Confusão - {model_name} (Acurácia: {acc:.2f})", fontsize=20)
        plt.xlabel("Classe Predita", fontsize=18)
        plt.ylabel("Classe Verdadeira", fontsize=18)
        plt.xticks(fontsize=16)
        plt.yticks(fontsize=16)
        plt.show()

if __name__ == "__main__":
    ##########
    # Item 2 #
    ##########

    # Carregar o dataset
    data = pd.read_csv("lista_3/train_data.csv", header=None, sep=";")
    X = data.iloc[:, :3].values  # As três primeiras colunas são as features
    y = data.iloc[:, 3].values   # A quarta coluna é a classe

    # # Normalizar as features
    # scaler = StandardScaler()
    # X = scaler.fit_transform(X)

    # Separar as amostras por classe (classe 1 e classe 2)
    class_1_data = X[y == 1]
    class_2_data = X[y == 2]

    # Calcular parâmetros dos modelos GaussI e GaussX
    mean1_GI, mean2_GI, cov_identity, pi1_GI, pi2_GI = calculate_gaussI_params(class_1_data, class_2_data, len(X))
    mean1_GX, cov1_GX, mean2_GX, cov2_GX, pi1_GX, pi2_GX = calculate_gaussX_params(class_1_data, class_2_data, len(X))

    # Preparar y para Regressão Logística (transformar para 0 e 1)
    y_logreg = np.where(y == 1, 0, 1)

    # Calcular parâmetros do modelo de Regressão Logística
    w_opt, b_opt = fit_logistic_regression(X, y_logreg)

    # Exibir os resultados
    print("Parâmetros GaussI:")
    print("Média classe 1:", mean1_GI)
    print("Média classe 2:", mean2_GI)
    print("Matriz de covariância (identidade):", cov_identity)
    print("Peso da classe 1:", pi1_GI)
    print("Peso da classe 2:", pi2_GI)

    print("\nParâmetros GaussX:")
    print("Média classe 1:", mean1_GX)
    print("Covariância classe 1:", cov1_GX)
    print("Média classe 2:", mean2_GX)
    print("Covariância classe 2:", cov2_GX)
    print("Peso da classe 1:", pi1_GX)
    print("Peso da classe 2:", pi2_GX)

    print("\nParâmetros Regressão Logística:")
    print("Coeficientes (w):", w_opt)
    print("Intercepto (b):", b_opt)

    ##########
    # Item 3 #
    ##########

    # Calcular log-likelihood no conjunto de treinamento
    log_likelihood_GI = log_likelihood_gaussI(X, mean1_GI, mean2_GI, cov_identity, pi1_GI, pi2_GI)
    log_likelihood_GX = log_likelihood_gaussX(X, mean1_GX, cov1_GX, mean2_GX, cov2_GX, pi1_GX, pi2_GX)
    params_opt = np.concatenate([w_opt, [b_opt]])
    log_likelihood_LR = -log_likelihood_logistic(params_opt, X, y_logreg)

    # Exibir os resultados
    print("Log-Likelihood GaussI:", log_likelihood_GI)
    print("Log-Likelihood GaussX:", log_likelihood_GX)
    print("Log-Likelihood LogReg:", log_likelihood_LR)

    ##########
    # Item 4 #
    ##########

    # Classificar o conjunto de treinamento com cada modelo
    y_pred_GI = predict_gaussI(X, mean1_GI, mean2_GI, cov_identity, pi1_GI, pi2_GI)
    y_pred_GX = predict_gaussX(X, mean1_GX, cov1_GX, mean2_GX, cov2_GX, pi1_GX, pi2_GX)
    y_pred_LR = predict_logreg(X, w_opt, b_opt)

    # Calcular e plotar a matriz de confusão para cada modelo
    models = {"GaussI": y_pred_GI, "GaussX": y_pred_GX, "LogReg": y_pred_LR}
    plot_confusion_matrix(y, models)
