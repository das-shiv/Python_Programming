class Car:
    color = None

class Motorcycle:
    color = None

def change_color(obj_arg,color):
    obj_arg.color = color

car1 = Car()
change_color(car1,"red") # car1 object is passed as an argument to the change_color function
print(f"The color of car1 is: {car1.color}")

m1 = Motorcycle()
change_color(m1,"Black") #m1 object is passed as an argument to the change_color function
print(f"The color of m1 is: {m1.color}")
