# 5. Write a program which accepts one number and prints that many numbers in reverse
# order.
# Input: 5
# Output: 5 4 3 2 1

def NumbersRev(no):

    for i in range(no):
        print(no)
        no = no - 1

    
def main():
    Value1 = int(input("Enter Number : "))
    NumbersRev(Value1)

if __name__ == "__main__":
    main()