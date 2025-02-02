import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import tkinter.messagebox as messagebox
from persistencia.QuartoDAO import *
from controle.CategoriaQuartoCtrl import CategoriaQuartoCtrl
from controle.QuartoCtrl import *

class TelaEditaQuarto:
    def __init__(self, janela,ID):
        super().__init__()
        self.id = ID
        self.janela = janela
        
        self.editaCadastro = ctk.CTkFrame(self.janela, fg_color="#a9a9a9", width=800, height=600)
        
        self.centralFrame = ctk.CTkFrame(self.editaCadastro, fg_color="#504B4B", width=500, height=500)
        self.centralFrame.place(relx=0.5, rely=0.5, anchor="center")

        self.titleTelaEdita = ctk.CTkLabel(self.editaCadastro, text= "Hotel Pousada Xangrila")
        self.titleTelaEdita.place(relx=0.15, rely=0)
        
        self.buttonVoltar = ctk.CTkButton(self.centralFrame, text="voltar", fg_color="#C50F11", hover_color='darkred', command= self.show_telaPrincipal)
        self.buttonVoltar.place(relx=0.05, rely=0.8)
        self.buttonEditar = ctk.CTkButton(self.centralFrame, text="Editar", fg_color="#C50F11", hover_color='darkred', command= self.editaQuarto)
        self.buttonEditar.place(relx=0.605, rely=0.8)
        
        self.textbox = ctk.CTkTextbox(self.centralFrame, width=300, height=100, font=("Arial", 14))
        self.textbox.place(relx=0.5, rely=0.6, anchor="center")
        text = f"ID: {self.id}"
        self.textbox.insert("1.0", text)
        self.textbox.configure(state="disabled") 
        
        categorias = CategoriaQuartoCtrl.retornarCategorias()
        self.entry_categoriaQuarto = ttk.Combobox(self.centralFrame,text="categoria do quarto", values= categorias)
        self.entry_categoriaQuarto.place(relx=0.15, rely=0.4)
        
        
    def show(self):
        self.editaCadastro.pack()
            
    def forget(self):
        self.editaCadastro.pack_forget()
    
    def show_telaPrincipal(self):
        self.forget()
        from visao.TelaPrincipal import TelaPrincipal
        telaPrincipal = TelaPrincipal(self.janela) 
        telaPrincipal.show()
        
    def editaQuarto(self):
        
        quarto = Quarto(self.id,self.entry_categoriaQuarto.get(),0)
        
        QuartoCtrl.editarQuarto(quarto)