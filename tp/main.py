import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from janela import Janela
from visao.TelaInicial import TelaInicial


def main():
    
    janela = Janela()
    
    telaInicial = TelaInicial(janela)
    telaInicial.show()

 
    janela.mainloop()
    
if __name__ == "__main__":
    main()