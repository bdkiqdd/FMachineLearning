# Imports
from flask import render_template,redirect,request
from flask import Blueprint
from werkzeug.wrappers import response
from Classes.instrutor import Instrutor
from Conectores import conector_instrutor

# Instancia da 'objeto' Blueprint
blue_instrutor = Blueprint("instrutores",__name__)

# Gerando rota index
@blue_instrutor.route('/instrutores')
def instrutores_index():
    instrutores = conector_instrutor.get_all()
    return render_template('instrutores/index.html', instrutores = instrutores, title = 'Instrutores')

# Gerando rota para criação de novo Instrutor
@blue_instrutor.route('/instrutores/novo')
def novo_instrutor():
    return render_template('instrutores/novo.html',title =' Novo Instrutor ')

# Pegando informações do form html e criando novo instrutor
@blue_instrutor.route('/instrutores', methods = ['POST'])
def cria_instrutor():
    nome = request.form['nome']
    sobrenome = request.form['sobrenome']
    data_nascimento = request.form['data_nascimento']
    novo_instrutor = Instrutor(nome,sobrenome,data_nascimento)
    conector_instrutor.create(novo_instrutor)
    return redirect('/instrutores')

# Gerando rota para edição de instrutor e fazendo a pesquisa do id no banco
@blue_instrutor.route('/instrutores/<id>/edit')
def edita_instrutor(id):
    instrutor = conector_instrutor.get_one(id)
    return render_template('/instrutores/editar.html',instrutor = instrutor, title = 'Editar informações do Instrutor')

# Pegando informações do form e editando o instrutor
@blue_instrutor.route('/instrutores/<id>',methods = ['POST'])
def atualiza_instrutor():
    nome = request.form['nome']
    sobrenome = request.form['sobrenome']
    data_nascimento = request.form['data_nascimento']
    att_instrutor = Instrutor(nome, sobrenome,data_nascimento)
    conector_instrutor.edit(att_instrutor)
    return redirect('/instrutores')

# Deleta instrutor
@blue_instrutor.route('/instrutores/<id>/delete')
def delete_instrutor(id):
    conector_instrutor.delete_one(id)
    return redirect('/instrutores')