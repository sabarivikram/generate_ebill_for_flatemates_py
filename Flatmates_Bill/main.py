from classes.bill import Bill
from classes.flatmate import Flatmate
from classes.pdfreport import PdfReport
from classes.fileshare import FileShare

#main
the_bill = Bill(float(input('Enter Bill Amount: ')),input('Enter Period (eg \'january 2025\'): ') )
f1 = Flatmate(input('Enter name of flatmate1: '),int(input('Enter No of days in flat: ')))
f2 = Flatmate(input('Enter name of flatmate2: '),int(input('Enter No of days in flat: ')))


print('Bill Amount for ',the_bill.period, ' is :',the_bill.amount)
print(f'{f1.name} pays: ',f1.pays(the_bill,f2))
print(f'{f2.name} pays: ',f2.pays(the_bill,f1))

pdf_bill = PdfReport(f'Ebill_{the_bill.period}.pdf')
pdf_bill.generate(f1,f2,the_bill)

fileshare = FileShare(f'output/{pdf_bill.filename}','')
print(fileshare.getUrl)