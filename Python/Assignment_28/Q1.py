# Q1) Count Lines in a File
# Problem Statement:
# Write a program which accepts a file name from the user and counts how many lines are present in the file.
# Input:
# Demo.txt
# Expected Output:
# Total number of lines in Demo.txt.

def main():
    FileName = input("Enter File name : ")
    try:
        fobj = open(FileName, "r")

        Count = 0

        for line in fobj:
            Count += 1

        print(f"Total number of lines in {FileName} are : ",Count)
        
        # Lines = fobj.readlines()
        # print(f"Total number of lines in {FileName} is : ",len(Lines))

    except FileNotFoundError as ffobj:
        print("File is not present in current directory")



if __name__ == "__main__":
    main()
