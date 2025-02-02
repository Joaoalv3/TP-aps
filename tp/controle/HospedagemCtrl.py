from persistencia.HospedagemDAO import HospedagemDAO

class HospedagemCtrl:

    def inserirHospedagem(novaHospedagem):
        HospedagemDAO.cadastrarHospedagem(novaHospedagem)

    def buscarPorId(id_hospedagem):
        return HospedagemDAO.buscarPorId(id_hospedagem)

    def editarHospedagem(hospedagemEditada):
        HospedagemDAO.editarHospedagem(hospedagemEditada)

    def removerHospedagem(idHospedagem):
        hospedagens = HospedagemDAO.preencherHospedagens()
        hospedagens_filtradas = [hospedagem for hospedagem in hospedagens if hospedagem.id.strip() != idHospedagem.strip()]

        if len(hospedagens) != len(hospedagens_filtradas):
            HospedagemDAO.inserirHospedagem(hospedagens_filtradas)
            return True
        else:
            return False