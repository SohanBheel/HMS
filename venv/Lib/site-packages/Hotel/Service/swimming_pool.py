class NegativeDiscount(Exception):
    def __init__(self):
        print("discount can't be negative")

class swimming_pool:
    def __init__(self,price):
        self.price = price

    def modifyprice(self,newprice):
        self.price=newprice

    def discountprice(self, discount=1):
        if discount < 0:
            raise NegativeDiscount
        self.price*=discount

    def display(self):
        return 'Swimming pool ticket price:{}'.format(self.price)

