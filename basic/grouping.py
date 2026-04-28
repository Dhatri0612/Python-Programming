import re
text = "hello hello world world python code"
match=re.findall(r"(\w+)\s+\1",text)
if match:
    print(match)