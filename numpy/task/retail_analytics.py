import numpy as np
sales=np.random.randint(-50,500,size=(30,5))
# print(sales)
sales[sales<0]=0
print("Sales after replacing negative number: ")
print(sales)

weeks=30//7
weekly_data=sales[:weeks*7]
weekly_data=weekly_data.reshape(weeks,7,5)
weekly_sales=np.sum(weekly_data,axis=1)
print("Weekly Sales")
print(weekly_sales)
avg_weekly_sales = np.mean(weekly_sales, axis=0)
print("Average Weekly Sales Per Product:")
print(avg_weekly_sales)

highest_product=np.argmax(avg_weekly_sales)
print("Product: ", highest_product+1)
print("Highest Average Weekly Sales: ")
print(avg_weekly_sales[highest_product])
