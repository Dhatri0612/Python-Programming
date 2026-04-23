class Account:
    def __init__(self,password):
        self.__password=password
    def set_password(self,old,new):
        if old==self.__password:
            self.__password=new
            print("Password changed") 
        else:
            print("Incorrect password")
    def login(self,password):
        if password==self.__password:
            print("Login Successful")
        else:
            print("Wrong Password")
a=Account("ab1234")
a.set_password("ab1234","abcd12")
a.login("abcd11")