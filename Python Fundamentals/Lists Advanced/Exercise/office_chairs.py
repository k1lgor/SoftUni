rooms = int(input())
free_chairs = 0

for room in range(rooms):
    chairs, visitors = input().split()

    if len(chairs) > int(visitors):
        free_chairs += len(chairs) - int(visitors)
        
    elif len(chairs) < int(visitors):
        free_chairs -= abs(len(chairs) - int(visitors))
        print(f'{abs(len(chairs) - int(visitors))} more chairs needed in room {room + 1}')
        
if free_chairs >= 0:        
    print(f'Game On, {free_chairs} free chairs left')
