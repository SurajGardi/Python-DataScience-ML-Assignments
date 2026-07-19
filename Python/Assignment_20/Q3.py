# 3: Design a Python application that creates two threads named EvenList and OddList.
# • Both threads should accept a list of integers as input.
# • The EvenList thread should:
# ◦ Extract all even elements from the list.
# ◦ Calculate and display their sum.
# • The OddList thread should:
# ◦ Extract all odd elements from the list.
# ◦ Calculate and display their sum.
# • Threads should run concurrently.

import threading

def EvenList(No):
    SumEven = 0

    for i in No:
        if i % 2 == 0:   
            SumEven += i

    print("Sum of Even Elements :", SumEven)

def OddList(No):
    SumOdd = 0

    for i in No:
        if i % 2 != 0:
            SumOdd += i

    print("Sum of Odd Elements :", SumOdd)


def main():

    Value = int(input("Enter List Size : "))

    Data = []

    for i in range(Value):

        num = int(input(f"Enter Number {i+1} : "))

        Data.append(num)

    print("Input List = ",Data)

    tobj1 = threading.Thread(name="EvenList", target=EvenList, args=(Data,))
    tobj2 = threading.Thread(name="OddList", target=OddList, args=(Data,))

    tobj1.start()
    tobj2.start()

    tobj1.join()
    tobj2.join()


if __name__ == "__main__":
    main()