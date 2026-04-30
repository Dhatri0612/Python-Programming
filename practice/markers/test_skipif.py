import pytest
def check_temperature(temp):
    return temp>0
temp=-5
@pytest.mark.skipif(temp <=0, reason="Temperature too low")
def test_skipif_check_temperature():
    assert check_temperature(temp)==True