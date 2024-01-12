from abc import ABC, abstractmethod #ABC is Abstract Base Class, it is imported from the abc module. abstractmethod is used to create abstract methods 
class Shape(ABC):  # Shape class is derived from ABC class
    @abstractmethod
    def area(self):  #area() is an abstract method, every class that is derived from Shape class must implement the area() method
        pass  

    @abstractmethod
    def perimeter(self):
        pass



class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        area = 3.14*self.radius*self.radius
        print(f"The area of the circle is: {area}")

    def perimeter(self):
        peri = 2*3.14*self.radius
        print(f"The perimeter of the circle is: {peri}")


class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        area = self.height*self.width
        print(f"The area of the rectangle is: {area}")

    def perimeter(self):
        peri = 2*self.height*self.width
        print(f"The perimeter of the rectangle is: {peri}")


c1 = Circle(12)
c1.area()
c1.perimeter()
print("-----------------------------------")

r1 = Rectangle(24,34)
r1.area()
r1.perimeter()


