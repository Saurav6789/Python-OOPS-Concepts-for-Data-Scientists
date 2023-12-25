"""In mulitlevel inheritance a class inherits from base class which inturn inherits from another class
"""

class Employee:
    def work(self):
        print("Employee works")


class Manager(Employee):
    def manages(self):
        print("Manager manages")
            
    
class programmer(Manager):
    def coding(self):
        print("programmer codes")   
        

# Creating an instance of the programmer

pgm = programmer()

# Accessing methods 

pgm.work()
pgm.manages()
pgm.coding()