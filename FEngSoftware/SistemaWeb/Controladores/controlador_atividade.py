# Imports

from flask import request,redirect,render_template
from flask import Blueprint
from Classes.atividade import Atividade
from Conectores import conector_atividade

# É como um Controller do MVC mas construido a mão, ou seja, pode se fazer a validação que quiser por aqui

# Instância da Classe
blue_atividade = Blueprint('atividades',__name__)

# Rota da página principal
@blue_atividade.route('/atividades')
def index():
    atividades = conector_atividade.get_all()
    return render_template('/atividades/index.html',atividades = atividades, title='Atividades')

# Rota para a página de criação
@blue_atividade.route('/atividades/novo')
def nova_atividade():
    return render_template('/atividades/novo.html')

# Pegando informações do form e criando novo
@blue_atividade.route('/atividades', methods=['POST'])
def cria_novo():
    nome_atividade = request.form['nome']
    duracao = request.form['duracao']
    tipo = request.form['tipo']
    nova_atividade = Atividade(nome_atividade,tipo,duracao)
    conector_atividade.create(nova_atividade)
    return redirect('/atividades')

# Rota para edição 
@blue_atividade.route('/atividades/<id>/edit')
def edita_atividade(id):
    return render_template("/atividades/editar.html")

# Pegando informações do form e fazendo a edição
@blue_atividade.route('/atividades/<id>')
def atualiza_atividade(id):
    nome_atividade = request.form['nome']
    duracao = request.form['duracao']
    tipo = request.form['tipo']
    att_atividade = Atividade(nome_atividade,tipo,duracao)
    conector_atividade.edit(att_atividade)
    return redirect('/atividades')

# Delentado item pelo id
@blue_atividade.route('/atividades/<id>/delete')
def delete_atividade(id):
    conector_atividade.delete_one(id)
    return redirect('/atividades')