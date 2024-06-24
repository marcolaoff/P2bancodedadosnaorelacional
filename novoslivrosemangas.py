from pymongo import MongoClient

# Conexão com o MongoDB
client = MongoClient('')

# Conexão com o banco de dados 'biblioteca'
db = client['biblioteca']

# Conexão com a coleção 'mangas'
colecao_mangas = db['mangas']

# Inserir mais documentos na coleção 'mangas'
novos_mangas = [
    {"titulo": "Fairy Tail", "autor": "Hiro Mashima", "ano": 2006, "genero": "Ação/Aventura"},
    {"titulo": "Hunter x Hunter", "autor": "Yoshihiro Togashi", "ano": 1998, "genero": "Ação/Aventura"},
    {"titulo": "Tokyo Ghoul", "autor": "Sui Ishida", "ano": 2011, "genero": "Horror"},
    {"titulo": "Sword Art Online", "autor": "Reki Kawahara", "ano": 2009, "genero": "Ação/Fantasia"},
    {"titulo": "Demon Slayer", "autor": "Koyoharu Gotouge", "ano": 2016, "genero": "Ação/Aventura"},
    {"titulo": "Black Clover", "autor": "Yūki Tabata", "ano": 2015, "genero": "Ação/Aventura"},
    {"titulo": "Blue Exorcist", "autor": "Kazue Katō", "ano": 2009, "genero": "Ação/Fantasia"},
    {"titulo": "JoJo's Bizarre Adventure", "autor": "Hirohiko Araki", "ano": 1987, "genero": "Ação/Aventura"},
    {"titulo": "Vinland Saga", "autor": "Makoto Yukimura", "ano": 2005, "genero": "Ação/Aventura"},
    {"titulo": "One Punch Man", "autor": "ONE", "ano": 2009, "genero": "Ação/Comédia"},
    {"titulo": "Gintama", "autor": "Hideaki Sorachi", "ano": 2003, "genero": "Ação/Comédia"},
    {"titulo": "The Seven Deadly Sins", "autor": "Nakaba Suzuki", "ano": 2012, "genero": "Ação/Fantasia"},
    {"titulo": "Akame ga Kill!", "autor": "Takahiro", "ano": 2010, "genero": "Ação/Aventura"},
    {"titulo": "Magi: The Labyrinth of Magic", "autor": "Shinobu Ohtaka", "ano": 2009, "genero": "Ação/Fantasia"},
    {"titulo": "Berserk", "autor": "Kentaro Miura", "ano": 1989, "genero": "Ação/Fantasia"},
    {"titulo": "Claymore", "autor": "Norihiro Yagi", "ano": 2001, "genero": "Ação/Fantasia"},
    {"titulo": "Noragami", "autor": "Adachitoka", "ano": 2011, "genero": "Ação/Fantasia"},
    {"titulo": "Dr. Stone", "autor": "Riichiro Inagaki", "ano": 2017, "genero": "Ação/Ficção Científica"},
    {"titulo": "Fire Force", "autor": "Atsushi Ōkubo", "ano": 2015, "genero": "Ação/Fantasia"},
    {"titulo": "Chainsaw Man", "autor": "Tatsuki Fujimoto", "ano": 2018, "genero": "Ação/Horror"}
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
    {"titulo": "Guerra e Paz", "autor": "Liev Tolstói", "ano": 1869, "genero": "Histórico"},
    {"titulo": "Ulisses", "autor": "James Joyce", "ano": 1922, "genero": "Ficção"},
    {"titulo": "A Odisséia", "autor": "Homero", "ano": -800, "genero": "Épico"},
    {"titulo": "Crime e Castigo", "autor": "Fiódor Dostoiévski", "ano": 1866, "genero": "Ficção/Psicologia"},
    {"titulo": "Orgulho e Preconceito", "autor": "Jane Austen", "ano": 1813, "genero": "Romance"},
    {"titulo": "1984", "autor": "George Orwell", "ano": 1949, "genero": "Distopia"},
    {"titulo": "A Revolução dos Bichos", "autor": "George Orwell", "ano": 1945, "genero": "Satira"},
    {"titulo": "Cem Anos de Solidão", "autor": "Gabriel Garcia Marquez", "ano": 1967, "genero": "Realismo Mágico"},
    {"titulo": "A Divina Comédia", "autor": "Dante Alighieri", "ano": 1320, "genero": "Épico"},
    {"titulo": "O Sol é para Todos", "autor": "Harper Lee", "ano": 1960, "genero": "Ficção"},
    {"titulo": "O Apanhador no Campo de Centeio", "autor": "J.D. Salinger", "ano": 1951, "genero": "Ficção"},
    {"titulo": "As Vinhas da Ira", "autor": "John Steinbeck", "ano": 1939, "genero": "Ficção"},
    {"titulo": "O Livro de Areia", "autor": "Jorge Luis Borges", "ano": 1975, "genero": "Ficção"},
    {"titulo": "O Processo", "autor": "Franz Kafka", "ano": 1925, "genero": "Ficção"},
    {"titulo": "Jane Eyre", "autor": "Charlotte Brontë", "ano": 1847, "genero": "Romance"},
    {"titulo": "Senhora", "autor": "José de Alencar", "ano": 1875, "genero": "Romance"},
    {"titulo": "Grande Sertão: Veredas", "autor": "João Guimarães Rosa", "ano": 1956, "genero": "Ficção"}
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
