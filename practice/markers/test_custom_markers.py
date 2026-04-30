import pytest
def login():
    return True
def fetch_data():
    return {"data":"ok"}
def slow_process():
    return True
@pytest.mark.api
def test_login():
    assert login()==True
@pytest.mark.api
def test_fetch_data():
    assert fetch_data()["data"]=="ok"
@pytest.mark.slow
def test_slow_process():
    assert slow_process()==True