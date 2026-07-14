class Student:
    college_name = "ABC College"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("adding new student in Database..")


s1 = Student("karan", 97)
print(s1.name, s1.marks)  # karan

print(s1.college_name) # or print(Student.college_name) # ABC College

s2 = Student("arjun", 88)
print(s2.name, s2.marks)

print(s2.college_name)
