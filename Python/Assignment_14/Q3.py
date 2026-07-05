# 3. Write a lambda function which accepts two numbers and returns maximum number.

Maximum = lambda No1, No2 : No1 > No2 

# def Maximum(No1, No2): 
#     return No1 > No2

def main():
    value1 = int(input("Enter 1st Number : "))
    value2 = int(input("Enter 2nd Number : "))

    Ret = Maximum(value1, value2)

    if Ret == True:   
        print(f"Maximun from {value1} and {value2} is : {value1}")
    else:
        print(f"Maximun from {value1} and {value2} is : {value2}")


if __name__ == "__main__":
    main()