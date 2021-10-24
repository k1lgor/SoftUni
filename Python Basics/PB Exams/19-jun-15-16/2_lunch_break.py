from math import ceil
name = input()
episode = int(input())
breaktime = int(input())

lunch = breaktime / 8
rest = breaktime / 4
time = breaktime - lunch - rest
if time < episode:
    print(f'You don\'t have enough time to watch {name}, you need {ceil(abs(time - episode))} more minutes.')
else:
    print(f'You have enough time to watch {name} and left with {ceil(abs(time - episode))} minutes free time.')