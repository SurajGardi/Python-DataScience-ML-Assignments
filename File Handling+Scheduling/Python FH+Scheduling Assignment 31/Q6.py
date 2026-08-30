"""

6: Write a program that schedules the following messages:
• Monday at 9:00 AM: Start your weekly goals
• Wednesday at 5:00 PM: Review your weekly progress
• Friday at 6:00 PM: Weekly work completed
Use:
schedule.every().monday.at(...)
schedule.every().wednesday.at(...)
schedule.every().friday.at(...)

"""

import schedule
import time


def MondayMessage():
    print("Start your weekly goals")

def WednesdayMessage():
    print("Review your weekly progress")

def FridayMessage():
    print("Weekly work completed")
    

def main():

    schedule.every().monday.at("09:00").do(MondayMessage)
    schedule.every().wednesday.at("17:00").do(WednesdayMessage)
    schedule.every().friday.at("18:00").do(FridayMessage)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()