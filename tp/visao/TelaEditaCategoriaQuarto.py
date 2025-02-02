import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import tkinter.messagebox as messagebox
from persistencia.CategoriaQuartoDAO import *
from controle.CategoriaQuartoCtrl import CategoriaQuartoCtrl

class TelaEditaCategoriaQuarto:
    def __init__(self, janela,ID):
        super().__init__()
        self.id = ID
        self.janela = janela
        
        self.editaCategoriaCadastro = ctk.CTkFrame(self.janela, fg_color="#a9a9a9", width=800, height=600)
        
        self.centralFrame = ctk.CTkFrame(self.editaCategoriaCadastro, fg_color="#504B4B", width=500, height=500)
        self.centralFrame.place(relx=0.5, rely=0.5, anchor="center")

        self.titleTelaEdita = ctk.CTkLabel(self.editaCategoriaCadastro, text= "Hotel Pousada Xangrila")
        self.titleTelaEdita.place(relx=0.15, rely=0)
        
        self.buttonVoltar = ctk.CTkButton(self.centralFrame, text="voltar", fg_color="#C50F11", hover_color='darkred', command= self.show_telaPrincipal)
        self.buttonVoltar.place(relx=0.05, rely=0.8)
        self.buttonEditar = ctk.CTkButton(self.centralFrame, text="Editar", fg_color="#C50F11", hover_color='darkred', command= self.editaCategoriaQuarto)
        self.buttonEditar.place(relx=0.605, rely=0.8)
        
        self.textbox = ctk.CTkTextbox(self.centralFrame, width=300, height=100, font=("Arial", 14))
        self.textbox.place(relx=0.5, rely=0.6, anchor="center")
        text = f"ID: {self.id}"
        self.textbox.insert("1.0", text)
        self.textbox.configure(state="disabled")
        
        self.entry_categoriaQuatoName = ctk.CTkEntry(self.centralFrame, placeholder_text="nome", width=280,height=40)
        self.entry_categoriaQuatoName.place(relx=0.15, rely=0.3)
        self.entry_categoriaQuatoValor = ctk.CTkEntry(self.centralFrame, placeholder_text="valor", width=280,height=40)
        self.entry_categoriaQuatoValor.place(relx=0.15, rely=0.4)
        
        
    def show(self):
        self.editaCategoriaCadastro.pack()
            
    def forget(self):
        self.editaCategoriaCadastro.pack_forget()
    
    def show_telaPrincipal(self):
        self.forget()
        from visao.TelaPrincipal import TelaPrincipal
        telaPrincipal = TelaPrincipal(self.janela) 
        telaPrincipal.show()
        
    def editaCategoriaQuarto(self):
        
        categoriaQuarto = CategoriaQuarto(self.id,self.entry_categoriaQuatoName.get(),self.entry_categoriaQuatoValor.get())
        
        CategoriaQuartoCtrl.editarCategoriaQuarto(categoriaQuarto)