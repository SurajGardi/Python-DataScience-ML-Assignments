"""
1. Write a program that accepts a list of integers and uses Pool.map()
to calculate the sum of squares from 1 to N for every element in the
list.
Example Input
[1000000,2000000,3000000,4000000]
Expected Output
[333333833333500000,
2666668666667000000,
...
]
"""

import multiprocessing

def SumSquare(No):

    Sum = 0

    for i in range(1, No + 1):
        Sum = Sum + (i * i)

    return Sum


def main():
    Data = [1000000,2000000,3000000,4000000]

    Result = []

    pobj = multiprocessing.Pool()

    Result = pobj.map(SumSquare, Data)

    pobj.close()
    pobj.join()

    print("Result is : ")
    print(Result)


if __name__ == "__main__":
    main()