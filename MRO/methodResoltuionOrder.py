"""In python, MRO is basically the order in which the parent classes are searched when a method is 
called by an object. In Python, the MRO is from bottom to top and left to right. This means that, 
first, the method is searched in the class of the object. If it's not found, 
it is searched in the immediate super class. In the case of multiple super classes, it is searched 
left to right, in the order by which was declared by the developer.
"""

class Employee:
    def show(self):
        print("Employee")


class Manager:
    def show(self):
        print("Manager")
    
    
class Developer(Employee,Manager):
   pass


# Creating an instance of class D
pgm1 = Developer()

# Accessing the 'show' method
pgm1.show()
