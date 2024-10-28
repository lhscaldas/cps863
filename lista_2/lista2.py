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

def calcular_log_likelihood(dados_classe, mu_k, cov_k):
    """
    Calcula a log-verossimilhança para uma classe, dada sua média e matriz de covariância.
    
    Parâmetros:
    - dados_classe: numpy.ndarray de shape (n_samples, n_features)
        Dados da classe.
    - mu_k: numpy.ndarray de shape (n_features,)
        Média da classe.
    - cov_k: numpy.ndarray de shape (n_features, n_features)
        Matriz de covariância da classe.
    
    Retorna:
    - log_likelihood: float
        A log-verossimilhança da classe.
    """
    n_samples, n_features = dados_classe.shape
    diff = dados_classe - mu_k
    inv_cov_k = np.linalg.inv(cov_k)
    exponent_term = np.einsum('ij,jk,ik->i', diff, inv_cov_k, diff)
    log_det_cov_k = np.linalg.slogdet(cov_k)[1]  # O determinante da matriz de covariância
    
    log_likelihood = -0.5 * (n_samples * n_features * np.log(2 * np.pi) + log_det_cov_k + np.sum(exponent_term))
    
    return log_likelihood

def ajustar_mistura_gaussianas(df):
    """
    Ajusta uma mistura de gaussianas a partir de um DataFrame utilizando soluções fechadas (MLE).
    
    Parâmetros:
    - df: DataFrame com os dados, onde as colunas devem incluir 'feature 1', 'feature 2', 'feature 3' e 'class label'.
    
    Retorna:
    - Um dicionário com os parâmetros (médias, matrizes de covariância, pesos) e log-verossimilhança para cada classe.
    """
    resultados = {}
    class_labels = df['class label'].unique()

    # Iterar sobre cada classe
    for class_label in class_labels:
        # Filtrar os dados para a classe atual
        dados_classe = df[df['class label'] == class_label][["feature 1", "feature 2", "feature 3"]].values
        
        N = len(dados_classe)  # Total de dados da classe
        medias = []
        covariancias = []
        pesos = []
        log_likelihoods = []

        # Calcular média, matriz de covariância e peso para a gaussiana correspondente à classe
        mu_k = np.mean(dados_classe, axis=0)
        cov_k = np.cov(dados_classe, rowvar=False)  # Matriz de covariância populacional
        peso_k = N / len(df)  # Peso em relação ao total de dados

        # Armazenar os parâmetros
        medias.append(mu_k)
        covariancias.append(cov_k)
        pesos.append(peso_k)

        # Calcular a log-verossimilhança para a classe atual
        log_likelihood = calcular_log_likelihood(dados_classe, mu_k, cov_k)
        log_likelihoods.append(log_likelihood)

        # Armazenar resultados para a classe atual
        resultados[class_label] = {
            'médias': medias,
            'covariâncias': covariancias,
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
    log_verossimilhança_total = np.sum([arr[0] for arr in log_verossimilhancas.values()])
    bic=calculate_bic(log_verossimilhança_total, 2, len(df2), 3)
    aic=calculate_aic(log_verossimilhança_total, 2, 3)
    print(f'Modelo com 2 componentes: AIC = {aic}, BIC = {bic}')
    # 3 classes
    df3 = df.copy()
    df3['class label'] = df3['class label'].replace(2, 1)
    results3 = ajustar_mistura_gaussianas(df3)
    log_verossimilhancas = {class_label: valores['log-verossimilhança'] for class_label, valores in results3.items()}
    log_verossimilhança_total = np.sum([arr[0] for arr in log_verossimilhancas.values()])
    bic=calculate_bic(log_verossimilhança_total, 3, len(df3), 3)
    aic=calculate_aic(log_verossimilhança_total, 3, 3)
    print(f'Modelo com 3 componentes: AIC = {aic}, BIC = {bic}')
    # 4 classes
    df4 = df.copy()
    results4 = ajustar_mistura_gaussianas(df4)
    log_verossimilhancas = {class_label: valores['log-verossimilhança'] for class_label, valores in results4.items()}
    log_verossimilhança_total = np.sum([arr[0] for arr in log_verossimilhancas.values()])
    bic=calculate_bic(log_verossimilhança_total, 4, len(df4), 3)
    aic=calculate_aic(log_verossimilhança_total, 4, 3)
    print(f'Modelo com 4 componentes: AIC = {aic}, BIC = {bic}')

def gerar_dados_gaussianos(results, n_samples=100):
    """
    Gera dados a partir de uma mistura de gaussianas ajustadas.

    Parâmetros:
    results (dict): Resultados da função ajustar_mistura_gaussianas contendo médias, covariâncias, pesos e classes.
    n_samples (int): Número de amostras a serem geradas para cada classe.

    Retorna:
    DataFrame: DataFrame contendo os dados gerados com as features e class label.
    """
    dados_gerados = []

    for class_label, valores in results.items():
        media = valores['médias'][0]
        covariancia = valores['covariâncias'][0]  # Usando a matriz de covariância
        peso = valores['pesos'][0]
        
        # Gera amostras para a classe atual
        n_samples_class = int(n_samples * peso)
        amostras = np.random.multivariate_normal(mean=media, cov=covariancia, size=n_samples_class)
        
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

def item_6():
    # Carregar o dataset
    df = pd.read_csv('lista_2/lista2-data_set.csv')

    # Ajustar o modelo de mistura de gaussianas
    df['class label'] = df['class label'].replace({2: 1, 3: 1})
    results = ajustar_mistura_gaussianas(df)

    # Gerar amostras a partir do modelo ajustado
    df_gerado = gerar_dados_gaussianos(results, n_samples=50)

    # Visualizar os dados originais e as amostras geradas
    plotar_dados_comparativos(df, df_gerado)

def calcular_previsao_condicional(resultados, classe, x_known, idx_prever):
    """
    Calcula a previsão condicional da feature faltante com base nas conhecidas,
    levando em consideração a classe do dado.
    
    Parâmetros:
    - resultados: dicionário com os parâmetros da mistura de gaussianas por classe
    - classe: rótulo da classe (class_label) do dado
    - x_known: vetor com os valores das features conhecidas (ex: [x2, x3])
    - idx_prever: índice da feature a ser prevista (0 para x1, 1 para x2, etc.)
    
    Saída:
    - Previsão da feature faltante.
    """
    
    previsao = 0.0
    
    # Obtém os parâmetros da mistura para a classe especificada
    medias = resultados[classe]['médias']
    covariancias = resultados[classe]['covariâncias']
    pesos = resultados[classe]['pesos']
    
    # Itera sobre cada componente da mistura
    for k in range(len(pesos)):
        # Média e covariância do componente k
        mu = medias[k]
        sigma = covariancias[k]
        
        # Divide a covariância entre as features conhecidas e a feature a ser prevista
        sigma_11 = sigma[idx_prever, idx_prever]  # Variância da feature a ser prevista
        sigma_12 = sigma[idx_prever, :]           # Covariância entre a feature a ser prevista e as conhecidas
        sigma_kk = sigma[np.ix_(range(len(x_known)), range(len(x_known)))]  # Covariância entre as conhecidas
        
        # Calcula a inversa da covariância das features conhecidas
        sigma_kk_inv = np.linalg.inv(sigma_kk)
        
        # Previsão condicional de x_faltante dada as features conhecidas
        mu_cond = mu[idx_prever] + sigma_12.dot(sigma_kk_inv).dot(x_known - mu[np.ix_(range(len(x_known)))])
        
        # Pondera a previsão com o peso da componente k
        previsao += pesos[k] * mu_cond
    
    return previsao


def preencher_dados_faltantes(df, resultados_filename="df_filled.csv"):
    """
    Preenche os valores faltantes em um DataFrame utilizando a previsão condicional com mistura de gaussianas.
    
    Parâmetros:
    - df: DataFrame contendo algumas linhas com dados faltantes
    - ajustar_mistura_gaussianas: função que ajusta o modelo de mistura de gaussianas e retorna os parâmetros
    - resultados_filename: nome do arquivo CSV onde será salvo o DataFrame com os dados preenchidos
    
    Saída:
    - df_filled: DataFrame com os dados faltantes preenchidos e salvo como CSV
    """
    # Obtendo linhas completas (sem NaN em qualquer coluna)
    df_full = df.dropna(how='any')  # Elimina linhas com NaN em qualquer coluna

    # Obtendo linhas com dados faltantes
    df_miss = df[df.isna().any(axis=1)]  # Linhas com dados faltantes em qualquer coluna
    
    # Ajusta a mistura de gaussianas usando o DataFrame completo
    resultados = ajustar_mistura_gaussianas(df_full)
    

    
    # Cria uma cópia de df_miss para preencher os valores faltantes
    df_filled = df_miss.copy()
    
    # Percorre cada linha de df_miss
    for index, row in df_miss.iterrows():
        # Identifica qual atributo está faltando (assume que só uma feature está faltando por vez)
        atributos_faltantes = row.isna()
        idx_faltante = atributos_faltantes.idxmax()  # Localiza o índice da primeira feature faltante
        
        # Identifica as features conhecidas e a classe associada
        x_known = row.dropna().values  # Obtém os valores das features conhecidas
        idx_prever = row.index.get_loc(idx_faltante)  # Índice da feature faltante
        
        # Supõe que a última coluna seja o 'label' (classe) do dado
        classe = row['class label']
        
        # Calcula a previsão condicional para a feature faltante
        previsao = calcular_previsao_condicional(resultados, classe, x_known, idx_prever)
        
        # Preenche a previsão no DataFrame df_filled
        df_filled.at[index, idx_faltante] = previsao
    
    # Salva o DataFrame preenchido em um arquivo CSV
    df_filled.to_csv(resultados_filename, index=False)
    
    return df_filled


def item_8():
    # Carregar o dataset
    df = pd.read_csv('lista_2/lista2-data_set_missing_data.csv')
    df['feature 2'] = pd.to_numeric(df['feature 2'], errors='coerce')
    df['feature 3'] = pd.to_numeric(df['feature 3'], errors='coerce')
    print("Tipos de dados em df:")
    print(df.dtypes)

    # Preencher os dados faltantes
    df_filled = preencher_dados_faltantes(df, resultados_filename="lista_2/df_filled.csv")

    # Exibir os dados preenchidos
    print(df_filled)
    

if __name__ == "__main__":
    item_8()