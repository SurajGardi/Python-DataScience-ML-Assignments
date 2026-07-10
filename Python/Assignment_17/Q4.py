# 4.Write a program which accept one number form user and return addition of its factors.
# Input : 12 Output : 16 (1+2+3+4+6)

def FactorsAddition(No):
    sum = 0

    for i in range(1, No // 2 + 1):
        if No % i == 0:
            sum += i

    return sum

def main():
    Value = int(input("Enter 1st number : "))
    
    Ret = FactorsAddition(Value)

    print(f"Addition of all factors of {Value} is : {Ret}")
if __name__ == "__main__":
    main()