from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

if __name__ == '__main__':
    c = canvas.Canvas('test1.pdf', pagesize=A4)

    c.drawString(100, 100, "Hello world")
    c.showPage()
    c.save()

