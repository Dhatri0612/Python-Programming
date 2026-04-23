from abc import ABC , abstractmethod
class Appliance(ABC):
    @abstractmethod
    def turn_on(self):
        pass

class Fan(Appliance):
    def turn_on(self):
        print("Fan is spinning")

class Light(Appliance):
    def turn_on(self):
        print("Light is glowing")

f=Fan()
l=Light()
f.turn_on()
l.turn_on()