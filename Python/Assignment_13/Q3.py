# 3. Write a program which accepts one number and checks whether it is perfect number or not.
# Input: 6
# Output: Perfect Number

def PerfectNo(no):
    sum = 0
    half = int(no / 2) + 1
    # print(half)
    for i in range(1,half):
        if no % i == 0 :
            sum = sum + i
        print(i)

    if no == sum :
        print("Perfect Number")
    else:
        print("Not Perfect Number")
    

def main():
    Value1 = int(input("Enter 1st Number : "))

    PerfectNo(Value1)

if __name__ == "__main__":
    main()