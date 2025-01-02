import os

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm

# Configuración de variables
LABEL_WIDTH = 106 * mm
LABEL_HEIGHT = 46 * mm
PAGE_WIDTH, PAGE_HEIGHT = letter
MARGIN_X = 1 * mm  # Margen desde la izquierda
MARGIN_Y = 1 * mm  # Margen desde arriba
FONT_SIZE = 10  # Tamaño de la letra, ajustable
LINE_SPACING = 5 * mm  # Espaciado entre líneas, ajustable
CAPTION_FONT_SIZE = 12  # Tamaño del caption
LOGO_PATH = "logo-Placeholder.jpg"  # Ruta del logo
LOGO_WIDTH = 40 * mm  # Ancho del logo
LOGO_HEIGHT = 40 * mm  # Alto del logo

def parse_input_file(input_file):
    """
    Procesa el archivo de entrada para extraer la información de los trabajadores.
    """
    with open(input_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    workers = []
    worker = {}

    for i, line in enumerate(lines):
        line = line.strip()
        if line.startswith("Nombre:"):
            worker["Nombre"] = line.split(":")[1].strip()
        elif line.startswith("Clave:"):
            worker["Clave"] = line.split(":")[1].strip()
        elif line.startswith("Temporada:"):
            worker["Temporada"] = line.split(":")[1].strip()
        elif line.startswith("Total Semanal:"):
            worker["Total Semanal"] = line.split(":")[1].strip()
        elif line.startswith("LUN"):
            worker["Dias"] = line  # Encabezados de días
            worker["Pagos"] = lines[i + 1].strip() if i + 1 < len(lines) else ""
        elif line.startswith("-" * 40):  # Indicador de separación
            if worker:
                workers.append(worker)
                worker = {}

    # Agregar el último trabajador si está incompleto
    if worker:
        workers.append(worker)

    return workers

def generate_pdf(workers, output_file):
    """
    Genera un PDF con etiquetas de trabajadores.
    """
    c = canvas.Canvas(output_file, pagesize=letter)

    labels_per_row = int((PAGE_WIDTH - 2 * MARGIN_X) // LABEL_WIDTH)
    labels_per_column = int((PAGE_HEIGHT - 2 * MARGIN_Y) // LABEL_HEIGHT)
    labels_per_page = labels_per_row * labels_per_column

    for i, worker in enumerate(workers):
        # Calcular la posición en la página actual
        index_on_page = i % labels_per_page
        row = index_on_page // labels_per_row
        col = index_on_page % labels_per_row

        # Si es la primera etiqueta de una nueva página, realiza un salto de página
        if index_on_page == 0 and i > 0:
            c.showPage()

        x = MARGIN_X + col * LABEL_WIDTH
        y = PAGE_HEIGHT - MARGIN_Y - (row + 1) * LABEL_HEIGHT

        # Dibujar el borde de la etiqueta
        c.rect(x, y, LABEL_WIDTH, LABEL_HEIGHT, stroke=1, fill=0)

        # Dibujar el logo en la esquina inferior derecha de la etiqueta
        logo_x = x + LABEL_WIDTH - LOGO_WIDTH - 5 * mm
        logo_y = y + 5 * mm
        c.drawImage(LOGO_PATH, logo_x, logo_y, width=LOGO_WIDTH, height=LOGO_HEIGHT)

        # Dibujar el caption en el centro superior de la etiqueta
        c.setFont("Helvetica-Bold", CAPTION_FONT_SIZE)
        caption_x = x + LABEL_WIDTH / 2
        caption_y = y + LABEL_HEIGHT - 8 * mm
        c.drawCentredString(caption_x, caption_y, "AGRICOLA LAURA ELENA SA DE CV")

        # Dibujar el contenido de la etiqueta
        c.setFont("Helvetica", FONT_SIZE)
        c.drawString(x + 5 * mm, caption_y - LINE_SPACING, f"Nombre: {worker.get('Nombre', 'N/A')}")
        c.drawString(x + 5 * mm, caption_y - 2 * LINE_SPACING, f"Clave: {worker.get('Clave', 'N/A')}")
        c.drawString(x + 5 * mm, caption_y - 3 * LINE_SPACING, f"Temporada: {worker.get('Temporada', 'N/A')}")
        c.drawString(x + 5 * mm, caption_y - 4 * LINE_SPACING, f"Total: {worker.get('Total Semanal', 'N/A')}")

        # Mostrar pagos de forma tabular
        dias = worker.get("Dias", "").split()  # Encabezados de días
        pagos = worker.get("Pagos", "").split()  # Valores de pagos

        # Dibujar encabezados de días
        y_offset = caption_y - 5 * LINE_SPACING
        for j, dia in enumerate(dias):
            c.drawString(x + 5 * mm + j * 15 * mm, y_offset, dia)

        # Dibujar valores de pagos
        y_offset -= LINE_SPACING
        for j, pago in enumerate(pagos):
            c.drawString(x + 5 * mm + j * 15 * mm, y_offset, pago)

    c.save()

# Ejecutar el script
input_file = "resumen_trabajadores.txt"
output_folder = "../archivos_pdf"  # Ruta relativa al directorio padre
output_file = os.path.join(output_folder, "etiquetas_nomina.pdf")
workers = parse_input_file(input_file)
generate_pdf(workers, output_file)

print(f"PDF generado: {output_file}")
