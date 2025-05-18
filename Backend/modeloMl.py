import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Datos entrenamiento
df = pd.read_csv("datos_creditos.csv")

# Variables derivadas
df["capacidad_ahorro"] = df["ingresos"] - df["gastos"]
df["cuota_aprox"] = df["monto_credito"] / df["cuotas"]
df["cuota_sobre_ingresos"] = df["cuota_aprox"] / df["ingresos"]

# Entrenamiento
X = df[["ingresos", "gastos", "monto_credito", "cuotas", "capacidad_ahorro", "cuota_sobre_ingresos"]]
y = df["rentable"]  # campo de interes

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
modelo = RandomForestClassifier()
modelo.fit(X_train, y_train)
joblib.dump(modelo, "modelo_credito.pkl")


# Evaluación
y_pred = modelo.predict(X_test)
print(classification_report(y_test, y_pred))

