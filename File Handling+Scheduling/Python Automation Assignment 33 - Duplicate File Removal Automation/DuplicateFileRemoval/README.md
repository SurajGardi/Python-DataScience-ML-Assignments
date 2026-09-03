# Duplicate File Removal Automation

## 1. Project Title

**Duplicate File Removal Automation Using Python**

---

## 2. Project Description

Duplicate File Removal Automation is a Python-based automation project that periodically scans a specified directory and its subdirectories to identify duplicate files.

The application calculates the checksum of every file using the MD5 hashing algorithm. Files having the same checksum are considered duplicate files.

For every group of duplicate files:

- The first file is preserved.
- All remaining duplicate files are deleted.
- The complete paths of deleted files are recorded in a log file.
- The checksum values are recorded in the log file.
- Operation statistics are recorded.
- The generated log file is sent to the receiver through email.
- The operation is repeated automatically after the specified time interval.

Duplicate detection is performed using file content and checksum values, not only by comparing file names.

---

## 3. Features

The project provides the following features:

- Recursive directory scanning
- Absolute directory path validation
- Checksum-based duplicate file detection
- MD5 checksum generation
- Automatic duplicate-file deletion
- Preservation of the first file from every duplicate group
- Timestamp-based log file generation
- Detailed operation logging
- Periodic execution using a specified time interval
- Email notification after every operation
- Log-file attachment with email
- Email delivery status logging
- Command-line argument support
- Help option
- Usage option
- Input validation
- File validation
- Exception handling
- Modular programming
- Separate user-defined module for project functions

---

## 4. Requirements

### Software Requirements

- Python 3.x
- Windows / Linux / macOS
- Internet connection for sending email

### Python Library Requirements

The project uses the following libraries.

#### Built-in Python Modules

- `os`
- `sys`
- `time`
- `hashlib`
- `datetime`
- `smtplib`
- `email`
- `re`

#### External Library

- `schedule`

Install the external library using:

```bash
pip install schedule
```

---

## 5. Project Structure

The project contains the following files:

```text
DuplicateFileRemoval/
│
├── DuplicateFileRemoval.py
├── MarvellousDuplicateModule.py
├── README.md
│
└── Marvellous/
    └── DuplicateRemovalLog_DD_MM_YYYY_HH_MM_SS.log
```

### DuplicateFileRemoval.py

This is the main Python program.

Responsibilities:

- Read command-line arguments
- Display Help and Usage information
- Validate command-line arguments
- Validate directory path
- Validate time interval
- Validate receiver email address
- Start the duplicate-removal operation
- Schedule repeated execution

### MarvellousDuplicateModule.py

This is the user-defined module containing the main functions used by the project.

Responsibilities:

- Create the `Marvellous` directory
- Create timestamp-based log files
- Write messages into log files
- Calculate file checksums
- Scan directories recursively
- Identify duplicate files
- Delete duplicate files
- Send email reports

### README.md

This file contains project documentation, installation instructions, execution commands, configuration details, and important information about the project.

### Marvellous Directory

The `Marvellous` directory is automatically created by the application if it does not already exist.

All generated log files are stored inside this directory.

Example:

```text
Marvellous/
│
└── DuplicateRemovalLog_02_09_2026_23_30_15.log
```

---

## 6. Command-Line Arguments

The application accepts three command-line arguments.

### Argument 1: Directory Path

The absolute path of the directory that needs to be scanned.

Example:

```text
E:/Data/Demo
```

The directory:

- Must be provided.
- Must be an absolute path.
- Must exist.
- Must be a directory.
- Must be accessible by the application.

**Important:** If the Windows path contains spaces, enclose the complete path in double quotes.

Example:

```powershell
python .\DuplicateFileRemoval.py "D:\Marvellous\Python-ML-AI-GenAI Assignments\File Handling+Scheduling\Python Automation Assignment 33 - Duplicate File Removal Automation\DuplicateFileRemoval\Demo" 1 surajgardi0707@gmail.com
```

### Argument 2: Time Interval

The time interval after which the duplicate-file removal operation should be repeated.

The interval is specified in minutes.

Example:

```text
50
```

The value:

- Must be numeric.
- Must be greater than zero.
- Is interpreted in minutes.

For testing, a smaller value such as `1` minute can be used.

### Argument 3: Receiver Email Address

The email address to which the generated log file and operation statistics will be sent.

Example:

```text
marvellousinfosystem@gmail.com
```

The email address must have a valid basic email format.

---

## 7. Execution Command

The general execution format is:

```bash
python DuplicateFileRemoval.py <DirectoryPath> <IntervalInMinutes> <ReceiverEmail>
```

Example:

```bash
python DuplicateFileRemoval.py E:/Data/Demo 50 marvellousinfosystem@gmail.com
```

For testing with a one-minute interval:

```bash
python DuplicateFileRemoval.py E:/Data/Demo 1 marvellousinfosystem@gmail.com
```

### Windows PowerShell Path with Spaces

If the directory path contains spaces, use double quotes around the complete path.

Example:

```powershell
python .\DuplicateFileRemoval.py "D:\Marvellous\Python-ML-AI-GenAI Assignments\File Handling+Scheduling\Python Automation Assignment 33 - Duplicate File Removal Automation\DuplicateFileRemoval\Demo" 1 surajgardi0707@gmail.com
```

---

## 8. Help Command

The application provides a Help option.

Use:

```bash
python DuplicateFileRemoval.py --help
```

or:

```bash
python DuplicateFileRemoval.py -h
```

The Help option displays:

- Purpose of the project
- Required command-line arguments
- Command format
- Description of arguments
- Example command

Example:

```text
Duplicate File Removal Automation

This script scans a directory, identifies duplicate files using
checksums, deletes duplicate files, creates a detailed log file,
and sends the log file through email.

Usage:
python DuplicateFileRemoval.py <DirectoryPath> <IntervalInMinutes> <ReceiverEmail>

Example:
python DuplicateFileRemoval.py E:/Data/Demo 50 marvellousinfosystem@gmail.com
```

---

## 9. Usage Command

The application also provides a Usage option.

Use:

```bash
python DuplicateFileRemoval.py --usage
```

or:

```bash
python DuplicateFileRemoval.py -u
```

The Usage option displays the command format:

```text
Usage:
python DuplicateFileRemoval.py <AbsoluteDirectoryPath> <TimeIntervalInMinutes> <ReceiverEmailAddress>
```

---

## 10. Duplicate File Detection

The application does not identify duplicate files based only on file names.

Instead, it calculates the MD5 checksum of every file.

For example:

```text
File A → MD5 → ABC123
File B → MD5 → ABC123
File C → MD5 → XYZ789
```

Since File A and File B have the same checksum, they are considered duplicates.

The application creates groups of files according to their checksum values.

For every duplicate group:

```text
First File
    ↓
Preserved

Remaining Files
    ↓
Deleted
```

For example:

```text
Demo/
│
├── A.txt
├── B.txt
├── C.txt
└── D.txt
```

If:

```text
A.txt → Hello
B.txt → Hello

C.txt → Python
D.txt → Python
```

Then:

```text
A.txt → Preserved
B.txt → Deleted

C.txt → Preserved
D.txt → Deleted
```

The complete paths of deleted files are recorded in the log file.

---

## 11. Recursive Directory Scanning

The application uses recursive directory scanning.

This means that files located inside subdirectories are also processed.

Example:

```text
E:/Data/Demo
│
├── File1.txt
├── File2.txt
│
├── Folder1
│   ├── File3.txt
│   └── File4.txt
│
└── Folder2
    └── File5.txt
```

All files are considered during the duplicate-file detection process.

---

## 12. Log File

A `Marvellous` directory is created automatically.

The log file is generated inside this directory.

The log file name contains the date and time of creation.

Example:

```text
DuplicateRemovalLog_02_09_2026_23_30_15.log
```

### Log Information

The log file contains:

- Starting time of directory scanning
- Completion time
- Directory scanned
- Total number of files scanned
- Total number of duplicate files found
- Total number of duplicate files deleted
- Original files preserved
- Duplicate files deleted
- Complete paths of deleted files
- Checksum values
- Errors encountered during execution
- Email delivery status

Example log information:

```text
========== Duplicate File Removal ==========

Starting time of directory scanning : 2026-09-02 23:30:15
Directory scanned : E:/Data/Demo

Original File : E:/Data/Demo/A.txt
Checksum : 5d41402abc4b2a76b9719d911017c592

Duplicate File : E:/Data/Demo/B.txt
Checksum : 5d41402abc4b2a76b9719d911017c592

Deleted : E:/Data/Demo/B.txt

========== Operation Statistics ==========

Total number of files scanned : 5
Total number of duplicate files found : 2
Total number of duplicate files deleted : 2

Email delivery status : Successfully sent
```

Operational messages are stored in the log file instead of being continuously displayed on the console.

---

## 13. Periodic Execution

The application uses the `schedule` library to perform the operation repeatedly.

For example:

```bash
python DuplicateFileRemoval.py E:/Data/Demo 50 marvellousinfosystem@gmail.com
```

The application performs the duplicate-file removal operation and then repeats it every 50 minutes.

For testing:

```bash
python DuplicateFileRemoval.py E:/Data/Demo 1 marvellousinfosystem@gmail.com
```

The operation will repeat every 1 minute.

The program continues running until it is manually terminated.

To stop the application:

```text
Ctrl + C
```

---

## 14. Email Notification

After every duplicate-file removal operation, the application sends an email to the receiver.

The email contains:

- Starting time
- Completion time
- Directory scanned
- Total files scanned
- Duplicate files found
- Duplicate files deleted
- Generated log file as an attachment

Example:

```text
Jay Ganesh,

The duplicate-file removal operation has been completed successfully.

Operation Statistics:

Starting time of scanning: 02 September 2026, 11:30:15 PM
Completion time of scanning: 02 September 2026, 11:30:27 PM
Directory scanned: E:/Data/Demo
Total number of files scanned: 125
Total number of duplicate files found: 14
Total number of duplicate files deleted: 14

Please find the detailed log file attached to this email.

Regards,
Marvellous Automation System
```

---

## 15. Email Configuration

The application uses Gmail SMTP for sending email.

The following SMTP configuration is used:

```text
SMTP Server : smtp.gmail.com
SMTP Port   : 587
Security    : STARTTLS
```

The sender email and application password are configured in:

```text
DuplicateFileRemoval.py
```

Example:

```python
SenderEmail = "your_email@gmail.com"
AppPassword = "your_app_password"
```

### Important

Do not share your Gmail password.

For Gmail, use an **App Password** with SMTP authentication.

Email credentials should not be hard-coded when the project is shared publicly.

A safer approach is to use environment variables or another secure configuration method.

---

## 16. Input Validation

Before starting the operation, the application validates all command-line inputs.

### Directory Validation

The application checks:

- Directory path is provided
- Path is absolute
- Directory exists
- Path represents a directory
- Directory is accessible

### Time Interval Validation

The application checks:

- Interval is provided
- Interval is numeric
- Interval is greater than zero

Valid:

```text
1
5
10
50
```

Invalid:

```text
0
-5
abc
```

### Email Validation

The application checks whether the receiver email has a valid basic format.

Example of valid format:

```text
user@gmail.com
```

Example of invalid format:

```text
user
user@
@gmail.com
```

---

## 17. File Validation

Before calculating a checksum or deleting a file, the application checks:

- Whether the file exists
- Whether the path represents a regular file
- Whether the file is readable
- Whether the file can be deleted
- Permission-related errors
- Errors caused by files that are locked or currently in use

Errors are recorded in the log file.

---

## 18. Exception Handling

The project handles expected errors using exception handling.

Examples include:

- Invalid directory
- Permission errors
- File access errors
- File deletion errors
- Checksum calculation errors
- Email connection errors
- Email authentication errors
- Unexpected execution errors

Errors are recorded in the generated log file.

---

## 19. Project Algorithm

The application follows these steps:

```text
1. Read command-line arguments
        ↓
2. Check Help / Usage option
        ↓
3. Validate command-line arguments
        ↓
4. Validate directory
        ↓
5. Validate time interval
        ↓
6. Validate receiver email
        ↓
7. Create Marvellous directory
        ↓
8. Create timestamp-based log file
        ↓
9. Start directory scanning
        ↓
10. Recursively scan all files
        ↓
11. Calculate checksum of every file
        ↓
12. Group files according to checksum
        ↓
13. Identify duplicate files
        ↓
14. Preserve first file
        ↓
15. Delete remaining duplicate files
        ↓
16. Record deleted files in log
        ↓
17. Calculate operation statistics
        ↓
18. Record completion time
        ↓
19. Generate email report
        ↓
20. Attach log file
        ↓
21. Send email
        ↓
22. Wait for specified interval
        ↓
23. Repeat operation
```

---

## 20. Testing Procedure

It is strongly recommended to test the application using a sample directory first.

### Step 1: Create Test Directory

Create:

```text
E:\Data\Demo
```

### Step 2: Create Duplicate Files

Create files such as:

```text
A.txt
B.txt
C.txt
D.txt
```

Put the same content into:

```text
A.txt
B.txt
```

and another same content into:

```text
C.txt
D.txt
```

### Step 3: Run the Application

Use:

```bash
python DuplicateFileRemoval.py E:/Data/Demo 1 your_receiver@gmail.com
```

### Step 4: Check the Directory

After execution:

```text
A.txt → Remains
B.txt → Deleted

C.txt → Remains
D.txt → Deleted
```

### Step 5: Check the Log

Open:

```text
Marvellous/
```

A log file similar to the following should be present:

```text
DuplicateRemovalLog_02_09_2026_23_30_15.log
```

Check that the log contains:

- Starting time
- Completion time
- Directory
- Total files scanned
- Duplicate files found
- Duplicate files deleted
- Deleted file paths
- Checksums
- Email status
- Errors, if any

### Step 6: Check Email

Check the receiver's mailbox.

The email should contain the operation statistics and the generated log file as an attachment.

---

## 21. Expected Result

After every scheduled execution:

1. The supplied directory is recursively scanned.
2. File checksums are calculated.
3. Duplicate files are identified.
4. The first file from every duplicate group is preserved.
5. Remaining duplicate files are deleted.
6. A timestamp-based log file is created.
7. Operation statistics are stored in the log.
8. Deleted file paths are stored in the log.
9. The log file is attached to an email.
10. The email is sent to the receiver.
11. The operation repeats after the specified interval.

---

## 22. Important Notes

### Backup

Deleted files may not be recoverable.

Always test the application on a sample directory before using it on important data.

### First File Preservation

For every duplicate group, the first file detected by the directory scan is preserved.

All remaining files with the same checksum are treated as duplicate copies and deleted.

### Checksum-Based Detection

Files are considered duplicates based on identical checksum values.

File names alone are not used to identify duplicates.

### Email Security

Do not publish or share your email password or App Password.

Email credentials should be stored securely.

### Testing

Always perform testing on a sample directory before running the application on important files.

---

## 23. Troubleshooting

### Problem: `No module named schedule`

Install the required package:

```bash
pip install schedule
```

### Problem: Invalid Directory

Make sure the supplied directory:

- Exists
- Is an absolute path
- Is actually a directory
- Can be accessed by the application

Example:

```bash
python DuplicateFileRemoval.py E:/Data/Demo 1 user@gmail.com
```

If the Windows path contains spaces, use double quotes:

```powershell
python .\DuplicateFileRemoval.py "D:\Path With Spaces\Demo" 1 user@gmail.com
```

### Problem: Invalid Number of Command-Line Arguments

If the directory path contains spaces, make sure the complete path is enclosed in double quotes.

Correct:

```powershell
python .\DuplicateFileRemoval.py "D:\My Folder\Demo" 1 user@gmail.com
```

Incorrect:

```powershell
python .\DuplicateFileRemoval.py D:\My Folder\Demo 1 user@gmail.com
```

### Problem: Email Authentication Failed

Check:

- Sender email address
- Gmail App Password
- Internet connection
- Gmail SMTP configuration

Do not use your normal Gmail password when App Password authentication is required.

### Problem: File Could Not Be Deleted

Possible reasons:

- File is currently open
- File is locked
- Insufficient permission
- File was already deleted
- Another application is using the file

The error will be recorded in the log file.

---

## 24. Author

**Suraj Gardi**

Python Automation Project

---

## 25. Conclusion

Duplicate File Removal Automation provides an automated solution for identifying and removing duplicate files from a directory.

The project combines:

- Python
- File handling
- `os.walk()`
- MD5 checksum generation
- Exception handling
- Command-line arguments
- Scheduling
- Logging
- Email automation
- Modular programming

The application can periodically scan directories, remove duplicate files, maintain detailed logs, and send operation reports through email.
