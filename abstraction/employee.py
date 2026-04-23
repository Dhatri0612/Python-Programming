from abc import ABC,abstractmethod
class Employee(ABC):
    @abstractmethod
    def salary(self):
        pass
class FullTime(Employee):
     def __init__(self, salary):
        self.salary_amount = salary
    
     def salary(self):
         return self.salary_amount
    
class PartTime(Employee):
    
    def __init__(self, hours, rate):
        self.hours = hours
        self.rate = rate
    
    def salary(self):
        return self.hours * self.rate

f = FullTime(30000)
p = PartTime(5, 200)

print("Full Time Salary:", f.salary())
print("Part Time Salary:", p.salary())