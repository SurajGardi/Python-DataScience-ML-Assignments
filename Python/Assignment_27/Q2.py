"""
2: Write a Python program to implement a class named BankAccount with the following
requirements:
• The class should contain two instance variables:
    ◦ Name (Account holder name)
    ◦ Amount (Account balance)
• The class should contain one class variable:
    ◦ ROI (Rate of Interest), initialized to 10.5
• Define a constructor (__init__) that accepts Name and initial Amount.
• Implement the following instance methods:
    ◦ Display() – displays account holder name and current balance
    ◦ Deposit() – accepts an amount from the user and adds it to balance
    ◦ Withdraw() – accepts an amount from the user and subtracts it from balance
    (Ensure withdrawal is allowed only if sufficient balance exists)
    ◦ CalculateInterest() – calculates and returns interest using formula:
Interest = (Amount * ROI) / 100
• Create multiple objects and demonstrate all methods.

"""

class BankAccount():
    # Class VAriable
    ROI = 10.5

    # Parameterized Constructor
    def __init__(self,name, amount):

        self.Name = name
        self.Amount = amount

    def Display(self):
        print("Account Holder Name is : ",self.Name)
        print("Current Account Balance is : ",self.Amount)


    def Deposit(self):
        self.Amount += int(input("Enter Amount to Add in Balance : "))
        print("Current Account Balance is : ",self.Amount)


    def Withdraw(self):
        amt = int(input("Enter Amount to withdrow : "))

        if amt > self.Amount:
            print("Insufficient Balance")
        else:
            self.Amount -= amt

    def CalculateInterest(self):
        Interest = (self.Amount * BankAccount.ROI) / 100
        return Interest
        
def main():

    Obj1 = BankAccount("Suraj Gardi", 5000)
    Obj2 = BankAccount("Vedant Khairnar", 10000)

    Obj1.Display()
    Obj1.Deposit()
    Obj1.Withdraw()
    print("Interest is :", Obj1.CalculateInterest())

    print("-------------------")
    
    Obj2.Display()
    Obj2.Deposit()
    Obj2.Withdraw()
    print("Interest is :", Obj2.CalculateInterest())


if __name__ == "__main__":
    main()