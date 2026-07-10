# 4. Write a lambda function using reduce() which accepts a list of numbers and returns the addition of all elements.

from functools import reduce

Addition = lambda No1, No2 : No1 + No2

def main():
    Data = [10, 20, 30, 10 , 20, 30]

    RData = reduce(Addition, Data)

    print("Addition After reduce : ",RData)

if __name__ == "__main__":
    main()