# Write a program which accepts one number and prints binary equivalent.

def Binary(number):

    binary = ""

    while number > 0:
        remainder = number % 2
        binary = str(remainder) + binary
        print(binary)
        number = number // 2

    print("Binary Equivalent is :", binary)


def main():

    no = int(input("Enter Number : "))

    Binary(no)


if __name__ == "__main__":
    main()