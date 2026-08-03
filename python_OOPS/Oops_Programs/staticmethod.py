#methods that don't use the self parameter are called static methods. Static methods are defined using the @staticmethod decorator and can be called on the class itself, rather than on an instance of the class. They do not have access to the instance (self) or class (cls) variables and are typically used for utility functions that don't require any information about the instance or class.
class Student:
    @staticmethod #decorator # for Removing error we use @staticmethod decorator. It is used to define a static method in a class. A static method is a method that belongs to the class rather than an instance of the class. It does not have access to the instance (self) or class (cls) variables and can be called on the class itself, rather than on an instance of the class.
    def college():
        print("this is a static method Bro")


# Static method ko DIRECT Class name se call kar sakte hain (Bina object banaye)
Student.college() # we can call the static method directly using the class name without creating an instance of the class.
