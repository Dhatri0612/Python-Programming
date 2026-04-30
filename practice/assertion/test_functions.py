import pytest
def square(n):
    return n*n

def is_even(n):
    return n%2==0

def divide(a,b):
    return a/b


def test_square_positive():
    assert square(4)==16
def test_square_zero():
    assert square(0)==0

def test_is_even():
    assert is_even(4)==True
def test_is_odd():
    assert is_even(5)==False

def test_divide():
    assert divide(10,2)==5.0

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(5,0)