class ATM:
    def __init__(self,pin):
        self.__pin=pin
    def check_pin(self,pin):
        if pin==self.__pin:
            print("Correct pin")
        else:
            print("Incorrect pin")
    def change_pin(self,old,new):
        if old==self.__pin:
            self.__pin=new
            print("PIN changed")
        else:
            print("Incorrect old PIN")
a=ATM(1234)
a.check_pin(5678)
a.change_pin(1234,5678)