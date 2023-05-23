from fpdf import FPDF
import pandas as pd
pdf = FPDF(orientation='L',unit='mm',format='A4')
df = pd.read_csv(r'topics.csv')




for index,row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family='Times',style='B',size=24)
    pdf.cell(w=0,h=12,txt=row['Topic'],ln=1,align='L')
    pdf.line(x1=10,y1=21,x2=285,y2=21)
    for i in range(row['Pages']-1):
        pdf.add_page()
pdf.output('Output.pdf')