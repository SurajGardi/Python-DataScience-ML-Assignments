"""
5: Write a program that calculates factorials of multiple numbers
simultaneously using multiprocessing.Pool.
Input

Data = [10, 15, 20, 25]
Expected Task
For every N, calculate:

N!
Expected Output Format
Process ID : 1240
Input Number : 20
Factorial : 2432902008176640000

"""

import multiprocessing
import os

def Factorial(No):

    PID = os.getpid()

    Fact = 1

    for i in range(1, No + 1):
        Fact = Fact * i

    return PID, No, Fact        # returns a tuple


def main():
    Data = [10,15,20,25]

    Result = []

    pobj = multiprocessing.Pool()

    Result = pobj.map(Factorial, Data)

    pobj.close()
    pobj.join()

    for PID, No, Fact in Result:
        print("Process ID :", PID)
        print("Input Number :", No)
        print("Factorial :", Fact)
        print("--------------------")

if __name__ == "__main__":
    main()