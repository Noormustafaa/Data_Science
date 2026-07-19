class Car:
    color = "Red"  # Class attribute
    @staticmethod
    def start():
        print("Car is starting...")
    
    @staticmethod
    def stop():
        print("Car is stopping...")

class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name



car1 = ToyotaCar("Toyota Camry")
car2 = ToyotaCar("Toyota Corolla")

print(car1.name)  # Output: Toyota Camry

print(car1.start())  # Output: Car is starting...
print(car1.color)