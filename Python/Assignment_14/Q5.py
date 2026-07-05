# 5. Write a lambda function which accepts one number and returns True if number is even otherwise False.


CheckEven = lambda No1 : No1 % 2 == 0 

def main():
    value1 = int(input("Enter Number : "))

    Ret = CheckEven(value1)

    if Ret == True:   
        print(f"{value1} is Even Number")
    else:
        print(f"{value1} is Odd Number")


if __name__ == "__main__":
    main()