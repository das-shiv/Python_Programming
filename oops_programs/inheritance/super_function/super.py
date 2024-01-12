class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"The {self.brand} is starting")


class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def start(self):
        super().start()
        print(f"The {self.model} model of {self.brand} brand is staring")


car1 = Car("Tata","Nano")
car1.start()