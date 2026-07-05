# 7. Write a lambda function which accepts one number and returns True if divisible by 5.

DivisibleBy5 = lambda No : No % 5 == 0

def main():
    value = int(input("Enter Number : "))

    Ret = DivisibleBy5(value)

    if Ret == True:   
        print(f"{value} is divisible by 5")
    else:
        print(f"{value} is not divisible by 5")

if __name__ == "__main__":
    main()