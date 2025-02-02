from modelo.Hospedagem import Hospedagem

class HospedagemDAO:

    def cadastrarHospedagem(novaHospedagem):
        with open("banco_de_dados/Hospedagem.txt", "a") as arquivo:
            linha = f"{novaHospedagem.id},{novaHospedagem.cpfCliente},{novaHospedagem.idQuarto}\n"
            arquivo.write(linha)

    def preencherHospedagens():
        hospedagens = []
        try:
            with open("banco_de_dados/Hospedagem.txt", "r") as arquivo:
                for linha in arquivo:
                    if not linha.strip():
                        continue
                    id, cpfCliente, idQuarto = linha.strip().split(',')
                    hospedagem = Hospedagem(id, cpfCliente, idQuarto)
                    hospedagens.append(hospedagem)
        except FileNotFoundError:
            return []
        return hospedagens

    def buscarPorId(id_hospedagem):
        hospedagens = HospedagemDAO.preencherHospedagens()
        for hospedagem in hospedagens:
            if id_hospedagem.strip() == hospedagem.id.strip():
                return hospedagem
        return None
    

    def editarHospedagem(hospedagemEditada):
        hospedagens = HospedagemDAO.preencherHospedagens()
        for hospedagem in hospedagens:
            if hospedagem.id.strip() == hospedagemEditada.id.strip():
                hospedagem.cpfCliente = hospedagemEditada.cpfCliente
                hospedagem.idQuarto = hospedagemEditada.idQuarto
                break
        
        with open("banco_de_dados/Hospedagem.txt", 'w') as arquivo:
            for hospedagem in hospedagens:
                arquivo.write(f"{hospedagem.id},{hospedagem.cpfCliente},{hospedagem.idQuarto}\n")
    
    def inserirHospedagem(listaHospedagem):
        with open("banco_de_dados/Hospedagem.txt", 'w') as arquivo:
            for hospedagem in listaHospedagem:
                arquivo.write(f"{hospedagem.id},{hospedagem.cpfCliente},{hospedagem.idQuarto}\n")