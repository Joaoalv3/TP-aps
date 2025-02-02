import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import tkinter.messagebox as messagebox
from visao.TelaCadastroFuncionario import TelaCadastroFuncionario
from visao.TelaPrincipal import TelaPrincipal
from controle.FuncionarioCtrl import *


class TelaInicial:
        def __init__(self, janela):

                self.janela = janela
                self.telaInicial = ctk.CTkFrame(self.janela, fg_color="#a9a9a9", width=800, height=600)

                self.centralFrame = ctk.CTkFrame(self.telaInicial, fg_color="#504B4B", width=400, height=300)
                self.centralFrame.place(relx=0.5, rely=0.5, anchor="center")

                self.titleTelainicial = ctk.CTkLabel(self.telaInicial, text= "Hotel Pousada Xangrila")
                self.titleTelainicial.place(relx=0.15, rely=0)

                self.entryLogin= ctk.CTkEntry(self.centralFrame, placeholder_text="Login", width=280,height=40)
                self.entryLogin.place(relx=0.15, rely=0.2)
                self.entrySenha = ctk.CTkEntry(self.centralFrame, show="*", placeholder_text="Senha", width=280,height=40)
                self.entrySenha.place(relx=0.15, rely=0.4)

                self.buttonLogin = ctk.CTkButton(self.centralFrame, text="Login", fg_color="#C50F11", hover_color='darkred', command= self.solicitarLogin)
                self.buttonLogin.place(relx=0.05, rely=0.8)
                self.button_telaResgitro = ctk.CTkButton(self.centralFrame, text="Cadastrar", fg_color="#C50F11", hover_color='darkred', command=self.show_telaCadastro)
                self.button_telaResgitro.place(relx=0.605, rely=0.8)

        def show(self):
                self.telaInicial.pack()
                
        def forget(self):
                self.telaInicial.pack_forget()

        def show_telaCadastro(self):
                self.forget()
                telaCadastro = TelaCadastroFuncionario(self.janela)
                telaCadastro.show()
                
        def mostrarTelaPrincipal(self):
                self.forget()
                telaPrincipal = TelaPrincipal(self.janela)
                telaPrincipal.show()     
        
        def solicitarLogin(self):
                   
                validacao = FuncionarioCtrl.validarLogin(self.entryLogin.get(),self.entrySenha.get())
                
                if validacao:
                        self.mostrarTelaPrincipal()     
                        
                else:
                        messagebox.showerror("Erro", "Login ou senha errada")
                
                
            
            
            
            



      