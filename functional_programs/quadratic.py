import math
a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=int(input("Enter c: "))
delta=b*b-4*a*c
if delta>0:
    x1=(-b+math.sqrt(delta))/(2*a)
    x2=(-b-math.sqrt(delta))/(2*a)
    print("Two real and different roots are: ",x1,x2)
elif delta==0:
    x=-1/(2*a)
    print("Both roots are same: ",x)
else:
    print("Roots are imaginary:- no real solution")