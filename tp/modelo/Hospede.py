from modelo.Pessoa import Pessoa

class Hospede(Pessoa):
    def __init__(self,nome,cpf,telefone,endereco):
        super().__init__(nome,cpf,telefone,endereco)

   
    