list=[2,8,31,5,97,55]
max=list[0]
smax=list[0]
for i in range(len(list)):
    if max<list[i]:
        smax=max
        max=list[i]
    elif max>list[i] and smax<list[i]:
        smax=list[i]
print(max)
print(smax)