# 6.Write a program which accept number from user and check whether that number is positive or
# negative or zero.
# Input : 11 Output : Positive Number
# Input : -8 Output : Negative Number
# Input : 0 Output : Zero

def ChkPositive(No):
    if No >= 0:
        print("Positive Number")
    else:
        print("Negative Number")


def main():
   Value = int(input("Enter Number : "))

   ChkPositive(Value)

if __name__ == "__main__":
    main()