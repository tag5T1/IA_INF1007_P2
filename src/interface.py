import tkinter as tk
from Champ import ChampStr, ChampBool
from donnees import PARAMETRES_NOMS, PARAMETRES_TYPES, set_historique, get_historique
from sklearn import linear_model
import pandas as pd
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Interface(tk.Tk):
    def __init__(self, params:list[str], model:linear_model.LogisticRegression, infos:dict[str, dict[str, int]]) -> None:
        """Initialisation de l'interface"""
        self.parametres: list[str] = params
        self.parametres_valeurs = [0.0] * len(params)
        self.infos = infos

        self.model:linear_model.LogisticRegression = model

        super().__init__()

        self.title('Prédiction League of Legends')

        top_bar = self.creer_top_bar(self)
        top_bar.pack(side="top")

        self.colonnes_frame = tk.Frame(self)
        self.colonnes_frame.pack(fill="both")

        self.colonne_entree_gauche = self.creer_colonne(self.colonnes_frame, self.parametres, True)
        self.colonne_entree_gauche.pack(side='left', anchor='n', expand=True)
        self.colonne_entree_droite = self.creer_colonne(self.colonnes_frame, self.parametres, False)
        self.colonne_entree_droite.pack(side='left', anchor='n', expand=True)

        self.bottom_frame = tk.Frame(self)
        self.bottom_frame.pack(expand=True, fill="both")

        self.graph_frame = tk.Frame(self.bottom_frame, height=100)
        self.graph_frame.pack(side="right", expand=False, fill="both")

        self.create_graph()

        self.hist_frame = tk.Frame(self.bottom_frame, height=100)
        self.hist_frame.pack(side="right", expand=True, fill="both")

        self.hist = []
        self.liste = TooltipListbox(self.hist_frame, self.hist)
        self.liste.pack(expand=True, fill="both")

        self.update_resultat(True)

    def create_graph(self) -> None:
        """Création du garphique intégré"""
        # the figure that will contain the plot
        self.fig = Figure(figsize = (10, 4), dpi = 100)

        self.plot = self.fig.add_subplot(111)

        self.canvas_graph = FigureCanvasTkAgg(self.fig, master = self.graph_frame)  
        self.canvas_graph.get_tk_widget().pack(expand=True, fill="both")

    def tracer_graph(self) -> None:
        self.plot.clear()
        # trace le graphique
        positions_x = list(range(len(self.parametres)))
        self.plot.plot(positions_x, [d["MIN"] for d in self.infos.values()], linestyle="", marker="o", markersize=6, color="red", label="Min")
        self.plot.plot(positions_x, [d["MAX"] for d in self.infos.values()], linestyle="", marker="o", markersize=6, color="blue", label="Max")
        self.plot.plot(positions_x, self.parametres_valeurs, linestyle="", marker="o", markersize=6, color="green", label="Sélectionné")

        self.plot.set_xticks(positions_x)
        self.plot.set_xticklabels(
            [PARAMETRES_NOMS.get(self.parametres[i], self.parametres[i]) for i in range(len(PARAMETRES_NOMS))],
            rotation=36, ha="right", rotation_mode="anchor")

        self.plot.legend()

        self.fig.subplots_adjust(bottom=0.42)
        self.canvas_graph.draw_idle()

    def creer_top_bar(self, container) -> tk.Frame:
        """Création de la barre d'affichage du résultat."""
        frame = tk.Frame(container)

        # Label du résultat
        self.stringvar_resultat = tk.StringVar(value="??%")
        tk.Label(frame, text="Pourcentage de victoire des bleu:", font=("", 24)).pack(side='left')
        tk.Label(frame, textvariable=self.stringvar_resultat, font=("", 24)).pack(side='left')

        tk.Button(frame, text="Prédire", command=self.update_resultat).pack(side='left')
        tk.Button(frame, text="Aléatoire", command=self.set_random).pack(side='left')

        return frame    

    def creer_colonne(self, container, parametres:list[str], est_colonne_gauche:bool) -> tk.Frame:
        """Création d'une colonne de paramètres"""
        frame = tk.Frame(container)
        if est_colonne_gauche:
            for i in range(0, round(len(parametres)/2) + 1):
                if PARAMETRES_TYPES.get(self.parametres[i], "STR") == "STR":
                    champ = ChampStr(frame, i, PARAMETRES_NOMS.get(self.parametres[i], self.parametres[i]), self.parametres_valeurs, self.infos.get(self.parametres[i], {"MIN": 0, "MAX": 0, "MOY": 0}))
                else:
                    champ = ChampBool(frame, i, PARAMETRES_NOMS.get(self.parametres[i], self.parametres[i]), self.parametres_valeurs, self.infos.get(self.parametres[i], {"MIN": 0, "MAX": 0, "MOY": 0}))
                champ.pack(anchor="e")
        else:
            for i in range(round(len(parametres)/2) + 1, len(parametres)):
                if PARAMETRES_TYPES.get(self.parametres[i], "STR") == "STR":
                    champ = ChampStr(frame, i, PARAMETRES_NOMS.get(self.parametres[i], self.parametres[i]), self.parametres_valeurs, self.infos.get(self.parametres[i], {"MIN": 0, "MAX": 0, "MOY": 0}))
                else:
                    champ = ChampBool(frame, i, PARAMETRES_NOMS.get(self.parametres[i], self.parametres[i]), self.parametres_valeurs, self.infos.get(self.parametres[i], {"MIN": 0, "MAX": 0, "MOY": 0}))
                champ.pack(anchor="e")

        return frame

    def update_resultat(self, start:bool=False) -> None:
        """Mise à jour de la prédiction."""
        valeurs_pred = pd.DataFrame([self.parametres_valeurs], columns=self.parametres)
        prediction = self.model.predict_proba(valeurs_pred)

        prediction = str(round(prediction[0][1] * 100, 3)) + "%"

        self.stringvar_resultat.set(prediction)

        pred_data = { "res": prediction,
            "data": {self.parametres[i]: self.parametres_valeurs[i] for i in range(len(self.parametres))}
            }

        self.hist.clear()
        self.hist.extend(get_historique())

        if not start:
            self.hist.append(pred_data)

            set_historique(self.hist)

        self.liste.update_list()

        self.tracer_graph()

    def set_random(self) -> None:
        """Affiche une valeur aléatoire dans chaque paramètre."""
        for w in self.colonne_entree_gauche.winfo_children():
            w.set_random() # type: ignore

        for w in self.colonne_entree_droite.winfo_children():
            w.set_random() # type: ignore

        self.tracer_graph()

class TooltipListbox(tk.Frame):
    def __init__(self, master, hist:list[dict[str, str | dict[str, float]]]) -> None:
        """Initialise la liste de l'historique."""
        super().__init__(master=master)
        self.hist = hist
        self.current_index = None
        self.tooltip_window = None

        self.listbox = tk.Listbox(self, font=("Arial", 12), width=35, height=6)
        self.listbox.pack(expand=True, fill="both", padx=20, pady=20)

        for item in self.hist:
            self.listbox.insert(tk.END, item["res"]) # type: ignore

            self.listbox.delete(0)

        self.listbox.bind("<Motion>", self._on_motion)
        self.listbox.bind("<Leave>", self._hide_tooltip)

    def update_list(self) -> None:
        """Met à jour la liste d'historique"""
        for i in range(len(self.hist)):
            self.listbox.delete(0)

        for item in self.hist[::-1]:
            self.listbox.insert(tk.END, item["res"]) # type: ignore

    def _on_motion(self, event) -> None:
        """Détecte un mouvement de la souris et déplace la boite en fonction."""
        # Trouve l'index de l'élément sous le curseur
        index = self.listbox.nearest(event.y)
        bbox = self.listbox.bbox(index)

        # Vérifie que la souris est bien au-dessus d'un élément réel (et pas dans le vide)
        if bbox is None or event.y < bbox[1] or event.y > bbox[1] + bbox[3]:
            self._hide_tooltip()
            self.current_index = None
            return

        if index != self.current_index:
            self.current_index = index
            item_text = self.listbox.get(index)

            tip_text = "".join([f"{list(self.hist[index]["data"].keys())[i]}: {list(self.hist[index]["data"].values())[i]}" + ("\n" if i % 5 == 0 else "") for i in range(len(self.hist[index]["data"]))])
            self._show_tooltip(tip_text, event.x_root + 15, event.y_root + 10)
        elif self.tooltip_window:
            self.tooltip_window.geometry(f"+{event.x_root + 15}+{event.y_root + 10}")

    def _show_tooltip(self, text, x, y) -> None:
        """Affiche la boite contenant la précision des paramètres."""
        self._hide_tooltip()
        if not text:
            return

        win = tk.Toplevel(self)
        win.wm_overrideredirect(True)  # Supprime la barre de titre et les bordures
        win.wm_geometry(f"+{x}+{y}")

        label = tk.Label(
            win,
            text=text,
            background="#ffffe0",
            foreground="#111111",
            relief="solid",
            borderwidth=1,
            font=("Arial", 10),
            padx=8,
            pady=4,
        )
        label.pack()
        self.tooltip_window = win

    def _hide_tooltip(self, event=None) -> None:
        """Cache la boite d'informations."""
        if self.tooltip_window:
            self.tooltip_window.destroy()
            self.tooltip_window = None
        self.current_index = None
