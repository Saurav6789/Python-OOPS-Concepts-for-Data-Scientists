"""Method overriding is way of doing specific implementation of the parent class method in the child class. 
This is needed when we need to have different definition of a parent class method in the child class.
"""

class Employee:
    def work(self):
        print("Employee works")
        
class developer(Employee):
    def work(self):
        print("Developer codes")


emp1 = developer()
emp1.work()