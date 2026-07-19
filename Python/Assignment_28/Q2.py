# Q2) Count Words in a File
# Problem Statement:
# Write a program which accepts a file name from the user and counts the total number of words in that file.
# Input:
# Demo.txt
# Expected Output:
# Total number of words in Demo.txt.


def main():
    FileName = input("Enter File name : ")
    try:
        fobj = open(FileName, "r")

        # Count = 0

        # for line in fobj:
        #     Words = line.split()
        #     Count += len(Words)

        # print(f"Total number of lines in {FileName} are : ",Count)
    
        Data = fobj.read()
        Words = Data.split()
        print("Total Words :", len(Words))

    except FileNotFoundError as ffobj:
        print("File is not present in current directory")



if __name__ == "__main__":
    main()
