class Employee():
    def __init__(self,last_name,first_name,salary):
        self.first_name=first_name
        self.last_name=last_name
        self.salary=salary
    def give_raise(self,increment=0):
        self.salary=5000
        self.salary+=increment
        
        
