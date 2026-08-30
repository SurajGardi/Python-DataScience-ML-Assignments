"""

4: Write a program that creates a new log file after every ten minutes.
The filename should contain the current date and time.
Example:
MarvellousLog_25_07_2026_16_30_00.txt
The file should contain:
Log file created successfully.
Creation Time: 25-07-2026 04:30:00 PM

"""

import schedule
import time
import datetime


def Display():

    CurrentTime = datetime.datetime.now()

    FormatedTime = CurrentTime.strftime("%d-%m-%Y %I:%M:%S %p")

    timestamp = CurrentTime.strftime("_%d_%m_%Y_%H_%M_%S")

    LogFileName = "MarvellousLog%s.txt"%timestamp

    fobj = open(LogFileName,"w")

    fobj.write("Log file created successfully.\n")
    fobj.write("Creation Time : "+FormatedTime)

    fobj.close()


def main():

    schedule.every(10).seconds.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()