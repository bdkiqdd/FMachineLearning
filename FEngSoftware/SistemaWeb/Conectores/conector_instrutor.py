from Classes.instrutor import Instrutor
from Database.connect import conn_base

# Faz o select no banco por todos os itens
def get_all():

    instrutores = []

    sql =   "Select  * from webschema.instrutor"
    results = conn_base(sql)

    for r in results:
        instrutor = Instrutor(r['nome']
                                ,r['sobrenome']
                                ,r['data_nascimento']
                                ,r['id'])
        instrutores.append(instrutor)

    return instrutores

# Faz select no banco, procurando por um ID
def get_one(id):
    
    sql =   " Select * from webschema.instrutor Where id = %s"
    values = [id]
    
    result = conn_base(sql,values)[0]

    if result is not None:
        instrutor = Instrutor(result['nome']
                                ,result['sobrenome']
                                ,result['data_nascimento']
                                ,result['id'])

    return instrutor

# Função para criação de item novo
def create(instrutor):

    sql =   " Insert into webschema.instrutor (nome,sobrenome,data_nascimento) VALUES (%s,%s,%s) Returning *;"
    values = [instrutor.nome,instrutor.sobrenome,instrutor.data_nascimento]

    results = conn_base(sql,values)

    instrutor.id = results[0]['id']

    return instrutor

# Função para deletar item 
def delete_one(id):
    
    sql =   " Delete from webschema.instrutor where id = %s "
    values = [id]

    conn_base(sql,values)

# Função para editar item 
def edit(instrutor):

    sql = " Update webschema.instrutor set (nome,sobrenome,data_nascimento) = (%s,%s,%s) Where id = %s;"
    values = [instrutor.nome,instrutor.sobrenome,instrutor.data_nascimento,instrutor.id]

    conn_base(sql,values)