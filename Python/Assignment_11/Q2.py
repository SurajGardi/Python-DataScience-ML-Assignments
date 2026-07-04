# 2.Write a program which accepts one number and prints count of digits in that number.
# Input: 7521
# Output: 4

def CountDigits(n):

    if n == 0:
        return 1
        
    count = 0
    while(n):
        n = n // 10
        count = count + 1
    
    print(count)

    

def main():
    Value1 = int(input("Enter Number : "))
    CountDigits(Value1)

if __name__ == "__main__":
    main()