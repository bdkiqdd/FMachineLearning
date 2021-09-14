from Classes.membros import Membros
from Database.connect import conn_base

def get_all():

    membros = []

    sql =   "Select  * from webschema.membro"
    results = conn_base(sql)

    for r in results:
        membro = Membros(r['nome']
                        ,r['sobrenome']
                        ,r['data_nascimento']
                        ,r['id'])
        membros.append(membro)

    return membros

def get_one(id):
    
    sql =   " Select * from webschema.membro Where id = %s"
    values = [id]
    
    result = conn_base(sql,values)[0]

    if result is not None:
        membro = Membros(result['nome']
                        ,result['sobrenome']
                        ,result['data_nascimento']
                        ,result['id'])

    return membro

def create(membro):

    sql =   " Insert into webschema.membro (nome,sobrenome,data_nascimento) VALUES (%s,%s,%s) Returning *;"
    values = [membro.nome,membro.sobrenome,membro.data_nascimento]

    results = conn_base(sql,values)

    membro.id = results[0]['id']

    return membro

def delete_one(id):
    
    sql =   " Delete from webschema.membro where id = %s "
    values = [id]

    conn_base(sql,values)

def edit(membro):

    sql = " Update webschema.membro set (nome,sobrenome,data_nascimento) = (%s,%s,%s) Where id = %s;"
    values = [membro.nome,membro.sobrenome,membro.data_nascimento,membro.id]

    conn_base(sql,values)