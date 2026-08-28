"""

2: Create a function named:
DisplayMessage(message)
Schedule the function using:
schedule.every(5).seconds.do(DisplayMessage, message)
The message should be accepted from the user.

"""

import schedule
import time

def DisplayMessage(message):
    print(message)


def main():

    message = input("Enter Message : ")

    schedule.every(5).seconds.do(DisplayMessage, message)

    while True:

        schedule.run_pending()

        time.sleep(1)


if __name__ == "__main__":
    main()