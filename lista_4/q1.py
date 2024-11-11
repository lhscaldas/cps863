import numpy as np
import pandas as pd

# Carregar o dataset onde os valores estão separados por espaços
# "header=None" indica que o arquivo não possui cabeçalhos
# "names=[...]" define os nomes das colunas para cada tipo de filme
data = pd.read_csv("lista_4/lista4-data_scores.csv", sep='\s+', header=None, names=['filme_1', 'filme_2', 'filme_3', 'filme_4', 'filme_5'])

# Inicializações de constantes
num_classes = 2        # Número de classes (duas)
num_filmes = 5         # Número de tipos de filmes
num_notas = 4          # Número de notas possíveis (1 a 4)

# Inicializar as probabilidades a priori das classes aleatoriamente usando a distribuição Dirichlet
# Isso garante que a soma das probabilidades seja 1
p_class = np.random.dirichlet(np.ones(num_classes), size=1).flatten()

# Inicializar as probabilidades condicionais para cada nota em cada tipo de filme em cada classe
# Utiliza a distribuição Dirichlet para garantir que as probabilidades condicionais somem 1
p_feature_given_class = np.random.dirichlet(np.ones(num_notas), size=(num_classes, num_filmes))

# Função de Expectativa-Maximização (E-step e M-step)
def expectation_maximization(data, p_class, p_feature_given_class, max_iter=100, tol=1e-4):
    # Iniciar o loop de iterações do algoritmo EM
    for iteration in range(max_iter):
        # Matriz para armazenar as responsabilidades de cada observação para cada classe
        responsibilities = np.zeros((len(data), num_classes))
        
        # E-step: calcular as responsabilidades
        for i in range(len(data)):             # Itera sobre cada observação
            for k in range(num_classes):       # Itera sobre cada classe
                prob = p_class[k]              # Probabilidade a priori da classe k
                for j in range(num_filmes):    # Itera sobre cada tipo de filme
                    # Ajusta a nota para índice (0-3) e multiplica pela probabilidade condicional
                    nota = data.iloc[i, j] - 1
                    prob *= p_feature_given_class[k, j, nota]
                responsibilities[i, k] = prob  # Guarda a probabilidade acumulada para a classe k
            
            # Normaliza as responsabilidades para que somem 1 para cada observação
            responsibilities[i, :] /= responsibilities[i, :].sum()
        
        # M-step: atualizar as probabilidades a priori e condicionais
        # Atualiza as probabilidades a priori como a média das responsabilidades
        new_p_class = responsibilities.mean(axis=0)
        
        # Cria um novo array para armazenar as probabilidades condicionais atualizadas
        new_p_feature_given_class = np.zeros_like(p_feature_given_class)
        
        # Calcula as novas probabilidades condicionais
        for k in range(num_classes):            # Itera sobre cada classe
            for j in range(num_filmes):         # Itera sobre cada tipo de filme
                for nota in range(num_notas):   # Itera sobre cada nota
                    # Soma ponderada das responsabilidades para cada nota no tipo de filme e classe
                    new_p_feature_given_class[k, j, nota] = np.sum(responsibilities[:, k] * (data.iloc[:, j] == (nota + 1)))
                # Normaliza as probabilidades para que somem 1 para cada tipo de filme na classe k
                new_p_feature_given_class[k, j, :] /= responsibilities[:, k].sum()
        
        # Critério de parada: verifica se a diferença entre as probabilidades antigas e novas é menor que a tolerância
        if np.linalg.norm(p_class - new_p_class) < tol and np.linalg.norm(p_feature_given_class - new_p_feature_given_class) < tol:
            # Imprime mensagem de convergência quando o critério de parada é atendido
            print(f"Convergência na iteração {iteration}")
            break
        
        # Atualiza as probabilidades para a próxima iteração
        p_class, p_feature_given_class = new_p_class, new_p_feature_given_class
    
    return p_class, p_feature_given_class, responsibilities

if __name__ == '__main__':
    # Executar o algoritmo EM
    p_class_final, p_feature_given_class_final, responsibilities = expectation_maximization(data, p_class, p_feature_given_class)

    # Imprimir as probabilidades a priori e condicionais finais
    print("Probabilidades a priori finais:")
    print(p_class_final)
    print("\nProbabilidades condicionais finais:")
    print(p_feature_given_class_final)

    # Calcular quantos usuários foram alocados a cada classe após a convergência
    class_allocation = responsibilities.argmax(axis=1)  # Classe com maior responsabilidade para cada observação
    class_counts = np.bincount(class_allocation, minlength=num_classes)

    print("\nQuantidade de usuários alocados em cada classe:")
    print(f"Classe 0: {class_counts[0]}")
    print(f"Classe 1: {class_counts[1]}")


