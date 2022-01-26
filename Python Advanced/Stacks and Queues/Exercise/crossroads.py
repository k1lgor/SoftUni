from collections import deque

green_light_duration = int(input())
free_window_duration = int(input())
command = input()

cars = deque()
cars_passed = 0
crashed = False
exited = False
car = ''
free = 0

while 'END' not in command:
    while command not in 'green':
        if command == 'END':
            exited = True
            break
        cars.append(command)
        command = input()
    if exited:
        break
    green = green_light_duration

    while green > 0 and len(cars) > 0:
        car = cars.popleft()
        green -= len(car)
        if green < 0:
            free = green + free_window_duration
            if free < 0:
                crashed = True
                break

        cars_passed += 1
    if crashed:
        break
    command = input()

if not crashed:
    print(f"Everyone is safe.\n{cars_passed} total cars passed the crossroads.")
else:
    print(f"A crash happened!\n{car} was hit at {car[free]}.")
