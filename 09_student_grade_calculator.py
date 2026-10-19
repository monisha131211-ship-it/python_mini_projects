# Project 9: Student Grade Calculator

print("Student Grade Calculator")
name = input("Enter student name: ")
subjects = ["Tamil", "English", "Maths", "Science", "Social"]

marks = []
for subject in subjects:
    m = float(input(f"Enter marks in {subject} (out of 100): "))
    marks.append(m)

total = sum(marks)
average = total / len(marks)

if average >= 90:
    grade = "A+"
elif average >= 75:
    grade = "A"
elif average >= 60:
    grade = "B"
elif average >= 40:
    grade = "C"
else:
    grade = "Fail"

print(f"\nStudent : {name}")
print(f"Total   : {total}")
print(f"Average : {average:.1f}")
print(f"Grade   : {grade}")
