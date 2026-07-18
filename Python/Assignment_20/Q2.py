# 2: Design a Python application that creates two threads named EvenFactor and OddFactor.
# • Both threads should accept one integer number as a parameter.
# • The EvenFactor thread should:
# ◦ Identify all even factors of the given number.
# ◦ Calculate and display the sum of even factors.
# • The OddFactor thread should:
# ◦ Identify all odd factors of the given number.
# ◦ Calculate and display the sum of odd factors.
# • After both threads complete execution, the main thread should display the message:
# “Exit from main”

# Input : 12 Output : 16 (1+2+3+4+6+12)


import threading

def EvenFactor(No):
    # print(threading.current_thread().name)
    Total = 0

    for i in range(1, No + 1):
        if No % i == 0 and i % 2 == 0:
            # print(i)
            Total += i

    print("Sum of Even Factors :", Total)



def OddFactor(No):
    # print(threading.current_thread().name)
    Total = 0

    for i in range(1, No + 1):
        if No % i == 0 and i % 2 != 0:
            # print(i)
            Total += i

    print("Sum of Odd Factors :", Total)


def main():

    tobj1 = threading.Thread(name="EvenFactor", target=EvenFactor, args=(12,))
    tobj2 = threading.Thread(name="OddFactor", target=OddFactor, args=(12,))

    tobj1.start()
    tobj2.start()

    tobj1.join()
    tobj2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()