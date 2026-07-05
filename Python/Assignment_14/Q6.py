# 5. Write a lambda function which accepts one number and returns True if number is Odd otherwise False.


CheckOdd = lambda No1 : No1 % 2 == 1 

def main():
    value1 = int(input("Enter Number : "))

    Ret = CheckOdd(value1)

    if Ret == True:   
        print(f"{value1} is Odd Number")
    else:
        print(f"{value1} is Even Number")


if __name__ == "__main__":
    main()