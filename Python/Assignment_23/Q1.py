"""
1: Write a Python program using multiprocessing.Pool to calculate the
sum of all even numbers from 1 to N for every number from the given
list.
Input
Data = [1000000, 2000000, 3000000, 4000000]

Expected Task
For each number N, calculate:
2 + 4 + 6 + ... + N

Expected Output Format:
Process ID : 1234
Input Number : 1000000
Sum of Even Numbers : 250000500000

"""

import multiprocessing
import os

def SumEven(No):

    PID = os.getpid()

    Sum = 0

    # for i in range(1, No + 1):
    #     if i % 2 == 0:
    #         Sum = Sum + i

    for i in range(2, No + 1, 2):
        Sum = Sum + i

    return PID, No, Sum


def main():
    Data = [1000000,2000000,3000000,4000000]

    Result = []

    pobj = multiprocessing.Pool()

    Result = pobj.map(SumEven, Data)

    pobj.close()
    pobj.join()

    for PID, No, Sum in Result:
        print("Process ID : ",PID)
        print("Input Number : ",No)
        print("Sum of Even Numbers : ",Sum)  
        print("---------------------------")      

if __name__ == "__main__":
    main()