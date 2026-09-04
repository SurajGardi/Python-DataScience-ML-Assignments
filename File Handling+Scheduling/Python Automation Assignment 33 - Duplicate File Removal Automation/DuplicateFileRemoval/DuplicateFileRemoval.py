import sys
import os
import time
import schedule
import datetime
import re

import MarvellousDuplicateModule as MM


SenderEmail = "test@gmail.com"
AppPassword = "xxxx xxxx xxxx xxxx"


def DisplayHelp():
    print("Duplicate File Removal Automation")
    print()
    print("This script scans a directory, identifies duplicate files using")
    print("checksums, deletes duplicate files, creates a detailed log file,")
    print("and sends the log file through email.")
    print()
    print("Usage:")
    print("python DuplicateFileRemoval.py <DirectoryPath> <IntervalInMinutes> <ReceiverEmail>")
    print()
    print("Example:")
    print("python DuplicateFileRemoval.py E:/Data/Demo 50 marvellousinfosystem@gmail.com")


def DisplayUsage():
    print("Usage:")
    print("python DuplicateFileRemoval.py <AbsoluteDirectoryPath> <TimeIntervalInMinutes> <ReceiverEmailAddress>")


def ValidateDirectory(DirectoryPath):
    if DirectoryPath == "":
        return False

    if not os.path.isabs(DirectoryPath):
        return False

    if not os.path.exists(DirectoryPath):
        return False

    if not os.path.isdir(DirectoryPath):
        return False

    if not os.access(DirectoryPath, os.R_OK):
        return False

    return True


def ValidateInterval(Interval):
    try:
        Value = float(Interval)

        if Value <= 0:
            return False

        return True

    except ValueError:
        return False


def ValidateEmail(Email):
    Pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

    if re.match(Pattern, Email):
        return True

    return False


def PerformDuplicateRemoval(DirectoryPath, ReceiverEmail):

    LogDirectory = MM.CreateLogDirectory()

    if LogDirectory is None:
        return

    LogFile = MM.CreateLogFile(LogDirectory)

    if LogFile is None:
        return

    StartTime = datetime.datetime.now()

    MM.WriteLog(LogFile, "========== Duplicate File Removal ==========")
    MM.WriteLog(LogFile, "Starting time of directory scanning : " + str(StartTime))
    MM.WriteLog(LogFile, "Directory scanned : " + DirectoryPath)
    MM.WriteLog(LogFile, "")

    try:

        FileDictionary, TotalFiles = MM.FindDuplicateFiles(
            DirectoryPath,
            LogFile
        )

        DuplicateFound, DuplicateDeleted = MM.DeleteDuplicateFiles(
            FileDictionary,
            LogFile
        )

        CompletionTime = datetime.datetime.now()

        Stats = {
            "StartTime": StartTime,
            "CompletionTime": CompletionTime,
            "Directory": DirectoryPath,
            "TotalFiles": TotalFiles,
            "DuplicateFound": DuplicateFound,
            "DuplicateDeleted": DuplicateDeleted
        }

        MM.WriteLog(LogFile, "")
        MM.WriteLog(LogFile, "========== Operation Statistics ==========")
        MM.WriteLog(LogFile, "Starting time : " + str(StartTime))
        MM.WriteLog(LogFile, "Completion time : " + str(CompletionTime))
        MM.WriteLog(LogFile, "Directory scanned : " + DirectoryPath)
        MM.WriteLog(LogFile, "Total number of files scanned : " + str(TotalFiles))
        MM.WriteLog(LogFile, "Total number of duplicate files found : " + str(DuplicateFound))
        MM.WriteLog(LogFile, "Total number of duplicate files deleted : " + str(DuplicateDeleted))

        MM.WriteLog(LogFile, "")
        MM.WriteLog(LogFile, "Sending email...")

        EmailStatus = MM.SendMail(
            SenderEmail,
            AppPassword,
            ReceiverEmail,
            LogFile,
            Stats
        )

        if EmailStatus:
            MM.WriteLog(LogFile, "Email delivery status : Successfully sent")
        else:
            MM.WriteLog(LogFile, "Email delivery status : Failed")

        MM.WriteLog(LogFile, "")
        MM.WriteLog(LogFile, "Operation completed successfully.")
        MM.WriteLog(LogFile, "============================================")

    except Exception as E:

        MM.WriteLog(LogFile, "Unexpected error : " + str(E))


def main():

    if len(sys.argv) == 2:

        if sys.argv[1] == "--help" or sys.argv[1] == "-h":
            DisplayHelp()
            return

        if sys.argv[1] == "--usage" or sys.argv[1] == "-u":
            DisplayUsage()
            return

    if len(sys.argv) != 4:
        print("Invalid number of command-line arguments.")
        print("Use --help or -h for help.")
        return

    DirectoryPath = sys.argv[1]
    Interval = sys.argv[2]
    ReceiverEmail = sys.argv[3]

    if not ValidateDirectory(DirectoryPath):
        print("Invalid directory path.")
        return

    if not ValidateInterval(Interval):
        print("Invalid time interval.")
        return

    if not ValidateEmail(ReceiverEmail):
        print("Invalid email address.")
        return

    Interval = float(Interval)

    # First execution
    PerformDuplicateRemoval(
        DirectoryPath,
        ReceiverEmail
    )

    # Repeated execution
    schedule.every(Interval).minutes.do(
        PerformDuplicateRemoval,
        DirectoryPath,
        ReceiverEmail
    )

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()