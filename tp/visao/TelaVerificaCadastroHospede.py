import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import tkinter.messagebox as messagebox
from visao.TelaCadastroHospede import TelaCadastroHospede
from visao.TelaPrincipal import TelaPrincipal
from visao.TelaCadastrarHospedagem import TelaCadastrarHospedagem

class VerificaCadastroHospede:
    def __init__(self, janela):
        super().__init__()
         
        self.janela = janela
        
        self.telaCadastro = ctk.CTkFrame(self.janela, fg_color="#a9a9a9", width=800, height=600)
        
        self.centralFrame = ctk.CTkFrame(self.telaCadastro, fg_color="#504B4B", width=500, height=500)
        self.centralFrame.place(relx=0.5, rely=0.5, anchor="center")
        
        self.buttonVoltar = ctk.CTkButton(self.centralFrame, text="voltar", fg_color="#C50F11", hover_color='darkred', command= self.show_telaPrincipal)
        self.buttonVoltar.place(relx=0.05, rely=0.8)
        
        button_cadastrado = ctk.CTkButton(self.centralFrame, text="Hospede ja cadastrado", fg_color="#C50F11", hover_color='darkred', command= self.show_telaCategoriaQuarto)
        button_cadastrado.place(relx=0.5, rely=0.4)
        button_cadastrar = ctk.CTkButton(self.centralFrame, text="Hospede não cadastrado", fg_color="#C50F11", hover_color='darkred', command= self.show_telaCasdastrarHospede)
        button_cadastrar.place(relx=0.5, rely=0.6)
    
    def show(self):
        self.telaCadastro.pack()
            
    def forget(self):
        self.telaCadastro.pack_forget()
    
    def show_telaCasdastrarHospede(self):
        self.forget()
        telaCadastroHospede = TelaCadastroHospede(self.janela)
        telaCadastroHospede.show()
        
    def show_telaPrincipal(self):
            self.forget()
            telaInicial = TelaPrincipal(self.janela)
            telaInicial.show()
            
    def show_telaCategoriaQuarto(self):
        self.forget()
        from visao.TelaPesquisaHospedeHospedagem import TelaPesquisaHospedeHospedagem
        telaPesquisaHospedeHospedagem = TelaPesquisaHospedeHospedagem(self.janela)
        telaPesquisaHospedeHospedagem.show()