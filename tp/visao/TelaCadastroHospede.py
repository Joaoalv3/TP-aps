import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import tkinter.messagebox as messagebox
from modelo.Hospede import *
from persistencia.HospedeDAO import *
from controle.HospedeCtrl import *

class TelaCadastroHospede:
        def __init__(self, janela):
                super().__init__()
                
                self.janela = janela
                
                self.telaCadastrohospede = ctk.CTkFrame(self.janela, fg_color="#a9a9a9", width=800, height=600)
                
                self.centralFrame = ctk.CTkFrame(self.telaCadastrohospede, fg_color="#504B4B", width=500, height=500)
                self.centralFrame.place(relx=0.5, rely=0.5, anchor="center")

                self.titleTelainicial = ctk.CTkLabel(self.telaCadastrohospede, text= "Hotel Pousada Xangrila")
                self.titleTelainicial.place(relx=0.15, rely=0)
                
                
                self.buttonVoltar = ctk.CTkButton(self.centralFrame, text="voltar", fg_color="#C50F11", hover_color='darkred', command= self.show_telaPrincipal)
                self.buttonVoltar.place(relx=0.05, rely=0.8)
                self.buttonResgitrar = ctk.CTkButton(self.centralFrame, text="Cadastrar", fg_color="#C50F11", hover_color='darkred', command= self.cadastrahospede)
                self.buttonResgitrar.place(relx=0.605, rely=0.8)
                
                self.entry_hospedeName = ctk.CTkEntry(self.centralFrame, placeholder_text="nome", width=280,height=40)
                self.entry_hospedeName.place(relx=0.15, rely=0.2)
                self.entry_hospedeCpf = ctk.CTkEntry(self.centralFrame, placeholder_text="cpf", width=280,height=40)
                self.entry_hospedeCpf.place(relx=0.15, rely=0.3)
                self.entry_hospedeTelefone = ctk.CTkEntry(self.centralFrame, placeholder_text="telefone", width=280,height=40)
                self.entry_hospedeTelefone.place(relx=0.15, rely=0.4)
                self.entry_hospedeEndereco = ctk.CTkEntry(self.centralFrame, placeholder_text="endereço", width=280,height=40)
                self.entry_hospedeEndereco.place(relx=0.15, rely=0.5)
        
    
        def show(self):
            self.telaCadastrohospede.pack()
                
        def forget(self):
            self.telaCadastrohospede.pack_forget()
            
        def cadastrahospede(self):
            
            novohospede = Hospede(self.entry_hospedeName.get(),self.entry_hospedeCpf.get(),self.entry_hospedeTelefone.get(),self.entry_hospedeEndereco.get())
            
            HospedeCtrl.inserirHospede(novohospede)
            self.showTelaCadastrarHopedagem()
            
        def show_telaPrincipal(self):
            self.forget()
            from visao.TelaPrincipal import TelaPrincipal
            telaInicial = TelaPrincipal(self.janela)
            telaInicial.show()
            
        def showTelaCadastrarHopedagem(self):
                self.forget()
                from visao.TelaCadastrarHospedagem import TelaCadastrarHospedagem
                telaCadastrarHospedagem = TelaCadastrarHospedagem(self.janela,self.entry_hospedeCpf.get())
                telaCadastrarHospedagem.show()
            
