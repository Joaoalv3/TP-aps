import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
from persistencia.CategoriaQuartoDAO import *
from controle.CategoriaQuartoCtrl import CategoriaQuartoCtrl

class TelaPesquisaCategoriaQuarto:
    def __init__(self, janela):
        self.janela = janela

        self.tela = ctk.CTkFrame(self.janela, fg_color="#a9a9a9", width=800, height=600)
        self.tela.pack(fill="both", expand=True)

        self.centralFrame = ctk.CTkFrame(self.tela, fg_color="#504B4B", width=400, height=300)
        self.centralFrame.place(relx=0.5, rely=0.5, anchor="center")

        self.entryPesquisaCategoria = ctk.CTkEntry(self.centralFrame, placeholder_text="ID da Categoria", width=280, height=40)
        self.entryPesquisaCategoria.place(relx=0.5, rely=0.2, anchor="center")

        # Botões ajustados
        buttonPesquisarCategoria = ctk.CTkButton(self.centralFrame, text="Pesquisar", fg_color="#C50F11", hover_color='darkred', command=self.RetornaCategoria)
        buttonPesquisarCategoria.place(relx=0.25, rely=0.35, anchor="center")

        buttonRemoverCategoria = ctk.CTkButton(self.centralFrame, text="Remover", fg_color="#C50F11", hover_color='darkred', command=self.RemoverCategoria)
        buttonRemoverCategoria.place(relx=0.75, rely=0.35, anchor="center")

        self.textbox = ctk.CTkTextbox(self.centralFrame, width=300, height=100, font=("Arial", 14))
        self.textbox.place(relx=0.5, rely=0.6, anchor="center")
        self.textbox.configure(state="disabled")

        # Botões de navegação ajustados
        self.buttonVoltar = ctk.CTkButton(self.centralFrame, text="Voltar", fg_color="#C50F11", hover_color='darkred', command=self.show_telaPrincipal)
        self.buttonVoltar.place(relx=0.25, rely=0.9, anchor="center")

        self.buttonTelaEditaQuarto = ctk.CTkButton(self.centralFrame, text="Editar", fg_color="#C50F11", hover_color='darkred', command=self.showTelaEditarCategoriaQuarto)
        self.buttonTelaEditaQuarto.place(relx=0.75, rely=0.9, anchor="center")

    def RetornaCategoria(self): 
        self.textbox.configure(state="normal")
        self.textbox.delete("1.0", tk.END)

        self.id_categoria = self.entryPesquisaCategoria.get()
        categoria = CategoriaQuartoCtrl.buscarPorId(self.id_categoria)
        if categoria is not None:
            text = f"ID: {categoria.id}, Nome: {categoria.nome}, Valor: {categoria.valor}"
            self.textbox.insert("1.0", text)
        else:
            messagebox.showinfo("Aviso", "Categoria de quarto não encontrada.")

        self.textbox.configure(state="disabled")

    def RemoverCategoria(self):
        id_categoria = self.entryPesquisaCategoria.get()
        resultado = CategoriaQuartoCtrl.removerCategoriaQuarto(id_categoria)
        if resultado:
            messagebox.showinfo("Sucesso", "Categoria de quarto removida com sucesso.")
            self.textbox.configure(state="normal")
            self.textbox.delete("1.0", tk.END)
            self.textbox.configure(state="disabled")
        else:
            messagebox.showinfo("Erro", "Categoria de quarto não encontrada.")

    def show(self):
        self.tela.pack()

    def forget(self):
        self.tela.pack_forget()
        
    def show_telaPrincipal(self):
        self.forget()
        from visao.TelaPrincipal import TelaPrincipal
        telaPrincipal = TelaPrincipal(self.janela)
        telaPrincipal.show()
        
    def showTelaEditarCategoriaQuarto(self):
        self.forget()
        from visao.TelaEditaCategoriaQuarto import TelaEditaCategoriaQuarto
        telaEditaCategoriaQuarto = TelaEditaCategoriaQuarto(self.janela, self.id_categoria)
        telaEditaCategoriaQuarto.show()
