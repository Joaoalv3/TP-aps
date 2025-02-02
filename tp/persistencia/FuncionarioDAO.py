from modelo.Funcionario import Funcionario

class FuncionarioDAO:
    def preencheFuncionarios():
        funcionarios = []
        try:
            with open("banco_de_dados/Funcionario.txt", 'r') as arquivo:
                for linha in arquivo:
                    linha = linha.strip()
                    if not linha:  
                        continue
                    
                    valores = linha.split(',')
                    if len(valores) != 6:
                        continue
                    
                    nome, cpf, telefone, endereco, login, senha = valores
                    funcionario = Funcionario(nome, cpf, telefone, endereco, login, senha)
                    funcionarios.append(funcionario)
        except FileNotFoundError:
            return []
        return funcionarios

    def cadastrarFuncionario(novoFuncionario):
        with open("banco_de_dados/Funcionario.txt", "a") as arquivo:
            linha = f"{novoFuncionario.nome},{novoFuncionario.cpf},{novoFuncionario.telefone},{novoFuncionario.endereco},{novoFuncionario.login},{novoFuncionario.senha}\n"
            arquivo.write(linha)

    def inseriFuncionario(listaFuncionario):
        
         with open("banco_de_dados/Funcionario.txts",'w') as arquivo:
                for funcionario in listaFuncionario:
                    arquivo.write(f"{funcionario.nome},{funcionario.cpf},{funcionario.telefone},{funcionario.endereco},{funcionario.login},{funcionario.senha}\n")