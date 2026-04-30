import pytest
from employee_data import validate_employee
def test_valid_employee():
    assert validate_employee("EMP-1234","john@company.com")==True

def test_invalid_employee_id():
    with pytest.raises(ValueError,match="Invalid Employee ID"):
        validate_employee("EMP-12","john@company.com")
def test_invalid_email():
    with pytest.raises(ValueError,match="Invalid email"):
        validate_employee("EMP-1234","john@gmail.com")
