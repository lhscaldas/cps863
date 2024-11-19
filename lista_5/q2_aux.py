import pandas as pd
import numpy as np

# importar dados
df = pd.read_csv("lista_5/customer_ratings.csv")
                 
# contar usuários para cada classe, dado que a coluna 'Customer Class' é a classe
classes = df['Customer Class'].value_counts()
print(classes)


                 