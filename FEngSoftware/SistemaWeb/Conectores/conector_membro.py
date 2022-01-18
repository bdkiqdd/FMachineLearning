from Classes.membro import Membro
from Database.connect import conn_base

# Faz o select no banco por todos os itens
def get_all():

    membros = []

    sql =   "Select  * from webschema.membro"
    results = conn_base(sql)

    for r in results:
        membro = Membro(r['nome']
                        ,r['sobrenome']
                        ,r['data_nascimento']
                        ,r['ativo']
                        ,r['id'])
        membros.append(membro)

    return membros

# Faz select no banco, procurando por um ID
def get_one(id):
    
    sql =   " Select * from webschema.membro Where id = %s"
    values = [id]
    
    result = conn_base(sql,values)[0]

    if result is not None:
        membro = Membro(result['nome']
                        ,result['sobrenome']
                        ,result['data_nascimento']
                        ,result['ativo']
                        ,result['id'])

    return membro

# Função para criação de item novo
def create(membro):

    sql =   " Insert into webschema.membro (nome,sobrenome,data_nascimento,ativo) VALUES (%s,%s,%s,1) Returning *;"
    values = [membro.nome,membro.sobrenome,membro.data_nascimento,membro.ativo]

    results = conn_base(sql,values)

    membro.id = results[0]['id']

    return membro

#Função para deletar item 
def delete(id):
    
    sql =   " Delete from webschema.membro where id = %s "
    values = [id]

    conn_base(sql,values)

# Função para "falso" delete
def soft_delete(id):
    
    sql =   " Update webschema.membro set (ativo) = (0) Where id = %s;"
    values = [id]

    conn_base(sql,values)

# Função para editar item 
def edit(membro):

    sql = " Update webschema.membro set (nome,sobrenome,data_nascimento) = (%s,%s,%s) Where id = %s;"
    values = [membro.nome,membro.sobrenome,membro.data_nascimento,membro.id]

    conn_base(sql,values)