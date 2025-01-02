@echo off

:: Llama a PowerShell para abrir el cuadro de diálogo gráfico y seleccionar un archivo
for /f "usebackq delims=" %%i in (`powershell -NoProfile -Command "Add-Type -AssemblyName System.Windows.Forms; $dialog = New-Object System.Windows.Forms.OpenFileDialog; $dialog.Filter = 'Archivos de Texto|*.txt'; if($dialog.ShowDialog() -eq [System.Windows.Forms.DialogResult]::OK){$dialog.FileName}"`) do set INPUT_FILE=%%i

:: Comprobar si se seleccionó un archivo
if "%INPUT_FILE%"=="" (
    echo No se seleccionó ningún archivo.
    pause
    exit /b
)

:: Crear el directorio para los archivos PDF un nivel arriba del directorio actual
set PDF_FOLDER=..\\archivos_pdf
if not exist "%PDF_FOLDER%" (
    mkdir "%PDF_FOLDER%"
)

:: Especificar los archivos de salida
set OUTPUT_FILE=resumen_trabajadores.txt
set PDF_FILE=%PDF_FOLDER%\etiquetas_nomina.pdf

:: Llamar al script de Python para procesar los datos
echo Procesando archivo con procesar_trabajadores.py...
python procesar_trabajadores.py "%INPUT_FILE%" "%OUTPUT_FILE%"
if %ERRORLEVEL% neq 0 (
    echo Ocurrió un error al ejecutar procesar_trabajadores.py
    pause
    exit /b
)

:: Llamar al script de Python para generar el etiquetado
echo Generando etiquetas con generar_etiquetado.py...
python generar_etiquetado.py "%OUTPUT_FILE%" "%PDF_FILE%"
if %ERRORLEVEL% neq 0 (
    echo Ocurrió un error al ejecutar generar_etiquetado.py
    pause
    exit /b
)

:: Confirmar finalización
echo Procesamiento completado. Archivo PDF generado: %PDF_FILE%
pause
