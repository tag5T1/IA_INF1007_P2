from sklearn import linear_model
from sklearn import metrics
from donnees import importer_donnees, split_data, create_donnees_data
import joblib
import json, os
import numpy as np
from exceptions import InfosInvalideError, ModeleInexistantError

class Modele:
    def __init__(self) -> None:
        """Initialisation du Modèle."""
        data = importer_donnees()
        self.X_train, self.X_test, self.y_train, self.y_test = split_data(data)

    def train_model(self) -> None:
        """Entrainement du modele."""
        log_reg = linear_model.LogisticRegression(max_iter=1000)
        log_reg.fit(self.X_train, self.y_train)

        joblib.dump(log_reg, open("modeles/log_reg_0.sav", "wb"))

        with open("modeles/log_reg_0_data.json", mode="w", encoding="utf-8") as f:
            json.dump(create_donnees_data(), f, indent=2)

    def test_model(self) -> float:
        """Test du modèle.\nRetourne la précision du modèle."""
        load_model:linear_model.LogisticRegression = joblib.load(open("modeles/log_reg_0.sav", 'rb'))

        y_pred = load_model.predict(self.X_test)

        return float(metrics.accuracy_score(self.y_test, y_pred))

    def compare_with_numpy(self) -> bool:
        """Comparaison de scikit avec numpy.\nRetourne un bool pour si les prédictions sont identiques ou non."""
        load_model: linear_model.LogisticRegression = joblib.load(open("modeles/log_reg_0.sav", 'rb'))

        X = np.asarray(self.X_test, dtype=np.float64)
        w = load_model.coef_.ravel()       # forme (n_features,) pour classification binaire
        b = float(load_model.intercept_[0])

        # Calcul vectoriel NumPy (score linéaire + sigmoïde)
        z = X @ w + b
        proba_pos_np = 1.0 / (1.0 + np.exp(-z))
        pred_np = (proba_pos_np >= 0.5).astype(int)

        # Résultats scikit-learn
        pred_sk = load_model.predict(self.X_test)

        identical_preds = np.array_equal(pred_np, pred_sk)

        return identical_preds

    @staticmethod
    def load_model(modele_name:str="log_reg_0.sav", modele_data_name:str="log_reg_0_data.json", donnees_modele_name:str="./donnees/high_diamond_ranked_10min.csv") -> tuple[linear_model.LogisticRegression, list[str], dict[str, dict[str, int]]]:
        """Charge le modèle et les données liées au modèle"""
        data = importer_donnees(donnees_modele_name)
        X_train, X_test, y_train, y_test = split_data(data)

        if os.path.exists(os.path.join(os.getcwd(), "modeles", modele_name)):
            load_model:linear_model.LogisticRegression = joblib.load(open(os.path.join(os.getcwd(), "modeles", modele_name), 'rb'))
        else:
            raise ModeleInexistantError()

        if os.path.exists(os.path.join(os.getcwd(), "modeles", modele_data_name)):
            with open(os.path.join(os.getcwd(), "modeles", modele_data_name), mode="r", encoding="utf-8") as f:
                infos = json.load(f)
        else:
            infos = {}

        try:
            infos["blueWardsPlaced"]
            infos["blueWardsPlaced"]["MIN"]
            infos["blueWardsPlaced"]["MAX"]
            infos["blueWardsPlaced"]["MOY"]
        except KeyError:
            raise InfosInvalideError("Les informations n'ont pas le bon formattage ou informations")

        return load_model, list(X_train.columns), infos

    def __str__(self) -> str:
        return f"Modele de données"

if __name__ == "__main__":
    modele = Modele()
    modele.train_model()
    print("Précision:", modele.test_model())

    print(modele.compare_with_numpy())

    modele.load_model()