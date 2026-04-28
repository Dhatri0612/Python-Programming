import re
logs = """
ERROR: Disk full
INFO: Process started
WARNING: Low memory
ERROR: File not found
"""
match=re.findall(r"ERROR:\s*(.*)",logs)
print(match)