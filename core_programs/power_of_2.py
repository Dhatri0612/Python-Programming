n=int(input("Enter value of n: "))
if n>=0 and n<31:
    for i in range(n+1):
        print(2,"^",i,"=",2**i)
else:
    print("Not a valid number")