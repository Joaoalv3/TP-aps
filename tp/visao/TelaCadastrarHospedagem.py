from tkinter import ttk
import customtkinter as ctk
import tkinter.messagebox as messagebox
from modelo.Hospedagem import Hospedagem
from persistencia.QuartoDAO import QuartoDAO
from controle.CategoriaQuartoCtrl import CategoriaQuartoCtrl
from controle.HospedagemCtrl import *
from controle.QuartoCtrl import *


class TelaCadastrarHospedagem:
    def __init__(self, janela, CPF):
        super().__init__()
        
        self.janela = janela
        self.cpf = CPF
        
        self.telaCadastro = ctk.CTkFrame(self.janela, fg_color="#a9a9a9", width=800, height=600)
        
        self.centralFrame = ctk.CTkFrame(self.telaCadastro, fg_color="#504B4B", width=500, height=500)
        self.centralFrame.place(relx=0.5, rely=0.5, anchor="center")
        
        self.titleTelaCadastro = ctk.CTkLabel(self.telaCadastro, text="Hotel Pousada Xangrila")
        self.titleTelaCadastro.place(relx=0.15, rely=0)
        
        self.entry_id = ctk.CTkEntry(self.centralFrame, placeholder_text="ID hospedagem", width=280, height=40)
        self.entry_id.place(relx=0.15, rely=0.2)
        
        self.buttonVoltar = ctk.CTkButton(self.centralFrame, text="Voltar", fg_color="#C50F11", hover_color='darkred', command=self.show_telaPrincipal)
        self.buttonVoltar.place(relx=0.8, rely=0.5)
        self.buttonRegistrar = ctk.CTkButton(self.centralFrame, text="Cadastrar", fg_color="#C50F11", hover_color='darkred', command=self.cadastraHospedagem)
        self.buttonRegistrar.place(relx=0.8, rely=0.9)
        
        categorias = CategoriaQuartoCtrl.retornarCategorias()
        self.entry_categoriaQuarto = ttk.Combobox(self.centralFrame, text="Categoria do quarto", values=categorias)
        self.entry_categoriaQuarto.place(relx=0.15, rely=0.4)
        self.entry_categoriaQuarto.bind("<<ComboboxSelected>>", self.atualizarTabelaQuartos)
        
            
        self.criarTabela()

    def show(self):
        self.telaCadastro.pack()
            
    def forget(self):
        self.telaCadastro.pack_forget()
        
    def show_telaPrincipal(self):
        self.forget()
        from visao.TelaPrincipal import TelaPrincipal
        telaPrincipal = TelaPrincipal(self.janela)
        telaPrincipal.show()
        
    def criarTabela(self):
        
        self.tabela = ttk.Treeview(self.centralFrame, columns=('id', 'categoria'), show='headings', height=10)
        self.tabela.heading('id', text='Número do Quarto')
        self.tabela.heading('categoria', text='Categoria')
        self.tabela.column('id', width=150, anchor='center')
        self.tabela.column('categoria', width=150, anchor='center')
        self.tabela.place(relx=0.15, rely=0.5)

        self.tabela.bind('<ButtonRelease-1>', self.selecionarItem)

    def atualizarTabelaQuartos(self, event):
        categoria_selecionada = self.entry_categoriaQuarto.get()
        quartos = QuartoDAO.preencherQuarto()
        
        
        for row in self.tabela.get_children():
            self.tabela.delete(row)

        
        for quarto in quartos:
            if quarto.categoriaQuarto == categoria_selecionada and quarto.reservado == '0':
                self.tabela.insert('', 'end', values=(quarto.id, quarto.categoriaQuarto))

    def selecionarItem(self, event):
       
        item_selecionado = self.tabela.selection()[0]
        valores = self.tabela.item(item_selecionado, "values")
        
        
        self.id_quarto_selecionado = valores[0]
        
       
        self.entry_id.delete(0, ctk.END)
        self.entry_id.insert(0, self.id_quarto_selecionado)
        
    def cadastraHospedagem(self):
        id_hospedagem = self.entry_id.get()
        cpf_cliente = self.cpf
        id_quarto = getattr(self, 'id_quarto_selecionado', None)


        if not id_quarto:
            messagebox.showwarning("Aviso", "Selecione um quarto antes de cadastrar!")
            return

        novaHospedagem = Hospedagem(id_hospedagem, cpf_cliente, id_quarto)
        HospedagemCtrl.inserirHospedagem(novaHospedagem)

        
        QuartoCtrl.atualizarStatusReserva(id_quarto, 1)
        
        messagebox.showinfo("Sucesso", "Hospedagem cadastrada com sucesso!")
        self.atualizarTabelaQuartos(None)
