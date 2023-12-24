"""This module is about the default construtor.
When we do not include the constructor in the class or forget to declare it, then that becomes 
the default constructor. It does not perform any task but initializes the objects.
"""

class Employee:  
    emp_id = 1231  
    name = "Saurav"  
  
    def display(self):  
        print(self.emp_id,self.name)  
  
emp1 = Employee()  
emp1.display() 