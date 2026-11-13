import tkinter as tk
from Champ import Champ

class Interface(tk.Tk):
    def __init__(self):
        super().__init__()
        self.parametres = ["Elims blue", "Deaths blue", "Assists blue", "Assists red", "kjahge"]
        self.parametres_valeurs = [0, 0, 0, 0, 0]

        self.title('Prédiction League of Legends')

        top_bar = self.creer_top_bar(self)
        top_bar.pack()

        colonne_entree_droite = self.creer_colonne(self, self.parametres, True)
        colonne_entree_droite.pack(side='left', anchor='n', expand=True, fill="y")

        colonne_entree_droite = self.creer_colonne(self, self.parametres, False)
        colonne_entree_droite.pack(side='left', anchor='n', expand=True, fill="y")

    def creer_top_bar(self, container):
        frame = tk.Frame(container)
        return frame

    def creer_colonne(self, container, parametres:list, est_colonne_gauche:bool):
        frame = tk.Frame(container)

        if est_colonne_gauche:
            for i in range(0, round(len(parametres)/2) + 1):
                champ = Champ(frame, i, self.parametres[i], self.parametres_valeurs)
                champ.pack(side="top", anchor="e")
        else:
            for i in range(round(len(parametres)/2) + 1, len(parametres)):
                champ = Champ(frame, i, self.parametres[i], self.parametres_valeurs)
                champ.pack(side="top", anchor="e")  

        return frame