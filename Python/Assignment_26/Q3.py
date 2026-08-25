"""
3: Write a Python program to implement a class named Arithmetic with the following
characteristics:
• The class should contain two instance variables: Value1 and Value2.
• Define a constructor (__init__) that initializes all instance variables to 0.
• Implement the following instance methods:
◦ Accept() – accepts values for Value1 and Value2 from the user.
◦ Addition() – returns the addition of Value1 and Value2.
◦ Subtraction() – returns the subtraction of Value1 and Value2.
◦ Multiplication() – returns the multiplication of Value1 and Value2.
◦ Division() – returns the division of Value1 and Value2 (handle division by zero
properly).

• Create multiple objects of the Arithmetic class and invoke all the instance methods.

"""

class Arithmatic():

    # Parameterizes constructor
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        self.Value1 = int(input("Enter 1st Value : "))
        self.Value2 = int(input("Enter 2nd Value : "))

    def Addition(self):
        return self.Value1 + self.Value2
    
    def Substraction(self):
        return self.Value1 - self.Value2
    
    def Multipication(self):
        return self.Value1 * self.Value2
    
    def Division(self):
        if self.Value2 == 0:
            return "Cannot divide by zero"
        return self.Value1 / self.Value2

def main():

    obj1 = Arithmatic()
    obj2 = Arithmatic()

    obj1.Accept()

    print(f"Addition of is : ",obj1.Addition())
    print("Substraction is : ",obj1.Substraction())
    print("Multipication is : ",obj1.Multipication())
    print("Division is : ",obj1.Division())

    print("---------------")

    obj2.Accept()

    print(f"Addition of is : ",obj2.Addition())
    print("Substraction is : ",obj2.Substraction())
    print("Multipication is : ",obj2.Multipication())
    print("Division is : ",obj2.Division())

if __name__ == "__main__":
    main()