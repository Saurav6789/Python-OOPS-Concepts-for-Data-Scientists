"""The method overloading can be better implemented by using the multipledispatch library which makes the code
less complex and much easy to use.  
"""

from multipledispatch import dispatch

class Calculator:
    @dispatch(int)
    def add(self, a):
        return a

    @dispatch(int, int)
    def add(self, a, b):
        return a + b

    @dispatch(int, int, int)
    def add(self, a, b, c):
        return a + b + c

    @dispatch(float, float)
    def add(self, a, b):
        return a + b

# Creating an instance of Calculator
calc = Calculator()

# Testing different overloaded cases
output1 = calc.add(5)
output2 = calc.add(5, 10)
output3 = calc.add(5, 10, 15)
output4 = calc.add(2.5, 3.5)

# Displaying results
print(f"Result 1: {output1}")
print(f"Result 2: {output2}")
print(f"Result 3: {output3}")
print(f"Result 4: {output4}")

