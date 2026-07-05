# 2. Write a program which accepts radius of circle and prints area of circle.


def AreaOfCircle(Radious, PI):
    Ans = PI * Radious * Radious
    return Ans


def main():
    Value1 = int(input("Enter radious of Circle : "))
    PI = 3.14

    Ret = AreaOfCircle(Value1, PI)

    print("Area of Circle is : ",Ret)

if __name__ == "__main__":
    main()