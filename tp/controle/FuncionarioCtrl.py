
from modelo.Funcionario import *
from persistencia.FuncionarioDAO import *

class FuncionarioCtrl:

    def validarLogin(login,senha):
        
        funcionarios = FuncionarioDAO.preencheFuncionarios()
            
        for funcionario in funcionarios:
            if funcionario.login == login:
                if funcionario.senha == senha:
                    return True
                else:
                    return False
        return False
    
    def removerFuncionario(cpf):
        funcionarios = FuncionarioDAO.preencheFuncionarios()
        encontrado = False
        
        for funcionario in funcionarios:
            if funcionario.cpf.strip() == cpf.strip():
                funcionarios.remove(funcionario)
                encontrado = True
                break
        if encontrado:    
            FuncionarioDAO.inseriFuncionario(funcionarios)
            return True
        else:
            return False
        
    def inserirFuncionario(novoFuncionario):
        FuncionarioDAO.cadastrarFuncionario(novoFuncionario)
    
    def buscarPorCpf(cpf):
        funcionarios = FuncionarioDAO.preencheFuncionarios()
        
        for funcionario in funcionarios:
            if cpf.strip() == funcionario.cpf.strip():
                return funcionario
            
        return None 
    
    def editarFuncionario(funcionarioEditado):
        funcionarios = FuncionarioDAO.preencheFuncionarios()
        for funcionario in funcionarios:
            if funcionario.cpf == funcionarioEditado.cpf:
                if funcionarioEditado.nome != "":
                    funcionario.nome = funcionarioEditado.nome
                if funcionarioEditado.telefone != "":
                    funcionario.telefone = funcionarioEditado.telefone
                if funcionarioEditado.endereco != " ":
                    funcionario.endereco = funcionarioEditado.endereco
                    
        FuncionarioDAO.cadastrarFuncionario(funcionario)
        
        