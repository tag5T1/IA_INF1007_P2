from sklearn import linear_model
from sklearn import metrics
from donnees import importer_donnees, split_data
import joblib

data = importer_donnees()
X_train, X_test, y_train, y_test = split_data(data)

print("X_train Shape:",  X_train.shape)
print("X_test Shape:", X_test.shape)
print("Y_train Shape:", y_train.shape)
print("Y_test Shape:", y_test.shape)

log_reg = linear_model.LogisticRegression(max_iter=500)
log_reg.fit(X_train, y_train)

joblib.dump(log_reg, open("modeles/log_reg_0.sav", "wb"))

load_model = joblib.load(open("modeles/log_reg_0.sav", 'rb'))

y_pred = load_model.predict(X_test)

print("Logistic Regression model accuracy:", metrics.accuracy_score(y_test, y_pred))