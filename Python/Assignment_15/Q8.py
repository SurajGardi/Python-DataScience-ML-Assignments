# 8. Write a lambda function using filter() which accepts a list of numbers and returns a list of numbers
# divisible by both 3 and 5.


CheckDivisible = lambda No : (No % 3 == 0) or (No % 5 == 0)

def main():
    Data = [15, 4, 5, 6 , 2, 7, 10]

    FData = list(filter(CheckDivisible, Data))

    print("Numbers divisible by both 3 and 5 : ",FData)

if __name__ == "__main__":
    main()