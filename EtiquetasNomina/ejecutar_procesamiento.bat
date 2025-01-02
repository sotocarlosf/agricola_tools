@echo off
:: Llama a PowerShell para abrir el cuadro de diálogo gráfico y seleccionar un archivo
for /f "usebackq delims=" %%i in (`powershell -NoProfile -Command "Add-Type -AssemblyName System.Windows.Forms; $dialog = New-Object System.Windows.Forms.OpenFileDialog; $dialog.Filter = 'Archivos de Texto|*.txt'; if($dialog.ShowDialog() -eq [System.Windows.Forms.DialogResult]::OK){$dialog.FileName}"`) do set INPUT_FILE=%%i

:: Comprobar si se seleccionó un archivo
if "%INPUT_FILE%"=="" (
    echo No se seleccionó ningún archivo.
    pause
    exit /b
)

:: Especificar el archivo de salida
set OUTPUT_FILE=resumen_trabajadores.txt

:: Llamar al script de Python con los archivos seleccionados
python procesar_trabajadores.py "%INPUT_FILE%" "%OUTPUT_FILE%"

:: Pausar para ver los resultados
pause
