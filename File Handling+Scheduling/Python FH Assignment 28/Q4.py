# Q4) Copy File Contents into Another File
# Problem Statement:
# Write a program which accepts two file names from the user.
# • First file is an existing file
# • Second file is a new file
# Copy all contents from the first file into the second file.
# Input:
# ABC.txt Demo.txt
# Expected Output:
# Contents of ABC.txt copied into Demo.txt.

def main():

    ExistingFile = input("Enter Existing File name : ")
    NewFile = input("Enter New File name : ")

    try:
        fobj = open(ExistingFile, "r")

        nobj = open(NewFile, "w")

        # for line in fobj:
        #     nobj.write(line)

        Data = fobj.read()
        nobj.write(Data)

        print("Contents copied successfully.")
            
        nobj.close()
        fobj.close()
    
    except FileNotFoundError as ffobj:
        print("File is not present in current directory")



if __name__ == "__main__":
    main()
