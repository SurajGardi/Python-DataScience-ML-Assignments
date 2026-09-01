"""

4: Write a program that copies all .txt files from one directory to
another every ten minutes.
The program should:
• Accept source and destination directories
• Validate both directories
• Copy only .txt files
• Maintain a log of copied files
• Avoid terminating if one file cannot be copied

"""

import os
import schedule
import time
import shutil


def CopyTextFiles(SourcePath, DestinationPath):

    if not os.path.isdir(SourcePath):
        print("Marvellous Automation Error : Source Directory Does Not Exist")
        return

    if not os.path.isdir(DestinationPath):
        print("Marvellous Automation Error : Destination Directory Does Not Exist")
        return

    if os.path.abspath(SourcePath) == os.path.abspath(DestinationPath):
        print("Source and Destination directories cannot be same.")
        return

    fobj = open("Q4_CopyLog.txt", "a")

    for FolderName, SubFolder, FileName in os.walk(SourcePath):

        for fname in FileName:

            if fname.endswith(".txt"):

                try:

                    SourceFile = os.path.join(FolderName, fname)

                    DestinationFile = os.path.join(DestinationPath, fname)

                    shutil.copy(SourceFile, DestinationFile)

                    fobj.write(
                        "Copied File : " + SourceFile + "\n"
                    )

                    print("File", fname, "Gets Copied")

                except Exception as eobj:

                    fobj.write(
                        "Failed To Copy File : "
                        + fname
                        + " -- "
                        + str(eobj)
                        + "\n"
                    )

                    print(
                        "Failed To Copy File",
                        fname,
                        eobj
                    )

    fobj.close()


def main():

    SourcePath = input("Enter Source Directory Path : ")

    DestinationPath = input("Enter Destination Directory Path : ")

    print("Automation Script Started")

    schedule.every(10).seconds.do(
        CopyTextFiles,
        SourcePath,
        DestinationPath
    )


    while True:

        schedule.run_pending()

        time.sleep(1)


if __name__ == "__main__":

    main()