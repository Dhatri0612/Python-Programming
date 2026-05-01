import re
class InputSanitizationError(Exception):
    pass
def sanitize_input(text):
    cleaned=re.sub(r"[^a-zA-Z0-9\s-]","",text)
    cleaned=cleaned.strip()
    if cleaned=="":
        raise InputSanitizationError("Input became empty after sanitization")
    return cleaned