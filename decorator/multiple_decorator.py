def before_decorator(func):
    def wrapper():
        print("before")
        func()
    return wrapper
def after_decorator(func):
    def wrapper():
        result=func()
        print("after")
        return result
    return wrapper

@before_decorator
@after_decorator
def greet():
    print("Hello")
greet()