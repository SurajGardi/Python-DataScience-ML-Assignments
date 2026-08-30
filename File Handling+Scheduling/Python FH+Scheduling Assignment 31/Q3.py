"""

3: Write a program that scans a specified directory every minute.
The task should display:
• Directory name
• Number of files
• Number of subdirectories
• Date and time of scanning
Use the os module.
Example output:
Directory Scanned: E:/Data
Total Files: 15
Total Subdirectories: 4
Scan Time: 25-07-2026 04:30:00 PM

"""

import schedule
import time
import datetime
import os
import sys


def Display(DirectoryPath):

    CurrentTime = datetime.datetime.now()

    FileCount = 0
    SubDirectoryCount = 0

    for FolderName, SubFolder, FileName in os.walk(DirectoryPath):
        for file in FileName:
            FileCount += 1

        for folder in SubFolder:
            SubDirectoryCount += 1

    print("Directory Scanned :", DirectoryPath)
    print("Total Files :", FileCount)
    print("Total Subdirectories :", SubDirectoryCount)
    print("Scan Time :",
          CurrentTime.strftime("%d-%m-%Y %I:%M:%S %p"))

    print("-----------------------------")


def main():

    schedule.every(3).seconds.do(Display,sys.argv[1])

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()