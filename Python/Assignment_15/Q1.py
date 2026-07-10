# 1. Write a lambda function using map() which accepts a list of numbers and returns a list of squares of each number.

Square = lambda No : No * No


def main():
    Data = [10, 20, 30, 40]

    print("Data is : ",Data)

    MData = list(map(Square, Data))

    print("Data After Map : ",MData)

if __name__ == "__main__":
    main()