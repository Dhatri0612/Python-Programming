def print_keys(**kwargs):
    for key in kwargs:
        print(key)
d={"name":"Dhatri","age":21}
print_keys(**d)