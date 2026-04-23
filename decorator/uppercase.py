def my_decorator(func):
    def wrapper():
        result=func()
        return result.upper()
    return wrapper


@my_decorator
def get_name():
    return "dhatri"
print(get_name())