import pytest
from health_care import validate_patient,PatientValidationError
def test_valid_patient():
    assert validate_patient(50,70)==True
def test_invalid_age():
    with pytest.raises(PatientValidationError,match="Invalid age"):
        validate_patient(140,70)
def test_invalid_heart_rate():
    with pytest.raises(PatientValidationError,match="Invalid heart rate"):
        validate_patient(50,240)
