class Animal:
       alive = True

       def eat(self):
              print("This animal is eating")
          
       def sleep(self):
              print("This animal is sleeping")

class Dog(Animal):
       def run(self):
              print("The dog is running")


class Fish(Animal):
       def swim(self):
              print("The fish is swimming")


class Pidgeon(Animal):
       def fly(self):
              print("The Pidgeon is flying")



dog1 = Dog()
print("Is the dog alive? ",dog1.alive)
dog1.run()
dog1.eat()
dog1.sleep()

print("----------------------------------------------------------------------")


fish1 = Fish()
print("Is the Fish alive? ",fish1.alive)
fish1.swim()
fish1.eat()
fish1.sleep()

print("-------------------------------------------------------------------------")


pidgeon1 = Pidgeon()
pidgeon1.alive = False
print("Is the Pidgeon alive? ",pidgeon1.alive)
pidgeon1.fly()
pidgeon1.eat()
pidgeon1.sleep()