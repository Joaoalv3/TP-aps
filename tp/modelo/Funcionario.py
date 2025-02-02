from modelo.Pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self,nome,cpf,telefone,endereco,login,senha):
        super().__init__(nome,cpf,telefone,endereco)
        self.login = login
        self.senha = senha
