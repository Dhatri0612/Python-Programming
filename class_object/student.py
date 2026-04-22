class Student:
    def __init__(self,name ,age):
        self.name=name
        self.age=age
    def details(self):
        print("Name: ",self.name)
        print("Age: ",self.age)

a=Student("Dhatri",21)
a.details()