import pytest
@pytest.fixture
def numbers():
    return [10,20,30]

def test_numbers_length(numbers):
    assert len(numbers)==3
def test_numbers_max(numbers):
    assert max(numbers)==30