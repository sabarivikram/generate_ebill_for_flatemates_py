class Flatmate:

    def __init__(self,name,days):
        self.name = name
        self.days = days
    
    def pays(self,bill,other_flatemate):
        weight = self.days / (self.days + other_flatemate.days)
        individual_bill = bill.amount * (weight)
        return individual_bill