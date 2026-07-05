# 2. Write a lambda function which accepts one number and returns cube of that number.

Cube = lambda No : No * No * No

def main():
    value = int(input("Enter Number : "))

    Ret = Cube(value)

    print(f"Cube of {value} is : {Ret}")

if __name__ == "__main__":
    main()