# 3.Write a program which accept N numbers from user and store it into List. Return Minimum
# number from that List.
# Input : Number of elements : 4
# Input Elements : 13 5 45 7
# Output : 5

from functools import reduce

def Minimum(No1, No2):
    if No1 < No2:
        return No1
    else:
        return No2

def main():

    Value = int(input("Enter Number : "))

    Data = []

    for i in range(Value):

        num = int(input(f"Enter Number {i+1} : "))

        Data.append(num)

    Ret = reduce(Minimum,Data)

    print("Minimum Number from list is : ",Ret)

if __name__ == "__main__":
    main()