# 2.Write a program which accept N numbers from user and store it into List. Return Maximum
# number from that List.
# Input : Number of elements : 7
# Input Elements : 13 5 45 7 4 56 34
# Output : 56

from functools import reduce

def Maximum(No1, No2):
    if No1 > No2:
        return No1
    else:
        return No2

def main():

    Value = int(input("Enter Number : "))

    Data = []

    for i in range(Value):

        num = int(input(f"Enter Number {i+1} : "))

        Data.append(num)

    Ret = reduce(Maximum,Data)

    print("MAximum Number from list is : ",Ret)

if __name__ == "__main__":
    main()