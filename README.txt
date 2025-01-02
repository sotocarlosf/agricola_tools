# Actualizar el contenido del README para explicar cómo instalar las dependencias
readme_updated_content = """
# Generador de Etiquetas de Trabajadores

Este proyecto genera etiquetas en formato PDF para trabajadores utilizando información de un archivo de entrada y un logo proporcionado.

## Requisitos Previos

Asegúrate de tener instaladas las siguientes herramientas:

1. **Python 3.6 o superior**: Puedes descargar Python desde [python.org](https://www.python.org/).
2. **Pip**: El gestor de paquetes para Python, incluido en la mayoría de las instalaciones de Python.

## Instalación de Dependencias

1. **Clona el repositorio o copia los archivos del proyecto**.
2. Verifica que existe un archivo `requirements.txt` con el siguiente contenido:
    ```
    reportlab
    ```
3. Abre una terminal o línea de comandos y navega al directorio del proyecto.

4. Ejecuta el siguiente comando para instalar las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

### Instalación Manual (Opcional)
Si prefieres instalar las dependencias de forma manual, ejecuta:
```bash
pip install reportlab
