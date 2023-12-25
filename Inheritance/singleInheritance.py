"""In single inheritance there is a base class ( parent class) and a derived class (child class )
"""
    
class Employee:
    def work(self):
        print("Employee works")
            
    
class programmer(Employee):
    def coding(self):
        print("programmer codes")
    
#Creating an instance of dog 
pgm1 = programmer()
    
#Accessing methods 
pgm1.work() # inheritance from parent class
pgm1.coding()
    