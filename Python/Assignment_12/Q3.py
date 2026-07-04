# 3. Write a program which accepts two numbers and prints addition, subtraction, multiplication and division.

def Addition(no1, no2):
    return no1 + no2

def Substraction(no1, no2):
    return no1 - no2

def Multiplication(no1, no2):
    return no1 * no2

def Division(no1, no2):
    return no1 / no2

    

def main():
    Value1 = int(input("Enter 1st Number : "))
    Value2 = int(input("Enter 2nd Number : "))

    Ret = Addition(Value1, Value2)
    print("Addition is : ",Ret)

    Ret = Substraction(Value1, Value2)
    print("Substraction is : ",Ret)

    Ret = Multiplication(Value1, Value2)
    print("Multiplication is : ",Ret)

    Ret = Division(Value1, Value2)
    print("Division is : ",Ret)

if __name__ == "__main__":
    main()