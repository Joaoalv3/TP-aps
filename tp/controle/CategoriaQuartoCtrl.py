from modelo.CategoriaQuarto import CategoriaQuarto
from persistencia.CategoriaQuartoDAO import CategoriaQuartoDAO
class CategoriaQuartoCtrl:
    
    def retornarCategorias():
        categorias = CategoriaQuartoDAO.preencherCategorias()
        nomeCategorias = []
        for categoria in categorias:
            nomeCategorias.append(categoria.nome)
        return nomeCategorias
    
    def preencheCategoriaQuarto(novaCategoriaQuarto):
        CategoriaQuartoDAO.cadastrarCategoriaQuarto(novaCategoriaQuarto)

    def editarCategoriaQuarto(categoriaQuartoEditado):
        try:
            categorias = CategoriaQuartoDAO.preencherCategorias()
            categoria_encontrada = False
            
            for categoria in categorias:
                if categoria.id == categoriaQuartoEditado.id:
                    if categoriaQuartoEditado.nome:
                        categoria.nome = categoriaQuartoEditado.nome
                    if categoriaQuartoEditado.valor:
                        categoria.valor = categoriaQuartoEditado.valor
                    categoria_encontrada = True
                    break
                    
            if categoria_encontrada:
                CategoriaQuartoDAO.inseriCategoriaQuarto(categorias)
            else:
                print("Categoria não encontrada!")
                
        except Exception as e:
            print(f"Erro ao editar categoria: {e}")
            
    def buscarPorId(id_categoria):
        categorias = CategoriaQuartoDAO.preencherCategorias()

        for categoria in categorias:
            if id_categoria.strip() == categoria.id:
                return categoria
            
    def removerCategoriaQuarto(id_categoria):
        categorias = CategoriaQuartoDAO.preencherCategorias()
        encontrado = False

        for categoria in categorias:
            if categoria.id.strip() == id_categoria.strip():
                categorias.remove(categoria)
                encontrado = True
                break

        if encontrado:
            CategoriaQuartoDAO.inseriCategoriaQuarto(categorias)
        else:
            return False