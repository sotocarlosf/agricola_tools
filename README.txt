# Crear un archivo README.md que explique cómo instalar las dependencias
readme_content = """
# Generador de Etiquetas de Trabajadores

Este proyecto genera etiquetas en formato PDF para trabajadores utilizando información de un archivo de entrada y un logo proporcionado.

## Requisitos Previos

Asegúrate de tener instaladas las siguientes herramientas:

1. **Python 3.6 o superior**: Puedes descargar Python desde [python.org](https://www.python.org/).
2. **Pip**: El gestor de paquetes para Python, incluido en la mayoría de las instalaciones de Python.

## Instalación de Dependencias

1. **Clona el repositorio o copia los archivos del proyecto**.
2. **Crea un archivo `requirements.txt`** con el siguiente contenido:
    ```
    reportlab
    ```
3. Abre una terminal o línea de comandos y navega al directorio del proyecto.

4. Ejecuta el siguiente comando para instalar las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

## Uso del Proyecto

1. Asegúrate de tener un archivo de entrada llamado `resumen_trabajadores.txt` con el formato adecuado.
2. Coloca un archivo de imagen llamado `logo-Placeholder.jpg` en el mismo directorio que el script.
3. Ejecuta el script principal con:
    ```bash
    python generar_etiquetas_trabajadores.py
    ```
4. El archivo PDF generado estará disponible como `etiquetas_trabajadores.pdf`.

## Personalización

- **Dimensiones de las etiquetas**: Puedes modificar las variables `LABEL_WIDTH` y `LABEL_HEIGHT` en el script.
- **Ruta del logo**: Cambia el valor de `LOGO_PATH` para apuntar a tu archivo de logo.

## Problemas Comunes

1. **Error de importación de `reportlab`**: Asegúrate de haber ejecutado `pip install -r requirements.txt`.
2. **Archivo de entrada inválido**: Verifica que el archivo de entrada sigue el formato esperado.

## Licencia

Este proyecto es de uso libre y puede ser adaptado según las necesidades del usuario.
"""

file_path_readme = "/mnt/data/README.md"
with open(file_path_readme, "w") as file:
    file.write(readme_content)

file_path_readme
