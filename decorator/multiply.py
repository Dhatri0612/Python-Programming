def my_decorator(func):
    def wrapper():
        result=func()
        return result*2
    return wrapper


@my_decorator
def get_number():
    return 5
print(get_number())