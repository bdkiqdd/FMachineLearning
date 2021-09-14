from Classes.agendamentos import Agendamentos
from Database.connect import conn_base
import conector_instrutores
import conector_atividades 
import conector_membros 

def get_all():

    agendamentos = []

    sql =   "Select  * from webschema.agendamento"
    results = conn_base(sql)

    for r in results:

        instrutor = conector_instrutores.get_one(r['instrutor'])
        atividade = conector_atividades.get_one(r['atividade'])
        perfil = conector_membros.get_one(r['perfil'])

        agendamento = Agendamentos(r['data']
                        ,instrutor
                        ,atividade
                        ,perfil
                        ,r['id'])

        agendamentos.append(agendamento)

    return agendamentos

def get_one(id):
    
    sql =   " Select * from webschema.agendamento Where id = %s"
    values = [id]
    
    result = conn_base(sql,values)[0]

    instrutor = conector_instrutores.get_one(result['instrutor'])
    atividade = conector_atividades.get_one(result['atividade'])
    perfil = conector_membros.get_one(result['perfil'])

    if result is not None:
        agendamento = Agendamentos(result['data']
                        ,instrutor
                        ,atividade
                        ,perfil
                        ,result['id'])

    return agendamento

def create(agendamento):

    sql =   " Insert into webschema.agendamento (data,instrutor,atividade,perfil) VALUES (%s,%s,%s) Returning *;"
    values = [agendamento.data,agendamento.instrutor,agendamento.atividade,agendamento.perfil]

    results = conn_base(sql,values)

    agendamento.id = results[0]['id']

    return agendamento

def delete_one(id):
    
    sql =   " Delete from webschema.agendamento where id = %s "
    values = [id]

    conn_base(sql,values)
