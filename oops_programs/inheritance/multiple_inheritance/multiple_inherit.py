class Prey:
    def flee(self):
        print("This animal can flee")

class Predator:
    def hunt(self):
        print("This animal can hunt")


class Rabbit(Prey):
    pass

class Lion(Predator):
    pass

class Fish(Prey, Predator):
    pass

rab1 = Rabbit()
print("Rabbit behaviour......")
rab1.flee()

lion1 = Lion()
print("Lion behaviour...........")
lion1.hunt()

fish1 = Fish()
print("Fish behaviour..........")
fish1.flee()
fish1.hunt()
