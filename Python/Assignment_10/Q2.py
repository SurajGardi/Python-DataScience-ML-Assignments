# 2. Write a program which accepts one number and prints sum of first N natural numbers.
# Input: 5
# Output: 15

def nNaturalNumSum(no):
    Ans = 0
    for i in range(no):
        i = i + 1
        Ans = Ans+i

    print(f"sum of first {no} natural numbers is : ",Ans)

def main():
    Value1 = int(input("Enter Number : "))
    nNaturalNumSum(Value1)

if __name__ == "__main__":
    main()
