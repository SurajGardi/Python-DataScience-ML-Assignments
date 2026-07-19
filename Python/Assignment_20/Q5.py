# 5: Design a Python application that creates two threads named Thread1 and Thread2.
# • Thread1 should display numbers from 1 to 50.
# • Thread2 should display numbers from 50 to 1 in reverse order.
# • Ensure that:
# ◦ Thread2 starts execution only after Thread1 has completed.
# • Use appropriate thread synchronizatio

import threading

def DisplayForward():
    print(threading.current_thread().name)
    for i in range(1, 51):
        print(i, end= " ")
    print()

def DisplayReverse():
    print(threading.current_thread().name)
    for i in range(50, 0, -1):
        print(i, end=" ")
    print()

def main():

    tobj1 = threading.Thread(name="Thread1", target=DisplayForward)
    tobj2 = threading.Thread(name="Thread2", target=DisplayReverse)

    tobj1.start()
    tobj1.join()          # Wait until Thread1 completes

    tobj2.start()
    tobj2.join()          # Wait until Thread2 completes

if __name__ == "__main__":
    main()