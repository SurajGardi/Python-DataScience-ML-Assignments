# 5. Write a lambda function using reduce() which accepts a list of numbers and returns the maximum element.

from functools import reduce

Maximum = lambda No1, No2 : No1 if  No1 > No2 else No2 

def main():
    Data = [10, 20, 30, 40, 10 , 20, 30]

    RData = reduce(Maximum, Data)

    print("Maximum After reduce : ",RData)

if __name__ == "__main__":
    main()