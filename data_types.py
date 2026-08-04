ad = "Farida"
yas = 18
boy = 1.60
sagirddir = True
bacariglar = ["Python", "SQL", "Excel"]

student = {
    "name": ad,
    "age": yas,
    "height": boy,
    "is_student": sagirddir,
    "skills": bacariglar
}

print("Student Information")
print(f"Name: {student['name']}")
print(f"Age: {student['age']}")
print(f"Height: {student['height']} m")
print(f"Is Student: {student['is_student']}")
print(f"Skills: {', '.join(student['skills'])}")

print("\nData Types")
print(type(ad))
print(type(yas))
print(type(boy))
print(type(sagirddir))
print(type(bacariglar))
print(type(student))
