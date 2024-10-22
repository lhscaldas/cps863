import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def visualizar_dados(csv_file):
    """
    Função para visualizar dados em 2 e 3 dimensões.
    
    Parâmetros:
    csv_file (str): Caminho para o arquivo CSV.
    """
    # Carregar o dataset
    df = pd.read_csv(csv_file)
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

if __name__ == "__main__":
    # Exemplo de uso, com o caminho ajustado para a pasta lista_2
    visualizar_dados('lista_2/lista2-data_set.csv')