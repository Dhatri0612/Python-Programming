import pytest
def reverse(s):
    return s[::-1]
def get_user():
    return {"name": "Dhatri", "age": 22}
def divide(a, b):
    return a / b

# test
def test_reverse():
    assert reverse("madam")=="madam"
    assert reverse("hello")=="olleh"
    assert reverse("")==""
def test_get_user():
    user=get_user()
    assert user["name"]=="Dhatri"
    assert user["age"]==22
    assert "name" in user
def test_divide():
    assert divide(10,2)==5.0
def test_divide_negative():
    assert divide(-10, 2) == -5.0
def test_divide_zero():
    with pytest.raises(ZeroDivisionError):
        divide(5,0)