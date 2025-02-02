import tkinter as tk
from tkinter import ttk
import customtkinter as ctk

class Janela(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.geometry("800x600")
        self.title("Hotel Pousada Xangrila")