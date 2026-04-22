class Father:
    def skills(self):
        print("father: ","Patience")
class Mother:
    def talent(self):
        print("mother: ","Singing")
class Child(Father,Mother):
    pass
c=Child()
c.talent()
c.skills()