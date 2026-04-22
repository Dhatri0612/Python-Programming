class Camera:
    def click(self):
        print("Photo clicked")
class Phone:
    def call(self):
        print("Calling")
class SmartPhone(Camera,Phone):
    pass
s=SmartPhone()
s.click()
s.call()