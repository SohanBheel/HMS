class NegativeDiscount(Exception):
    def __init__(self):
        print("discount can't be negative")

class NegativeRoom(Exception):
    def __init__(self):
        print("not enough available room(s)")

class Room:
    def __init__(self,price,availablenumber):
        self.price = price
        self.availablenumber=availablenumber

    def modifyprice(self,newprice):
        self.price=newprice

    def discountprice(self, discount=1):
        if discount < 0:
            raise NegativeDiscount
        self.price*=discount

    def reduceroomnumber(self,reduceamount):
        if reduceamount > self.availablenumber:
            raise NegativeRoom
        self.availablenumber-=reduceamount

    def addroomnumber(self,addamount):
        self.availablenumber+=int(addamount)

    def display(self):
        return 'Price:{} Availablenumber:{}'.format(self.price, self.availablenumber)
