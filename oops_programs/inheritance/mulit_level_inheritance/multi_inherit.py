class Oragnism:
    alive = True


class Animal(Oragnism):
    def eat(self):
        print("This animal is eating")

class Dog(Animal):
    def bark(self):
        print("This dog is barking")


dog1 = Dog()
print("Is this dog alive? ",dog1.alive)
dog1.eat()
dog1.bark()

