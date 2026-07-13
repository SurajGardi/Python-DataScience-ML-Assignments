# 2.Write a program which contains one lambda function which accepts two parameters and return
# its multiplication.
# Input : 4 3 Output : 12
# Input : 6 3 Output : 18

multiplicationX = lambda No1, No2 : No1 * No2 

def main():
    Value1 = int(input("Enter 1st Number : "))
    Value2 = int(input("Enter 2nd Number : "))

    Ret = multiplicationX(Value1, Value2)

    print(f"Multiplication is : ",Ret)

if __name__ == "__main__":
    main()