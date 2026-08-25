"""
4. Write a program that calculates
1^5+2^5+3^5+.....+N^5
for multiple values of N simultaneously using Pool.
Input

[1000000,
2000000,
3000000,
4000000]
Measure total execution time.

"""
import multiprocessing
import time

def Calculate(No):

    Sum = 0

    for i in range(1, No + 1):
        Sum = Sum + i ** 5        

    return No, Sum        # returns a tuple


def main():

    Data = [1000000,2000000,3000000,4000000]

    Result = []

    pobj = multiprocessing.Pool()

    Start_time = time.perf_counter()

    Result = pobj.map(Calculate, Data)

    pobj.close()
    pobj.join()

    End_time = time.perf_counter()

    for No, Sum in Result:
        
        print("Input Number :", No)
        print("Sum of Fifth Powers :", Sum)
        print("--------------------")

    print(f"Time required is : {End_time - Start_time:.4f} seconds")


if __name__ == "__main__":
    main()