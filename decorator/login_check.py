def login_required(func):
    def wrapper():
        print("user logged in")
        func()
    return wrapper

@login_required
def profile():
    print("user profile")
profile()