# 7. Write a program which contains one function that accept one number from user and returns
# true if number is divisible by 5 otherwise return false.
# Input : 8 Output : False
# Input : 25 Output : True

def ChkDivisible(No):
    if No % 5 == 0:
        return True
    else:
        return False

def main():
    Value = int(input("Enter Number : "))

    Ret = ChkDivisible(Value)

    print(Ret)

if __name__ == "__main__":
    main()