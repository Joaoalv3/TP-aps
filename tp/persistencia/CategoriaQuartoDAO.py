from modelo.CategoriaQuarto import *


class CategoriaQuartoDAO:

    def cadastrarCategoriaQuarto(novaCategoriaQuarto):
        with open("banco_de_dados/CategoriaQuarto.txt", "a") as arquivo:
            linha = f"{novaCategoriaQuarto.id},{novaCategoriaQuarto.nome},{novaCategoriaQuarto.valor}\n"
            arquivo.write(linha)
        
    def preencherCategorias():
        categorias = []
        try:
            with open("banco_de_dados/CategoriaQuarto.txt", 'r') as arquivo:
                for linha in arquivo:
                    if not linha.strip():
                        continue
                    id, nome, valor = linha.strip().split(',')
                    categoria = CategoriaQuarto(id, nome, valor)  
                    categorias.append(categoria)
        except FileNotFoundError:
            return []
        return categorias
        
    def inseriCategoriaQuarto(listaCategoriaQuarto):
        with open("banco_de_dados/CategoriaQuarto.txt", 'w') as arquivo:
            for categoria in listaCategoriaQuarto:
                arquivo.write(f"{categoria.id},{categoria.nome},{categoria.valor}\n")