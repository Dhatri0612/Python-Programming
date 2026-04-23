# Public
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

e1 = Employee("Dhatri", 21)
print("Name:", e1.name)
print("Age:", e1.age)


# Private
class Employee:
    def __init__(self):
        self.__name = "Harry"

e2 = Employee()
# print(e2.__name)  # error , cannot be accessed directly
print(e2._Employee__name)  # can be accessed indirectly


# Protected
class Employee:
    def __init__(self):
        self._name = "Harry"

e3 = Employee()
print(e3._name)
