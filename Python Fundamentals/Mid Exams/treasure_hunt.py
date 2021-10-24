treasure = input().split('|')
command = input()
        
while 'Yohoho!' not in command:
    
    action, *items = command.split()
    
    if 'Loot' in action:
        for item in items:
            if item not in treasure:
                treasure.insert(0, item)

    elif 'Drop' in action:
        index = int(items[0])
        if 0 <= index < len(treasure):
            treasure.append(treasure.pop(index))

    elif 'Steal' in action:
        index = int(items[0])
        print(', '.join(treasure[-index:]))
        treasure = treasure[:-index]
        
    command = input()
    
summary = sum(len(item) for item in treasure)

if len(treasure) != 0:
    print(f"Average treasure gain: {(summary / len(treasure)):.2f} pirate credits.")
else:
    print("Failed treasure hunt.")