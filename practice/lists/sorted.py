list=[1,2,3,4]
issorted=True
for i in range(len(list)-1):
    if list[i]>list[i+1]:
        issorted=False
        break
if(issorted):
    print("sorted")
else:
    print("unsorted")
