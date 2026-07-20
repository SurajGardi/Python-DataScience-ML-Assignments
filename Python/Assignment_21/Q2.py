# 2: Design a Python application that creates two threads.
# • Thread 1 should calculate and display the maximum element from an list.
# • Thread 2 should calculate and display the minimum element from the same list.
# • The list should be accepted from the user.

from functools import reduce
import threading

Maximum = lambda No1, No2: No1 if No1 > No2 else No2
Minimum = lambda No1, No2: No1 if No1 < No2 else No2


def DisplayMaximum(Data):

    Max = reduce(Maximum, Data)
    print("Maximum Element :", Max)


def DisplayMinimum(Data):

    Min = reduce(Minimum, Data)
    print("Minimum Element :", Min)


def main():

    Value = int(input("Enter List Size : "))

    Data = []

    for i in range(Value):
        num = int(input(f"Enter Number {i+1} : "))
        Data.append(num)

    print("Input List :", Data)

    tobj1 = threading.Thread(name="Maximum", target=DisplayMaximum, args=(Data,))
    tobj2 = threading.Thread(name="Minimum", target=DisplayMinimum, args=(Data,))

    tobj1.start()
    tobj2.start()

    tobj1.join()
    tobj2.join()

    print("Exit from main")


if __name__ == "__main__":
    main()