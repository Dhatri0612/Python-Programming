class Shape:
    def area(self):
        print("Area not specified")
class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def area(self):
        print("Rectangle area: ",self.length*self.breadth)

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        print("Circle area: ",3.14*self.radius*self.radius)

r=Rectangle(10,5)
c=Circle(7)
r.area()
c.area()