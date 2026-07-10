# 10. Write a program which accept name from user and display length of its name.
# Input : Marvellous 
# Output : 10

def LengthX(word):
    count = 0

    for ch in word:
        count += 1

    return count

def main():
    name = input("Enter Name : ")

    Ret = LengthX(name)

    print("Length of word is : ",Ret)

if __name__ == "__main__":
    main()