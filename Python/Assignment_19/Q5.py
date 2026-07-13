# 5.Write a program which contains filter(), map() and reduce() in it. Python application which
# contains one list of numbers. List contains the numbers which are accepted from user. 
# Filter should filter out all prime numbers. 
# Map function will multiply each number by 2. 
# Reduce will return Maximum number from that numbers. (You can also use normal functions instead of lambda functions).
# Input List = [2, 70 , 11, 10, 17, 23, 31, 77]
# List after filter = [2, 11, 17, 23, 31]
# List after map = [4, 22, 34, 46, 62]
# Output of reduce = 62

from functools import reduce

def CheckPrime(No):

    if No <= 1:
        return False
    

    for i in range(2, No // 2 + 1):
        if No % i == 0:
            return False
        
    return True


Multiply = lambda No : No * 2

Maximum = lambda No1, No2 : No1 if No1 > No2 else No2


def main():

    Value = int(input("Enter Number : "))

    Data = []

    for i in range(Value):

        num = int(input(f"Enter Number {i+1} : "))

        Data.append(num)

    print("Input List = ",Data)

    FData = list(filter(CheckPrime, Data))
    print("List after filter = ",FData)

    MData = list(map(Multiply, FData))
    print("List after map = ",MData)

    RData = reduce(Maximum, MData)
    print("Output of reduce = ",RData)


if __name__ == "__main__":
    main()