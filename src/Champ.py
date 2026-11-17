import tkinter as tk
import random
from tkinter import ttk

class Champ(tk.Frame):
    def __init__(self, container:ttk.Frame, index:int, label:str, param_val:list, infos):
        super().__init__(container)
        self.index = index
        self.parametres_valeurs = param_val
        self.infos = infos
              
        self.string_var = tk.StringVar(self, str(self.infos["MOY"]))
        self.string_var.trace_add('write', self.changer_valeur_param)

        # Label du paramètre
        ttk.Label(self, text=label).pack(side='left')
        # Champ d'entrée du paramètre
        champ = ttk.Entry(self, width=30, textvariable=self.string_var)
        champ.pack(side='left')

    def changer_valeur_param(self, var, index, mode):
        self.parametres_valeurs[self.index] = float(self.string_var.get())

    def set_random(self):
        self.string_var.set(random.randint(int(self.infos["MIN"]),int(self.infos["MAX"]))) # type: ignore
