"""

6: Write a script that schedules the following tasks:
• Print Lunch Time! every day at 1:00 PM.
• Print Wrap up work every day at 6:00 PM.
Both tasks should be handled by separate functions.

"""


import schedule
import time

def LunchTime():
    print("It's Lunch Time")

def WrapUp():
    print("Heyyy Wrap Up Work - Jitna pagar utni dihadi..")

def main():

    schedule.every().day.at("13:00").do(LunchTime)
    schedule.every().day.at("18:00").do(WrapUp)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()