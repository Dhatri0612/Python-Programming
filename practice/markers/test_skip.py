import pytest
def login():
    return True

@pytest.mark.skip(reason="Login API not ready")
def test_skip_login():
    assert login()==True