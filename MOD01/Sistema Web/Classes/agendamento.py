# Criando a classe
class Agendamento:

    # Construtor da classe 
    def __init__(self,data,instrutor,atividade,perfil,id=None):
        self.data = data
        self.instrutor = instrutor
        self.atividade = atividade
        self.perfil = perfil
        self.id = id