import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import tkinter.messagebox as messagebox


class TelaPrincipal:
    def __init__(self, janela):
    
        self.janela = janela
        self.telaPrincipal = ctk.CTkFrame(self.janela, fg_color="#a9a9a9", width=800, height=600)
        
        self.centralFrame = ctk.CTkFrame(self.telaPrincipal, fg_color="#504B4B", width=400, height=300)
        self.centralFrame.place(relx=0.5, rely=0.5, anchor="center")
        
        # Primeira coluna de botões
        button_telaCadastrarCategoriaQuarto = ctk.CTkButton(self.centralFrame, text="Cadastrar categoria de quarto", fg_color="#C50F11", hover_color='darkred', command=self.show_telaCasdastrarCategoriaQuarto)
        button_telaCadastrarCategoriaQuarto.grid(row=0, column=0, padx=10, pady=10)
        
        button_telaPesquisaCategoriaQuarto = ctk.CTkButton(self.centralFrame, text="Pesquisar categoria de quarto", fg_color="#C50F11", hover_color='darkred', command=self.show_telaPesquisaCategoriaQuarto)
        button_telaPesquisaCategoriaQuarto.grid(row=1, column=0, padx=10, pady=10)
        
        button_telaCategoriaQuarto = ctk.CTkButton(self.centralFrame, text="Cadastrar quarto", fg_color="#C50F11", hover_color='darkred', command=self.show_telaCategoriaQuarto)
        button_telaCategoriaQuarto.grid(row=2, column=0, padx=10, pady=10)
        
        button_telaPesquisaQuarto = ctk.CTkButton(self.centralFrame, text="Pesquisar quarto", fg_color="#C50F11", hover_color='darkred', command=self.show_telaPesquisaQuarto)
        button_telaPesquisaQuarto.grid(row=3, column=0, padx=10, pady=10)

        button_telaPesquisaHospede = ctk.CTkButton(self.centralFrame, text="Pesquisar hóspede", fg_color="#C50F11", hover_color='darkred', command=self.show_telaPesquisaHospede)
        button_telaPesquisaHospede.grid(row=4, column=0, padx=10, pady=10)

        # Segunda coluna de botões
        button_telaCadastrarHospedagem = ctk.CTkButton(self.centralFrame, text="Cadastrar hospedagem", fg_color="#C50F11", hover_color='darkred', command=self.show_telaCadastrarHospedagem)
        button_telaCadastrarHospedagem.grid(row=0, column=1, padx=10, pady=10)
        
        button_telaPesquisaHospedagem = ctk.CTkButton(self.centralFrame, text="Pesquisar hospedagem", fg_color="#C50F11", hover_color='darkred', command=self.show_telaPesquisaHospedagem)
        button_telaPesquisaHospedagem.grid(row=1, column=1, padx=10, pady=10)

        button_telaPesquisaFuncionario = ctk.CTkButton(self.centralFrame, text="Pesquisar funcionário", fg_color="#C50F11", hover_color='darkred', command=self.show_telaPesquisaFuncionario)
        button_telaPesquisaFuncionario.grid(row=2, column=1, padx=10, pady=10)
        
        button_logout = ctk.CTkButton(self.centralFrame, text="Logout", fg_color="#C50F11", hover_color='darkred', command=self.logout)
        button_logout.grid(row=4, column=1, padx=10, pady=10)
          
    def show(self):
        self.telaPrincipal.pack()
        
    def forget(self):
        self.telaPrincipal.pack_forget()

    def show_telaCasdastrarCategoriaQuarto(self):
        self.forget()
        from visao.TelaCadastrarCategoriaQuarto import TelaCadastroCategoriaQuarto
        telaCadastroCategoriaQuarto = TelaCadastroCategoriaQuarto(self.janela)
        telaCadastroCategoriaQuarto.show()
        
    def show_telaCategoriaQuarto(self):
        self.forget()
        from visao.TelaCadastroQuarto import TelaCadastraQuarto
        telaCadastroQuarto = TelaCadastraQuarto(self.janela)
        telaCadastroQuarto.show()

    def show_telaCadastrarHospedagem(self):
        self.forget()
        from visao.TelaVerificaCadastroHospede import VerificaCadastroHospede
        telaVerificaCadastroHospede = VerificaCadastroHospede(self.janela)
        telaVerificaCadastroHospede.show()

    def show_telaPesquisaHospedagem(self):
        self.forget()
        from visao.TelaPesquisaHospedagem import TelaPesquisaHospedagem
        telaPesquisaHospedagem = TelaPesquisaHospedagem(self.janela)
        telaPesquisaHospedagem.show()
    
    def show_telaPesquisaFuncionario(self):
        self.forget()
        from visao.TelaPesquisaFuncionario import TelaPesquisaFuncionario
        telaTelaPesquisaFuncionario = TelaPesquisaFuncionario(self.janela)
        telaTelaPesquisaFuncionario.show()
    
    def show_telaPesquisaHospede(self):
        self.forget()
        from visao.TelaPesquisaHospede import TelaPesquisaHospede
        telaTelaPesquisaHospede = TelaPesquisaHospede(self.janela)
        telaTelaPesquisaHospede.show()
    
    def show_telaPesquisaQuarto(self):
        self.forget()
        from visao.TelaPesquisaQuarto import TelaPesquisaQuarto
        telaPesquisaQuarto = TelaPesquisaQuarto(self.janela)
        telaPesquisaQuarto.show()
        
    def show_telaPesquisaCategoriaQuarto(self):
        self.forget()
        from visao.TelaPesquisaCategoriaQuarto import TelaPesquisaCategoriaQuarto
        telaPesquisaCategoriaQuarto = TelaPesquisaCategoriaQuarto(self.janela)
        telaPesquisaCategoriaQuarto.show()
    
    
    def logout(self):
        self.forget()
        from visao.TelaInicial import TelaInicial
        telaInicial = TelaInicial(self.janela)
        telaInicial.show()

