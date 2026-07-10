# 5.Write a program which display 10 to 1 on screen.
# Output : 10 9 8 7 6 5 4 3 2 1

def DisplayRev(No):
    for i in range(No,0,-1):
        print(i,  end=" ")

def main():
    Value = int(input("Enter Number : "))

    DisplayRev(Value)

if __name__ == "__main__":
    main()