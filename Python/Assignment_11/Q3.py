# 3. Write a program which accepts one number and prints sum of digits.
# Input: 123
# Output: 6

def sumDigits(n):
    count = 0
    sum = 0

    while(n):
        digit = n % 10
        sum = sum + digit
        n = n // 10
        count = count + 1
    
    print(sum)

    

def main():
    Value1 = int(input("Enter Number : "))
    sumDigits(Value1)

if __name__ == "__main__":
    main()