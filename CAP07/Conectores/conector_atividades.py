from Classes.atividades import Atividades
from Database.connect import conn_base

def get_all():

    atividades = []

    sql =   "Select  * from webschema.atividade"
    results = conn_base(sql)

    for r in results:
        atividade = Atividades(r['nome_atividade']
                                ,r['tipo']
                                ,r['duracao']
                                ,r['id'])
        atividades.append(atividade)

    return atividades

def get_one(id):
    
    sql =   " Select * from webschema.atividade Where id = %s"
    values = [id]
    
    result = conn_base(sql,values)[0]

    if result is not None:
        atividade = Atividades(result['nome_atividade']
                                ,result['sobrenome']
                                ,result['duracao']
                                ,result['id'])

    return atividade

def create(atividade):

    sql =   " Insert into webschema.atividade (nome_atividade,tipo,duracao) VALUES (%s,%s,%s) Returning *;"
    values = [atividade.nome_atividade
                ,atividade.tipo
                ,atividade.duracao]

    results = conn_base(sql,values)

    atividade.id = results[0]['id']

    return atividade

def delete_one(id):
    
    sql =   " Delete from webschema.atividade where id = %s "
    values = [id]

    conn_base(sql,values)

def edit(atividade):

    sql = " Update webschema.atividade set (nome_atividade,tipo,duracao) = (%s,%s,%s) Where id = %s;"
    values = [atividade.nome_atividade,
                atividade.tipo,
                atividade.duracao,
                atividade.id]

    conn_base(sql,values)