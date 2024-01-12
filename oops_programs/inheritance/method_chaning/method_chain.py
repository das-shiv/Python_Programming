class Car:
    def start(self):
        print("The car has started")
        return self

    def drive(self):
        print("The car is driving")
        return self

    def brake(self):
        print("The brakes are applied")
        return self

    def stop(self):
        print("The car has stopped")
        return self

car1 = Car()

# Method chaining
car1.start().drive().brake().stop()
