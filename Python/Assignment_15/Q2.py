# 2. Write a lambda function using filter() which accepts a list of numbers and returns a list of even numbers.

CheckEven = lambda No : (No % 2 == 0)

def main():
    Data = [1, 4, 5, 6 , 2, 7, 8]

    FData = list(filter(CheckEven, Data))

    print("Even Data After Filter : ",FData)

if __name__ == "__main__":
    main()