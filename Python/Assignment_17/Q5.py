# 5.Write a program which accept one number for user and check whether number is prime or not.
# Input : 5 Output : It is Prime Number

def CheckPrime(No):
    if No <= 1:
        print("Not Prime Number")
        return
    
    else:
        prime = True

        for i in range(2, No // 2 + 1):
            if No % i == 0:
                prime = False
                break
    
    if prime == True:
        print("Prime Number")
    else :
        print("Not Prime Number")

    

def main():
    Value1 = int(input("Enter Number : "))
    CheckPrime(Value1)

if __name__ == "__main__":
    main()