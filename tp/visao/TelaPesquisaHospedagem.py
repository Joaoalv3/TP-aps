import tkinter as tk
import customtkinter as ctk
import tkinter.messagebox as messagebox
from controle.HospedagemCtrl import HospedagemCtrl

class TelaPesquisaHospedagem:
    def __init__(self, janela):
        self.janela = janela
        
        self.tela = ctk.CTkFrame(self.janela, fg_color="#a9a9a9", width=800, height=600)
        self.tela.pack(fill="both", expand=True)

        self.centralFrame = ctk.CTkFrame(self.tela, fg_color="#504B4B", width=400, height=300)
        self.centralFrame.place(relx=0.5, rely=0.5, anchor="center")

        self.entryPesquisaHospedagem = ctk.CTkEntry(self.centralFrame, placeholder_text="123.456.789-00", width=280, height=40)
        self.entryPesquisaHospedagem.place(relx=0.5, rely=0.2, anchor="center")  
        
        buttonPesquisarid = ctk.CTkButton(self.centralFrame, text="Pesquisar", fg_color="#C50F11", hover_color='darkred', command=self.RetornaHospedagem)
        buttonPesquisarid.place(relx=0.5, rely=0.35, anchor="center")

        self.textbox = ctk.CTkTextbox(self.centralFrame, width=300, height=100, font=("Arial", 14))
        self.textbox.place(relx=0.5, rely=0.6, anchor="center")
        self.textbox.configure(state="disabled")
        
        self.buttonVoltar = ctk.CTkButton(self.centralFrame, text="Voltar", fg_color="#C50F11", hover_color='darkred', command=self.showtelaPrincipal)
        self.buttonVoltar.place(relx=0.3, rely=0.85, anchor="center")
        
        self.buttonremover = ctk.CTkButton(self.centralFrame, text="Remover", fg_color="#C50F11", hover_color='darkred', command= self.removerHospedagem)
        self.buttonremover.place(relx=0.7, rely=0.85, anchor="center") 
    
    def RetornaHospedagem(self):
        self.textbox.configure(state="normal")
        self.textbox.delete("1.0", tk.END)

        self.idHospedagem = self.entryPesquisaHospedagem.get()
        hospedagem = HospedagemCtrl.buscarPorId(self.idHospedagem)
        if hospedagem is not None:
            text = f"ID: {hospedagem.id}, CPF do Hóspede: {hospedagem.cpfCliente}, Quarto Reservado: {hospedagem.idQuarto}"
            self.textbox.insert("1.0", text)
        else:
            messagebox.showinfo("Aviso", "Hospedagem não encontrada.")
        
        self.textbox.configure(state="disabled")

    def show(self):
        self.tela.pack()

    def forget(self):
        self.tela.pack_forget()
        
    def showtelaPrincipal(self):
        self.forget()
        from visao.TelaPrincipal import TelaPrincipal
        telaPrincipal = TelaPrincipal(self.janela)
        telaPrincipal.show()
        
    def showTelaEditarHospedagem(self):
        self.forget()
        from visao.TelaEditaHospedagem import TelaEditarHospedagem
        telaEditaHospedagem = TelaEditarHospedagem(self.janela, self.idHospedagem)
        telaEditaHospedagem.show()
    
    def removerHospedagem(self):
        id = self.entryPesquisaHospedagem.get()
        result = HospedagemCtrl.removerHospedagem(id)
        
        if result:
            messagebox.showinfo("Sucesso", "Hospedagem removido com sucesso.")
        else:
            messagebox.showinfo("Erro", "Erro ao remover hospedagem ou hospedagem não encontrado.")