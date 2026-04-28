import re
numbers = ["9876543210", "12345", "9123456780"]
valid_numbers=[]
for num in numbers:
    if re.findall(r"^\d{10}$",num):
        valid_numbers.append(num)
print(valid_numbers)