import pymongo

# Conexão com o MongoDB
client = pymongo.MongoClient('')
db = client['biblioteca']

# Conexão com a coleção 'mangas'
colecao_mangas = db['mangas']

# Recuperar e mostrar todos os documentos da coleção 'mangas'
print("Mangás Registrados:")
for manga in colecao_mangas.find():
    print(manga)

# Conexão com a coleção 'livros'
colecao_livros = db['livros']

# Recuperar e mostrar todos os documentos da coleção 'livros'
print("\nLivros Registrados:")
for livro in colecao_livros.find():
    print(livro)
