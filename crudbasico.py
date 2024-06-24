from pymongo import MongoClient

# Conexão com o MongoDB
client = MongoClient('')

# Conexão com o banco de dados 'biblioteca'
db = client['biblioteca']

# Conexão com a coleção 'mangas'
colecao_mangas = db['mangas']

# Conexão com a coleção 'livros'
colecao_livros = db['livros']

# Funções CRUD para 'mangas'
def criar_manga(titulo, autor, ano, genero):
    manga = {"titulo": titulo, "autor": autor, "ano": ano, "genero": genero}
    colecao_mangas.insert_one(manga)
    print(f"Mangá '{titulo}' inserido com sucesso.")

def ler_mangas():
    print("Documentos na coleção 'mangas':")
    for manga in colecao_mangas.find():
        print(manga)

def atualizar_manga(titulo, novos_dados):
    colecao_mangas.update_one({"titulo": titulo}, {"$set": novos_dados})
    print(f"Mangá '{titulo}' atualizado com sucesso.")

def deletar_manga(titulo):
    colecao_mangas.delete_one({"titulo": titulo})
    print(f"Mangá '{titulo}' deletado com sucesso.")

# Funções CRUD para 'livros'
def criar_livro(titulo, autor, ano, genero):
    livro = {"titulo": titulo, "autor": autor, "ano": ano, "genero": genero}
    colecao_livros.insert_one(livro)
    print(f"Livro '{titulo}' inserido com sucesso.")

def ler_livros():
    print("\nDocumentos na coleção 'livros':")
    for livro in colecao_livros.find():
        print(livro)

def atualizar_livro(titulo, novos_dados):
    colecao_livros.update_one({"titulo": titulo}, {"$set": novos_dados})
    print(f"Livro '{titulo}' atualizado com sucesso.")

def deletar_livro(titulo):
    colecao_livros.delete_one({"titulo": titulo})
    print(f"Livro '{titulo}' deletado com sucesso.")

# Demonstrando operações CRUD com 'mangas'
print("Operações CRUD com 'mangas':")
criar_manga("Dragon Ball Super", "Akira Toriyama", 2015, "Ação/Aventura")
ler_mangas()
atualizar_manga("Dragon Ball Super", {"ano": 2016})
ler_mangas()
deletar_manga("Dragon Ball Super")
ler_mangas()

# Demonstrando operações CRUD com 'livros'
print("\nOperações CRUD com 'livros':")
criar_livro("O Alquimista", "Paulo Coelho", 1988, "Ficção")
ler_livros()
atualizar_livro("O Alquimista", {"ano": 1990})
ler_livros()
deletar_livro("O Alquimista")
ler_livros()