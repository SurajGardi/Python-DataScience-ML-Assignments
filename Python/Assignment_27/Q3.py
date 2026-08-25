"""
3: Write a Python program to implement a class named Numbers with the following
specifications:
• The class should contain one instance variable:
    ◦ Value
• Define a constructor (__init__) that accepts a number from the user and initializes Value.
• Implement the following instance methods:
    ◦ ChkPrime() – returns True if the number is prime, otherwise returns False
    ◦ ChkPerfect() – returns True if the number is perfect, otherwise returns False
    ◦ Factors() – displays all factors of the number
    ◦ SumFactors() – returns the sum of all factors
• Create multiple objects and call all methods.

"""

class Numbers():

    # Parameterizes constructor
    def __init__(self, No):
        self.Value = No

    def ChkPrime(self):
        if self.Value <= 1:
            print("Not Prime Number")
            return
        else:

            prime = True

            for n in range(2, self.Value // 2 + 1):
                if self.Value % n == 0:
                    prime = False
                    break
        if prime:
            return True
        else:
            return False
            
    
    def ChkPerfect(self):
        sum = 0
       
        for i in range(1,self.Value // 2 + 1):
            if self.Value % i == 0 :
                sum = sum + i
    
        if self.Value == sum :
            return True
        else:
            return False
    
    def Factors(self):
        for i in range(1,self.Value+1):
                if self.Value % i == 0:
                    print(i)
    
    def SumFactors(self):
        sum = 0
        
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                sum += i

        return sum

def main():

    obj1 = Numbers(7)
    obj2 = Numbers(9)

    print(obj1.ChkPrime())
    print(obj1.ChkPerfect())
    obj1.Factors()
    print("Sum of all factors is : ",obj1.SumFactors())

    print("-----------------------")

    print(obj2.ChkPrime())
    print(obj2.ChkPerfect())
    obj2.Factors()
    print("Sum of all factors is : ",obj2.SumFactors())


if __name__ == "__main__":
    main()