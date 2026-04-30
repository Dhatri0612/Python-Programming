import pytest
def max_num(a,b):
    return a if a>b else b
@pytest.mark.parametrize("a,b,result",[
    (4,2,4),
    (2,5,5),
    (5,5,5),
    (-3,-1,-1),
    (-5,2,2)
])
def test_max_num(a,b,result):
    assert max_num(a,b)==result