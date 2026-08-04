student = {
    "name": "Farida",
    "age": 18,
    "major": "Information Technology",
    "gpa": 86
}

print("Student Profile")

for key, value in student.items():
    print(f"{key.capitalize()}: {value}")
