# Q3) Copy File Contents into a New File (Command Line)
# Problem Statement:
# Write a program which accepts an existing file name through command line arguments, creates a new file
# named Demo.txt, and copies all contents from the given file into Demo.txt.
# Input (Command Line):
# ABC.txt
# Expected Output:
# Create Demo.txt and copy contents of ABC.txt into Demo.txt.


import sys

def main():

    if(len(sys.argv) == 2):

        ExistingFile = sys.argv[1]
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
