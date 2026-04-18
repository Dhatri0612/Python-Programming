t = (1, 2, 3, 2, 4)

max = t[0]
min= t[0]

for num in t:
    if num > max:
        max = num
    if num < min:
        min= num

print("Max =", max)
print("Min =", min)