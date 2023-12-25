"""In python, polymorphism refers to the way in which different object classes can share the same method name,
and those methods can be called from the same place even though a variety of different objects might be 
passed in
"""

class developer:
    def __init__(self,name):
        self.name = name
        
    def work(self):
        return self.name + " writes codes"


class manager:
    def __init__(self,name):
        self.name = name 
    
    def work(self):
        return self.name + " manages team"
    

saurav = developer("saurav")
prakash = manager("prakash")

print(saurav.work())
print(prakash.work())
        