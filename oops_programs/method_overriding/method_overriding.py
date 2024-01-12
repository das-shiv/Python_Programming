class Animal:
    def eat(self):
        print("This animal is eating")


class Rabbit(Animal):
    def eat(self):
        print("This rabbit is eating")  #The eat method from Animal class is overriden in the Rabbit class.



rab1 = Rabbit()
rab1.eat()