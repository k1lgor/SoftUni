steps_per_day = 10000
steps = ''
walked = 0
while steps != 'Going home':
    steps = input()
    if steps == 'Going home':
        steps = input()
        walked += int(steps)
        if walked >= steps_per_day:
            print(
                f'Goal reached! Good job!\n{abs(walked - steps_per_day)} steps over the goal!')
        else:
            print(f'{steps_per_day - walked} more steps to reach goal.')
        break
    walked += int(steps)
    if walked >= steps_per_day:
        print(
            f'Goal reached! Good job!\n{abs(walked - steps_per_day)} steps over the goal!')
        break
