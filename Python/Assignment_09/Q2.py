# 2. Write a program which contains one function ChkGreater() that accepts two numbers
# and prints the greater number.
# Input: 10 20
# Output: 20 is greater

def ChkGreater(No1, No2):
    if No1 > No2 :
        print(No1 ,"is greter than ",No2)
    else:
        print(No2 ,"is greter than ",No1)


def main():
    Value1 = int(input("Enter 1st Number : "))
    Value2 = int(input("Enter 2nd Number : "))

    ChkGreater(Value1, Value2)

if __name__ == "__main__":
    main()