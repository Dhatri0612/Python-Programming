class Animal:
    def __init__(self):
        print("Animal created")
class Dog(Animal):
    def __init__(self):
        super().__init__()
        print("Dog created")
d=Dog()