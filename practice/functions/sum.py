def summ(*args):
    total=0
    for num in args:
        total+=num
    return total
a=(1,2,3,4)
print(summ(*a))