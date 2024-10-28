import pandas as pd

# Carregar o dataset
df = pd.read_csv('lista_2/lista2-data_set_missing_data.csv')

# Exibir os tipos de dados das colunas
print("Tipos de dados em df:")
print(df.dtypes)

# Verificar se há valores não numéricos em 'feature 2' e 'feature 3'
print("Linhas com caracteres não numéricos em 'feature 2':")
non_numeric_feature_2 = df[~df['feature 2'].astype(str).str.replace('.', '', regex=False).str.isnumeric()]
print(non_numeric_feature_2)

print("Linhas com caracteres não numéricos em 'feature 3':")
non_numeric_feature_3 = df[~df['feature 3'].astype(str).str.replace('.', '', regex=False).str.isnumeric()]
print(non_numeric_feature_3)

# Contar o número de NaN em cada coluna
print("\nContagem de valores faltantes por coluna:")
print(df.isna().sum())

# Exibir as primeiras linhas do DataFrame para uma revisão visual
print("\nPrimeiras linhas do DataFrame:")
print(df.head())

# Forçar a conversão das colunas para float
df['feature 2'] = pd.to_numeric(df['feature 2'], errors='coerce')
df['feature 3'] = pd.to_numeric(df['feature 3'], errors='coerce')

# Verificar os tipos de dados novamente
print("Tipos de dados em df após conversão:")
print(df.dtypes)

# Verificar a contagem de valores faltantes novamente
print("\nContagem de valores faltantes por coluna após conversão:")
print(df.isna().sum())


# Exibir linhas que se tornaram NaN após a conversão
nan_feature_2 = df[df['feature 2'].isna()]
nan_feature_3 = df[df['feature 3'].isna()]

print("Linhas com NaN em 'feature 2' após conversão:")
print(nan_feature_2)

print("Linhas com NaN em 'feature 3' após conversão:")
print(nan_feature_3)

