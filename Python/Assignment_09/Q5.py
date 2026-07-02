# 5. Write a program which accepts one number and checks whether it is divisible by 3 and 5
# Input: 15
# Output: Divisible by 3 and 5


def chkDivisible(No):
    
    if (No % 3 == 0 and No % 5 == 0) :
        print("Divisible by 3 and 5")
    else:
        print("Not Divisible by 3 and 5")


def main():
    Value1 = int(input("Enter the Number : "))

    chkDivisible(Value1)

if __name__ == "__main__":
    main()