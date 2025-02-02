import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import tkinter.messagebox as messagebox
from controle.HospedeCtrl import *
from persistencia.HospedeDAO import *

class TelaPesquisaHospedeHospedagem:
    def __init__(self, janela):
        self.janela = janela

       
        self.tela = ctk.CTkFrame(self.janela, fg_color="#a9a9a9", width=800, height=600)
        self.tela.pack(fill="both", expand=True) 

        
        self.centralFrame = ctk.CTkFrame(self.tela, fg_color="#504B4B", width=400, height=300)
        self.centralFrame.place(relx=0.5, rely=0.5, anchor="center")

       
        self.entryPesquisaHospede = ctk.CTkEntry(self.centralFrame, placeholder_text="123.456.789-00", width=280, height=40)
        self.entryPesquisaHospede.place(relx=0.5, rely=0.2, anchor="center")  

        
        buttonPesquisarCpf = ctk.CTkButton(self.centralFrame, text="Pesquisar", fg_color="#C50F11", hover_color='darkred', command=self.RetornaHospede)
        buttonPesquisarCpf.place(relx=0.5, rely=0.35, anchor="center") 

        buttonCadastrarHospedagem = ctk.CTkButton(self.centralFrame, text="Cadastrar", fg_color="#C50F11", hover_color='darkred', command= self.show_telaCastrarHospedagem)
        buttonCadastrarHospedagem.place(relx=0.7, rely=0.85, anchor="center")
        
        self.textbox = ctk.CTkTextbox(self.centralFrame, width=300, height=100, font=("Arial", 14))
        self.textbox.place(relx=0.5, rely=0.6, anchor="center")  
        self.textbox.configure(state="disabled")  

       
        self.buttonVoltar = ctk.CTkButton(self.centralFrame, text="Voltar", fg_color="#C50F11", hover_color='darkred', command=self.show_telaPrincipal)
        self.buttonVoltar.place(relx=0.3, rely=0.85, anchor="center")  

    def RetornaHospede(self):
        self.textbox.configure(state="normal")  
        self.textbox.delete("1.0", tk.END)  
        self.cpf = self.entryPesquisaHospede.get()
        hospede = HospedeCtrl.buscarPorCpf(self.cpf)
        if hospede is not None:
            text = f"Nome: {hospede.nome}, Cpf: {hospede.cpf}, Telefone: {hospede.telefone}, Endereço: {hospede.endereco}"
            self.textbox.insert("1.0", text)
        else:
            messagebox.showinfo("Aviso", "Hóspede não encontrado.")
        
        self.textbox.configure(state="disabled")  


    def show(self):
        self.tela.pack()

    def forget(self):
        self.tela.pack_forget()

    def show_telaPrincipal(self):
        self.forget()
        from visao.TelaPrincipal import TelaPrincipal
        telaPrincipal = TelaPrincipal(self.janela)
        telaPrincipal.show()
    
    def show_telaCastrarHospedagem(self):
        self.forget()
        from visao.TelaCadastrarHospedagem import TelaCadastrarHospedagem
        telaCadastrarHospedagem = TelaCadastrarHospedagem(self.janela,self.cpf)
        telaCadastrarHospedagem.show()
