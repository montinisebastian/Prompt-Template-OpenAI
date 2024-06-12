
# Prompt-Template-OpenAI

Este proyecto utiliza la API de OpenAI para generar respuestas automáticas a prompts de texto. El script está diseñado para interactuar con el modelo de lenguaje GPT-3.5 Turbo de OpenAI, proporcionando una interfaz sencilla para enviar preguntas y recibir respuestas.

## Descripción del Código

El archivo `main.py` realiza las siguientes funciones:

- **Carga de la configuración del entorno**: Utiliza `dotenv` para cargar las variables de entorno necesarias para la configuración de la API.
- **Configuración de logging**: Establece el nivel de logging y el formato para registrar eventos importantes y errores.
- **Inicialización del cliente OpenAI**: Crea una instancia del cliente OpenAI utilizando la clave de API cargada desde las variables de entorno.
- **Función `chat_with_openai`**: Esta función toma un prompt de usuario como entrada y utiliza la API de OpenAI para obtener y registrar una respuesta. Maneja excepciones para capturar y registrar errores durante la solicitud.

## Configuración del Entorno

Para ejecutar este proyecto, necesitas realizar los siguientes pasos:

1. **Clonar el Repositorio**:
   ```bash
   git clone https://github.com/montinisebastian/Prompt-Template.git
   cd Prompt-Template
   ```

2. **Configurar Variables de Entorno**:
   - Crea un archivo `.env` en el directorio raíz del proyecto.
   - Añade la siguiente línea al archivo, sustituyendo `tu_clave_de_api` por tu clave de API de OpenAI:
     ```
     OPENAI_API_KEY=tu_clave_de_api
     ```

3. **Instalar Dependencias**:
   Asegúrate de tener Python instalado y luego ejecuta el siguiente comando en la terminal para instalar las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```

## Ejecución del Script

Para ejecutar el script, simplemente usa el siguiente comando en la terminal:

```bash
python main.py
```

El script pedirá un prompt de usuario y luego mostrará la respuesta generada por el modelo GPT-3.5 Turbo de OpenAI en la consola.

## Contribuciones

Las contribuciones a este proyecto son bienvenidas. Si deseas mejorar el código o añadir nuevas funcionalidades, considera hacer un fork del repositorio y enviar un pull request con tus cambios.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT.
