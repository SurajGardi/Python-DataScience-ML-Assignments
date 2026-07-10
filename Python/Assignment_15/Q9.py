# 9. Write a lambda function using reduce() which accepts a list of numbers and returns the product of all elements.

from functools import reduce

ListProduct = lambda No1, No2 : No1 * No2 

def main():
    Data = [1, 4, 5, 0 , 2]

    # Data = list(map(lambda x: 1 if x == 0 else x, Data))      # to ignore 0 replacing it with 1

    RData = reduce(ListProduct, Data)

    print("product of all elements : ",RData)

if __name__ == "__main__":
    main()