# 8. Write a program which accept number from user and print that number of “*” on screen.
# Input : 5 
# Output : * * * * *

def Display(No):
    for i in range(No):
        print("*", end=" ")

def main():
    Value = int(input("Enter Number : "))

    Display(Value)

if __name__ == "__main__":
    main()