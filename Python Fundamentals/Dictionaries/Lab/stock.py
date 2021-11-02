random_list = input().split(" ")
products = input().split(" ")

random_dict = {}

for i in range(0, len(random_list), 2):
    key = random_list[i] 
    random_dict[key] = int(random_list[i + 1])

for item in products:
    if item in random_dict:
        print(f"We have {random_dict[item]} of {item} left")
    else:
        print(f"Sorry, we don't have {item}")