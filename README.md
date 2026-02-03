📊 Analizador Predictivo de Fuga de Clientes (Churn Analysis)
Este proyecto es un MVP (Producto Mínimo Viable) que utiliza Inteligencia Artificial para predecir la probabilidad de que un cliente abandone un servicio financiero. Integra un modelo de Machine Learning entrenado en Python, un backend robusto con FastAPI y una interfaz moderna desarrollada con Tailwind CSS.

🚀 Características
Predicción en Tiempo Real: Interfaz web para introducir datos del cliente y obtener resultados instantáneos.

Modelo de Machine Learning: Clasificador basado en Random Forest entrenado con datos reales de comportamiento bancario.

Análisis de Series Temporales: Evaluación de la evolución de deuda de los clientes de marzo a septiembre.

Arquitectura Desacoplada: Backend (API) y Frontend (HTML/JS) separados para mayor escalabilidad.

🛠️ Stack Tecnológico

Lenguaje: Python 3.x 


IA & Data Science: Pandas, Scikit-learn, Joblib 


Backend: FastAPI, Pydantic, Uvicorn 


Frontend: HTML5, JavaScript, Tailwind CSS 


Base de Datos: PostgreSQL / CSV 

📂 Estructura del Proyecto
Plaintext
analizador_bajas/
├── data/
│   └── BASEFUGA_GENERAL.csv   # Dataset de entrenamiento (Kaggle)
├── src/
│   ├── main.ipynb             # Análisis exploratorio y entrenamiento
├── index.html                 # Interfaz de usuario (Frontend)
├── api.py                 # Servidor FastAPI
├── requirements.txt           # Dependencias del proyecto
├── modelo_fuga.pkl        # Modelo entrenado exportado
└── README.md                  # Documentación
⚙️ Instalación y Uso
Clonar el repositorio:

Bash
git clone https://github.com/tu-usuario/analizador_bajas.git
cd analizador-bajas
Configurar el entorno virtual:

Bash
python -m venv .env
# Activar en Windows
.env\Scripts\activate
Instalar dependencias:

Bash
pip install -r requirements.txt
Ejecutar la API:

Bash
uvicorn src.api:app --reload
Abrir la Interfaz: Simplemente abre el archivo index.html en tu navegador favorito.

📈 Metodología de IA
El modelo analiza 20 variables críticas, incluyendo:


Factores Demográficos: Edad, Género, Ciudad, Nivel Educativo.

Comportamiento Financiero: Renta, deudas mensuales (Marzo-Septiembre) y meses en morosidad.

Preprocesamiento: Limpieza de nulos y One-Hot Encoding para variables categóricas.

👩‍💻 Sobre la Autora

Olatz Larrañaga - Desarrolladora de Aplicaciones Web con formación en Inteligencia Artificial y Data Science. Perfil proactivo orientado a la calidad del código y la resolución de problemas analíticos.