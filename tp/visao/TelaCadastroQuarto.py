import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import tkinter.messagebox as messagebox
from modelo.Quarto import *
from persistencia.QuartoDAO import *
from persistencia.CategoriaQuartoDAO import *
from controle.QuartoCtrl import *
from controle.CategoriaQuartoCtrl import CategoriaQuartoCtrl




class TelaCadastraQuarto:
    def __init__(self, janela):
        super().__init__()
         
        self.janela = janela
        
        self.telaCadastro = ctk.CTkFrame(self.janela, fg_color="#a9a9a9", width=800, height=600)
        
        self.centralFrame = ctk.CTkFrame(self.telaCadastro, fg_color="#504B4B", width=500, height=500)
        self.centralFrame.place(relx=0.5, rely=0.5, anchor="center")

        self.titleTelaCadastro = ctk.CTkLabel(self.telaCadastro, text= "Hotel Pousada Xangrila")
        self.titleTelaCadastro.place(relx=0.15, rely=0)
        
        
        self.buttonVoltar = ctk.CTkButton(self.centralFrame, text="voltar", fg_color="#C50F11", hover_color='darkred', command= self.show_telaPrincipal)
        self.buttonVoltar.place(relx=0.05, rely=0.8)
        self.buttonResgitrar = ctk.CTkButton(self.centralFrame, text="Cadastrar", fg_color="#C50F11", hover_color='darkred', command= self.cadastraQuarto)
        self.buttonResgitrar.place(relx=0.605, rely=0.8)
        
        self.entry_id= ctk.CTkEntry(self.centralFrame, placeholder_text="Numero do quarto", width=280,height=40)
        self.entry_id.place(relx=0.15, rely=0.2)
        categorias = CategoriaQuartoCtrl.retornarCategorias()
        self.entry_categoriaQuarto = ttk.Combobox(self.centralFrame,text="categoria do quarto", values= categorias)
        self.entry_categoriaQuarto.place(relx=0.15, rely=0.4)
        
    def show(self):
        self.telaCadastro.pack()
            
    def forget(self):
        self.telaCadastro.pack_forget()
        
    def show_telaPrincipal(self):
            self.forget()
            from visao.TelaPrincipal import TelaPrincipal
            telaPrincipal = TelaPrincipal(self.janela) 
            telaPrincipal.show()
    
    def cadastraQuarto(self):
        
        novoQuarto = Quarto(self.entry_id.get(),self.entry_categoriaQuarto.get(),0)
        
        QuartoCtrl.inserirQuarto(novoQuarto)
        
    
        