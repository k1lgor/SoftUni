from math import floor as fl

needed_processors = int(input())
workers = int(input())
days = int(input())

work_time = 8
processor_time = 3
price = 110.1

working_hrs = workers * days * work_time
ttl_processors = fl(working_hrs / processor_time)

if ttl_processors >= needed_processors:
    print(f'Profit: -> {abs((ttl_processors - needed_processors) * price):.2f} BGN')
else:
    print(f'Losses: -> {abs((ttl_processors - needed_processors) * price):.2f} BGN')