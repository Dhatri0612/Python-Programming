list=[1,2,2,3,4,4]
res=[]
for i in range(len(list)):
    if list[i] not in res:
        res.append(list[i])
print(res)

