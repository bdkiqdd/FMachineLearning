from Classes.aparelhos import Aparelhos
from Database.connect import conn_base

def get_all():

    aparelhos = []

    sql =   "Select  * from webschema.aparelho"
    results = conn_base(sql)

    for r in results:
        aparelho = Aparelhos(r['nome_aparelho']
                            ,r['id'])
        aparelhos.append(aparelho)

    return aparelhos

def get_one(id):
    
    sql =   " Select * from webschema.aparelho Where id = %s"
    values = [id]
    
    result = conn_base(sql,values)[0]

    if result is not None:
        aparelho = Aparelhos(result['nome_aparelho']
                            ,result['id'])

    return aparelho

def create(aparelho):

    sql =   " Insert into webschema.aparelho (nome_aparelho) VALUES (%s) Returning *;"
    values = [aparelho.nome_aparelho]

    results = conn_base(sql,values)

    aparelho.id = results[0]['id']

    return aparelho

def delete_one(id):
    
    sql =   " Delete from webschema.aparelho where id = %s "
    values = [id]

    conn_base(sql,values)

def edit(aparelho):

    sql = " Update webschema.aparelho set (nome_aparelho) = (%s) Where id = %s;"
    values = [aparelho.nome_aparelho
                ,aparelho.id]

    conn_base(sql,values)