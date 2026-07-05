# 8. Write a lambda function which accepts two numbers and returns addition.

Addition = lambda No1, No2 : No1 + No2 



def main():
    value1 = int(input("Enter 1st Number : "))
    value2 = int(input("Enter 2nd Number : "))

    Ret = Addition(value1, value2)

    print(f"Addition of {value1} and {value2} is : {Ret}")
   

if __name__ == "__main__":
    main()