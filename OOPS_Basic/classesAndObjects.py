"""This Module contains the details about creating class and Objects in Python to show data and behaviour are 
encapsulated together 
"""
# Creating a class and defining the attributes 
class Employee:
    def __init__(self,name,salary) -> None:
        self.name = name
        self.salary = salary
        
        
# Creating instances of the objects 

emp1 = Employee("Saurav",12000)
print(f"Employee 1: {emp1.name} {emp1.salary}")
    