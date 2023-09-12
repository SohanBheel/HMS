import sys
import os
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)
from Hotel.Person.customers import Customers
class NegativeBill(Exception):
    def __init__(self):
        print("bill can't be negative")
class Children(Customers):
    def __init__(self, name, age,durationday, bill, pooltime=0):
        Customers.__init__(self, name, age,durationday,bill)
        self.pooltime=pooltime
    def add_children_pool_time(self,time):
        self.pooltime+=time
    def add_bill(self,amount):
        Customers.addbill(self,amount)
    def reduce_bill(self,amount):
        if amount > self.bill:
            raise NegativeBill
        else:
            Customers.reducebill(self,amount)
    def display(self):
        return 'Name:{} Age:{} Duration:{} bill:{} pooltime:{}'.format(self.name, self.age, self.duration, self.bill, self.pooltime)