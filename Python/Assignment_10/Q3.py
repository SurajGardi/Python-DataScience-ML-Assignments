# 3. Write a program which accepts one number and prints factorial of that number.
# Input: 5
# Output: 120

def Factorial(no):
    Fact = 1
    for i in range(no):
        i = i + 1
        Fact = Fact * i

    print(f"Factorial of {no} is : ",Fact)

def main():
    Value1 = int(input("Enter Number : "))
    Factorial(Value1)

if __name__ == "__main__":
    main()
