import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import tkinter.messagebox as messagebox
from modelo.Funcionario import *
from controle.FuncionarioCtrl import *
from persistencia.HospedeDAO import *

class TelaCadastroFuncionario:
    def __init__(self, janela):
        super().__init__()
         
        self.janela = janela
        
        self.telaCadastro = ctk.CTkFrame(self.janela, fg_color="#a9a9a9", width=800, height=600)
        
        self.centralFrame = ctk.CTkFrame(self.telaCadastro, fg_color="#504B4B", width=500, height=500)
        self.centralFrame.place(relx=0.5, rely=0.5, anchor="center")

        self.titleTelainicial = ctk.CTkLabel(self.telaCadastro, text= "Hotel Pousada Xangrila")
        self.titleTelainicial.place(relx=0.15, rely=0)
        
        
        self.buttonVoltar = ctk.CTkButton(self.centralFrame, text="voltar", fg_color="#C50F11", hover_color='darkred', command= self.show_telaInicial)
        self.buttonVoltar.place(relx=0.05, rely=0.8)
        self.buttonResgitrar = ctk.CTkButton(self.centralFrame, text="Cadastrar", fg_color="#C50F11", hover_color='darkred', command= self.cadastraFuncionario)
        self.buttonResgitrar.place(relx=0.605, rely=0.8)
        
        self.entry_funcionarioName = ctk.CTkEntry(self.centralFrame, placeholder_text="nome", width=280,height=40)
        self.entry_funcionarioName.place(relx=0.15, rely=0.2)
        self.entry_funcionarioCpf = ctk.CTkEntry(self.centralFrame, placeholder_text="cpf", width=280,height=40)
        self.entry_funcionarioCpf.place(relx=0.15, rely=0.3)
        self.entry_funcionarioTelefone = ctk.CTkEntry(self.centralFrame, placeholder_text="telefone", width=280,height=40)
        self.entry_funcionarioTelefone.place(relx=0.15, rely=0.4)
        self.entry_funcionarioEndereco = ctk.CTkEntry(self.centralFrame, placeholder_text="endereço", width=280,height=40)
        self.entry_funcionarioEndereco.place(relx=0.15, rely=0.5)
        self.entry_funcionarioLogin = ctk.CTkEntry(self.centralFrame, placeholder_text="login", width=280,height=40)
        self.entry_funcionarioLogin.place(relx=0.15, rely=0.6)
        self.entry_password = ctk.CTkEntry(self.centralFrame, show="*", placeholder_text="Senha", width=280,height=40)
        self.entry_password.place(relx=0.15, rely=0.7)
    
    def show(self):
        self.telaCadastro.pack()
            
    def forget(self):
        self.telaCadastro.pack_forget()
        
    def show_telaInicial(self):
            self.forget()
            from visao.TelaInicial import TelaInicial
            telaInicial = TelaInicial(self.janela)
            telaInicial.show()
    
    def cadastraFuncionario(self):
        
        novoFuncionario = Funcionario(self.entry_funcionarioName.get(),self.entry_funcionarioCpf.get(),self.entry_funcionarioTelefone.get(),self.entry_funcionarioEndereco.get(),self.entry_funcionarioLogin.get(),self.entry_password.get())
        
        FuncionarioCtrl.inserirFuncionario(novoFuncionario)
        
    