# 3. Write a program which accepts one number and prints square of that number.
# Input: 5
# Output: 25

def Square(No):
    Ans = No * No

    print(f"Square of {No} is : ",Ans)


def main():
    Value1 = int(input("Enter the Number : "))

    Square(Value1)

if __name__ == "__main__":
    main()