# 🏋️‍♂️ Telegram Workout Logger

Un bot de Telegram desarrollado en Python que automatiza el registro de entrenamientos (gimnasio y calistenia) directamente en una base de datos de Google Sheets. 

El bot recibe un mensaje de texto multilínea con la rutina del día, procesa la información utilizando Expresiones Regulares (Regex) y envía los datos estructurados a la nube mediante la API de Google.

## ✨ Características

* **Procesamiento de Lenguaje Natural Básico:** Extrae el nombre del ejercicio, repeticiones, series y carga/asistencia desde texto plano.
* **Soporte Multilínea:** Capacidad de procesar una rutina completa en un solo mensaje.
* **Clasificación Dinámica:** Detecta automáticamente el tipo de entrenamiento (ej. "Gym Superior" o "Calistenia Piernas") leyendo la primera línea del mensaje.
* **Integración Cloud:** Conexión segura de servidor a servidor con Google Sheets mediante Cuentas de Servicio (Service Accounts).

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 3
* **APIs:** Telegram Bot API, Google Sheets API, Google Drive API
* **Librerías Principales:** * `python-telegram-bot` (Manejo asíncrono del bot)
  * `gspread` (Interacción con Google Sheets)
  * `python-dotenv` (Manejo de variables de entorno)
  * `re` (Expresiones regulares nativas)

## 🚀 Instalación y Configuración

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/NicolasAVM96/telegram-to-sheets-bot]
   cd telegram-workout-logger

2. **Ejecutar script:**
    En este caso se usa "uv", de Astral, por lo cual se recomienda tenerlo instalado.
    * **Inicializacion del proyecto:** 
    Inicializa el proyecto (Se debe tener el archivo pyproject.toml en la carpeta del proyecto), esto instalara automaticamente las dependencias y creara el .venv de manera automatica
    ```bash
    uv run bot_main.py

3. **APIs y TOKEN:**
    * **Google Sheets:** 
    Se debe crear un proyecto en el panel de agentes Google Cloud, habilitar la API de Google Sheets, crear y descargar el archivo "credentials.json". Este te entregara una direccion email, la cual debes compartirle tu xlm de google sheets.
    * **Bot de Telegram:** 
    Para poder obtener un token de Telegram, debes buscar a @BotFather en tus chats y agregar /newbot e indicarle el nombre de tu bot. Una vez completado este paso, se te entregara el TOKEN.

    