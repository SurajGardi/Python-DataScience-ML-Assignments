# Q5) Search a Word in File
# Problem Statement:
# Write a program which accepts a file name and a word from the user and checks whether that word is present in
# the file or not.
# Input:
# Demo.txt Marvellous
# Expected Output:
# Display whether the word Marvellous is found in Demo.txt or not.


def main():
    FileName = input("Enter File name : ")

    word = input("Enter word to search in file : ")

    try:
        fobj = open(FileName, "r")

        Data = fobj.read()
        
        if word in Data:
            print(f"{word} is present in file")
        else:
            print(f"{word} is NOT present in file")

        fobj.close()
    
    except FileNotFoundError as ffobj:
        print("File is not present in current directory")



if __name__ == "__main__":
    main()
