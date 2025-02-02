import customtkinter as ctk
import tkinter.messagebox as messagebox
from persistencia.HospedeDAO import *
from controle.HospedeCtrl import *


class TelaEditaHospede:
    def __init__(self, janela, CPF):
        super().__init__()
        self.cpf = CPF
        self.janela = janela
        
        self.editaHospedeFrame = ctk.CTkFrame(self.janela, fg_color="#a9a9a9", width=800, height=600)
        
        self.centralFrame = ctk.CTkFrame(self.editaHospedeFrame, fg_color="#504B4B", width=500, height=500)
        self.centralFrame.place(relx=0.5, rely=0.5, anchor="center")

        self.titleTelaEdita = ctk.CTkLabel(self.editaHospedeFrame, text="Hotel Pousada Xangrila")
        self.titleTelaEdita.place(relx=0.15, rely=0)
        
        self.buttonVoltar = ctk.CTkButton(self.centralFrame, text="Voltar", fg_color="#C50F11", hover_color='darkred', command=self.show_telaPrincipal)
        self.buttonVoltar.place(relx=0.05, rely=0.8)
        self.buttonEditar = ctk.CTkButton(self.centralFrame, text="Editar", fg_color="#C50F11", hover_color='darkred', command=self.editaFuncionario)
        self.buttonEditar.place(relx=0.605, rely=0.8)
        
        self.entry_hospedeName = ctk.CTkEntry(self.centralFrame, placeholder_text="Nome", width=280, height=40)
        self.entry_hospedeName.place(relx=0.15, rely=0.2)
        self.entry_hospedeCpf = ctk.CTkEntry(self.centralFrame,width=280, height=40)
        self.entry_hospedeCpf.place(relx=0.15, rely=0.3)
        self.entry_hospedeCpf.insert(0, self.cpf)
        self.entry_hospedeCpf.configure(state="disabled")
        self.entry_hospedeTelefone = ctk.CTkEntry(self.centralFrame, placeholder_text="Telefone", width=280, height=40)
        self.entry_hospedeTelefone.place(relx=0.15, rely=0.4)
        self.entry_hospedeEndereco = ctk.CTkEntry(self.centralFrame, placeholder_text="Endereço", width=280, height=40)
        self.entry_hospedeEndereco.place(relx=0.15, rely=0.5)

    def show(self):
        self.editaHospedeFrame.pack()
            
    def forget(self):
        self.editaHospedeFrame.pack_forget()
        
    def show_telaPrincipal(self):
        self.forget()
        from visao.TelaPrincipal import TelaPrincipal
        telaPrincipal = TelaPrincipal(self.janela)
        telaPrincipal.show()
            
    def editaFuncionario(self):
        hospede = Hospede(self.entry_hospedeName.get(), self.cpf, self.entry_hospedeTelefone.get(), self.entry_hospedeEndereco.get())
        HospedeCtrl.editarHospede(hospede)
        messagebox.showinfo("Sucesso", "Hospede editado com sucesso!")
