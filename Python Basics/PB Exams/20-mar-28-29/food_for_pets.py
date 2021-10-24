days = int(input())
ttl_food = float(input())
cat = 0
dog = 0
cat_food = 0
dog_food = 0
biscuits = 0
food = 0
cur_food = 0
ttl_biscuits = 0
for i in range(1, days + 1):
    dog = int(input())
    cat = int(input())
    dog_food += dog
    cat_food += cat
    cur_food = dog + cat
    if i % 3 == 0:
        biscuits += cur_food * 0.1

food = cat_food + dog_food
print(f'Total eaten biscuits: {round(biscuits)}gr.')
print(f'{(food / ttl_food) * 100:.2f}% of the food has been eaten.')
print(f'{(dog_food / food) * 100:.2f}% eaten from the dog.')
print(f'{(cat_food / food) * 100:.2f}% eaten from the cat.')