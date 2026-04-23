class Employee:
    def __init__(self,salary):
        self.__salary=salary
    def increase_salary(self,amount):
        self.__salary+=amount
    def show_salary(self):
        print(f"Salary is {self.__salary}")
e=Employee(40000)
e.increase_salary(500)
e.show_salary()