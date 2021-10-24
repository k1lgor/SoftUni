pics = int(input())
scenes = int(input())
time_scene = int(input())

warmup = pics * 0.15
ttl = scenes * time_scene + warmup
if pics < ttl:
    print(f'Time is up! To complete the movie you need {round(abs(pics - ttl))} minutes.')
else:
    print(f'You managed to finish the movie on time! You have {round(abs(pics - ttl))} minutes left!')