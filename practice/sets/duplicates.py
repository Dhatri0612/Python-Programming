l = [1, 2, 2, 3, 3, 4, 5, 5, 6]
seen = set()
duplicates = set()
for num in l:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)

print(duplicates)