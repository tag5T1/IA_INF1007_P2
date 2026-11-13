import tkinter as tk
from tkinter import ttk

class Champ(tk.Frame):
    def __init__(self, container:ttk.Frame, index:int, label:str, param_val:list):
        super().__init__(container)
        self.index = index
        self.parametres_valeurs = param_val
              
        self.string_var = tk.StringVar(self, self.parametres_valeurs[index])
        self.string_var.trace_add('write', self.changer_valeur_param)

        # Label du paramètre
        ttk.Label(self, text=label).pack(side='left')
        # Champ d'entrée du paramètre
        champ = ttk.Entry(self, width=30, textvariable=self.string_var)
        champ.pack(side='left')


    def changer_valeur_param(self, var, index, mode):
        self.parametres_valeurs[self.index] = self.string_var.get()
        print(int(self.string_var.get()))