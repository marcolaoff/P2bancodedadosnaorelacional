import pymongo
import pandas as pd
import matplotlib.pyplot as plt

# Conexão com o MongoDB
client = pymongo.MongoClient('')
db = client['biblioteca']

# Carregar dados da coleção 'mangas'
mangas = pd.DataFrame(list(db['mangas'].find()))
# Carregar dados da coleção 'livros'
livros = pd.DataFrame(list(db['livros'].find()))

# Remover a coluna '_id' que não é necessária para a visualização
mangas.drop('_id', axis=1, inplace=True)
livros.drop('_id', axis=1, inplace=True)

# Visualizar os primeiros registros das coleções
print("Mangás:")
print(mangas.head())
print("\nLivros:")
print(livros.head())

# Visualização de Mangás por Ano
plt.figure(figsize=(10, 5))
mangas['ano'].value_counts().sort_index().plot(kind='bar')
plt.title('Número de Mangás por Ano')
plt.xlabel('Ano')
plt.ylabel('Número de Mangás')
plt.show()

# Visualização de Livros por Gênero
plt.figure(figsize=(10, 5))
livros['genero'].value_counts().plot(kind='bar')
plt.title('Número de Livros por Gênero')
plt.xlabel('Gênero')
plt.ylabel('Número de Livros')
plt.show()
