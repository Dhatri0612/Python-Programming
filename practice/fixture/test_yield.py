import pytest
@pytest.fixture
def temp_data():
    print("Start")
    yield [10,20]
    print("End")
def test_temp_data(temp_data):
    assert len(temp_data)==2