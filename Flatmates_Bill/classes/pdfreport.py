from fpdf import FPDF
import webbrowser
import os

class PdfReport:

    def __init__(self,filename):
        self.filename = filename
    
    def generate(self,f1,f2,bill):

        pdf = FPDF(orientation='P',unit='pt',format='A4')

        pdf.add_page()
        pdf.image('resources/house.png',w=30,h=30)
        pdf.set_font(family='Times',style='B',size=24)
        pdf.cell(w=0,h=80,txt='Flatemates Bill', border=0,align='C',ln=1)
        pdf.set_font(family='Times',style='B',size=14)
        pdf.cell(w=100,h=40,txt='Period ', border=0)
        pdf.set_font(family='Times',style='',size=14)
        pdf.cell(w=150,h=40,txt= bill.period, border=0,ln=1)
        pdf.set_font(family='Times',style='B',size=12)
        pdf.cell(w=100,h=25,txt= f1.name, border=0)
        pdf.set_font(family='Times',style='U',size=12)
        pdf.cell(w=100,h=25,txt=str(round(f1.pays(bill,f2),2)), border=0,ln=1)
        pdf.set_font(family='Times',style='B',size=12)
        pdf.cell(w=100,h=25,txt=f2.name, border=0)
        pdf.set_font(family='Times',style='U',size=12)
        pdf.cell(w=100,h=25,txt=str(round(f2.pays(bill,f1),2)), border=0,ln=1)
        pdf.set_font(family='Times',style='B',size=14)
        pdf.cell(w=160,h=40,txt='Total Bill Amount ', border=0)
        pdf.set_font(family='Times',style='B',size=14)
        pdf.cell(w=0,h=40,txt=str(bill.amount), border=0)

        os.chdir('output')
        pdf.output(self.filename)
        webbrowser.open(self.filename)