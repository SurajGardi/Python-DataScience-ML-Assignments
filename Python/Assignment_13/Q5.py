# 5. Write a program which accepts marks and displays grade.
# Condition Example:
# • ≥ 75 → Distinction
# • ≥ 60 → First Class
# • ≥ 50 → Second Class
# • < 50 → Fail

def DisplayGrade(subjects, marksList):
    totalMarks = 0
    for mark in marksList:
        totalMarks += mark

    Average = totalMarks / subjects

    print("Average =", Average)

    if Average >= 75 :
        print("Distinction")
    elif Average >= 60 and Average < 75:
        print("First Class")
    elif Average >= 50 and Average < 60:
        print("Second Class")
    else:
        print("Fail")


    
def main():
    no = int(input("Enter number of subjects : "))

    marksList = []

    for i in range(no):
        mark = int(input(f"Enter Marks of subject {i+1}: "))
        marksList.append(mark)
        # marksList.append(int(input("Enter Marks: ")))

    DisplayGrade(no, marksList)


if __name__ == "__main__":
    main()
    