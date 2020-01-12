from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.pdfmetrics import registerFontFamily

import json




#solucion: esto es una función. la función que usa esta funcón, solo pasa el nombre, cc, y orden.

## Registered font family
pdfmetrics.registerFont(TTFont('Vera', 'Vera.ttf'))
pdfmetrics.registerFont(TTFont('VeraBd', 'VeraBd.ttf'))
pdfmetrics.registerFont(TTFont('VeraIt', 'VeraIt.ttf'))
pdfmetrics.registerFont(TTFont('VeraBI', 'VeraBI.ttf'))
# Registered fontfamily
registerFontFamily('Vera',normal='Vera',bold='VeraBd',italic='VeraIt',boldItalic='VeraBI')

# create a new PDF with Reportlab

#nombre="John Michael"
#cc="11110000"
#can.drawString(2*x+0, 3*y+52, nombre)
#can.setFont('VeraBd', 17)
#can.drawString(3*x+80, 3*y+25, cc)
#can.save()
'''
with open("asistentes.json", "r") as read_file:
    data = json.load(read_file)
    print(data)

for cc, nombre in data.items():
    print(inicio)
    print(cc, nombre)
    can = canvas.Canvas(packet, pagesize=letter)
    can.setFont('VeraBd', 27)
    x=100
    y=100
    can.drawString(2*x+0, 3*y+52, nombre)
    can.setFont('VeraBd', 17)
    can.drawString(3*x+80, 3*y+25, str(cc))
    can.save()
    #
    try:
        
        time.sleep(1)
        packet.seek(0)
        # move to the beginning of the StringIO buffer
        new_pdf = PdfFileReader(packet)
        # read your existing PDF
        existing_pdf = PdfFileReader(open("plantilla.pdf", "rb"))
        output = PdfFileWriter()
        # add the "watermark" (which is the new pdf) on the existing page
        page = existing_pdf.getPage(0)
        page2 = new_pdf.getPage(0)
        page.mergePage(page2)
        output.addPage(page)
        # finally, write "output" to a real file
        init=str(inicio)+".pdf"
        print(init, type(init))
        outputStream = open(init, "wb")
        output.write(outputStream)
        print(inicio)
        inicio=inicio+1
        print("ok")
        
        outputStream.close()
    except Exception as e:
        print(e)
'''        
def crear_pdf( cc,nombre, id, palab, tam):
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)
    can.setFont('VeraBd', 27)
    x=100
    y=100
    #
    if palab==2:
        print(2)
        can.drawString(4*x+30-9*tam, 3*y+52, nombre)
    elif palab==3:
        print(3)
        can.drawString(4*x+30-9*tam, 3*y+52, nombre)
    elif palab==4:
        print(4)
        can.drawString(4*x+30-9*tam, 3*y+52, nombre)
    else:
        print("Error, nombre incompleto")
    #
    #
    #can.drawString(2*x+0, 3*y+52, nombre)
    can.setFont('VeraBd', 17)
    can.drawString(3*x+80, 3*y+25, str(cc))
    can.save()
    #
    #
    packet.seek(0)
    # move to the beginning of the StringIO buffer
    new_pdf = PdfFileReader(packet)
    # read your existing PDF
    existing_pdf = PdfFileReader(open("plantilla.pdf", "rb"))
    output = PdfFileWriter()
    # add the "watermark" (which is the new pdf) on the existing page
    page = existing_pdf.getPage(0)
    page2 = new_pdf.getPage(0)
    page.mergePage(page2)
    output.addPage(page)
    # finally, write "output" to a real file
    init=str(id)+".pdf"
    print(init, type(init))
    outputStream = open(init, "wb")
    output.write(outputStream)
    id=id+1
    print("Completado")
    outputStream.close()
    #time.sleep(0.1)
def automatizar_pdf(data,inicio):
    for cc, nombre in data.items():
        palabras=len(nombre.split())
        tamano=len(nombre)
        print(palabras, tamano)
        crear_pdf(cc, nombre, inicio, palabras,tamano)
        inicio=inicio+1
        time.sleep(0.3)

if __name__ == "__main__":
    print("Bienvenido al Gestor de Certificados de Phikubo")
    inicio=91
    #n="jOHn Michael"
    #c="12315"
    #i=91
    import time
    #crear_pdf(n,c,i)
    #crear_pdf(n,c,9)
    with open("asistentes.json", "r", encoding='utf-8') as read_file:
        data = json.load(read_file)
    automatizar_pdf(data,inicio)
else:
    pass
