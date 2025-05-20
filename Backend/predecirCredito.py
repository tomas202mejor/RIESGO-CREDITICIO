import pandas as pd
import joblib

#Cargar el modelo
modelo = joblib.load("modelo_credito.pkl")

#Crear registro con los datos del usuario
nuevo_registro = {
    "ingresos": 2800000,
    "gastos": 1300000,
    "monto_credito": 8000000,
    "cuotas": 9
}

#DataFrame para evaluar registro
df_nuevo = pd.DataFrame([nuevo_registro])

#Variables derivadas
df_nuevo["capacidad_ahorro"] = df_nuevo["ingresos"] - df_nuevo["gastos"]
df_nuevo["cuota_aprox"] = df_nuevo["monto_credito"] / df_nuevo["cuotas"]
df_nuevo["cuota_sobre_ingresos"] = df_nuevo["cuota_aprox"] / df_nuevo["ingresos"]

#Seleccionar las columnas en el orden esperado
X_nuevo = df_nuevo[["ingresos", "gastos", "monto_credito", "cuotas", "capacidad_ahorro", "cuota_sobre_ingresos"]]

#Predecir con el modelo
prediccion = modelo.predict(X_nuevo)
probabilidades = modelo.predict_proba(X_nuevo)[0]

print(f"La rentabilidad cliente es: {prediccion[0]} (1=Rentable, 0=No rentable)")
print(f"Probabilidad de no rentable (0): {probabilidades[0]:.2f}")
print(f"Probabilidad de rentable (1): {probabilidades[1]:.2f}")
