import pytest

def cube(n):
    return n**3
@pytest.mark.parametrize("n,result",[
    (2,8),
    (3,27),
    (4,64),
    (0,0),
    (-2,-8)
])
def test_cube(n,result):
    assert cube(n)==result