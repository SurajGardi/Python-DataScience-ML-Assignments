# 1. Write a program which accepts one number and checks whether it is prime or not.
# Input: 11
# Output: Prime Number

def CheckPrime(n):
    if n <= 1:
        print(False)
    else:
        prime = True

        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                prime = False
                break
    
    if prime == True:
        print("Prime Number")
    else :
        print("Not Prime Number")

    

def main():
    Value1 = int(input("Enter Number : "))
    CheckPrime(Value1)

if __name__ == "__main__":
    main()