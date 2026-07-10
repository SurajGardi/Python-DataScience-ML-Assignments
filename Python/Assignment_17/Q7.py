# 7. Write a program which accept one number and display below pattern.
# Input : 5
# Output : 
            # 1 2 3 4 5
            # 1 2 3 4 5
            # 1 2 3 4 5
            # 1 2 3 4 5
            # 1 2 3 4 5

def DisplayPattern(No):
    for i in range(No):
        for j in range(No):
            print(j+1, end=" ")
        print()

def main():

    Value = int(input("Enter Number : "))
    
    DisplayPattern(Value)

if __name__ == "__main__":
    main()