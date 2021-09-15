from flask import render_template,redirect,request
from flask import Blueprint
from Classes.instrutores import Instrutores
from Conectores import conector_instrutores

instrutores_Blue = Blueprint("instrutores",__name__)

@instrutores_Blue.route('/instrutores')
def instrutores_index():
    instrutores = conector_instrutores.get_all()
    return render_template('instrutores/index.html', instrutores = instrutores, title = 'Instrutores')

@instrutores_Blue.route('/instrutores/novo')
def novo_instrutor():
    return render_template('instrutores/novo.html',title =' Novo Instrutor ')

