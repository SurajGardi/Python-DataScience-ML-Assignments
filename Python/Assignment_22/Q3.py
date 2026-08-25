"""
3. For every number in the given list, count how many prime numbers
exist between 1 and N using multiprocessing Pool.
Example
10000
20000
30000
40000
Display total prime count for each number.
"""
import multiprocessing

def PrimeCount(No):

    Count = 0

    for i in range(2, No + 1):

        isPrime = True

        for j in range(2, i // 2 + 1):
            if i % j == 0:
                isPrime = False
                break

        if isPrime == True:
            Count += 1
                
        

    return No, Count        # returns a tuple


def main():
    Data = [10000,20000,30000,40000]

    Result = []

    pobj = multiprocessing.Pool()

    Result = pobj.map(PrimeCount, Data)

    pobj.close()
    pobj.join()

    for No, Count in Result:
        
        print("Input Number :", No)
        print("Prime Count :", Count)
        print("--------------------")

if __name__ == "__main__":
    main()