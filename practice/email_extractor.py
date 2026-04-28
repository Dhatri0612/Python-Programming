import re
# text="sharma.priya12@gmail.com"
# match=re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",text)
# print(match)
text = """
Contact us at support@gmail.com or sales@yahoo.com
Also try admin@company.org
"""
match=re.findall(r"[a-zA-Z0-9_.%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",text)
if match:
    print(match)