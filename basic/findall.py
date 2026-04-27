import re
text="one1 two2 three3"
match=re.findall(r"\w+\d",text)
print(match)