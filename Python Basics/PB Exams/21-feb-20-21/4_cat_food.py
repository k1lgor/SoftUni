cats = int(input())
grams_food = 0
group1 = 0
group2 = 0
group3 = 0
price_food = 0
for i in range(cats):
    grams_food = float(input())
    if 100 <= grams_food < 200:
        group1 += 1
    elif 200 <= grams_food < 300:
        group2 += 1
    elif 300 <= grams_food < 400:
        group3 += 1
    price_food += grams_food
price_food /= 1000
print(f'Group 1: {group1} cats.\nGroup 2: {group2} cats.\nGroup 3: {group3} cats.\nPrice for food per day: {(price_food * 12.45):.2f} lv.')