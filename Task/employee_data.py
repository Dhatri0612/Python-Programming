import re
def validate_employee(emp_id,email):
    id_pattern=r"^EMP-\d{4}$"
    email_pattern=r"^[a-zA-Z]+@company\.com$"
    if not re.fullmatch(id_pattern,emp_id):
        raise ValueError("Invalid Employee ID")
    if not re.fullmatch(email_pattern,email):
        raise ValueError("Invalid email")
    return True