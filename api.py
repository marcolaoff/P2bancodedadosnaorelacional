from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
import config

app = Flask(__name__)
app.config["MONGO_URI"] = config.MONGO_URI
mongo = PyMongo(app)

@app.route('/')
def index():
    return "Bem-vindo à API da Biblioteca!"

# Rotas para a coleção 'mangas'
@app.route('/mangas', methods=['POST'])
def add_manga():
    data = request.json
    mongo.db.mangas.insert_one(data)
    return jsonify(message="Mangá adicionado com sucesso!"), 201

@app.route('/mangas', methods=['GET'])
def get_mangas():
    mangas = mongo.db.mangas.find()
    result = []
    for manga in mangas:
        manga['_id'] = str(manga['_id'])
        result.append(manga)
    return jsonify(result), 200

@app.route('/mangas/<id>', methods=['GET'])
def get_manga(id):
    manga = mongo.db.mangas.find_one({"id": id})
    if manga:
        manga['_id'] = str(manga['_id'])
        return jsonify(manga), 200
    else:
        return jsonify(message="Mangá não encontrado"), 404

@app.route('/mangas/<id>', methods=['PUT'])
def update_manga(id):
    data = request.json
    result = mongo.db.mangas.update_one({"id": id}, {"$set": data})
    if result.matched_count > 0:
        return jsonify(message="Mangá atualizado com sucesso!"), 200
    else:
        return jsonify(message="Mangá não encontrado"), 404

@app.route('/mangas/<id>', methods=['DELETE'])
def delete_manga(id):
    result = mongo.db.mangas.delete_one({"id": id})
    if result.deleted_count > 0:
        return jsonify(message="Mangá deletado com sucesso!"), 200
    else:
        return jsonify(message="Mangá não encontrado"), 404

# Rotas para a coleção 'livros'
@app.route('/livros', methods=['POST'])
def add_livro():
    data = request.json
    mongo.db.livros.insert_one(data)
    return jsonify(message="Livro adicionado com sucesso!"), 201

@app.route('/livros', methods=['GET'])
def get_livros():
    livros = mongo.db.livros.find()
    result = []
    for livro in livros:
        livro['_id'] = str(livro['_id'])
        result.append(livro)
    return jsonify(result), 200

@app.route('/livros/<id>', methods=['GET'])
def get_livro(id):
    livro = mongo.db.livros.find_one({"id": id})
    if livro:
        livro['_id'] = str(livro['_id'])
        return jsonify(livro), 200
    else:
        return jsonify(message="Livro não encontrado"), 404

@app.route('/livros/<id>', methods=['PUT'])
def update_livro(id):
    data = request.json
    result = mongo.db.livros.update_one({"id": id}, {"$set": data})
    if result.matched_count > 0:
        return jsonify(message="Livro atualizado com sucesso!"), 200
    else:
        return jsonify(message="Livro não encontrado"), 404

@app.route('/livros/<id>', methods=['DELETE'])
def delete_livro(id):
    result = mongo.db.livros.delete_one({"id": id})
    if result.deleted_count > 0:
        return jsonify(message="Livro deletado com sucesso!"), 200
    else:
        return jsonify(message="Livro não encontrado"), 404

if __name__ == '__main__':
    app.run(debug=True)
