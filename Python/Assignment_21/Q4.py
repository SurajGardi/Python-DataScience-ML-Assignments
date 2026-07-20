# 4: Design a Python application that creates two threads.
# • Thread 1 should compute the sum of elements from a list.
# • Thread 2 should compute the product of elements from the same list.
# • Return the results to the main thread and display them.


from functools import reduce
import threading

SumResult = 0
ProductResult = 0

def Addition(No1, No2):
    return No1 + No2

def Multiplication(No1, No2):
    return No1 * No2

def CalculateSum(Data):

    global SumResult

    SumResult = reduce(Addition, Data)

def CalculateProduct(Data):

    global ProductResult

    ProductResult = reduce(Multiplication, Data)

def main():

    Value = int(input("Enter List Size : "))

    Data = []

    for i in range(Value):
        num = int(input(f"Enter Number {i+1} : "))
        Data.append(num)

    print("Input List :", Data)

    tobj1 = threading.Thread(target=CalculateSum, args=(Data,))
    tobj2 = threading.Thread(target=CalculateProduct, args=(Data,))

    tobj1.start()
    tobj2.start()

    tobj1.join()
    tobj2.join()

    print("Sum of Elements :", SumResult)
    print("Product of Elements :", ProductResult)

if __name__ == "__main__":
    main()