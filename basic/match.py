import re

text = "hello123"

match = re.match(r"hello", text)

if match:
    print("Matched at start")
else:
    print("No match")