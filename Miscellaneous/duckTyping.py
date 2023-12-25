"""In python,the type or class of an object is determined by its behavior rather than its explicit type. 
"""

class Whale: 
    def swim(self): 
        print("Swim with the huge fins") 
  
class Airplane: 
    def fly(self): 
        print("fly with fuel") 
  
class Fish: 
    def swim(self): 
        print("fish swim in sea") 
  
# Attributes having same name are 
# considered as duck typing 
for obj in Whale(), Fish(),Airplane(): 
    obj.swim() 