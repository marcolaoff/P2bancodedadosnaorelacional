from pymongo import MongoClient

# Conexão com o MongoDB
client = MongoClient('')

# Conexão com o banco de dados 'biblioteca'
db = client['biblioteca']

# Conexão com a coleção 'mangas'
colecao_mangas = db['mangas']

# Inserir número de vendas na coleção 'mangas'
vendas_mangas = [
    {"titulo": "Naruto", "vendas": 250000000},
    {"titulo": "One Piece", "vendas": 480000000},
    {"titulo": "Attack on Titan", "vendas": 100000000},
    {"titulo": "Dragon Ball", "vendas": 250000000},
    {"titulo": "Death Note", "vendas": 30000000},
    {"titulo": "Bleach", "vendas": 120000000},
    {"titulo": "Fullmetal Alchemist", "vendas": 80000000},
    {"titulo": "My Hero Academia", "vendas": 50000000},
    {"titulo": "Fairy Tail", "vendas": 72000000},
    {"titulo": "Hunter x Hunter", "vendas": 78000000},
    {"titulo": "Tokyo Ghoul", "vendas": 44000000},
    {"titulo": "Sword Art Online", "vendas": 20000000},
    {"titulo": "Demon Slayer", "vendas": 120000000},
    {"titulo": "Black Clover", "vendas": 16000000},
    {"titulo": "Blue Exorcist", "vendas": 25000000},
    {"titulo": "JoJo's Bizarre Adventure", "vendas": 100000000},
    {"titulo": "Vinland Saga", "vendas": 5500000},
    {"titulo": "One Punch Man", "vendas": 30000000},
    {"titulo": "Gintama", "vendas": 55000000},
    {"titulo": "The Seven Deadly Sins", "vendas": 37000000},
    {"titulo": "Akame ga Kill!", "vendas": 3000000},
    {"titulo": "Magi: The Labyrinth of Magic", "vendas": 18000000},
    {"titulo": "Berserk", "vendas": 50000000},
    {"titulo": "Claymore", "vendas": 8000000},
    {"titulo": "Noragami", "vendas": 7000000},
    {"titulo": "Dr. Stone", "vendas": 12000000},
    {"titulo": "Fire Force", "vendas": 8000000},
    {"titulo": "Chainsaw Man", "vendas": 6000000}
]

# Atualizar documentos na coleção 'mangas' com o número de vendas
for manga in vendas_mangas:
    colecao_mangas.update_one({"titulo": manga["titulo"]}, {"$set": {"vendas": manga["vendas"]}})

# Conexão com a coleção 'livros'
colecao_livros = db['livros']

# Inserir número de vendas na coleção 'livros'
vendas_livros = [
    {"titulo": "Dom Quixote", "vendas": 500000000},
    {"titulo": "O Grande Gatsby", "vendas": 25000000},
    {"titulo": "Moby Dick", "vendas": 5000000},
    {"titulo": "Guerra e Paz", "vendas": 36000000},
    {"titulo": "Ulisses", "vendas": 3000000},
    {"titulo": "A Odisséia", "vendas": 2400000},
    {"titulo": "Crime e Castigo", "vendas": 18000000},
    {"titulo": "Orgulho e Preconceito", "vendas": 20000000},
    {"titulo": "1984", "vendas": 30000000},
    {"titulo": "A Revolução dos Bichos", "vendas": 25000000},
    {"titulo": "Cem Anos de Solidão", "vendas": 50000000},
    {"titulo": "A Divina Comédia", "vendas": 10000000},
    {"titulo": "O Sol é para Todos", "vendas": 40000000},
    {"titulo": "O Apanhador no Campo de Centeio", "vendas": 65000000},
    {"titulo": "As Vinhas da Ira", "vendas": 14000000},
    {"titulo": "O Livro de Areia", "vendas": 2000000},
    {"titulo": "O Processo", "vendas": 10000000},
    {"titulo": "Jane Eyre", "vendas": 20000000},
    {"titulo": "Senhora", "vendas": 15000000},
    {"titulo": "Grande Sertão: Veredas", "vendas": 12000000}
]

# Atualizar documentos na coleção 'livros' com o número de vendas
for livro in vendas_livros:
    colecao_livros.update_one({"titulo": livro["titulo"]}, {"$set": {"vendas": livro["vendas"]}})

print("Atualização de vendas concluída.")
e