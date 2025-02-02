from persistencia.QuartoDAO import QuartoDAO

class QuartoCtrl:

    def inserirQuarto(novoQuarto):
        QuartoDAO.cadastrarQuarto(novoQuarto)

    def buscarPorId(id_quarto):
        quartos = QuartoDAO.preencherQuarto()
        for quarto in quartos:
            if id_quarto.strip() == quarto.id:
                return quarto
        return None

    def editarQuarto(quartoEditado):
        quartos = QuartoDAO.preencherQuarto()
        for quarto in quartos:
            if quarto.id == quartoEditado.id:
                quarto.categoriaQuarto = quartoEditado.categoriaQuarto
        QuartoDAO.inserirQuarto(quartos)

    def removerQuarto(id_quarto):
        quartos = QuartoDAO.preencherQuarto()
        quartos_atualizados = [quarto for quarto in quartos if quarto.id.strip() != id_quarto.strip()]

        if len(quartos) > len(quartos_atualizados):
            QuartoDAO.inserirQuarto(quartos_atualizados)
            return True
        else:
            return False

    def atualizarStatusReserva(id_quarto, reservado):
        quartos = QuartoDAO.preencherQuarto()
        for quarto in quartos:
            if quarto.id == id_quarto:
                quarto.reservado = reservado
                break
        QuartoDAO.inserirQuarto(quartos)
