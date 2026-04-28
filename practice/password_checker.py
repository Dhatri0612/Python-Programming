import re
passwords = ["abc123", "123456", "abcdef", "a1b2c3"]
valid=[]
for p in passwords:
    if re.fullmatch(r"(?=.*[a-zA-Z])(?=.*\d)[a-zA-Z0-9]{6,}",p):
        valid.append(p)
print(valid)
