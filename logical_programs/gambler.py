import random
stake=int(input("Enter stake: "))
goal=int(input("Enter goal: "))
trial=int(input("Enter number of trial: "))
win=0
bets=0
for i in range(trial):
    cash=stake
    while cash>0 and cash<goal:
        bets+=1
        if random.random()>0.5:
            cash+=1
        else:
            cash-=1
    if cash==goal:
        win+=1
print("Total number of wins: ",win)
win_percent=(win/trial)*100
loss_percent=100-win_percent
print("Win percentage is: ",win_percent)
print("Loss percentage is: ",loss_percent)
print("Total bets:", bets)