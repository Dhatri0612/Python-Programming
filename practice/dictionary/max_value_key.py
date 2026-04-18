d = {"a": 10, "b": 5, "c": 15}
max_key = None
max_val = 0
for key, val in d.items():
    if val > max_val:
        max_val = val
        max_key = key

print("Max key:", max_key)
print("Max value:", max_val)