"""

7: Write a Python program that performs a file backup every hour.
The program should:
1. Accept the source file path.
2. Accept the destination directory path.
3. Copy the source file to the destination directory.
4. Add the current date and time to the backup filename.
5. Write the backup operation details into:
backup_log.txt
Example backup filename:
Data_25_07_2026_16_30_00.txt
Example log entry:
Backup completed successfully at 25-07-2026 04:30:00 PM
Use the shutil module for file copying.

"""

import schedule
import time
import os
import shutil
from pathlib import Path
import datetime


def FileBackup(src_path, dest_path):

    BackupDir = Path(dest_path)

    if not BackupDir.exists():
        BackupDir.mkdir()

    for Foldername, Subfolder, Filename in os.walk(src_path):

        for fname in Filename:

            SourceFile = os.path.join(Foldername, fname)

            CurrentTime = datetime.datetime.now()

            Name, Extension = os.path.splitext(fname)

            TimeStamp = CurrentTime.strftime("%d_%m_%Y_%H_%M_%S")

            BackupFile = Name + "_" + TimeStamp + Extension

            DestinationFile = os.path.join(dest_path, BackupFile)

            shutil.copy(SourceFile, DestinationFile)

            FormatedTime = CurrentTime.strftime("%d-%m-%Y %I:%M:%S %p")

            fobj = open("backup_log.txt", "a")

            fobj.write(
                f"Backup completed successfully at {FormatedTime}\n"
            )

            fobj.close()

            print(f"{fname} backed up successfully.")

def main():

    print("Automation Script Started...")

    src_path = input("Enter Source Directory : ")
    dest_path = input("Enter Destination Directory : ")

    FileBackup(src_path, dest_path)

    # For testing
    # schedule.every(1).minutes.do(FileBackup, src_path, dest_path)

    # For final submission:
    schedule.every(1).hour.do(FileBackup, src_path, dest_path)

    while True:

        schedule.run_pending()

        time.sleep(1)


if __name__ == "__main__":
    main()