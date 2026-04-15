import random
n=int(input("Enter number of times to flip coin "))
if n<0:
    print("please enter positive number")
else:
    heads=0
    tails=0
    for i in range(n):
        if random.random()<0.5:
            heads+=1
        else: 
            tails+=1
    heads_percentage=(heads/n)*100
    tails_percentage=(tails/n)*100
    print(heads_percentage)
    print(tails_percentage)