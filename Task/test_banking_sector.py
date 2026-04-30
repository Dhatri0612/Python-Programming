import pytest
from banking_sector import transfer,TransferError
def test_successful_transfer():
    result=transfer("1234567890","0987654321",500,1000)
    assert result==500
def test_zero_amount():
    with pytest.raises(TransferError,match="Invalid amount"):
        transfer("1234567890","0987654321",0,1000)
def test_insufficient_balance():
    with pytest.raises(TransferError,match="Insufficient balance"):
        transfer("1234567890","0987654321",500,200)
def test_invalid_account_number():
    with pytest.raises(TransferError,match="Invalid account number"):
        transfer("1234","0987654321",500,1000)
