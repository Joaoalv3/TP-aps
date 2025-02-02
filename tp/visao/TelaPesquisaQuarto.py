import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
from persistencia.QuartoDAO import *
from controle.QuartoCtrl import *


class TelaPesquisaQuarto:
    def __init__(self, janela):
        self.janela = janela

        self.tela = ctk.CTkFrame(self.janela, fg_color="#a9a9a9", width=800, height=600)
        self.tela.pack(fill="both", expand=True)


        self.centralFrame = ctk.CTkFrame(self.tela, fg_color="#504B4B", width=400, height=300)
        self.centralFrame.place(relx=0.5, rely=0.5, anchor="center")


        self.entryPesquisaQuarto = ctk.CTkEntry(self.centralFrame, placeholder_text="ID do Quarto", width=280, height=40)
        self.entryPesquisaQuarto.place(relx=0.5, rely=0.2, anchor="center")


        buttonPesquisarQuarto = ctk.CTkButton(self.centralFrame, text="Pesquisar", fg_color="#C50F11", hover_color='darkred', command=self.RetornaQuarto)
        buttonPesquisarQuarto.place(relx=0.25, rely=0.35, anchor="center")


        self.textbox = ctk.CTkTextbox(self.centralFrame, width=300, height=100, font=("Arial", 14))
        self.textbox.place(relx=0.5, rely=0.6, anchor="center")
        self.textbox.configure(state="disabled")

        self.buttonVoltar = ctk.CTkButton(self.centralFrame, text="Voltar", fg_color="#C50F11", hover_color='darkred', command=self.show_telaPrincipal)
        self.buttonVoltar.place(relx=0.25, rely=0.9, anchor="center")
        self.buttonTelaEditaQuarto =  ctk.CTkButton(self.centralFrame, text="editar quarto", fg_color="#C50F11", hover_color='darkred', command= self.showTelaEditarQuarto)
        self.buttonTelaEditaQuarto.place(relx=0.75, rely=0.9, anchor="center")
        self.buttonRemover = ctk.CTkButton(self.centralFrame, text="Remover", fg_color="#C50F11", hover_color='darkred', command=self.RemoverQuarto)
        self.buttonRemover.place(relx=0.75, rely=0.35, anchor="center") 

    def RetornaQuarto(self):
        self.textbox.configure(state="normal")
        self.textbox.delete("1.0", tk.END)

        self.id_quarto = self.entryPesquisaQuarto.get()
        quarto = QuartoCtrl.buscarPorId(self.id_quarto)
        if quarto is not None:
            text = f"ID: {quarto.id}, Categoria: {quarto.categoriaQuarto}, Reservado: {'Sim' if quarto.reservado == '1' else 'Não'}"
            self.textbox.insert("1.0", text)
        else:
            messagebox.showinfo("Aviso", "Quarto não encontrado.")
        
        self.textbox.configure(state="disabled")
        
    def RemoverQuarto(self):
        id_quarto = self.entryPesquisaQuarto.get()
        resultado = QuartoCtrl.removerQuarto(id_quarto)
        if resultado:
            messagebox.showinfo("Sucesso", "Quarto removido com sucesso.")
            self.textbox.configure(state="normal")
            self.textbox.delete("1.0", tk.END)
            self.textbox.configure(state="disabled")
        else:
            messagebox.showinfo("Erro", "Quarto não encontrado.")

    def show(self):
        self.tela.pack()

    def forget(self):
        self.tela.pack_forget()
        
    def show_telaPrincipal(self):
        self.forget()
        from visao.TelaPrincipal import TelaPrincipal
        telaPrincipal = TelaPrincipal(self.janela)
        telaPrincipal.show()
    
    def showTelaEditarQuarto(self):
        self.forget()
        from visao.TelaEditaQuarto import TelaEditaQuarto
        telaEditaQuarto = TelaEditaQuarto(self.janela,self.id_quarto)
        telaEditaQuarto.show()