import tkinter as tk
from tkinter import ttk
from Champ import Champ

class Interface:
    def __init__(self):
        self.parametres = ["Elims blue", "Deaths blue", "Assists blue", "Assists red", "kjahge"]
        self.parametres_valeurs = [0, 0, 0, 0, 0]



    def creer_top_bar(self, container):
        frame = ttk.Frame(container)

        self.stringvar_resultat = tk.StringVar(value="??%")
        # Label du résultat
        tk.Label(frame, text="Pourcentage de victoire", font=("", 24)).pack(side='left')
        tk.Label(frame, textvariable=self.stringvar_resultat, font=("", 24)).pack(side='left')

        tk.Button(frame, text="Prédire", command=self.update_resultat).pack()

        return frame    


    def creer_colonne(self, container, parametres:list, est_colonne_gauche:bool):
        frame = ttk.Frame(container)

        if est_colonne_gauche:
            for i in range(0, round(len(parametres)/2) + 1):
                champ = Champ(frame, i, self.parametres[i], self.parametres_valeurs)
                champ.pack()
        else:
            for i in range(round(len(parametres)/2) + 1, len(parametres)):
                champ = Champ(frame, i, self.parametres[i], self.parametres_valeurs)
                champ.pack()  

        return frame


    def create_main_window(self):
        root = tk.Tk()
        root.title('Prédiction League of Legends')
        root.resizable(False, False)

        top_bar = self.creer_top_bar(root)
        top_bar.pack(side="top")

        colonne_entree_droite = self.creer_colonne(root, self.parametres, True)
        colonne_entree_droite.pack(side='left', anchor='n')

        colonne_entree_droite = self.creer_colonne(root, self.parametres, False)
        colonne_entree_droite.pack(side='left', anchor='n')

        root.mainloop()


    def update_resultat(self, valeur:float):
        if valeur <= 1:
            valeur *= 100
        self.stringvar_resultat.set(f"{valeur}%")