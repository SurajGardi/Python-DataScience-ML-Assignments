# Q2) Display File Contents
# Problem Statement:
# Write a program which accepts a file name from the user, opens that file, and displays the entire contents on the
# console.
# Input:
# Demo.txt
# Expected Output:
# Display contents of Demo.txt on console.


import os

def main():
    file = input("Enter File Name : ")

    for FolderName, SubFolder, FileName in os.walk("Marvellous"):
        if file in FileName:

            path = os.path.join(FolderName, file)

            fobj = open(path, "r")

            Data = fobj.read()

            print(Data)

            fobj.close()

        print("File is not present in current directory")


if __name__ == "__main__":
    main()