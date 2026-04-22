class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def show_details(self):
        print("Name: ",self.name)
        print("Salary: ",self.salary)
class Manager(Employee):
    def __init__(self,bonus):
        super().__init(name,salary)
        self.bonus=bonus
    def total_Salary(self):
        print("total salary: ",salary+bonus)

m=Manager()