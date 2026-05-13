import numpy as np
time_spent = np.random.randint(20, 180, size=(14, 6))
print("Time Spent Data:")
print(time_spent)
# Total time spent per course
total_time = np.sum(time_spent, axis=0)
print("Total Time Spent Per Course:")
print(total_time)

# Average daily engagement per course
average_engagement = np.mean(time_spent, axis=0)
print("Average Daily Engagement:")
print(average_engagement)
threshold = 100
high_engagement_courses = np.where(average_engagement > threshold)[0] + 1
print("Courses Exceeding Threshold:")
print(high_engagement_courses)

# Rank courses based on engagement
ranking = np.argsort(total_time)[::-1] + 1
print("Course Ranking:")
print(ranking)