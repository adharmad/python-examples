from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

if __name__ == '__main__':
    c = canvas.Canvas('test3.pdf', pagesize=A4)

    c.line(10, 10, 10, 50)
    c.line(10, 10, 50, 10)
    c.line(50, 10, 10, 50)
    c.line(50, 10, 50, 50)
    c.showPage()
    c.save()

