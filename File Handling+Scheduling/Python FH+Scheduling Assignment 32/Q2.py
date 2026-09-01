"""

2: Write a Python program that monitors the size of a specified file
every 30 seconds.
Write the following details into:
FileSizeLog.txt
• File path
• File size in bytes
• Date and time
Handle the situation where the file does not exist.

"""

import schedule
import time
import datetime
import os

def MonitorFileSize(FilePath):
    timeStamp = datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

    Ret = os.path.exists(FilePath)

    fobj = open("Q2_FileSizeLog.txt","a")

    if(Ret == False):
        fobj.write("File Path: "+FilePath+" -- File Does Not Exist\n")
        fobj.write("Date and Time: "+timeStamp+"\n\n")
        print("File",FilePath,"Does Not Exist")
    else:
        FileSize = os.path.getsize(FilePath)
        fobj.write("File Path: "+FilePath+"\n")
        fobj.write("File Size: "+str(FileSize)+" bytes\n")
        fobj.write("Date and Time: "+timeStamp+"\n\n")
        print("File Path :",FilePath,"File Size :",FileSize,"bytes")

    fobj.close()

def main():
    FilePath = input("Enter File Path : ")

    print("Automation Script Started")

    schedule.every(30).seconds.do(MonitorFileSize,FilePath)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()