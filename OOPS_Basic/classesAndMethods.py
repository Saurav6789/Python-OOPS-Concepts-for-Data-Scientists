"""This module contains the details about creating a class and defining the methods inside it. These methods 
are used to perform operations on the objects.
"""

class Employee:
    def __init__(self,salary,expenditure,bonus,tax) -> None:
        self.salary = salary
        self.expenditure = expenditure
        self.bonus = bonus
        self.tax = tax 
        
    def calculateSavings(self):
        return (self.salary + self.bonus) - (self.expenditure + self.tax)

#Creating a instance of the class 

emp1 = Employee(12000,4000,2000,1000)
print(emp1.calculateSavings())
    
    
        
        
