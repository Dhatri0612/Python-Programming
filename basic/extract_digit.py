import re
text="abc123xyz"
match=re.findall(r"\d+",text)
print(match)