# 6. Write a program which accept one number and display below pattern.
# Input : 5
# Output : 

#             * * * * *
#             * * * *
#             * * *
#             * *
#             *


def DisplayPattern(No):
    
    for i in range(No):
        for j in range(No-i):
            print("*", end=" ")
        print()

    # By using reverse range
    """for i in range(No, 0, -1):
        for j in range(i):
            print("*", end=" ")
        print()"""

def main():

    Value = int(input("Enter Number : "))
    
    DisplayPattern(Value)

if __name__ == "__main__":
    main()