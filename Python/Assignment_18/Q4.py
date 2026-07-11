# 4.Write a program which accept N numbers from user and store it into List. Accept one another
# number from user and return frequency of that number from List.
# Input : Number of elements : 11
# Input Elements : 13 5 45 7 4 56 5 34 2 5 65
# Element to search : 5
# Output : 3

def Frequency(No,srch):
    count = 0
    
    for i in No:
        if i == srch:
            count+=1
    
    return count

def main():

    Value = int(input("Enter Number : "))

    Data = []

    for i in range(Value):

        num = int(input(f"Enter Number {i+1} : "))

        Data.append(num)

    srch = int(input("Enter Element to search : "))

    Ret = Frequency(Data,srch)

    print(f"Frequency of {srch} from list is : ",Ret)

if __name__ == "__main__":
    main()