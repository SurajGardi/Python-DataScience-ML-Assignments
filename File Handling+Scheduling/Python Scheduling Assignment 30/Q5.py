"""

5: Schedule a task that executes every five minutes.
The task should write the current date and time into a file named:
Marvellous.txt
New entries should be appended without removing previous entries.
Example file contents:
Task executed at: 25-07-2026 04:30:00 PM
Task executed at: 25-07-2026 04:35:00 PM

"""

import schedule
import time
import datetime

def Display():

    fobj = open("Marvellous.txt", "a")

    CurrentTime = datetime.datetime.now()

    FormatedTime = CurrentTime.strftime("%d-%m-%Y %I:%M:%S %p")

    fobj.write(f"Task executed at: " + FormatedTime + "\n")       # write() only takes one string argument using + and fstring.
    # fobj.write(f"Task executed at: {FormatedTime}\n")       # write() only takes one string argument using + and fstring.

    fobj.close()


def main():

    schedule.every(5).minutes.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()