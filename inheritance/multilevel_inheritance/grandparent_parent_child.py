class GrandParent:
    def home(self):
        print("GrandParent's home")
class Parent(GrandParent):
    def car(self):
        print("Parent's car")
class Child(Parent):
    def bike(self):
        print("Child's bike")
c=Child()
c.bike()
c.car()
c.home()