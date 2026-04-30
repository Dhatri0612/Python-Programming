import pytest
@pytest.fixture
def user():
    return {"name": "Dhatri", "age": 22}

# def test_user(user):
#     assert user["name"]=="Dhatri"
#     assert user["age"]>18
#     assert "name" in user

def test_user_name(user):
    assert user["name"] == "Dhatri"

def test_user_age(user):
    assert user["age"] > 18

def test_user_keys(user):
    assert "name" in user