"""

1: Write a program that creates a new text file every minute.
The filename should contain the current timestamp.
Example:
File_25_07_2026_16_30_00.txt
Write the following information into the file:
• Filename
• Creation date
• Creation time

"""

import schedule
import time
import datetime

def Display():

    CurrentDateTime = datetime.datetime.now()
    FormatedTime = CurrentDateTime.strftime('%d_%m_%Y_%H_%M_%S')

    CurrentDate = CurrentDateTime.strftime('%d-%m-%Y')
    CurrentTime = CurrentDateTime.strftime('%I:%M:%S %p')

    FileName = "Q1_File_%s.txt"%FormatedTime

    fobj = open(FileName, "w")

    fobj.write(f"File Name : {FileName} \n")
    fobj.write(f"Creation Date : {CurrentDate} \n")
    fobj.write(f"Creation Time : {CurrentTime} \n")
    
    fobj.close()

def main():

    schedule.every(1).minutes.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()