# Q4) Compare Two Files (Command Line)
# Problem Statement:
# Write a program which accepts two file names through command line arguments and compares the contents of
# both files.
# • If both files contain the same contents, display Success
# • Otherwise display Failure
# Input (Command Line):
# Demo.txt Hello.txt
# Expected Output:
# Success OR Failure

import sys

def main():

    if(len(sys.argv) == 3):

        ExistingFile = sys.argv[1]
        NewFile = sys.argv[2]

        try:
            fobj = open(ExistingFile, "r")
            nobj = open(NewFile, "r")
            

            ExData = fobj.read()
            NewData = nobj.read()
            
            if ExData == NewData:
                print("Success")
            else:
                print("Failure")
                
            nobj.close()
            fobj.close()
        
        except FileNotFoundError as ffobj:
            print("File is not present in current directory")



if __name__ == "__main__":
    main()
