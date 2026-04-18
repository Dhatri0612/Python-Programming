t = (1, 2, 3, 4)
rev = ()
for i in range(len(t)-1, -1, -1):
    rev = rev + (t[i],)
print(rev)