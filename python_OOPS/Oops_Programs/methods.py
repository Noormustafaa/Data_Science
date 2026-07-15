# creating class
class Student:
    def __init__(self, fullname):
        self.name = fullname
       

    def hello(self):
        print("hello", self.name)


    def welcome(self):
        print("welcome", self.name)


# creating object
s1 = Student("karan")
s1.hello()
s1.welcome()
