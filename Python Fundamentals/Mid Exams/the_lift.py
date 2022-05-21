def empty_spots(empty, queue, ppl):
    if queue == 0 and empty > 0:
        return print("The lift has empty spots!")
    elif queue > 0:
        return print(f"There isn't enough space! {queue} people in a queue!")
    elif empty == ppl and queue == 0:
        return


queue = int(input())
ppl = queue
wagon = list(map(lambda x: int(x), input().split(' ')))
empty = 0

for index in range(len(wagon)):

    if wagon[index] < 4 and queue >= 4:
        free_seats = 4 - wagon[index]
        wagon[index] += free_seats
        queue -= free_seats
    elif wagon[index] < 4:
        wagon[index] += queue
        queue -= queue

total_seats = sum(wagon)
empty_seats = len(wagon) * 4 - total_seats
empty_spots(empty_seats, queue, ppl)

print(' '.join(list(map(str, wagon))))
