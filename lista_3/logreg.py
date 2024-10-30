import numpy as np
import pandas as pd
from scipy.optimize import minimize
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, accuracy_score
import seaborn as sns

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

def classify_logreg(x, w, b):
    linear_model = np.dot(w, x) + b
    p_y_given_x = sigmoid(linear_model)
    return 1 if p_y_given_x >= 0.5 else 0  # Corrected classification

def predict_logreg(X, w, b):
    predictions = np.array([classify_logreg(x, w, b) for x in X])
    return np.where(predictions == 0, 1, 2)  # Map back to original labels


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
    # Carregar o dataset
    data = pd.read_csv("lista_3/train_data.csv", header=None, sep=";")
    X = data.iloc[:, :3].values  # As três primeiras colunas são as features
    y = data.iloc[:, 3].values   # A quarta coluna é a classe

    # Separar as amostras por classe (classe 1 e classe 2)
    class_1_data = X[y == 1]
    class_2_data = X[y == 2]

    # Preparar y para Regressão Logística (transformar para 0 e 1)
    y_logreg = np.where(y == 1, 0, 1)

    # Calcular parâmetros do modelo de Regressão Logística
    w_opt, b_opt = fit_logistic_regression(X, y_logreg)

    print("\nParâmetros Regressão Logística:")
    print("Coeficientes (w):", w_opt)
    print("Intercepto (b):", b_opt)

    # Calcular log-likelihood final com os parâmetros otimizados
    params_opt = np.concatenate([w_opt, [b_opt]])
    log_likelihood_LR = -log_likelihood_logistic(params_opt, X, y_logreg)

    y_pred_LR = predict_logreg(X, w_opt, b_opt)

    # Calcular e plotar a matriz de confusão para cada modelo
    models = {"RegLog": y_pred_LR}
    plot_confusion_matrix(y, models)

