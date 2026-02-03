from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
import joblib

app = FastAPI()

# Configuración obligatoria para que el navegador permita la conexión
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # Permite peticiones desde cualquier origen (tu index.html)
    allow_credentials=True,
    allow_methods=["*"],      # Permite todos los métodos (incluyendo OPTIONS y POST)
    allow_headers=["*"],      # Permite todos los encabezados
)

modelo = joblib.load("modelo_fuga.pkl")

# Definir la estructura de datos que recibe el endpoint
class Cliente(BaseModel):
    GENERO: str
    RENTA: float
    EDAD: int
    NIV_EDUC: str
    E_CIVIL: str
    COD_OFI: int
    COD_COM: int
    CIUDAD: str
    D_Marzo: int
    D_Abril: int
    D_Mayo: int
    D_Junio: int
    D_Julio: int
    D_Agosto: int
    D_Septiembre: int
    M_MOROSO: int
    MONTO: float
    SEGURO: str

@app.post("/predict")
def predecir(cliente: Cliente):
    # Convertimos a DataFrame
    df = pd.DataFrame([cliente.dict()])

    # Codificamos las variables categoricas
    df = pd.get_dummies(df, columns=["GENERO", "NIV_EDUC", "E_CIVIL", "CIUDAD","SEGURO"])

    importances = modelo.feature_names_in_  # columnas que usó el modelo
    for col in importances:
        if col not in df.columns:
            df[col] = 0
    df = df[importances]

    # Predecir
    prediccion = modelo.predict(df)[0]
    prob = modelo.predict_proba(df)[0].tolist()

    return {
        "prediccion": int(prediccion),
        "probabilidades": prob
    }