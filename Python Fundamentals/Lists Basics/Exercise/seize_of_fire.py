fire = input().split("#")
water = int(input())

effort = 0
total_fire = 0
cells = []

print('Cells:')
for i in fire:
    single_fire = i.split(" = ")
    fire_type = single_fire[0]
    fire_level = int(single_fire[1])
    
    if water < fire_level:
        continue
    
    if fire_type == 'High' and 81 <= fire_level <= 125:
        water -= fire_level
        effort += fire_level * 0.25
        total_fire += fire_level
        cells.append(fire_level)
    elif fire_type == 'Medium' and 51 <= fire_level <= 80:
        water -= fire_level
        effort += fire_level * 0.25
        total_fire += fire_level
        cells.append(fire_level)
    elif fire_type == 'Low' and 1 <= fire_level <= 50:
        water -= fire_level
        effort += fire_level * 0.25
        total_fire += fire_level
        cells.append(fire_level)
       
for cell in cells:
    print(f'- {cell}')
print(f'Effort: {effort:.2f}\nTotal Fire: {total_fire}')
