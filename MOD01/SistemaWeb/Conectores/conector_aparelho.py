from Classes.aparelho import Aparelho
from Database.connect import conn_base

# Faz o select no banco por todos os itens
def get_all():

    aparelhos = []

    sql =   "Select  * from webschema.aparelho"
    results = conn_base(sql)

    for r in results:
        aparelho = Aparelho(r['nome_aparelho']
                            ,r['id'])
        aparelhos.append(aparelho)

    return aparelhos

# Faz select no banco, procurando por um ID
def get_one(id):
    
    sql =   " Select * from webschema.aparelho Where id = %s"
    values = [id]
    
    result = conn_base(sql,values)[0]

    if result is not None:
        aparelho = Aparelho(result['nome_aparelho']
                            ,result['id'])

    return aparelho

# Função para criação de item novo
def create(aparelho):

    sql =   " Insert into webschema.aparelho (nome_aparelho) VALUES (%s) Returning *;"
    values = [aparelho.nome_aparelho]

    results = conn_base(sql,values)

    aparelho.id = results[0]['id']

    return aparelho

# Função para deletar item 
def delete_one(id):
    
    sql =   " Delete from webschema.aparelho where id = %s "
    values = [id]

    conn_base(sql,values)

# Função para editar item 
def edit(aparelho):

    sql = " Update webschema.aparelho set (nome_aparelho) = (%s) Where id = %s;"
    values = [aparelho.nome_aparelho
                ,aparelho.id]

    conn_base(sql,values)