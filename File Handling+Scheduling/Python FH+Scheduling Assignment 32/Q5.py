"""
5: Write a program that deletes all empty files from a specified
directory every hour.

The program should:
• Scan the directory recursively
• Detect files whose size is zero bytes
• Delete the empty files
• Store deleted file paths in a log file
• Handle permission errors
• Test the program only on a sample directory
"""

import os
import schedule
import time
import datetime


def DeleteEmptyFiles(DirectoryPath):

    CurrentTime = datetime.datetime.now()

    LogFile = open("Q5_DeleteLog.txt", "a")

    for FolderName, SubFolder, FileName in os.walk(DirectoryPath):

        for fname in FileName:

            FilePath = os.path.join(FolderName, fname)

            try:

                if os.path.getsize(FilePath) == 0:

                    os.remove(FilePath)

                    LogFile.write(
                        f"Deleted File : {FilePath}\n"
                    )

                    LogFile.write(
                        f"Deleted At : {CurrentTime.strftime('%d-%m-%Y %I:%M:%S %p')}\n"
                    )

                    LogFile.write("-----------------------------\n")

                    print("Deleted Empty File :", FilePath)

            except PermissionError:

                print("Permission Denied :", FilePath)

            except OSError as eobj:

                print("Unable to Delete :", FilePath)
                print("Error :", eobj)

    LogFile.close()


def main():

    DirectoryPath = input("Enter Directory Path : ")

    if not os.path.isdir(DirectoryPath):

        print("Directory does not exist.")

        return

    print("Automation Script Started...")

    # DeleteEmptyFiles(DirectoryPath)

    schedule.every(1).hours.do(
        DeleteEmptyFiles,
        DirectoryPath
    )

    while True:

        schedule.run_pending()

        time.sleep(1)


if __name__ == "__main__":

    main()