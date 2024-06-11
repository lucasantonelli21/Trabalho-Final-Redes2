from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

def conectar():
    return sqlite3.connect('users.db')

def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user TEXT NOT NULL,
            nomeCompleto TEXT NOT NULL,
            cpf TEXT NOT NULL
        )
    ''')
    conexao.commit()
    conexao.close()

criar_tabela()

@app.route('/users', methods=['GET'])
def ler_Users():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM users')
    Users = cursor.fetchall()
    conexao.close()
    return jsonify(Users)

@app.route('/users', methods=['POST'])
def criar_User():
    dados = request.json
    user = dados['user']
    nomeCompleto = dados['nomeCompleto']
    cpf = dados['cpf']
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('''
        INSERT INTO users (user, nomeCompleto, cpf) VALUES (?, ?, ?)
    ''', (user, nomeCompleto, cpf))
    conexao.commit()
    conexao.close()
    return jsonify({'mensagem': 'User criado com sucesso'})

@app.route('/users/<int:id>', methods=['PUT'])
def atualizar_User(id):
    dados = request.json
    user = dados['user']
    nomeCompleto = dados['nomeCompleto']
    cpf = dados['cpf']
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('''
        UPDATE users SET user = ?, nomeCompleto = ?, cpf = ? WHERE id = ?
    ''', (user, nomeCompleto, cpf, id))
    conexao.commit()
    conexao.close()
    return jsonify({'mensagem': 'User atualizado com sucesso'})

@app.route('/users/<int:id>', methods=['DELETE'])
def deletar_User(id):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('DELETE FROM users WHERE id = ?', (id,))
    conexao.commit()
    conexao.close()
    return jsonify({'mensagem': 'User deletado com sucesso'})

if __name__ == "__main__":
    app.run(debug=True)
