import pytest
def divide(a,b):
    return a/b
@pytest.mark.parametrize("a,b,result",[
    pytest.param(10,2,5 ,marks=pytest.mark.fast),
    pytest.param(20,4,5,marks=pytest.mark.fast),
    pytest.param(5,0,None, marks=pytest.mark.xfail(reason="dividion by zero")),
    pytest.param(9,3,3, marks=pytest.mark.fast)
])
def test_divide(a,b,result):
    assert divide(a,b)==result