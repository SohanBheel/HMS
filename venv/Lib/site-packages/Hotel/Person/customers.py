class NegativeBill(Exception):
    def __init__(self):
        print("bill can't be negative")
        
class Customers():#adults
    def __init__(self, name, age, durationday,bill=0):
        self.name = name
        self.age = age
        self.duration=durationday
        self.bill=bill
        
    def addbill(self,amount):
        self.bill+=amount
        
    def reducebill(self,amount):
        if amount > self.bill:
            raise NegativeBill
        else:
            self.bill-=amount
        
    def display(self):
        return 'Name:{} Age:{} Duration:{} bill:{}'.format(self.name, self.age, self.duration, self.bill)
        
  