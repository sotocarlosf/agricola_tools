import sys

# Leer los nombres de los archivos desde los argumentos
input_file = sys.argv[1] if len(sys.argv) > 1 else 'T3961965.TXT'
output_file = sys.argv[2] if len(sys.argv) > 2 else 'resumen_trabajadores.txt'

# Palabras clave para buscar los datos
employee_key = "NOMBRE DEL TRABAJADOR"
payment_key = "TOTAL :"
day_key = "DIA"
season_key = "TEMPORADA:"
separator_line = "RECIBI A MI ENTERA SATISFACCCION"
clave_key = "CLAVE"

# Lista para almacenar la información procesada
records = []

with open(input_file, 'r', encoding='latin-1') as infile:
    lines = infile.readlines()

    current_record = {}
    in_payment_section = False  # Para identificar el bloque de días y pagos
    days_of_week = ["LUNE", "MARTE", "MIER", "JUEV", "VIER", "SABA", "DOMI"]  # Días de la semana
    current_record["Pagos"] = {day: "0.00" for day in days_of_week}  # Inicializar días con "0.00"

    for i, line in enumerate(lines):
        line = line.strip()
        
        # Buscar la temporada correctamente
        if season_key in line:
            if 'Temporada' not in current_record:  # Solo guardar la temporada una vez
                current_record['Temporada'] = line.split(":")[1].strip().split()[0]
        
        # Buscar el nombre del trabajador en la línea siguiente a "NOMBRE DEL TRABAJADOR"
        if employee_key in line:
            name_line = lines[i + 1].strip()  # Leer la línea siguiente
            if name_line:
                current_record['Nombre'] = name_line
        
        # Buscar la clave del trabajador en la línea dos líneas debajo de "CLAVE"
        if clave_key in line:
            clave_line = lines[i + 2].strip()  # Leer dos líneas debajo
            if clave_line:
                # Verificar si la línea contiene un valor numérico válido
                clave_parts = clave_line.split()
                for part in clave_parts:
                    if part.isdigit():  # Tomar la primera parte numérica encontrada
                        current_record['Clave'] = part
                        break
        
        # Entrar en la sección de días y pagos
        if day_key in line and not in_payment_section:
            in_payment_section = True
        
        # Procesar días y pagos si estamos en la sección
        if in_payment_section and line and ":" not in line and payment_key not in line:
            parts = line.split()
            days_found = [day for day in days_of_week if day in parts]  # Buscar días en la línea
            if days_found:
                payment = parts[-1]  # Asumir que el último valor es el pago
                for day in days_found:
                    current_record["Pagos"][day] = payment  # Asignar el pago a cada día encontrado
        
        # Salir de la sección de pagos al llegar a otra clave
        if payment_key in line:
            in_payment_section = False
            total_payment = line.split(payment_key)[-1].strip()
            current_record['Total'] = total_payment
        
        # Buscar el fin del bloque actual y guardar los datos
        if separator_line in line:
            if current_record:
                records.append(current_record)
                current_record = {}
                current_record["Pagos"] = {day: "0.00" for day in days_of_week}  # Reiniciar días
                in_payment_section = False

# Escribir la información en el archivo de salida
with open(output_file, 'w', encoding='utf-8') as outfile:
    for record in records:
        # Encabezado de cada trabajador con AGRICOLA LAURA ELENA SA DE CV
        outfile.write("-" * 40 + "\n")
        outfile.write("AGRICOLA LAURA ELENA SA DE CV\n")
        outfile.write(f"Nombre: {record.get('Nombre', 'N/A')}\n")
        outfile.write(f"Clave: {record.get('Clave', 'N/A')}\n")
        outfile.write(f"Temporada: {record.get('Temporada', 'N/A')}\n\n")
        
        # Tabla horizontal de pagos por día
        outfile.write("LUNE    MARTE     MIER    JUEV    VIER    SABA    DOMI   \n")
        outfile.write(" ".join([f"{record['Pagos'].get(day, '0.00'):<7}" for day in days_of_week]) + "\n\n")
        
        # Total semanal
        outfile.write(f"Total Semanal: {record.get('Total', 'N/A')}\n")
        outfile.write("-" * 40 + "\n")

print(f"Información procesada y almacenada en {output_file}")
