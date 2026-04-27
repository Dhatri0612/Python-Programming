import re
text="one1 two2 three3"
match=re.finditer(r"\w+\d",text)
for m in match:
    print(m.group())