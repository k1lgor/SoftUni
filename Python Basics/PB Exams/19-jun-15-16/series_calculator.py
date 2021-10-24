from math import floor
tv_serial = input()
seasons = int(input())
episodes = int(input())
noads_time_episode = float(input())

withads_time_episode = noads_time_episode * 1.2
extra = seasons * 10
ttl = withads_time_episode * episodes * seasons + extra
print(f'Total time needed to watch the {tv_serial} series is {floor(ttl)} minutes.')