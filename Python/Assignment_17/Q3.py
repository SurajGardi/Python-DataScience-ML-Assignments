# 3. Write a program which accept one number from user and return its factorial.
# Input : 5 
# Output : 120

def Factorial(No):
    fact = 1

    for i in range(1, No+1):
        fact = fact * i

    return fact

def main():
    Value = int(input("Enter 1st number : "))
    
    Ret = Factorial(Value)

    print(f"Factorial of {Value} is : {Ret}")
if __name__ == "__main__":
    main()