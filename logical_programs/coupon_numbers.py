import random
def generate_coupon(n):
    return random.randint(0,n-1)

def collect_coupons(n):
    collected=set()
    count=0
    while len(collected)<n:
        num=generate_coupon(n)
        count+=1
        if num not in collected:
            collected.add(num)
    return count   

n=int(input("Enter number of distinct coupons: "))
total_random_numbers=collect_coupons(n)
print("Total random numbers are: ",total_random_numbers)     