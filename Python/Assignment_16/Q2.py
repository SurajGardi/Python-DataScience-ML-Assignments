# 2. Write a program which contains one function named as ChkNum() which accept one
# parameter as number. If number is even then it should display “Even number” otherwise
# display “Odd number” on console.
# Input : 11 Output : Odd Number
# Input : 8 Output : Even Number

def ChkNum(No):
    if No % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")

def main():

    Value = int(input("Enter Number : "))
    
    ChkNum(Value)

if __name__ == "__main__":
    main()