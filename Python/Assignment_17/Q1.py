"""1.Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub()
for subtraction, Mult() for multiplication and Div() for division. All functions accepts two
parameters as number and perform the operation. Write on python program which call all the
functions from Arithmetic module by accepting the parameters from user."""

from Arithmatic import *

def main():
    print("Enter 1st Number : ")
    Value1 = int(input())
    print("Enter 2nd Number : ")
    Value2 = int(input())

    Ret = Add(Value1, Value2)  
    print("Addition is : ",Ret)
    
    Ret = Sub(Value1, Value2) 
    print("Substraction is : ",Ret)
    
    Ret = Mult(Value1, Value2) 
    print("Multiplication is : ",Ret)
    
    Ret = Div(Value1, Value2) 
    print("Division is : ",Ret)

if __name__ == "__main__":
    main()