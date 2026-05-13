import numpy as np
transactions = np.random.randint(-5000, 5000, size=(50, 20))
print("Transaction Data:")
print(transactions)

# Separate debit and credit transactions
debit_transactions = transactions[transactions < 0]
credit_transactions = transactions[transactions > 0]
print("Debit Transactions:")
print(debit_transactions)
print("Credit Transactions:")
print(credit_transactions)

# Compute daily net balance changes
daily_net_balance = np.sum(transactions, axis=0)
print("Daily Net Balance Changes:")
print(daily_net_balance)

# Identify accounts with continuous negative balance trends
negative_trend_accounts = np.where(np.all(transactions < 0, axis=1))[0] + 1
print("Accounts with Continuous Negative Balance Trends:")
print(negative_trend_accounts)