student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}
for i in student_scores:
    if 91 <= student_scores[i] <= 100:
        student_grades[i] = "Outstanding"
    elif 81 <= student_scores[i] <= 90:
        student_grades[i] = "Exceeds Expectations"
    elif 71 <= student_scores[i] <= 80:
        student_grades[i] = "Acceptable"
    else:
        student_grades[i] = "Fail"

# TODO-2: Write your code below to add the grades to student_grades.👇


# 🚨 Don't change the code below 👇
print(student_grades)

for i in student_grades:
    print(f"{i} is {student_grades[i]}")
