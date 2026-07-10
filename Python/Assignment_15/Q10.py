# 10.Write a lambda function using filter() which accepts a list of numbers and returns the count of even numbers.

CheckCountEven = lambda No : (No % 2 == 0) 

def main():
    Data = [1, 4, 5, 6 , 2, 7, 8]

    FData = list(filter(CheckCountEven, Data))

    # Count = len(list(filter(CheckCountEven, Data)))
    # print("Count of Even Numbers :", Count)

    print("Count of Even Numbers : ",len(FData))

if __name__ == "__main__":
    main()