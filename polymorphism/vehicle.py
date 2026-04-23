class Vehicle:
    def start(self):
        print("Vehicle started")
class Car(Vehicle):
    def start(self):
        print("Car starts with key")
class Bike(Vehicle):
    def start(self):
        print("Bike starts with kick")
# c=Car()
# b=Bike()
# c.start()
# b.start()
vehicle=[Car(),Bike()]
for v in vehicle:
    v.start()