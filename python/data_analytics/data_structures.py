"""
DICTIONARIES

Built-in, mutable, and efficient data structure that stores data in key-value pairs.
"""

students = {
    "engineering": 220,
    "medicine": 150,
    "arts": 160,
    "languages": 110,
    "law": 130,
}

colleges = {
    "byu": {"students": 1400, "subjects": 15},
    "cal": {"students": 2300, "subjects": 11},
    "mit": {"students": 900, "subjects": 10},
}


def getStudentsBySubject(subject: str):
    if subject in students:
        # print(f"Total of {subject} students is {students[subject]}.")
        return students[subject]
    else:
        # print("Subject do not exist")
        return None


def getStudentsByCollege(college: str):
    if college in colleges:
        return colleges[college]["students"]
    else:
        return None


def setStudents(subject: str, students_value: int):
    # updates an existent OR creates a new one
    students[subject] = students_value


def updateColleges(college, students: int = 0, subjects: int = 1):
    # updates an existent OR creates a new one
    colleges[college] = {"students": students, "subjects": subjects}


print("\nPART 1 - get")
print(students)
print(students.keys())
subject = "engineering"
engineering_students = getStudentsBySubject(subject)
print(f"Total of {subject} students is {students[subject]}.")
college = "mit"
mit_students = getStudentsByCollege(college)
print(f"There's a total of {mit_students} students at {college}.")

print("\nPART 2 - set")
subject = "medicine"
setStudents("geology", 100)
setStudents(subject, 170)
print(students)
college = "harvard"
updateColleges(college, subjects=9)
print(colleges)

print("\nPART 3 - delete")
del students[subject]
print(students)
