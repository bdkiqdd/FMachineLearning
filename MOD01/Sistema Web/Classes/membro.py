class Membro:
    
    def __init__(self,nome,sobrenome,data_nascimento,ativo,id=None):
        self.data_nascimento = data_nascimento
        self.nome = nome
        self.sobrenome = sobrenome
        self.ativo = ativo
        self.id = id
        