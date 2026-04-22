class Person:
    def __init__(self,name):
        self.name=name
    def show_name(self):
        print("Name: ",self.name)
class Student(Person):
    def __init__(self, name,marks):
        # Person.__init__(self,name)
        super().__init__(name)
        self.marks=marks
    def show_marks(self):
        print("Marks: ",self.marks)

s=Student("Dhatri",80)
s.show_name()
s.show_marks()
