# 1. Write a lambda function which accepts one number and returns square of that number.

Square = lambda No : No * No


def main():
    Value1 = int(input("Enter Number : "))

    Ret = Square(Value1)

    print(f"Square of {Value1} is : ",Ret)

if __name__ == "__main__":
    main()