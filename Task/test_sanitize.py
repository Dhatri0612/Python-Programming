import pytest
from sanitize import sanitize_input,InputSanitizationError
def test_valid_name():
    assert sanitize_input("John Doe!")=="John Doe"
def test_only_special_chars():
    with pytest.raises(InputSanitizationError):
        sanitize_input("!@#$%")
def test_payment_test():
    assert sanitize_input("Payment: 100$")=="Payment 100"