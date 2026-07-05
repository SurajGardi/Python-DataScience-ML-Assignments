# 10. Write a lambda function which accepts three numbers and returns largest number.

Largest = lambda No1, No2, No3 : No1 if  No1 > No2 and No1 > No3 else No2 if No2 > No1 and No2 > No3 else No3

# def Largest(No1, No2, No3):
#     return No1 if  No1 > No2 and No1 > No3 else No2 if No2 > No1 and No2 > No3 else No3

# def Largest(No1, No2, No3):
#     if No1 > No2 and No3:
#         return No1
#     elif No2 > No1 and No3:
#         return No2
#     else:
#         return No3
    
def main():
    value1 = int(input("Enter 1st Number : "))
    value2 = int(input("Enter 2nd Number : "))
    value3 = int(input("Enter 3rd Number : "))

    Ret = Largest(value1, value2,value3)

    print(f"Largest Number is {Ret}")
   

if __name__ == "__main__":
    main()