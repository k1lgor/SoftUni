from math import ceil
breads = int(input())

max_sugar = 0
max_flour = 0
flout = 0
sugar = 0
ttl_sugar = 0
ttl_flour = 0
for i in range(breads):
    cur_sugar = int(input())
    cur_flour = int(input())
    if cur_sugar > max_sugar:
        max_sugar = cur_sugar
    ttl_sugar += cur_sugar
    if cur_flour > max_flour:
        max_flour = cur_flour
    ttl_flour += cur_flour
sugar = ceil(ttl_sugar / 950)
flour = ceil(ttl_flour / 750)
print(f'Sugar: {sugar}\nFlour: {flour}\nMax used flour is {max_flour} grams, max used sugar is {max_sugar} grams.')
