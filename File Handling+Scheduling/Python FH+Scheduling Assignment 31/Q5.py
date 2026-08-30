"""

5:Write a program that accepts a directory name from the user and
counts the number of files inside it every five minutes.
Write the result into:
DirectoryCountLog.txt
Each entry should contain:
• Directory path
• Number of files
• Date and time

"""

import schedule
import time
import datetime
import os


def Display(DirectoryPath):

    CurrentDate = datetime.datetime.now()

    TotalFileCount = 0

    for FolderName, SubFolder, FileName in os.walk(DirectoryPath):

        for file in FileName:
            TotalFileCount += 1

    LogFileName = "DirectoryCountLog.txt"

    fobj = open(LogFileName, "a")

    fobj.write("Directory Path : " + DirectoryPath + "\n")
    fobj.write(f"Number of Files : {TotalFileCount}\n")
    fobj.write(
        f"Date and Time : {CurrentDate.strftime('%d-%m-%Y %I:%M:%S %p')}\n"
    )
    fobj.write("-----------------------------\n")

    fobj.close()


def main():
    print("Automation Script Started...")

    DirectoryName = input("Enter Directory Name : ")

    schedule.every(10).seconds.do(Display, DirectoryName)

    while True:

        schedule.run_pending()

        time.sleep(1)


if __name__ == "__main__":
    main()