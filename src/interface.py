import tkinter as tk
from tkinter import ttk
from Champ import Champ
from donnees import PARAMETRES_NOMS
from sklearn import linear_model
import pandas as pd

class Interface(tk.Tk):
    def __init__(self, params, model, infos):
        self.parametres: list[str] = params
        self.parametres_valeurs = [0.0] * len(params)
        self.infos = infos

        self.model:linear_model.LogisticRegression = model

        super().__init__()

        self.title('Prédiction League of Legends')

        top_bar = self.creer_top_bar(self)
        top_bar.pack(side="top")

        self.colonne_entree_gauche = self.creer_colonne(self, self.parametres, True)
        self.colonne_entree_gauche.pack(side='left', anchor='n', expand=True)

        self.colonne_entree_droite = self.creer_colonne(self, self.parametres, False)
        self.colonne_entree_droite.pack(side='left', anchor='n', expand=True)

        self.update_resultat()

    def creer_top_bar(self, container):
        frame = ttk.Frame(container)

        self.stringvar_resultat = tk.StringVar(value="??%")
        # Label du résultat
        tk.Label(frame, text="Pourcentage de victoire des bleu:", font=("", 24)).pack(side='left')
        tk.Label(frame, textvariable=self.stringvar_resultat, font=("", 24)).pack(side='left')

        tk.Button(frame, text="Prédire", command=self.update_resultat).pack(side='left')
        tk.Button(frame, text="Aléatoire", command=self.set_random).pack(side='left')

        return frame    

    def creer_colonne(self, container, parametres:list, est_colonne_gauche:bool):
        frame = ttk.Frame(container)
        if est_colonne_gauche:
            for i in range(0, round(len(parametres)/2) + 1):
                champ = Champ(frame, i, PARAMETRES_NOMS.get(self.parametres[i], self.parametres[i]), self.parametres_valeurs, self.infos.get(self.parametres[i], {"MIN": 0, "MAX": 0, "MOY": 0}))
                champ.pack(anchor="e")
        else:
            for i in range(round(len(parametres)/2) + 1, len(parametres)):
                champ = Champ(frame, i, PARAMETRES_NOMS.get(self.parametres[i], self.parametres[i]), self.parametres_valeurs, self.infos.get(self.parametres[i], {"MIN": 0, "MAX": 0, "MOY": 0}))
                champ.pack(anchor="e")  

        return frame

    def update_resultat(self):
        valeurs_pred = pd.DataFrame([self.parametres_valeurs], columns=self.parametres)
        prediction = self.model.predict_proba(valeurs_pred)

        self.stringvar_resultat.set(str(round(prediction[0][1] * 100, 3)) + "%")

    def set_random(self):
        for w in self.colonne_entree_gauche.winfo_children():
            w.set_random() # type: ignore

        for w in self.colonne_entree_droite.winfo_children():
            w.set_random() # type: ignore
