# 10. Write a program which accept number from user and return addition of digits in that number.
# Input : 5187934 Output : 37

def SumDigits(No):
    total = 0
    
    while No != 0:
        Digit = No % 10
        total = total + Digit
        No = No // 10  

    return total
        
def main():
    Value = int(input("Enter Number : "))

    Ret = SumDigits(Value)

    print("Sum of Digits are : ",Ret)

if __name__ == "__main__":
    main()