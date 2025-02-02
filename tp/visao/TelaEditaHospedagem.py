from tkinter import ttk
import customtkinter as ctk
import tkinter.messagebox as messagebox
from modelo.Hospedagem import Hospedagem
from persistencia.QuartoDAO import QuartoDAO
from controle.CategoriaQuartoCtrl import CategoriaQuartoCtrl
from controle.QuartoCtrl import QuartoCtrl
from controle.HospedagemCtrl import HospedagemCtrl

class TelaEditarHospedagem:
    def __init__(self, janela, cpfCliente):
        super().__init__()
        
        self.cpf = cpfCliente
        self.janela = janela

        self.telaEditar = ctk.CTkFrame(self.janela, fg_color="#a9a9a9", width=800, height=600)
        
        self.centralFrame = ctk.CTkFrame(self.telaEditar, fg_color="#504B4B", width=500, height=500)
        self.centralFrame.place(relx=0.5, rely=0.5, anchor="center")
        
        self.titleTelaEditar = ctk.CTkLabel(self.telaEditar, text="Editar Hospedagem")
        self.titleTelaEditar.place(relx=0.15, rely=0)
        
        # Entrada para o ID do novo quarto
        self.entry_id = ctk.CTkEntry(self.centralFrame, placeholder_text="ID Quarto", width=280, height=40)
        self.entry_id.place(relx=0.15, rely=0.2)
        
        # Combobox para selecionar a categoria do quarto
        categorias = CategoriaQuartoCtrl.retornarCategorias()
        self.entry_categoriaQuarto = ttk.Combobox(self.centralFrame, values=categorias)
        self.entry_categoriaQuarto.place(relx=0.15, rely=0.4)
        self.entry_categoriaQuarto.bind("<<ComboboxSelected>>", self.atualizarTabelaQuartos)
        
        # Criar a tabela para selecionar o novo quarto
        self.criarTabela()

        # Botão para voltar à tela principal
        self.buttonVoltar = ctk.CTkButton(self.centralFrame, text="Voltar", fg_color="#C50F11", hover_color='darkred', command=self.show_telaPrincipal)
        self.buttonVoltar.place(relx=0.05, rely=0.8)
        
        # Botão para salvar a edição da hospedagem
        self.buttonSalvar = ctk.CTkButton(self.centralFrame, text="Salvar", fg_color="#C50F11", hover_color='darkred', command=self.salvarEdicaoHospedagem)
        self.buttonSalvar.place(relx=0.605, rely=0.8)
        
        # Inicializar com os dados da hospedagem atual
        self.inicializarDados()

    def show(self):
        self.telaEditar.pack()
            
    def forget(self):
        self.telaEditar.pack_forget()
        
    def show_telaPrincipal(self):
        self.forget()
        from visao.TelaPrincipal import TelaPrincipal
        telaPrincipal = TelaPrincipal(self.janela)
        telaPrincipal.show()
        
    def criarTabela(self):
        # Configurar a tabela para exibir os quartos
        self.tabela = ttk.Treeview(self.centralFrame, columns=('id', 'categoria'), show='headings', height=10)
        self.tabela.heading('id', text='Número do Quarto')
        self.tabela.heading('categoria', text='Categoria')
        self.tabela.column('id', width=150, anchor='center')
        self.tabela.column('categoria', width=150, anchor='center')
        self.tabela.place(relx=0.15, rely=0.5)

        self.tabela.bind('<ButtonRelease-1>', self.selecionarItem)

    def atualizarTabelaQuartos(self, event):
        # Função para atualizar a tabela de acordo com a categoria selecionada
        categoria_selecionada = self.entry_categoriaQuarto.get()
        quartos = QuartoDAO.preencherQuarto()
        
        # Limpar a tabela antes de inserir novos dados
        for row in self.tabela.get_children():
            self.tabela.delete(row)
        
        # Inserir os quartos disponíveis na tabela
        for quarto in quartos:
            if quarto.categoriaQuarto == categoria_selecionada and quarto.reservado == '0':
                self.tabela.insert('', 'end', values=(quarto.id, quarto.categoriaQuarto))

    def selecionarItem(self, event):
        # Função para selecionar um quarto na tabela e preencher o campo de ID
        item_selecionado = self.tabela.selection()[0]
        valores = self.tabela.item(item_selecionado, "values")
        self.id_quarto_selecionado = valores[0]
        
        self.entry_id.delete(0, ctk.END)
        self.entry_id.insert(0, self.id_quarto_selecionado)

    def salvarEdicaoHospedagem(self):
        novo_id_quarto = self.entry_id.get()
        id_hospedagem = getattr(self, 'id_hospedagem_atual', None)

        if not novo_id_quarto:
            messagebox.showwarning("Aviso", "Selecione um quarto antes de salvar!")
            return

        # Atualizar a hospedagem no banco de dados
        try:
            HospedagemCtrl.editarHospedagem(id_hospedagem, novo_id_quarto)
            messagebox.showinfo("Sucesso", "Hospedagem editada com sucesso!")
            self.atualizarTabelaQuartos(None)
        except ValueError as e:
            messagebox.showwarning("Erro", str(e))

    def inicializarDados(self):
        # Inicializar os dados da hospedagem atual
        hospedagem_atual = HospedagemCtrl.buscarPorId(self.id_hospedagem_atual)
        if hospedagem_atual:
            self.entry_id.insert(0, hospedagem_atual.id_quarto)
            categoria_quarto = QuartoCtrl.buscarPorId(hospedagem_atual.id_quarto).categoriaQuarto
            self.entry_categoriaQuarto.set(categoria_quarto)
            self.atualizarTabelaQuartos(None)
        else:
            messagebox.showwarning("Erro", "Hospedagem não encontrada!")
