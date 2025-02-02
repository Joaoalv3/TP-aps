from modelo.Quarto import Quarto

class QuartoDAO:

    def cadastrarQuarto(novoQuarto):
        with open("banco_de_dados/Quarto.txt", "a") as arquivo:
            linha = f"{novoQuarto.id},{novoQuarto.categoriaQuarto},{novoQuarto.reservado}\n"
            arquivo.write(linha)

    def preencherQuarto():
        quartos = []
        try:
            with open("banco_de_dados/Quarto.txt", "r") as arquivo:
                for linha in arquivo:
                    if not linha.strip():
                        continue

                    id, categoriaQuarto, reservado = linha.strip().split(',')
                    quarto = Quarto(id, categoriaQuarto, reservado)
                    quartos.append(quarto)
        except FileNotFoundError:
            return []
        return quartos

    def inserirQuarto(listaQuarto):
        with open("banco_de_dados/Quarto.txt", 'w') as arquivo:
            for quarto in listaQuarto:
                arquivo.write(f"{quarto.id},{quarto.categoriaQuarto},{quarto.reservado}\n")