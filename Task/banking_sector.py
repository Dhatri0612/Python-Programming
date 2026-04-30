import re
class TransferError(Exception):
    pass
def transfer(from_account,to_account,amount,balance):
    account_pattern=r"^\d{10}$"
    if not re.fullmatch(account_pattern,from_account) or not re.fullmatch(account_pattern,to_account):
        raise TransferError("Invalid account number")
    if amount<=0:
        raise TransferError("Invalid amount")
    if amount>balance:
        raise TransferError("Insufficient balance")
    return balance-amount