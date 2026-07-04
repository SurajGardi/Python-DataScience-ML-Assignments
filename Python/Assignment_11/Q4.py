# 4. Write a program which accepts one number and prints reverse of that number.
# Input: 123
# Output: 321

def reverceBySlicing(n):
    rev = int(str(n)[::-1])

    print("Reverse number by using Slicing : ", rev)

def reverseNum(n):
    count = 0
    rev = 0

    while(n):
        digit = n % 10
        rev = rev*10 + digit
        # print(rev)
        n = n // 10
        count = count + 1
    
    print("Reverse Number by using custom logic : ",rev)

    
def main():
    Value1 = int(input("Enter Number : "))
    reverceBySlicing(Value1)
    reverseNum(Value1)

if __name__ == "__main__":
    main()