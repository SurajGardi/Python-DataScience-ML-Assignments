# 1. Write a program which accepts one number and prints multiplication table of that number.
# Input: 4
# Output:
# 4 8 12 16 20 24 28 32 36 40

def multTable(No):
    for i in range(10):
        print((i+1) * No)
        i = i + 1

def main():
    Value1 = int(input("Enter Number : "))
    multTable(Value1)

if __name__ == "__main__":
    main()