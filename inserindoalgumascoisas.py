from pymongo import MongoClient

# Conexão com o MongoDB
client = MongoClient('')

# Conexão com o banco de dados 'biblioteca'
db = client['biblioteca']

# Conexão com a coleção 'mangas'
colecao_mangas = db['mangas']

# Inserir mais documentos na coleção 'mangas'
novos_mangas = [
    {"titulo": "Bleach", "autor": "Tite Kubo", "ano": 2001, "genero": "Ação/Aventura"},
    {"titulo": "Fullmetal Alchemist", "autor": "Hiromu Arakawa", "ano": 2001, "genero": "Ação/Aventura"},
    {"titulo": "My Hero Academia", "autor": "Kohei Horikoshi", "ano": 2014, "genero": "Ação/Aventura"},
]

# Inserir os novos documentos na coleção 'mangas'
colecao_mangas.insert_many(novos_mangas)

# Conexão com a coleção 'livros'
colecao_livros = db['livros']

# Inserir mais documentos na coleção 'livros'
novos_livros = [
    {"titulo": "Dom Quixote", "autor": "Miguel de Cervantes", "ano": 1605, "genero": "Aventura"},
    {"titulo": "O Grande Gatsby", "autor": "F. Scott Fitzgerald", "ano": 1925, "genero": "Romance"},
    {"titulo": "Moby Dick", "autor": "Herman Melville", "ano": 1851, "genero": "Aventura"},
]

# Inserir os novos documentos na coleção 'livros'
colecao_livros.insert_many(novos_livros)

# Ler todos os documentos da coleção 'mangas' para verificar a inserção
print("Documentos na coleção 'mangas' após adição:")
for manga in colecao_mangas.find():
    print(manga)

# Ler todos os documentos da coleção 'livros' para verificar a inserção
print("\nDocumentos na coleção 'livros' após adição:")
for livro in colecao_livros.find():
    print(livro)
