# 1. Write a program which accepts one character and checks whether it is vowel or consonant.
# Input: a
# Output: Vowel

def CheckVowel(ch):
    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U':
        print("Vowel")
    else :
        print("Not vowel")

def CheckVowel2(ch):
    vowel = 'aeiouAEIOU'
    if ch in vowel:
        print("Vowel(Checked frm CheckVowel2)")
    else :
        print("Not vowel (Checked frm CheckVowel2)")

    

def main():
    Value1 = input("Enter character : ")
    CheckVowel(Value1)
    CheckVowel2(Value1)

if __name__ == "__main__":
    main()