class Student:
    def __init__(self):
        self.__marks=0
    def set_marks(self,marks):
        if 0<=marks<=100:
            self.__marks=marks
        else:
            print("invalid marks")
    def get_marks(self):
        return self.__marks
s=Student()
s.set_marks(80)
print(s.get_marks())
