# Imports
from flask import render_template, request, redirect
from flask import Blueprint
from Classes.agendamento import Agendamento
from Conectores import conector_agendamento
from Conectores import conector_membro
from Conectores import conector_atividade

# É como um Controller do MVC mas construido a mão, ou seja, pode se fazer a validação que quiser por aqui

# Cria o blueprint (instância da classe)
blue_agendamento = Blueprint("agendamentos", __name__)


# Rota para a página index.html
@blue_agendamento.route("/agendamentos")
def agendamentos_index():
    agendamentos = conector_agendamento.get_all()
    return render_template("agendamentos/index.html", agendamentos = agendamentos, title = "agendamentos")


# Rota para novo membro
@blue_agendamento.route("/agendamentos/novo/membro/<id>")
def novo_membro_agendamento(id):
    membro = conector_membro.get_one(id)
    atividades = conector_atividade.get_all()
    return render_template("agendamentos/novo-membro.html", membro = membro, atividades = atividades, title = "Novo Agendamento")


# Rota para nova atividade
@blue_agendamento.route("/agendamentos/novo/atividade/<id>")
def nova_atividade_agendamento(id):
    atividade = conector_atividade.get_one(id)
    membros = conector_membro.get_all()
    return render_template("agendamentos/nova-atividade.html", atividade = atividade, membros = membros, title = "Novo Agendamento")


# Rota para criar agendamento a partir de atividade
@blue_agendamento.route("/agendamentos/atividade", methods = ["POST"])
def cria_agendamento_from_atividade():
    atividade_id = request.form["atividade"]
    membro_id = request.form["membro"]
    atividade = conector_atividade.get_one(atividade_id)
    membro = conector_membro.get_one(membro_id)
    novo_agendamento = Agendamento( atividade, membro )
    conector_agendamento.create(novo_agendamento)
    pagina_atividade = "/atividades/" + atividade_id
    return redirect (pagina_atividade)


# Rota para criar agendamento a partir de membro
@blue_agendamento.route("/agendamentos/membro", methods=["POST"])
def cria_agendamento_from_membro():
    atividade_id = request.form["atividade"]
    membro_id = request.form["membro"]
    atividade = conector_atividade.get_one(atividade_id)
    membro = conector_membro.get_one(membro_id)
    novo_agendamento = Agendamento( atividade, membro )
    conector_agendamento.create(novo_agendamento)
    pagina_membros = "/membros/" + membro_id
    return redirect (pagina_membros)


# Rota para delete
@blue_agendamento.route("/agendamentos/<id>/delete")
def deleta_agendamento(id):
    conector_agendamento.delete(id)
    return redirect("/agendamentos")


# Rota para deletar agendamento de membro
@blue_agendamento.route("/agendamentos/delete/membro/<membro_id>/<atividade_id>")
def deleta_agendamento_membro(membro_id, atividade_id):
    conector_agendamento.delete(membro_id, atividade_id)
    pagina_membro = "/membros/" + membro_id
    return redirect (pagina_membro)


# Rota para deletar agendamento de atividade
@blue_agendamento.route("/agendamentos/delete/atividade/<membro_id>/<atividade_id>")
def deleta_agendamento_atividade(membro_id, atividade_id):
    conector_agendamento.delete(membro_id, atividade_id)
    pagina_agendamento = "/atividades/" + atividade_id
    return redirect (pagina_agendamento)


