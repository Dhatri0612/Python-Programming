import numpy as np
temp=np.random.randint(20,45,size=(7,24))
print(temp)
daily_max=np.max(temp,axis=1)
print("Daily maximum temp:",daily_max)
daily_min=np.min(temp,axis=1)
print("Daily minimum temp:",daily_min)

variation=daily_max-daily_min
print(variation)
largest_variation_day=np.argmax(variation)+1
print("Largest temperature variation: ",largest_variation_day)

mean_temp=np.mean(temp)
std_temp=np.std(temp)
lower_limit=mean_temp-2*std_temp
upper_limit=mean_temp+2*std_temp
temp[(temp<lower_limit) | (temp>upper_limit)]=mean_temp
print("Updated temperature data after replacing outliers:")
print(temp)

