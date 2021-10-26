days, players, ttl_energy = int(input()), int(input()), float(input())
water_daily, food_daily = float(input()), float(input())

needed_water = water_daily * players * days
needed_food = food_daily * players * days

for day in range(1, days + 1):
    lost_energy = float(input())
    
    if ttl_energy <= 0:
        print(f"You will run out of energy. You will be left with {needed_food:.2f} food and {needed_water:.2f} water.")
        break
    ttl_energy -= lost_energy
    if day % 2 == 0:
        ttl_energy += ttl_energy * 0.05
        needed_water -= needed_water * 0.3
    if day % 3 == 0:
        needed_food -= needed_food / players
        ttl_energy += ttl_energy * 0.1

if ttl_energy > 0:
    print(f"You are ready for the quest. You will be left with - {ttl_energy:.2f} energy!")    
    