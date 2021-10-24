pirate = list(map(int, input().split(">")))
warship = list(map(int, input().split(">")))
HP = int(input())

def checker(ship, start, end=0):
    if 0 <= start < len(ship) and 0 <= end < len(ship):
        return True
    return False

while True:
    
    action, *indices = input().split()

    if action == 'Retire':
        print(f"Pirate ship status: {sum(pirate)}\nWarship status: {sum(warship)}")
        break
    
    if action == 'Status':
        count = sum([1 for x in pirate if x < HP * 0.2])
        print(f"{count} sections need repair.")
        
    if action == 'Fire':
        index, damage = list(map(int, indices))
        if checker(warship, index):
            warship[index] -= damage
            if warship[index] <= 0:
                print("You won! The enemy ship has sunken.")
                exit()
    if action == 'Defend':
        start, end, damage = list(map(int, indices))
        if checker(pirate, start, end):
            for i in range(start, end + 1):
                pirate[i] -= damage
                if pirate[i] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    exit()
        
    if action == 'Repair':
        index, heal = list(map(int, indices))
        if 0 <= index < len(pirate):
            pirate[index] += heal
            if pirate[index] > HP:
                pirate[index] = HP
    
    