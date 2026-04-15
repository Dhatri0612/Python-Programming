m=int(input("Enter number of rows: "))
n=int(input("Enter number of columns: "))
arr=[]
for i in range(m):
    row=[]
    for j in range(n):
        val=int(input())
        row.append(val)
    arr.append(row)
for i in range(m):
    for j in range(n):
        print(arr[i][j],end=" ")
    print()

