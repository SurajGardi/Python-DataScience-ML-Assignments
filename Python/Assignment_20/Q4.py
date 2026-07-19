# 4: Design a Python application that creates three threads named Small, Capital, and Digits.
# • All threads should accept a string as input.
# • The Small thread should count and display the number of lowercase characters.
# • The Capital thread should count and display the number of uppercase characters.
# • The Digits thread should count and display the number of numeric digits.
# • Each thread must also display:
# ◦ Thread ID
# ◦ Thread Name

import threading

def Display(Type, Count):
    print(f"Total {Type} characters are : {Count}")

def CheckSmall(String):
    Count = 0

    print("Thread ID for CheckSmall : ",threading.current_thread().ident)
    print("Thread Name  for CheckSmall: ",threading.current_thread().name)

    for ch in String:
        if(ch >= 'a' and ch <= 'z'):
            Count += 1
    
    Display("Small", Count)


def CheckCapital(String):
    Count = 0

    print("Thread ID for CheckCapital : ",threading.current_thread().ident)
    print("Thread Name for CheckCapital : ",threading.current_thread().name)

    for ch in String:
        if(ch >= 'A' and ch <= 'Z'):
            Count += 1
    
    Display("Capital", Count)



def CheckDigits(String):
    Count = 0

    print("Thread ID for CheckDigits : ",threading.current_thread().ident)
    print("Thread Name for CheckDigits : ",threading.current_thread().name)

    for ch in String:
        if(ch >= '0' and ch <= '9'):
            Count += 1
    
    Display("Digits", Count)


def main():

    Value = input("Enter String : ")

    fobj1 = threading.Thread(name="Small", target=CheckSmall, args=(Value,))
    fobj2 = threading.Thread(name="Capital", target=CheckCapital, args=(Value,))
    fobj3 = threading.Thread(name="Digits", target=CheckDigits, args=(Value,))

    fobj1.start()
    fobj1.join()

    fobj2.start()
    fobj2.join()
    
    fobj3.start()
    fobj3.join()


if __name__ == "__main__":
    main()