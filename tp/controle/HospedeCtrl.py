from modelo.Hospede import *
from persistencia.HospedeDAO import HospedeDAO

class HospedeCtrl:
    
    def inserirHospede(novoHospede):
        HospedeDAO.cadastrarHospede(novoHospede)
        
    def buscarPorCpf(cpf):
        hospedes = HospedeDAO.preencherHospedes()

        for hospede in hospedes:
            if cpf.strip() == hospede.cpf.strip():
                return hospede

        return None
    
    def removerHospede(cpf):
        hospedes = HospedeDAO.preencherHospedes()
        encontrado = False

        for hospede in hospedes:
            if hospede.cpf.strip() == cpf.strip():
                hospedes.remove(hospede)
                encontrado = True
                break

        if encontrado:
            HospedeDAO.inserirHospede(hospedes)
            return True
        else:
            return False
        
    def editarHospede(funcionarioHospede):
        Hospedes = HospedeDAO.preencherHospedes()
        for hospede in Hospedes:
            if hospede.cpf == funcionarioHospede.cpf:
                if funcionarioHospede.nome != "":
                    hospede.nome = funcionarioHospede.nome
                if funcionarioHospede.telefone != "":
                    hospede.telefone = funcionarioHospede.telefone
                if funcionarioHospede.endereco != " ":
                    hospede.endereco = funcionarioHospede.endereco
        
        HospedeDAO.inserirHospede(hospede)