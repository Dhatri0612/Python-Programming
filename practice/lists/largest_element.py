list=[2,8,31,5,97,55]
max=list[0]
for i in range(len(list)):
    if max<list[i]:
        max=list[i]
print(max)