"""
3: Write a program that counts how many even numbers exist
between 1 and N using Pool.map().
Input
Data = [1000000, 2000000, 3000000, 4000000]
Expected Output Format
Process ID : 1236
Input Number : 1000000

"""
import multiprocessing
import os

def CountEven(No):

    PID = os.getpid()

    Count = 0

    # for i in range(1, No + 1):
    #     if i % 2 == 0:
    #         Count = Count + 1

    for i in range(2, No + 1, 2):
        Count = Count + 1

    return PID, No, Count


def main():
    Data = [1000000,2000000,3000000,4000000]

    Result = []

    pobj = multiprocessing.Pool()

    Result = pobj.map(CountEven, Data)

    pobj.close()
    pobj.join()

    for PID, No, Count in Result:
        print("Process ID : ",PID)
        print("Input Number : ",No)
        print("Count of Even Numbers : ",Count)  
        print("---------------------------")      

if __name__ == "__main__":
    main()