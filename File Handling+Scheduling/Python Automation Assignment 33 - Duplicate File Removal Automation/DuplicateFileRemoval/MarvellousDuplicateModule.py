import os
import hashlib
import datetime
import smtplib

from email.message import EmailMessage


def CreateLogDirectory():
    DirectoryName = "Marvellous"

    try:
        if not os.path.exists(DirectoryName):
            os.mkdir(DirectoryName)

        return DirectoryName

    except Exception as E:
        return None
 

def CreateLogFile(LogDirectory):
    CurrentTime = datetime.datetime.now()

    FileName = "DuplicateRemovalLog_" + CurrentTime.strftime("%d_%m_%Y_%H_%M_%S") + ".log"

    FilePath = os.path.join(LogDirectory, FileName)

    try:
        File = open(FilePath, "w")
        File.close()

        return FilePath

    except Exception:
        return None


def WriteLog(FilePath, Message):
    try:
        File = open(FilePath, "a")
        File.write(Message + "\n")
        File.close()

    except Exception:
        pass


def CheckSum(FilePath):
    try:
        if not os.path.exists(FilePath):
            return None

        if not os.path.isfile(FilePath):
            return None

        if not os.access(FilePath, os.R_OK):
            return None

        Hash = hashlib.md5()

        File = open(FilePath, "rb")

        Data = File.read(4096)

        while Data:
            Hash.update(Data)
            Data = File.read(4096)

        File.close()

        return Hash.hexdigest()

    except Exception:
        return None


def FindDuplicateFiles(DirectoryPath, LogFile):
    FileDictionary = {}

    TotalFiles = 0

    try:
        for FolderName, SubFolders, FileNames in os.walk(DirectoryPath):

            for FileName in FileNames:

                FilePath = os.path.join(FolderName, FileName)

                TotalFiles = TotalFiles + 1

                try:
                    Checksum = CheckSum(FilePath)

                    if Checksum is None:
                        WriteLog(LogFile, "Unable to calculate checksum : " + FilePath)
                        continue

                    if Checksum not in FileDictionary:
                        FileDictionary[Checksum] = []

                    FileDictionary[Checksum].append(FilePath)

                except Exception as E:
                    WriteLog(LogFile, "Error while processing : " + FilePath)
                    WriteLog(LogFile, "Error : " + str(E))

        return FileDictionary, TotalFiles

    except Exception as E:
        WriteLog(LogFile, "Error while scanning directory : " + str(E))

        return FileDictionary, TotalFiles


def DeleteDuplicateFiles(FileDictionary, LogFile):
    DuplicateFound = 0
    DuplicateDeleted = 0

    try:

        for Checksum, FileList in FileDictionary.items():

            if len(FileList) > 1:

                # First file will be preserved
                OriginalFile = FileList[0]

                WriteLog(LogFile, "Original File : " + OriginalFile)
                WriteLog(LogFile, "Checksum : " + Checksum)

                for FilePath in FileList[1:]:

                    DuplicateFound = DuplicateFound + 1

                    WriteLog(LogFile, "Duplicate File : " + FilePath)
                    WriteLog(LogFile, "Checksum : " + Checksum)

                    try:

                        if not os.path.exists(FilePath):
                            WriteLog(LogFile, "File does not exist : " + FilePath)
                            continue

                        if not os.path.isfile(FilePath):
                            WriteLog(LogFile, "Not a regular file : " + FilePath)
                            continue

                        if not os.access(FilePath, os.R_OK):
                            WriteLog(LogFile, "File is not readable : " + FilePath)
                            continue

                        os.remove(FilePath)

                        DuplicateDeleted = DuplicateDeleted + 1

                        WriteLog(LogFile, "Deleted : " + FilePath)

                    except PermissionError:
                        WriteLog(LogFile, "Permission denied : " + FilePath)

                    except Exception as E:
                        WriteLog(LogFile, "Unable to delete : " + FilePath)
                        WriteLog(LogFile, "Error : " + str(E))

        return DuplicateFound, DuplicateDeleted

    except Exception as E:
        WriteLog(LogFile, "Error while deleting duplicate files : " + str(E))

        return DuplicateFound, DuplicateDeleted


def SendMail(SenderEmail, Password, ReceiverEmail, LogFile, Stats):
    try:

        Message = EmailMessage()

        Message["From"] = SenderEmail
        Message["To"] = ReceiverEmail
        Message["Subject"] = "Duplicate File Removal Report"

        Body = """Jay Ganesh,

The duplicate-file removal operation has been completed successfully.

Operation Statistics:

Starting time of scanning: {0}
Completion time of scanning: {1}
Directory scanned: {2}
Total number of files scanned: {3}
Total number of duplicate files found: {4}
Total number of duplicate files deleted: {5}

Please find the detailed log file attached to this email.

Regards,
Duplicate File Removal Automation System
""".format(
            Stats["StartTime"],
            Stats["CompletionTime"],
            Stats["Directory"],
            Stats["TotalFiles"],
            Stats["DuplicateFound"],
            Stats["DuplicateDeleted"]
        )

        Message.set_content(Body)

        File = open(LogFile, "rb")
        Data = File.read()
        File.close()

        Message.add_attachment(
            Data,
            maintype="application",
            subtype="octet-stream",
            filename=os.path.basename(LogFile)
        )

        Server = smtplib.SMTP("smtp.gmail.com", 587)

        Server.starttls()

        Server.login(SenderEmail, Password)

        Server.send_message(Message)

        Server.quit()

        return True

    except Exception as E:
        WriteLog(LogFile, "Email sending failed : " + str(E))

        return False