# 6. Write a lambda function using reduce() which accepts a list of numbers and returns the Minimum element.

from functools import reduce

Minimum = lambda No1, No2 : No1 if  No1 < No2 else No2 

def main():
    Data = [50, 20, 30, 40, 10 , 20, 30]

    RData = reduce(Minimum, Data)

    print("Minimum After reduce : ",RData)

if __name__ == "__main__":
    main()