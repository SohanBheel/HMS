class NegativeSalary(Exception):
    def __init__(self):
        print("salary can't be negative")
        
class Employee():
    def __init__(self, name, age, hourlyrate, workhour=0, salary=0):
        self.name = name
        self.age = age
        self.workhour=workhour
        self.salary=salary
        self.hourlyrate=hourlyrate
        
    def add_work_salary(self,hours):
        self.workhour+=hours
        self.salary+=hours*self.hourlyrate
        
    def add_bonus(self,bonus):
        self.salary+=bonus
        
    def reduce_salary(self,money):
        if money > self.salary:
            raise NegativeSalary
        else:
            self.salary-=money
        
    def display(self):
        return 'Name:{} Age:{} Hourlyrate:{} Workhour:{} Salary:{}'.format(self.name, self.age, self.hourlyrate, self.workhour, self.salary)