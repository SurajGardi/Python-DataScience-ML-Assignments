# 1.Write a program which accept N numbers from user and store it into List. Return addition of all
# elements from that List.
# Input : Number of elements : 6
# Input Elements : 13 5 45 7 4 56
# Output : 130

from functools import reduce

def Addition(No1, No2):
    return No1 + No2

def main():
    Value = int(input("ENter Number : "))

    Data = list()

    for i in range(Value):
        num = int(input(f"Enter Number {i+1} : "))
        Data.append(num)

    Ret = reduce(Addition, Data)

    print("Addition is : ",Ret)

if __name__ == "__main__":
    main()