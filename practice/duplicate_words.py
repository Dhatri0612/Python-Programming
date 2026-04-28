import re
text = "this is is a test test string"
match=re.findall(r"(\w+)\s+\1",text)
print(match)