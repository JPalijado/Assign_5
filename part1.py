import math

def InputGrade():
    grade = float(input("Enter Grade: "))
    return grade

def RoundOffGrade(grade):
    if (grade % 1) >= 0.5:
        rGrade = math.ceil(grade)
    else:
        rGrade = math.floor(grade)
    return rGrade

def DisplayOutput(rGrade):
    if rGrade >= 97 and rGrade <= 100:
        print("Mark: 1.0 \nDescription: Excellent")
    elif rGrade >= 94 and rGrade <= 96:
        print("Mark: 1.25 \nDescription: Excellent")
    elif rGrade >= 91 and rGrade <= 93:
        print("Mark: 1.5 \nDescription: Very Good")
    elif rGrade >= 88 and rGrade <= 90:
        print("Mark: 1.75 \nDescription: Very Good")
    elif rGrade >= 85 and rGrade <= 87:
        print("Mark: 2.0 \nDescription: Good") 
    elif rGrade >= 82 and rGrade <= 84:
        print("Mark: 2.25 \nDescription: Good")
    elif rGrade >= 79 and rGrade <= 81:
        print("Mark: 2.5 \nDescription: Satisfactory")
    elif rGrade >= 76 and rGrade <= 78:
        print("Mark: 2.75 \nDescription: Satisfactory")
    elif rGrade == 75:
        print("Mark: 3.0 \nDescription: Passing")
    elif rGrade >= 76 and rGrade <= 74:
        print("Mark: 5.0 \nDescription: Failure")
    else:
        print("Invalid grade")

grade = InputGrade()
rGrade = RoundOffGrade(grade)

DisplayOutput(rGrade)
