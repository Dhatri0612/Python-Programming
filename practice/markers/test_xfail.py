import pytest
def add(a,b):
    return a+b

@pytest.mark.xfail(reason="Wrong output")
def test_xfail_add():
    assert add(2,2)==5