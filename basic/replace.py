import re
text="abc123"
match=re.sub(r"\d","#",text)
print(match)