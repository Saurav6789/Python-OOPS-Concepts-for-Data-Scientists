    """In this section , we will see the example for method overloading. Two or more methods have the 
    same name but different numbers of parameters or different types of parameters, or both. 
    These methods are called overloaded methods and this is called method overloading. 
    """
class Calculator:
    def add(self, a, b=None, c=None):
        """
        Method overloading for addition.

        :param a: First operand.
        :param b: Second operand (default is None).
        :param c: Third operand (default is None).
        :return: Sum of operands.
        """
        if b is None and c is None:
            return a
        elif c is None:
            return a + b
        else:
            return a + b + c

# Creating an instance of Calculator
calc = Calculator()

# Testing different overloaded cases
output1 = calc.add(10)
output2 = calc.add(15, 10)
output3 = calc.add(15, 10, 20)

# Displaying results
print(f"Result 1: {output1}")
print(f"Result 2: {output2}")
print(f"Result 3: {output3}")

        """The above way is a bit complex as it uses multiple if/else statement and is not desired way of 
        achieve method overloading. We will be using Multiple Dispatch Decorator 
        """