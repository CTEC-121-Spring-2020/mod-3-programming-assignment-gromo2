# Module 3
#   Programming Assignment 4
#     Prob-3.py

# <Garrett>

def letterGrade(score):
    if score == 5:
        print("A")
    elif score == 4:
        print("B")
    elif score == 3:
        print("C")
    elif score == 2:
        print("D")
    else: print("F")

    grade = unitTest

    return grade

def unitTest():
    letterGrade(4)
    letterGrade(3)
    letterGrade(5)
    letterGrade(1)
    letterGrade(2)
    letterGrade(0)
    

if __name__ == "__main__":
    unitTest()