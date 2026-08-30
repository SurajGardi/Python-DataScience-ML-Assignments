"""

1: Write a program that accepts:
• A message from the user
• A time interval in seconds
Schedule the program to display the message repeatedly after the specified interval.
Example input:
Enter message: Jay Ganesh
Enter interval in seconds: 5
Expected output:
Jay Ganesh
every five seconds.

Validate that the interval is greater than zero.

"""

import schedule
import time

def main():

    message = input("Enter Message : ")
    interval = int(input("Enter interval in seconds : "))

    if interval <= 0:
        print("Interval must be greater than zero")
        return

    schedule.every(interval).seconds.do(lambda: print(message))

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()