n=int(input("Enter value of n: "))
arr=[]
print("Enter n elements: ")
for i in range(n):
    arr.append(int(input()))
count=0
print("Triplets are:")
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if arr[i]+arr[j]+arr[k]==0:
                print(arr[i],arr[j],arr[k])
                count+=1
print("total triplets: ",count)