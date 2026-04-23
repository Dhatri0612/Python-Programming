from abc import ABC,abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass
class UPI(Payment):
    def pay(self,amount):
        print("paid rs ",amount,"using UPI")
class Card(Payment):
    def pay(self,amount):
        print("paid rs ",amount,"using card")
u=UPI()
c=Card()
u.pay(500)
c.pay(1000)
