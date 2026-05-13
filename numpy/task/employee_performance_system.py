import numpy as np
ratings=np.random.randint(0,6,size=(100,4))
print(ratings)
min_value=ratings.min()
max_value=ratings.max()
normalized_ratings = (ratings - min_value) / (max_value - min_value)
print("Normalized Ratings")
print(normalized_ratings)

avg_ratings_per_employee=np.mean(ratings,axis=1)
print("Average Ratings Per Employee")
print(avg_ratings_per_employee)

company_mean=np.mean(avg_ratings_per_employee)
above_mean_employees=np.where(avg_ratings_per_employee>company_mean)[0]
print("Company Mean Rating:", company_mean)
print("Employees with Above Average Performance:")
print(above_mean_employees)