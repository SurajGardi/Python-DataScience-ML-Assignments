"""
2: Write a Python program using multiprocessing.Pool to calculate the
sum of all odd numbers from 1 to N.
Input
Data = [1000000, 2000000, 3000000, 4000000]
Expected Task
For each number N, calculate:

1 + 3 + 5 + ... + N
Expected Output Format

Process ID : 1235
Input Number : 1000000
Sum of Odd Numbers : 250000000000

"""

import multiprocessing
import os

def SumOdd(No):

    PID = os.getpid()

    Sum = 0

    # for i in range(1, No + 1):
    #     if i % 2 != 0:
    #         Sum = Sum + i

    for i in range(1, No + 1, 2):
        Sum = Sum + i

    return PID, No, Sum


def main():
    Data = [1000000,2000000,3000000,4000000]

    Result = []

    pobj = multiprocessing.Pool()

    Result = pobj.map(SumOdd, Data)

    pobj.close()
    pobj.join()

    for PID, No, Sum in Result:
        print("Process ID : ",PID)
        print("Input Number : ",No)
        print("Sum of Odd Numbers : ",Sum)  
        print("---------------------------")      

if __name__ == "__main__":
    main()