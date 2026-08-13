# Q5) Frequency of a String in File
# Problem Statement:
# Write a program which accepts a file name and one string from the user and returns the frequency (count of
# occurrences) of that string in the file.
# Input:
# Demo.txt Hii
# Expected Output:
# Count how many times "Hii" appears in Demo.txt.


def main():

    FileName = input("Enter File name : ")

    word = input("Enter word to search in file : ")

    Count = 0

    try:
        fobj = open(FileName, "r")

        Data = fobj.read()


        Words = Data.split()

        Count = 0

        for i in Words:
            if i == word:
                Count += 1  

        
        # Count = Data.count(word)

        print(f"{word} appears {Count} times in {FileName}")
        
        fobj.close()
    
    except FileNotFoundError as ffobj:
        print("File is not present in current directory")


if __name__ == "__main__":
    main()
