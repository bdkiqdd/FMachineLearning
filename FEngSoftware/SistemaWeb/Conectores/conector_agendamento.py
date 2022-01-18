from Classes.agendamento import Agendamento
from Database.connect import conn_base
import Conectores.conector_instrutor as conector_instrutor
import Conectores.conector_atividade as conector_atividade 
import Conectores.conector_membro as conector_membro

# Faz o select no banco por todos os itens
def get_all():

    agendamentos = []

    sql =   "Select  * from webschema.agendamento"
    results = conn_base(sql)

    for r in results:

        instrutor = conector_instrutor.get_one(r['instrutor'])
        atividade = conector_atividade.get_one(r['atividade'])
        perfil = conector_membro.get_one(r['perfil'])

        agendamento = Agendamento(r['data']
                                    ,instrutor
                                    ,atividade
                                    ,perfil
                                    ,r['id'])

        agendamentos.append(agendamento)

    return agendamentos

# Faz select no banco, procurando por um ID
def get_one(id):
    
    sql =   " Select * from webschema.agendamento Where id = %s"
    values = [id]
    
    result = conn_base(sql,values)[0]

    instrutor = conector_instrutor.get_one(result['instrutor'])
    atividade = conector_atividade.get_one(result['atividade'])
    perfil = conector_membro.get_one(result['perfil'])

    if result is not None:
        agendamento = Agendamento(result['data']
                                    ,instrutor
                                    ,atividade
                                    ,perfil
                                    ,result['id'])

    return agendamento

# Função para criação de item novo
def create(agendamento):

    sql =   " Insert into webschema.agendamento (data,instrutor,atividade,perfil) VALUES (%s,%s,%s) Returning *;"
    values = [agendamento.data,agendamento.instrutor,agendamento.atividade,agendamento.perfil]

    results = conn_base(sql,values)

    agendamento.id = results[0]['id']

    return agendamento

# Função para deletar item 
def delete(id):
    
    sql =   " Delete from webschema.agendamento where id = %s "
    values = [id]

    conn_base(sql,values)
