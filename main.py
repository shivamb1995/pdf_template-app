from fpdf import FPDF
import pandas as pd
pdf = FPDF(orientation='L',unit='mm',format='A4')
df = pd.read_csv(r'topics.csv')

pdf.set_auto_page_break(auto=False,margin=0)


for index,row in df.iterrows():
    # Set Header
    pdf.add_page()
    pdf.set_font(family='Times',style='B',size=20)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0,h=12,txt=row['Topic'],ln=1,align='L')
    pdf.line(x1=10,y1=21,x2=285,y2=21)
    # Set Footer
    pdf.ln(175)
    pdf.set_font(family='Times',style='BI',size=8)
    pdf.cell(w=0,h=12,align='R',txt=row['Topic'])
    for i in range(row['Pages']-1):
        pdf.add_page()
        # Set Footer
        pdf.ln(186)
        pdf.set_font(family='Times',style='BI',size=8)
        pdf.cell(w=0,h=12,align='R',txt=row['Topic'])

pdf.output('Output.pdf')