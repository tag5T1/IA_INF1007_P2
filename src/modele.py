from sklearn import linear_model
from sklearn import metrics
from donnees import importer_donnees, split_data, create_donnees_data
import joblib
import json, os
import numpy as np

class Modele:
    def __init__(self) -> None:
        data = importer_donnees()
        self.X_train, self.X_test, self.y_train, self.y_test = split_data(data)

    def train_model(self):
        log_reg = linear_model.LogisticRegression(max_iter=1000)
        log_reg.fit(self.X_train, self.y_train)

        joblib.dump(log_reg, open("modeles/log_reg_0.sav", "wb"))

        with open("modeles/log_reg_0_data.json", mode="w", encoding="utf-8") as f:
            json.dump(create_donnees_data(), f, indent=2)

    def test_model(self):
        load_model:linear_model.LogisticRegression = joblib.load(open("modeles/log_reg_0.sav", 'rb'))

        y_pred = load_model.predict(self.X_test)

        print("Logistic Regression model accuracy:", metrics.accuracy_score(self.y_test, y_pred))
        return metrics.accuracy_score(self.y_test, y_pred)

    def compare_with_numpy(self):
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
    def load_model():
        data = importer_donnees()
        X_train, X_test, y_train, y_test = split_data(data)

        load_model:linear_model.LogisticRegression = joblib.load(open("modeles/log_reg_0.sav", 'rb'))
        if os.path.exists(os.path.join(os.getcwd(), "modeles", "log_reg_0_data.json")):
            with open(os.path.join(os.getcwd(), "modeles", "log_reg_0_data.json"), mode="r", encoding="utf-8") as f:
                infos = json.load(f)
        else:
            infos = {}

        return load_model, X_train.columns, infos

    def __str__(self) -> str:
        return f"Modele de données"

if __name__ == "__main__":
    modele = Modele()
    modele.train_model()
    modele.test_model()

    print(modele.compare_with_numpy())