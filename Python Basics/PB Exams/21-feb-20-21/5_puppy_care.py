food_bought = int(input())
command = ''

food_bought_grams = food_bought * 1000

while command != 'Adopted':
    command = input()
    if command == 'Adopted':
        break
    food_bought_grams -= int(command)
if food_bought_grams < 0:
    print(f'Food is not enough. You need {abs(food_bought_grams)} grams more.')
else:
    print(f'Food is enough! Leftovers: {food_bought_grams} grams.')
