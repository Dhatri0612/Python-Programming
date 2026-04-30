import pytest
from e_commerce import calculate_total
def test_valid_total():
    items=[100,200,300,400]
    tax_rate=0.1
    result=calculate_total(items,tax_rate)
    assert result==1100

def test_negative_price():
    items=[100,-50,200]
    tax_rate=0.1
    with pytest.raises(ValueError,match="Negative price not allowed"):
        calculate_total(items,tax_rate)


def test_invalid_tax_rate():
    items = [100, 200]
    with pytest.raises(ValueError,match="Invalid tax rate"):
        calculate_total(items,1.5)