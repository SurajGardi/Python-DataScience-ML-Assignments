# 5. Write a program which accepts one number and checks whether it is palindrome or not.
# Input: 121
# Output: Palindrome

def ChkPalindromeBySlicing(n):
    rev = int(str(n)[::-1])

    if n == rev:
        print(n," is palindrome (Chked using Slicing)")
    else:
        print(n," is Not palindrome (Chked Using Slicing)")

def ChkPalindromeNum(n):
    count = 0
    rev = 0
    no = n
    while(n):
        
        digit = n % 10
        rev = rev*10 + digit
        # print(rev)
        n = n // 10
        count = count + 1
    
    if no == rev:
        print(no," is palindrome (Chked using Custom logic)")
    else:
        print(no," is Not palindrome (Chked Using Custom Logic)")

    
def main():
    Value1 = int(input("Enter Number : "))
    ChkPalindromeBySlicing(Value1)
    ChkPalindromeNum(Value1)

if __name__ == "__main__":
    main()