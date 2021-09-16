# Imports 
from flask import render_template,redirect, request
from flask import Blueprint
from Classes.membro import Membro
from Conectores import conector_membro,conector_agendamento

# Objeto
blue_membro = Blueprint('membros',__name__)

# Rota da página principal
@blue_membro.route('/membros')
def index_mebros():
    membros = conector_membro.get_all()
    return render_template('membros/index.html',membros = membros,title = 'Todos os membros')

@blue_membro.route('/membros/novo')
def novos_membros():
    return render_template('membros/novo.html',title= 'Novo Membro')

@blue_membro.route('/membros',methods = ['POST'])
def cria_novo():
    nome = request.form['nome']
    sobrenome = request.form['sobrenome']
    data_nascimento = request.form['data_nascimento']
    ativo = request.form['ativo']
    novo_membro = Membro(nome,sobrenome,data_nascimento,ativo)
    conector_membro.create(novo_membro)
    return redirect('/membro')

@blue_membro.route('/membros/<id>/edit')
def edita_membro():
    membro = conector_membro.get_one(id)
    return render_template('mebros/edit.html',membro = membro, title = 'Edita Membro')