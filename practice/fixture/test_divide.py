import pytest
@pytest.fixture
def numbers():
    return (10,2)

def test_divide(numbers):
    a,b=numbers
    assert a/b==5