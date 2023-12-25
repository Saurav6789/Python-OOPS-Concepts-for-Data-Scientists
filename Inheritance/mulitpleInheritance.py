"""In case of mulitple inheritance there is a child class which inherits from more than one or more parent class
"""

class Employee: 
    def work(self):
        print("Employee works")

class Programmar():
    def coding(self):
        print("programmar codes")

class juniorProgrammar(Employee,Programmar):
    pass

prgm1 = juniorProgrammar()

# Accessing methods
prgm1.work()  # Inherited from Employee
prgm1.coding()  # Inherited from Programmar