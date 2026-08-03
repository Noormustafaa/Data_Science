# There are four Pillars of OOPs
# 1. Encapsulation
# 2. Inheritance
# 3. Polymorphism
# 4. Abstraction


#Abstraction# means in English we say  Hidden ! Thing which is not visible to the user. In OOPs, Abstraction is a process of hiding the implementation details and showing only functionality to the user. In other words, it shows only essential things to the user and hides the internal details.
#Hidding Implementation details from the user is called Abstraction. It helps to reduce programming complexity and effort. It also helps the programmer to build a secure program.
#Showing just Functionality to the user and hiding the internal details is called Abstraction. It helps to reduce programming complexity and effort. It also helps the programmer to build a secure program.

# Example when a car's start's , We don't know how the engine works, we just know that when we turn the key, the car starts. This is an example of abstraction in real life. We don't need to know the internal details of how the engine works, we just need to know how to use it.
class Car:

    def __init__(self):
        self.acc = False
        self.brake = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("Car is started..")


car1 = Car()
car1.start()  # Output: Car is started..   # Assume it as a automated car 

# so here unnecessary details are hidden from the user. The user doesn't need to know how the car is started, he just needs to know that when he presses the start button, the car starts. This is an example of abstraction in OOPs.
