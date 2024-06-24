from pymongo import MongoClient

# Conexão com o MongoDB
client = MongoClient('')

# Criação do banco de dados 'biblioteca'
db = client['biblioteca']

# Criação da coleção 'mangas'
colecao_mangas = db['mangas']

# Inserir documentos na coleção 'mangas'
mangas = [
    {"id": "1", "titulo": "Naruto", "autor": "Masashi Kishimoto", "ano": 1999, "genero": "Ação/Aventura", "vendas": 250000000},
    {"id": "2", "titulo": "One Piece", "autor": "Eiichiro Oda", "ano": 1997, "genero": "Ação/Aventura", "vendas": 517000000},
    {"id": "3", "titulo": "Attack on Titan", "autor": "Hajime Isayama", "ano": 2009, "genero": "Ação/Drama", "vendas": 100000000},
    {"id": "4", "titulo": "Dragon Ball", "autor": "Akira Toriyama", "ano": 1984, "genero": "Ação/Aventura", "vendas": 250000000},
    {"id": "5", "titulo": "Death Note", "autor": "Tsugumi Ohba", "ano": 2003, "genero": "Suspense/Psicologia", "vendas": 30000000}
]

# Inserir os documentos na coleção
colecao_mangas.insert_many(mangas)

# Ler todos os documentos da coleção 'mangas'
print("Documentos na coleção 'mangas':")
for manga in colecao_mangas.find():
    print(manga)

# Criação da coleção 'livros'
colecao_livros = db['livros']

# Inserir documentos na coleção 'livros'
livros = [
    {"id": "1", "titulo": "O Senhor dos Anéis", "autor": "J.R.R. Tolkien", "ano": 1954, "genero": "Fantasia", "vendas": 150000000},
    {"id": "2", "titulo": "1984", "autor": "George Orwell", "ano": 1949, "genero": "Distopia", "vendas": 30000000},
    {"id": "3", "titulo": "A Revolução dos Bichos", "autor": "George Orwell", "ano": 1945, "genero": "Satira", "vendas": 25000000},
    {"id": "4", "titulo": "O Hobbit", "autor": "J.R.R. Tolkien", "ano": 1937, "genero": "Fantasia", "vendas": 140000000},
    {"id": "5", "titulo": "Cem Anos de Solidão", "autor": "Gabriel Garcia Marquez", "ano": 1967, "genero": "Realismo Mágico", "vendas": 50000000}
]

# Inserir os documentos na coleção 'livros'
colecao_livros.insert_many(livros)

# Ler todos os documentos da coleção 'livros'
print("\nDocumentos na coleção 'livros':")
for livro in colecao_livros.find():
    print(livro)
