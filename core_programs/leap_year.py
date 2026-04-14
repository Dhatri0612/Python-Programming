year=input("Enter year: ")
if len(year)<4:
    print("please enter 4 digit number")
else:
    if int(year)%4==0:
        print("It is a leap year")
    else:
        print("it is not a leap year")