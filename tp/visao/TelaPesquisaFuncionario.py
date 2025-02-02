import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import tkinter.messagebox as messagebox
from controle.FuncionarioCtrl import *
from persistencia.FuncionarioDAO import *

class TelaPesquisaFuncionario:
    def __init__(self,janela):

        self.janela = janela

        self.tela = ctk.CTkFrame(self.janela, fg_color="#a9a9a9", width=800, height=600)

        self.centralFrame = ctk.CTkFrame(self.tela, fg_color="#504B4B", width=400, height=300)
        self.centralFrame.place(relx=0.5, rely=0.5, anchor="center")

        self.entryPesquisaFuncionario = ctk.CTkEntry(self.centralFrame, placeholder_text="123.456.789-00", width=280,height=40)
        self.entryPesquisaFuncionario.place(relx=0.5, rely=0.2, anchor="center")  

        buttonPesquisarCpf = ctk.CTkButton(self.centralFrame, text="pesquisar", fg_color="#C50F11", hover_color='darkred', command= self.RetornaFuncionario)
        buttonPesquisarCpf.place(relx=0.25, rely=0.35, anchor="center")

        self.textbox = ctk.CTkTextbox(self.centralFrame, width=300, height=50, font=("Arial", 14))
        self.textbox.place(relx=0.5, rely=0.6, anchor="center")  
        self.textbox.configure(state="disabled")  
        
        self.buttonVoltar = ctk.CTkButton(self.centralFrame, text="voltar", fg_color="#C50F11", hover_color='darkred', command= self.show_telaPrincipal)
        self.buttonVoltar.place(relx=0.25, rely=0.9, anchor="center")
        self.buttonremover = ctk.CTkButton(self.centralFrame, text="Remover", fg_color="#C50F11", hover_color='darkred', command= self.RemoverFuncionario)
        self.buttonremover.place(relx=0.75, rely=0.35, anchor="center")
        self.buttonTelaEditaFuncionario =  ctk.CTkButton(self.centralFrame, text="editar", fg_color="#C50F11", hover_color='darkred', command= self.showTelaEditarFuncionario)
        self.buttonTelaEditaFuncionario.place(relx=0.75, rely=0.9, anchor="center")
   
    
    '''def PegarCpf(self):
        cpf = self.entryPesquisaFuncionario.get()
        self.hospede = FuncionarioDAO.buscarPorCpf(cpf)
        return self.hospede'''

    def RetornaFuncionario(self):
        self.textbox.configure(state="normal")  
        self.textbox.delete("1.0", tk.END)  
        self.cpf = self.entryPesquisaFuncionario.get()
        funcionario = FuncionarioCtrl.buscarPorCpf(self.cpf)
        if funcionario is not None:
            text = f"Nome: {funcionario.nome}, Cpf: {funcionario.cpf}, Telefone: {funcionario.telefone}, Endereço: {funcionario.endereco}"
            self.textbox.insert("1.0", text)
        else:
            messagebox.showinfo("Aviso", "Funcionario não encontrado.")
        
        self.textbox.configure(state="disabled")  
    
    def RemoverFuncionario(self):
        cpf = self.entryPesquisaFuncionario.get()
        result = FuncionarioCtrl.removerFuncionario(cpf)
        if result:
            messagebox.showinfo("Sucesso", "funcionario removido com sucesso.")
        else:
            messagebox.showinfo("Erro", "Erro ao remover funcionario ou funcionario não encontrado.")
    
    def show(self):
        self.tela.pack()
            
    def forget(self):
        self.tela.pack_forget()
    
    def show_telaPrincipal(self):
            self.forget()
            from visao.TelaPrincipal import TelaPrincipal
            telaPrincipal = TelaPrincipal(self.janela)
            telaPrincipal.show() 
            
    def showTelaEditarFuncionario(self):
        self.forget()
        from visao.TelaEditaFuncionario import TelaEditaFuncionario
        telaEditaFuncionario = TelaEditaFuncionario(self.janela,self.cpf)
        telaEditaFuncionario.show()