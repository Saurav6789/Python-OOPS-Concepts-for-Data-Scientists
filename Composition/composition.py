"""In Python, a class can inference to one or more objects of other classes as an instance variable, 
rather than inheriting it
"""

class Employee:
    def work(self):
        print("Employee is on work")
    
    def vacation(self):
        print("Employee is on vacation")


class Developer:
    def __init__(self) -> None:
        self.employee =Employee()
    
    def work(self):
        print("Developer is working")
        # Delegating the work operation to the Employee
        self.employee.work()
        
    def vacation(self):
        print("Developer is on vacation")
        # Delegating the vacation operation to the Employee
        self.employee.vacation()
        

#Creating an instance of Developer

dev1 = Developer()

#Using the methods which delegates to the Employee methods 

dev1.work()
dev1.vacation() 
        
                