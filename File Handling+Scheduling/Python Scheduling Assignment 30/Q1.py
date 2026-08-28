"""

1: Write a Python program that prints:
Jay Ganesh...
every two seconds.
Use:
schedule.every(2).seconds.do(...)
Expected output:
Jay Ganesh...
Jay Ganesh...
Jay Ganesh...

"""

import schedule
import time

def Display():
    print("Jay Ganesh...")

def main():

    schedule.every(2).seconds.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()