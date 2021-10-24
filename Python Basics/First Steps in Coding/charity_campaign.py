days = int(input())
bakers = int(input())
cakes = int(input())
waffles = int(input())
pancakes = int(input())

ttl_sum = (((cakes * 45) + (waffles * 5.8) + (pancakes * 3.2)) * bakers) * days

print(f"{ttl_sum - (ttl_sum / 8)}")
