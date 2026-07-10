# 9. Write a program which display first 10 even numbers on screen.
# Output : 2 4 6 8 10 12 14 16 18 20

def DisplyEven(No):
    count = 0
    number = 2

    while count < No:
        print(number, end=" ")
        number += 2
        count += 1       
        
def main():
    Value = int(input("Enter Number : "))

    DisplyEven(Value)

if __name__ == "__main__":
    main()