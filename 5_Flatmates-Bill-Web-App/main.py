from flask.views import MethodView
from wtforms import Form,StringField,SubmitField
from flask import Flask,render_template,request
from flatmates_bill.flat import Bill,Flatmate

class HomePage(MethodView):
    def get(self):
        return render_template('index.html')
    
class BillForm(Form):
    amount = StringField('Bill Amount: ', default='100')
    period = StringField('Bill Period: ', default='March 2025')

    name1 = StringField('Name: ', default='Vikram')
    days_in_house1 = StringField('Days in the house: ', default='14')

    name2 = StringField('Name: ', default='Dhruv')
    days_in_house2 = StringField('Days in the house: ', default='16')

    button = SubmitField('Calculate')

class BillFormPage(MethodView):
    
    def get(self):
        bill_form = BillForm()
        return render_template('bill_form_page.html',result = False,billform = bill_form)
    
    def post(self):       
        billform = BillForm(request.form)
        the_bill = Bill(float(billform.amount.data),billform.period.data)
        flatemate1 = Flatmate(billform.name1.data,float(billform.days_in_house1.data))
        flatemate2 = Flatmate(billform.name2.data,float(billform.days_in_house2.data))

        return render_template('bill_form_page.html',result = True,billform = billform,name1 = flatemate1.name,name2 = flatemate2.name,flatemate1_pays = flatemate1.pays(the_bill,flatemate2),flatemate2_pays = flatemate2.pays(the_bill,flatemate1))

    

class ResultPage(MethodView):
    def post(self):
        billform = BillForm(request.form)
        the_bill = Bill(float(billform.amount.data),billform.period.data)
        flatemate1 = Flatmate(billform.name1.data,float(billform.days_in_house1.data))
        flatemate2 = Flatmate(billform.name2.data,float(billform.days_in_house2.data))

        return render_template('results.html',name1 = flatemate1.name,name2 = flatemate2.name,flatemate1_pays = flatemate1.pays(the_bill,flatemate2),flatemate2_pays = flatemate2.pays(the_bill,flatemate1))



app = Flask(__name__)
app.add_url_rule('/',view_func=HomePage.as_view('home_page'))
app.add_url_rule('/bill_form_page',view_func=BillFormPage.as_view('bill_form_page'))
app.add_url_rule('/results', view_func=ResultPage.as_view('results'))
app.run(debug=True)
