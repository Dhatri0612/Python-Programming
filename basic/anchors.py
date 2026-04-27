import re

text = "1hello"

# Start with digit
if re.search(r"^\d", text):
    print("Starts with digit")
else:
    print("Does not start with digit")

# End with letter
if re.search(r"[a-zA-Z]$", text):
    print("Ends with letter")
else:
    print("Does not end with letter")

# Word boundary
txt = "cat scatter category cat"
print(re.findall(r"\bcat\b", txt))

# Not word boundary
print(re.findall(r"\Bcat\B", txt))