import math
days = int(input())
food_left = int(input())
dog_food = float(input())
cat_food = float(input())
turtle_food = float(input())

ttl = dog_food * days + cat_food * days + turtle_food * days / 1000

if food_left >= ttl:
    print(f'{math.floor(abs(ttl - food_left))} kilos of food left.')
else:
    print(f'{math.ceil(abs(ttl - food_left))} more kilos of food are needed.')
