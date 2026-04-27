import re
text="Hello12 world_21"
match=re.findall(r"\w+",text)
print(match)