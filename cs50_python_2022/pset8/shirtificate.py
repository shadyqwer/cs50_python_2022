from fpdf import FPDF

name = input("Name: ")
pdf = FPDF()

pdf.add_page()
pdf.set_font('Times', size=36)
pdf.cell(w=0, h=0, txt='CS50 Shirtificate', align='C', new_x='LMARGIN', new_y='NEXT')
pdf.image('shirtificate.png', x=0, y=70)
pdf.set_font_size(30)
pdf.set_text_color(255, 255, 255)
pdf.cell(w=0, h=260, txt=f'{name} took CS5O', align='C')
pdf.output('shirtificate.pdf')