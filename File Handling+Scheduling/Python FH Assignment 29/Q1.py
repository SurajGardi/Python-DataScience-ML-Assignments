# Q1) Check File Exists in Current Directory
# Problem Statement:
# Write a program which accepts a file name from the user and checks whether that file exists in the current directory or not.
# Input:
# Demo.txt
# Expected Output:
# Display whether Demo.txt exists or not.

import os 

def main():
    Name = input("Enter File name : ")
  
        
    for FolderName, SubFolder, FileName in os.walk("Marvellous"):

        if Name in FileName:
            print(f"{Name} is exist in this Directory")
            return
        
    print(f"{Name} is NOT exist in this Directory")



if __name__ == "__main__":
    main()
