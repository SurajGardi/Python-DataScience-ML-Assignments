# 1: Design a Python application that creates two separate threads named Even and Odd.
# • The Even thread should display the first 10 even numbers.
# • The Odd thread should display the first 10 odd numbers.
# • Both threads should execute independently using the threading module.
# • Ensure proper thread creation and execution.


import threading

def DisplayEven(No):
    print(threading.current_thread().name)
    for i in range(2, No * 2 + 1, 2):
        print(i)


def DisplayOdd(No):
    print(threading.current_thread().name)
    for i in range(1, No * 2, 2):
        print(i)

def main():

    tobj1 = threading.Thread(name="Even", target=DisplayEven, args=(10,))
    tobj2 = threading.Thread(name="Odd", target=DisplayOdd, args=(10,))

    tobj1.start()
    tobj2.join()

    tobj2.start()
    tobj2.join()

if __name__ == "__main__":
    main()