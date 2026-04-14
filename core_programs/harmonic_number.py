n=int(input("Enter value of n: "))
if n==0:
    print("It's not a valid number")
else:
    harmonic=0
    for i in range(1,n+1):
        harmonic+=(1/i)
    print("Harmonic value: ", harmonic)