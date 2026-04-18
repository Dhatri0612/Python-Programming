def info(**kwargs):
    for key,value in kwargs.items():
        print(key,":",value)
d={"name":"Dhatri","age":21,"marks":85}
info(**d)
