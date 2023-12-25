"""In python , there are class and static methods that are bound to class rather than the instance of the class.
A class method can access or modify the class state while a static method can't access or modify it.
"""

class Employee:
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age
    
    #class method to create the overall savings
    @classmethod
    def calSavings(cls,salary,expenditure):
        return salary-expenditure
    
    # static method to check if the employee has the experience more than one year 
    @staticmethod
    def expEmployee(exp):
        return exp >1 
    
emp1 = Employee("saurav",35)
emp2_savings = Employee.calSavings(12000,4000)
print(emp1.age)
print(emp2_savings)   
print(Employee.expEmployee(3)) 