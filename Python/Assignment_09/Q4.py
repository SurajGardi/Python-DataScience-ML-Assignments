# 4. Write a program which accepts one number and prints cube of that number.

def Cube(No):
    Ans = No * No * No

    print(f"Cube of {No} is : ",Ans)


def main():
    Value1 = int(input("Enter the Number : "))

    Cube(Value1)

if __name__ == "__main__":
    main()