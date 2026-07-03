# 4. Write a program which accepts one number and prints all even numbers till that number.
# Input: 10
# Output: 2 4 6 8 10

def CheckEven(no):
    for i in range(no):
        i = i + 1
        if(i % 2 == 0):
            print(i)

    

def main():
    Value1 = int(input("Enter Number : "))
    CheckEven(Value1)

if __name__ == "__main__":
    main()
