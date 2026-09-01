"""

3: Write a program that reads and displays the contents of a specified
text file every minute.
Handle the following conditions:
• File does not exist
• File is empty
• Permission is denied
• File cannot be opened

"""

import schedule
import time
import os


def DirectoryScan(DirectoryName, Filename):

    for FolderName, SubFolder, FileName in os.walk(DirectoryName):

        for Fname in FileName:

            if Filename == Fname:

                return os.path.join(FolderName, Fname)

    return None


def DisplayContent(DirectoryName, Filename):

    Fname = DirectoryScan(DirectoryName, Filename)

    if Fname is None:

        print("File does not exist")
        return

    if not os.path.isfile(Fname):

        print("Specified path is not a file")
        return

    try:

        fobj = open(Fname, "r")

        Data = fobj.read()

        if Data == "":
            print("File is empty")
        else:
            print("File Contents :")
            print(Data)

        fobj.close()

    except PermissionError:

        print("Permission denied")

    except OSError:

        print("File cannot be opened")


def main():

    DirectoryName = input("Enter Directory Name : ")
    Filename = input("Enter File Name : ")

    print("Automation Script Started...")

    schedule.every(1).minutes.do(
        DisplayContent,
        DirectoryName,
        Filename
    )

    while True:

        schedule.run_pending()

        time.sleep(1)


if __name__ == "__main__":
    main()