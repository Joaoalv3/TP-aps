import customtkinter as ctk
import tkinter.messagebox as messagebox
from persistencia.FuncionarioDAO import *
from controle.FuncionarioCtrl import *


class TelaEditaFuncionario:
    def __init__(self, janela, CPF):
        super().__init__()
        self.cpf = CPF
        self.janela = janela
        
        self.editaFuncionarioFrame = ctk.CTkFrame(self.janela, fg_color="#a9a9a9", width=800, height=600)
        
        self.centralFrame = ctk.CTkFrame(self.editaFuncionarioFrame, fg_color="#504B4B", width=500, height=500)
        self.centralFrame.place(relx=0.5, rely=0.5, anchor="center")

        self.titleTelaEdita = ctk.CTkLabel(self.editaFuncionarioFrame, text="Hotel Pousada Xangrila")
        self.titleTelaEdita.place(relx=0.15, rely=0)
        
        self.buttonVoltar = ctk.CTkButton(self.centralFrame, text="Voltar", fg_color="#C50F11", hover_color='darkred', command=self.show_telaPrincipal)
        self.buttonVoltar.place(relx=0.05, rely=0.8)
        self.buttonEditar = ctk.CTkButton(self.centralFrame, text="Editar", fg_color="#C50F11", hover_color='darkred', command=self.editaFuncionario)
        self.buttonEditar.place(relx=0.605, rely=0.8)
        
        self.entry_funcionarioName = ctk.CTkEntry(self.centralFrame, placeholder_text="Nome", width=280, height=40)
        self.entry_funcionarioName.place(relx=0.15, rely=0.2)
        self.entry_funcionarioCpf = ctk.CTkEntry(self.centralFrame,placeholder_text= f"{self.cpf}" ,width=280, height=40)
        self.entry_funcionarioCpf.place(relx=0.15, rely=0.3)
        self.entry_funcionarioCpf.configure(state="disabled")
        self.entry_funcionarioTelefone = ctk.CTkEntry(self.centralFrame, placeholder_text="Telefone", width=280, height=40)
        self.entry_funcionarioTelefone.place(relx=0.15, rely=0.4)
        self.entry_funcionarioEndereco = ctk.CTkEntry(self.centralFrame, placeholder_text="Endereço", width=280, height=40)
        self.entry_funcionarioEndereco.place(relx=0.15, rely=0.5)

    def show(self):
        self.editaFuncionarioFrame.pack()
            
    def forget(self):
        self.editaFuncionarioFrame.pack_forget()
        
    def show_telaPrincipal(self):
        self.forget()
        from visao.TelaPrincipal import TelaPrincipal
        telaPrincipal = TelaPrincipal(self.janela)
        telaPrincipal.show()
            
    def editaFuncionario(self):
        funcionario = Funcionario(self.entry_funcionarioName.get(), self.cpf, self.entry_funcionarioTelefone.get(), self.entry_funcionarioEndereco.get(),"","")
        FuncionarioCtrl.editarFuncionario(funcionario)
        messagebox.showinfo("Sucesso", "Funcionário editado com sucesso!")
