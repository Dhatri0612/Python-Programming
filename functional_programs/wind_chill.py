t=float(input("Enter temprature: "))
v=float(input("Enter wind speed: "))
w=35.74+0.6215*t +(0.4275*t -35.75)*pow(v,0.16)
print("Wind Chill = ",w)