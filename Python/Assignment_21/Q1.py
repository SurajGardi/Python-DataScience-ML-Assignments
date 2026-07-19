# 1: Design a Python application that creates two threads named Prime and NonPrime.
# • Both threads should accept a list of integers.
# • The Prime thread should display all prime numbers from the list.
# • The NonPrime thread should display all non-prime numbers from the list.

import threading

def ChkPrime(No):

    if No <= 1:
        return False

    for i in range(2, No // 2 + 1):
        if No % i == 0:
            return False

    return True


def DisplayPrime(Data):

    print("Prime Numbers are : ", end=" ")

    for i in Data:
        if ChkPrime(i):
            print(i, end=" ")

    print()


def DisplayNonPrime(Data):

    print("Non-Prime Numbers are : ", end=" ")

    for i in Data:
        if not ChkPrime(i):
            print(i, end=" ")

    print()


def main():

    Value = int(input("Enter List Size : "))

    Data = []

    for i in range(Value):
        num = int(input(f"Enter Number {i+1} : "))
        Data.append(num)

    print("Input List =", Data)

    tobj1 = threading.Thread(name="Prime", target=DisplayPrime, args=(Data,))
    tobj2 = threading.Thread(name="NonPrime", target=DisplayNonPrime, args=(Data,))

    tobj1.start()
    tobj2.start()

    tobj1.join()
    tobj2.join()


if __name__ == "__main__":
    main()