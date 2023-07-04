from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

class PDFGenerator:
    def __init__(self, filename, data):
        self.filename = filename
        self.data = data

    def generar_reporte_productos(self):
        doc = SimpleDocTemplate(self.filename, pagesize=letter)
        table_data = []
        table_data.append(["Código", "Nombre", "Precio"])
        for producto in self.data:
            table_data.append([
                producto["codigo"],
                producto["nombre"],
                str(producto["precio"])
            ])

        table = Table(table_data)
        style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ])

        table.setStyle(style)
        elements = [table]
        doc.build(elements)

