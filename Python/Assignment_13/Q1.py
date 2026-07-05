# 1. Write a program which accepts length and width of rectangle and prints area.

def AreaOfrectangle(length, width):
    area = length * width
    return area


def main():
    Value1 = int(input("Enter length of rectangle : "))
    Value2 = int(input("Enter width of rectangle : "))

    Ret = AreaOfrectangle(Value1, Value2)

    print("Area of rectangle is : ",Ret)

if __name__ == "__main__":
    main()