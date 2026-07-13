# 4.Write a program which contains filter(), map() and reduce() in it. Python application which
# contains one list of numbers. List contains the numbers which are accepted from user. 
# Filter should filter out all such numbers which are even. 
# Map function will calculate its square.
# Reduce will return addition of all that numbers.
# Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
# List after filter = [2, 4, 4, 2, 8, 10]
# List after map = [4, 16, 16, 4, 64, 100]
# Output of reduce = 204


from functools import reduce

CheckEven = lambda No : No % 2 == 0

Square = lambda No : No * No

Addition = lambda No1, No2 : No1 + No2


def main():

    Value = int(input("Enter List Size : "))

    Data = []

    for i in range(Value):

        num = int(input(f"Enter Number {i+1} : "))

        Data.append(num)

    print("Input List = ",Data)

    FData = list(filter(CheckEven, Data))
    print("List after filter = ",FData)

    MData = list(map(Square, FData))
    print("List after map = ",MData)

    RData = reduce(Addition, MData)
    print("Output of reduce = ",RData)


if __name__ == "__main__":
    main()