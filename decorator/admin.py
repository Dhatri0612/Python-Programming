is_admin=False
def my_decorator(func):
    def wrapper():
        if is_admin:
            func()
        else:
            print("access denied")
    return wrapper

@my_decorator
def delete_user():
    print("User Deleted")

delete_user()