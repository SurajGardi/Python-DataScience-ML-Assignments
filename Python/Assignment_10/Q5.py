# 5.Write a program which accepts one number and prints all odd numbers till that number.

def CheckOdd(no):
    for i in range(no):
        i = i + 1
        if(i % 2 == 1):
            print(i)

    

def main():
    Value1 = int(input("Enter Number : "))
    CheckOdd(Value1)

if __name__ == "__main__":
    main()
