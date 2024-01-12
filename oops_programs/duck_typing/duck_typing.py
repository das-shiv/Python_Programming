class Duck:
    def walk(self):
        print("The duck is walking")

    def talk(self):
        print("The duck is qualking")


class Dog:
    def walk(self):
        print("The dog is walking")

    def talk(self):
        print("The dog is barking")


class Person:
    def catch(self,obj):
        obj.walk()
        obj.talk()


duck = Duck()
dog = Dog()
p = Person()

p.catch(duck) # here we are passing the duck object, and hence the catch function will invoke Duck class's walk and talk method.

p.catch(dog) # here we are passing the dog object, and hence the catch function will invoke Dog class's walk and talk method.

