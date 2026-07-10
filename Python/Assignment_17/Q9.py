# 9. Write a program which accept number from user and return number of digits in that number.
# Input : 5187934 Output : 7

def CountDigit(No):
    count = 0

    if No == 0:
        return 1
    
    while No != 0:
        No = No // 10  
        count += 1

    return count
        
def main():
    Value = int(input("Enter Number : "))

    Ret = CountDigit(Value)

    print("Total Digits are : ",Ret)

if __name__ == "__main__":
    main()