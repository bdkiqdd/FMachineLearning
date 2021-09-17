# Imports 
from flask import render_template,redirect, request
from flask import Blueprint
from Classes.membro import Membro
from Conectores import conector_membro,conector_agendamento

# É como um Controller do MVC mas construido a mão, ou seja, pode se fazer a validação que quiser por aqui

# Instância da Classe
blue_membro = Blueprint('membros',__name__)

# Rota da página principal
@blue_membro.route('/membros')
def index_mebros():
    membros = conector_membro.get_all()
    return render_template('membros/index.html',membros = membros,title = 'Todos os membros')

# Rota para a página de criação
@blue_membro.route('/membros/novo')
def novos_membros():
    return render_template('membros/novo.html',title= 'Novo Membro')

# Pegando informações no forme fazendo a criação 
@blue_membro.route('/membros',methods = ['POST'])
def cria_novo():
    nome = request.form['nome']
    sobrenome = request.form['sobrenome']
    data_nascimento = request.form['data_nascimento']
    ativo = request.form['ativo']
    novo_membro = Membro(nome,sobrenome,data_nascimento,ativo)
    conector_membro.create(novo_membro)
    return redirect('/membros')

# Rota para a edição
@blue_membro.route('/membros/<id>/edit')
def edita_membro(id):
    membro = conector_membro.get_one(id)
    return render_template('mebros/edit.html',membro = membro, title = 'Edita Membro')

# Pegando as informações no form e fazendo a edição
@blue_membro.route('/membros/<id>', methods = ['POST'])
def atualiza_membro(id):
    nome = request.form['nome']
    sobrenome = request.form['sobrenome']
    data_nascimento = request.form['data_nascimento']
    ativo = request.form['ativo']
    att_membro = Membro(nome,sobrenome,data_nascimento,ativo)
    conector_membro.edit(att_membro)
    return redirect('/membros')

# Fazendo a edição do item pelo id
@blue_membro.route('/membros/<id>/delete')
def delete_membro(id):
    conector_membro.delete(id)
    return redirect('/membros')