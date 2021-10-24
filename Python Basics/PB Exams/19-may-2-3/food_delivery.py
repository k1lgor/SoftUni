chicken = 10.35
fish = 12.4
veggy = 8.15
delivery = 2.5

chicken_menu = int(input())
fish_menu = int(input())
veggy_menu = int(input())

ttl = chicken * chicken_menu + fish * fish_menu + veggy * veggy_menu
dessert = ttl * 0.2 # + dessert
ttl += delivery + dessert
print(f'Total: {ttl:.2f}')