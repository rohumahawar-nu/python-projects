print("====== Student Result Management System ======")

name = input("Enter your name: ")

subjects = ["Math", "Physics", "Chemistry", "English", "Computer"]

marks = []

for subject in subjects:
    while True:
        m = int(input(f"Enter {subject} marks: "))

        if 0 <= m <= 100:
            marks.append(m)
            break
        else:
            print("Marks must be between 0 and 100")


def total_marks(marks):
    return sum(marks)


def average_marks(marks):
    return sum(marks) / len(marks)


def percentage(marks):
    return (sum(marks) / 500) * 100


def result_status(marks):
    for mark in marks:
        if mark < 33:
            return "Fail"

    if average_marks(marks) >= 40:
        return "Pass"
    else:
        return "Fail"


def grade(marks):
    avg = average_marks(marks)

    if avg >= 90:
        return "A+"
    elif avg >= 75:
        return "B+"
    elif avg >= 60:
        return "C+"
    elif avg >= 45:
        return "D+"
    else:
        return "F"


print("\n========== STUDENT REPORT ==========")
print("Student Name :", name)
print("Total Marks  :", total_marks(marks), "/500")
print("Average      :", round(average_marks(marks), 2))
print("percentage:",round(percentage(marks),2),"%")
print("Result:",result_status(marks))
print("Grade:",grade(marks))
print("======================================")
        
        
