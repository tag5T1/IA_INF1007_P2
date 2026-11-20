import tkinter as tk
import random
from tkinter import ttk

class Champ(tk.Frame):
    def __init__(self, container:ttk.Frame, index:int, label:str, param_val:list, infos):
        """Initialisation du champ d'entrée"""
        super().__init__(container)
        self.index = index
        self.parametres_valeurs = param_val
        self.infos = infos
                
        self.tk_var = tk.Variable(self, str(self.infos["MOY"]))
        self.tk_var.trace_add('write', self.changer_valeur_param)

        # Label du paramètre
        ttk.Label(self, text=label).pack(side='left')
        # Champ d'entrée du paramètre
        self.champ = ttk.Entry(self, width=30, textvariable=self.tk_var)
        self.champ.pack(side='right')

    def changer_valeur_param(self, var, index, mode):
        """Met à jour la liste des valeurs de paramètre lors d'une modification de champ."""
        try:
            self.parametres_valeurs[self.index] = float(self.tk_var.get())
        except ValueError:
            if self.tk_var.get() != "":
                self.tk_var.set(self.parametres_valeurs[self.index])

    def set_random(self):
        """Défini une valeur aléatoire dans le champ. Bornée entre le min et le max du paramètre."""
        self.tk_var.set(random.randint(int(self.infos["MIN"]),int(self.infos["MAX"]))) # type: ignore

class ChampStr(Champ):
    def __init__(self, container:ttk.Frame, index:int, label:str, param_val:list, infos):
        """Initialisation du champ string"""
        super().__init__(container, index, label, param_val, infos)
              
        self.tk_var = tk.StringVar(self, str(self.infos["MOY"]))
        self.tk_var.trace_add('write', self.changer_valeur_param)

        # Champ d'entrée du paramètre
        self.champ.destroy()
        self.champ = ttk.Entry(self, width=30, textvariable=self.tk_var)
        self.champ.pack(side='left')

class ChampBool(Champ):
    def __init__(self, container:ttk.Frame, index:int, label:str, param_val:list, infos):
        """Initialisation du champ de bool"""
        super().__init__(container, index, label, param_val, infos)
              
        self.tk_var = tk.BooleanVar(self, bool(int(self.infos["MOY"])))
        self.tk_var.trace_add('write', self.changer_valeur_param)

        # Champ d'entrée du paramètre
        self.champ.destroy()
        self.champ = ttk.Checkbutton(self, width=30, variable=self.tk_var)
        self.champ.pack(side='left')

    def set_random(self):
        """Défini l'état du checkbox aléatoirement. (0 ou 1)"""
        self.tk_var.set(random.randint(0, 1)) # type: ignore
