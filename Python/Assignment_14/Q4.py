# 4. Write a lambda function which accepts two numbers and returns minimum number.

Minimum = lambda No1, No2 : No1 > No2 

def main():
    value1 = int(input("Enter 1st Number : "))
    value2 = int(input("Enter 2nd Number : "))

    Ret = Minimum(value1, value2)

    if Ret == True:   
        print(f"Minimum from {value1} and {value2} is : {value2}")
    else:
        print(f"Minimum from {value1} and {value2} is : {value1}")


if __name__ == "__main__":
    main()