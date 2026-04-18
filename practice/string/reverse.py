str = input("Enter string: ")
rev = ""
for i in range(len(str)-1, -1, -1):
    rev += str[i]
print(rev)