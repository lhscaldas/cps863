import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.lines import Line2D

def visualizar_dados(df):
    """
    Função para visualizar dados em 2 e 3 dimensões.
    
    Parâmetros:
    csv_file (str): Caminho para o arquivo CSV.
    """
    # Carregar o dataset
    X = df[['feature 1', 'feature 2', 'feature 3']].values
    y = df['class label'].values

    # Lista de combinações de features (vistas) para 2D
    combinacoes = [
        ('feature 1', 'feature 2'),
        ('feature 1', 'feature 3'),
        ('feature 2', 'feature 3')
    ]

    # Obter a paleta de cores do matplotlib
    palette = plt.cm.Set1.colors  # Cores da paleta Set1
    colors = [palette[int(label)-1] for label in y]
    
    # Mapeamento de rótulos para as legendas das classes
    class_labels = {1: 'classe 1', 2: 'classe 2', 3: 'classe 3', 4: 'classe 4'}
    legend_patches = [mpatches.Patch(color=palette[i], label=f'classe {i+1}') for i in range(len(class_labels))]

    # Plotar as combinações 2D usando matplotlib scatter
    for f1, f2 in combinacoes:
        plt.figure(figsize=(8, 6))
        plt.scatter(df[f1], df[f2], c=colors, edgecolor='k', s=50)
        plt.title(f'Visualização {f1} vs {f2}')
        plt.xlabel(f1)
        plt.ylabel(f2)
        plt.legend(handles=legend_patches)
        plt.show()
    
    # Plotar a visualização em 3D com as mesmas cores e legendas
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(df['feature 1'], df['feature 2'], df['feature 3'], c=colors, edgecolor='k', s=50)
    ax.set_title('Visualização em 3D')
    ax.set_xlabel('feature 1')
    ax.set_ylabel('feature 2')
    ax.set_zlabel('feature 3')
    
    # Adicionar a legenda no gráfico 3D
    plt.legend(handles=legend_patches)
    plt.show()

def item_1():
    df = pd.read_csv('lista_2/lista2-data_set.csv')
    visualizar_dados(df)

def calcular_log_likelihood(dados, mu, sigma):
    """
    Calcula a log-verossimilhança de um conjunto de dados dado os parâmetros da gaussiana.
    
    Parâmetros:
    - dados: Os dados da classe.
    - mu: Média da gaussiana.
    - sigma: Variância da gaussiana.
    
    Retorna:
    - log_likelihood: O valor da log-verossimilhança.
    """
    N = len(dados)
    log_likelihood = - (N / 2) * np.log(2 * np.pi * sigma) - (1 / (2 * sigma)) * np.sum((dados - mu) ** 2)
    return log_likelihood

def ajustar_mistura_gaussianas(df):
    """
    Ajusta uma mistura de gaussianas a partir de um DataFrame utilizando soluções fechadas.
    
    Parâmetros:
    - df: DataFrame com os dados, onde as colunas devem incluir 'feature 1', 'feature 2', 'feature 3' e 'class label'.
    
    Retorna:
    - Um dicionário com os parâmetros (médias, variâncias, pesos) e log-verossimilhança para cada classe.
    """
    resultados = {}
    class_labels = df['class label'].unique()
    n_gaussianas = len(class_labels)  # Número de gaussianas igual ao número de classes

    # Iterar sobre cada classe
    for class_label in class_labels:
        # Filtrar os dados para a classe atual
        dados_classe = df[df['class label'] == class_label][["feature 1", "feature 2", "feature 3"]].values
        
        N = len(dados_classe)  # Total de dados da classe
        medias = []
        variancias = []
        pesos = []
        log_likelihoods = []

        # Calcular média, variância e peso para a gaussiana correspondente à classe
        mu_k = np.mean(dados_classe, axis=0)
        sigma_k2 = np.var(dados_classe, axis=0, ddof=0)  # Variância populacional
        peso_k = N / len(df)  # Peso em relação ao total de dados

        # Armazenar os parâmetros
        medias.append(mu_k)
        variancias.append(sigma_k2)
        pesos.append(peso_k)

        # Calcular a log-verossimilhança para a classe atual
        log_likelihood = calcular_log_likelihood(dados_classe, mu_k, sigma_k2)
        log_likelihoods.append(log_likelihood)

        # Armazenar resultados para a classe atual
        resultados[class_label] = {
            'médias': medias,
            'variâncias': variancias,
            'pesos': pesos,
            'log-verossimilhança': log_likelihoods
        }

    return resultados

def item_2():
    # Carregando o dataset do arquivo CSV
    df = pd.read_csv('lista_2/lista2-data_set.csv') 

    # Calculando os parâmetros para cada classe
    resultados = ajustar_mistura_gaussianas(df)
    print(resultados)

def item_3():
    # Carregando o dataset do arquivo CSV
    df = pd.read_csv('lista_2/lista2-data_set.csv') 

    # Unificar classes 1 e 2
    df['class label'] = df['class label'].replace(2, 1)

    # Calculando os parâmetros para cada classe
    resultados = ajustar_mistura_gaussianas(df)
    print(resultados)

def item_4():
    # Carregando o dataset do arquivo CSV
    df = pd.read_csv('lista_2/lista2-data_set.csv') 

    # Unificar classes 1, 2 e 3
    df['class label'] = df['class label'].replace({2: 1, 3: 1})

    # Calculando os parâmetros para cada classe
    resultados = ajustar_mistura_gaussianas(df)
    print(resultados)

def calculate_aic(log_likelihood, n_components, n_features):
    k = n_components * (n_features + 1) - 1  # Número de parâmetros
    aic = 2 * k - 2 * log_likelihood
    return aic

def calculate_bic(log_likelihood, n_components, n_samples, n_features):
    k = n_components * (n_features + 1) - 1  # Número de parâmetros
    bic = np.log(n_samples) * k - 2 * log_likelihood
    return bic

def item_5():
    df = pd.read_csv('lista_2/lista2-data_set.csv')
    # 2 classes
    df2 = df.copy()
    df2['class label'] = df2['class label'].replace({2: 1, 3: 1})
    results2 = ajustar_mistura_gaussianas(df2)
    log_verossimilhancas = {class_label: valores['log-verossimilhança'] for class_label, valores in results2.items()}
    log_verossimilhança_total = sum(sum(arr) for valores in log_verossimilhancas.values() for arr in valores)
    bic=calculate_bic(log_verossimilhança_total, 2, len(df2), 3)
    aic=calculate_aic(log_verossimilhança_total, 2, 3)
    print(f'Modelo com 2 componentes: AIC = {aic}, BIC = {bic}')
    # 3 classes
    df3 = df.copy()
    df3['class label'] = df3['class label'].replace(2, 1)
    results3 = ajustar_mistura_gaussianas(df3)
    log_verossimilhancas = {class_label: valores['log-verossimilhança'] for class_label, valores in results3.items()}
    log_verossimilhança_total = sum(sum(arr) for valores in log_verossimilhancas.values() for arr in valores)
    bic=calculate_bic(log_verossimilhança_total, 3, len(df3), 3)
    aic=calculate_aic(log_verossimilhança_total, 3, 3)
    print(f'Modelo com 3 componentes: AIC = {aic}, BIC = {bic}')
    # 4 classes
    df4 = df.copy()
    results4 = ajustar_mistura_gaussianas(df4)
    log_verossimilhancas = {class_label: valores['log-verossimilhança'] for class_label, valores in results4.items()}
    log_verossimilhança_total = sum(sum(arr) for valores in log_verossimilhancas.values() for arr in valores)
    bic=calculate_bic(log_verossimilhança_total, 4, len(df4), 3)
    aic=calculate_aic(log_verossimilhança_total, 4, 3)
    print(f'Modelo com 4 componentes: AIC = {aic}, BIC = {bic}')

def gerar_dados_gaussianos(results, n_samples=100):
    """
    Gera dados a partir de uma mistura de gaussianas ajustadas.

    Parâmetros:
    results (dict): Resultados da função ajustar_mistura_gaussianas contendo médias, variâncias, pesos e classes.
    n_samples (int): Número de amostras a serem geradas para cada classe.

    Retorna:
    DataFrame: DataFrame contendo os dados gerados com as features e class label.
    """
    dados_gerados = []

    for class_label, valores in results.items():
        media = valores['médias'][0]
        variancia = valores['variâncias'][0]
        peso = valores['pesos'][0]
        
        # Gera amostras para a classe atual
        n_samples_class = int(n_samples * peso)
        amostras = np.random.multivariate_normal(mean=media, cov=np.diag(variancia), size=n_samples_class)
        
        # Adiciona os dados gerados à lista
        for amostra in amostras:
            dados_gerados.append((*amostra, class_label))

    # Cria um DataFrame a partir dos dados gerados
    df_gerado = pd.DataFrame(dados_gerados, columns=['feature 1', 'feature 2', 'feature 3', 'class label'])

    return df_gerado



def plotar_dados_comparativos(df_original, df_gerado):
    """
    Plota os dados originais e gerados em gráficos 2D e 3D para comparação.

    Parâmetros:
    df_original (DataFrame): DataFrame contendo os dados originais.
    df_gerado (DataFrame): DataFrame contendo os dados gerados.
    """
    # Lista de combinações de features (vistas) para 2D
    combinacoes = [
        ('feature 1', 'feature 2'),
        ('feature 1', 'feature 3'),
        ('feature 2', 'feature 3')
    ]

    # Obter a paleta de cores do matplotlib
    palette = plt.cm.Set1.colors  
    labels = df_original['class label'].unique()
    
    # Criar patches para as classes
    legend_patches = [mpatches.Patch(color=palette[int(label) - 1], label=f'classe {label}') for label in labels]

    # Plotar as combinações 2D
    for f1, f2 in combinacoes:
        plt.figure(figsize=(8, 6))
        
        # Dados originais (círculos)
        for label in labels:
            subset = df_original[df_original['class label'] == label]
            plt.scatter(subset[f1], subset[f2], color=palette[int(label) - 1], marker='o', label=f'Original classe {label}', edgecolor='k', s=50, alpha=0.2)

        # Dados gerados (triângulos)
        for label in df_gerado['class label'].unique():
            subset = df_gerado[df_gerado['class label'] == label]
            plt.scatter(subset[f1], subset[f2], color=palette[int(label) - 1], marker='^', label=f'Gerado classe {label}', edgecolor='k', s=50)

        plt.title(f'Comparação: {f1} vs {f2}')
        plt.xlabel(f1)
        plt.ylabel(f2)
        
        # Definir a legenda com Line2D para os marcadores
        legend_elements = [
            Line2D([0], [0], marker='o', color='w', label='Original', markerfacecolor='k', markersize=10, alpha=0.2),
            Line2D([0], [0], marker='^', color='w', label='Gerado', markerfacecolor='k', markersize=10)
        ]
        plt.legend(handles=legend_patches + legend_elements, loc='lower right')
        plt.show()

    # Plotar a visualização em 3D
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Dados originais
    for label in labels:
        subset = df_original[df_original['class label'] == label]
        ax.scatter(subset['feature 1'], subset['feature 2'], subset['feature 3'],
                   color=palette[int(label) - 1], marker='o', label=f'Original classe {label}', edgecolor='k')

    # Dados gerados
    for label in df_gerado['class label'].unique():
        subset = df_gerado[df_gerado['class label'] == label]
        ax.scatter(subset['feature 1'], subset['feature 2'], subset['feature 3'],
                   color=palette[int(label) - 1], marker='^', label=f'Gerado classe {label}', edgecolor='k')

    ax.set_title('Comparação em 3D')
    ax.set_xlabel('Feature 1')
    ax.set_ylabel('Feature 2')
    ax.set_zlabel('Feature 3')

    # Adicionar legenda
    ax.legend(handles=legend_patches + legend_elements, loc='lower right')

    plt.show()

# Exemplo de uso
# plotar_dados_comparativos(df_original, df_gerado)



def item_6():
    df = pd.read_csv('lista_2/lista2-data_set.csv')
    X = df[['feature 1', 'feature 2', 'feature 3']].values

    # Ajustar o modelo de mistura de gaussianas
    results = ajustar_mistura_gaussianas(df)

    # Gerar amostras a partir do modelo ajustado
    df_gerado = gerar_dados_gaussianos(results, n_samples=50)

    # Visualizar os dados originais e as amostras geradas
    plotar_dados_comparativos(df, df_gerado)


if __name__ == "__main__":
    item_6()