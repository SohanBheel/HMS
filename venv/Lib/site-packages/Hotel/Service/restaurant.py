import pandas as pd

class Restaurant:
    def __init__(self,menu={},employee=[]): 
        self.menu = menu
        self.employee=employee
    
    def addfood(self,food,price):
        self.menu[food]=price
        
    def addemployee(self,employee):
        self.employee.append(employee)
    
    def display(self):
        menu_list=[]
        price_list=[]
        emp_list=[]

        if len(self.menu)==0:
            menu_list.append("NAN")
            price_list.append("NAN")
        else:
            for item in self.menu:
                menu_list.append(item)
                price_list.append(self.menu[item])
        if len(self.employee)==0:
            emp_list.append("NAN")
        else:
            for people in self.employee:
                emp_list.append(people)

        data_menu = {'Menu':menu_list,'Price':price_list}
        menu_df = pd.DataFrame(data_menu)
        menu_df = menu_df.to_string(index=False)

        data_emp = {'Employee':emp_list}
        emp_df = pd.DataFrame(data_emp)
        emp_df = emp_df.to_string(index=False)

        return menu_df+'\n'+'\n'+emp_df