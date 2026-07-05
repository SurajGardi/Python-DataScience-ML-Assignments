# 9. Write a lambda function which accepts two numbers and returns multiplication.

Multiplication = lambda No1, No2 : No1 * No2 



def main():
    value1 = int(input("Enter 1st Number : "))
    value2 = int(input("Enter 2nd Number : "))

    Ret = Multiplication(value1, value2)

    print(f"Multiplication of {value1} and {value2} is : {Ret}")
   

if __name__ == "__main__":
    main()