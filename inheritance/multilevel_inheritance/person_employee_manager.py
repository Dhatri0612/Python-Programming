class Person:
    def __init__(self,name):
        self.name=name
    def show_name(self):
        print("Name: ",self.name)
class Employee(Person):
    def __init__(self,name,salary):
        super().__init__(name)
        self.salary=salary
    def show_salary(self):
        print("Salary",self.salary)
class Manager(Employee):
    def __init__(self, name, salary,bonus):
        super().__init__(name, salary)
        self.bonus=bonus
    def total_salary(self):
        total=self.salary+self.bonus
        print("Total salary",total)
m=Manager("Priti",50000,10000)
m.show_name()
m.show_salary()
m.total_salary()

