def my_decorator(func):
    def wrapper(*args,**kwargs):
        print("Start")
        func(*args,**kwargs)
        print("End")
    return wrapper



@my_decorator
def say_hello(name):
    print("Hello",name)

say_hello("Dhatri")