class Students:

        #Called Default Constructor
    def __init__(self):
        
        print(self)

        print("Hi This is Constructor")

    def __init__(self, fullname):
        self.name = fullname
        print(self)

        print("Hi This is Constructor")

s1 = Students("Noor Mustafaa")
print(s1)
print(s1.name)

s2= Students("Ali Khan")
print(s2.name)
