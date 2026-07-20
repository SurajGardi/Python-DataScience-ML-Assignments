# 3: Design a Python application where multiple threads update a shared variable.
# • Use a Lock to avoid race conditions.
# • Each thread should increment the shared counter multiple times.
# • Display the final value of the counter after all threads complete execution.

import threading

Counter = 0
lock = threading.Lock()

def Increment(Times):

    global Counter

    for i in range(Times):
        with lock:
            Counter += 1

def main():

    t1 = threading.Thread(target=Increment, args=(1000,))
    t2 = threading.Thread(target=Increment, args=(1000,))
    t3 = threading.Thread(target=Increment, args=(1000,))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("Final Counter Value :", Counter)

if __name__ == "__main__":
    main()