class Shape():
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        print("Area of rectangle: ",self.length*self.breadth)
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        print("Area of Circle: ",3.14*self.radius*self.radius)
shape=[Rectangle(4,5),Circle(5)]
for s in shape:
    s.area()