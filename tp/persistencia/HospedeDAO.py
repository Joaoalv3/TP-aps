from modelo.Hospede import Hospede

class HospedeDAO:

    def cadastrarHospede(novoHospede):
        with open("banco_de_dados/Hospede.txt", "a") as arquivo:
            linha = f"{novoHospede.nome},{novoHospede.cpf},{novoHospede.telefone},{novoHospede.endereco}\n"
            arquivo.write(linha)
            
    def preencherHospedes():
        hospedes = []
        try:
            with open("banco_de_dados/Hospede.txt", "r") as arquivo:
                for linha in arquivo:
                    if not linha.strip(): 
                        continue
                    valores = linha.strip().split(',')
                    
                    if len(valores) != 4:
                        continue
                    
                    nome, cpf, telefone, endereco = valores
                    hospede = Hospede(nome.strip(), cpf.strip(), telefone.strip(), endereco.strip())
                    hospedes.append(hospede)
        except FileNotFoundError:
            return []
        return hospedes       
    
        
    def inserirHospede(listaHospe):
         with open("banco_de_dados/Hospede.txt", 'w') as arquivo:
                for hospede in listaHospe:
                    arquivo.write(f"{hospede.nome},{hospede.cpf},{hospede.telefone},{hospede.endereco}\n")
        