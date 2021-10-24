# numbers = list(map(lambda x: int(x), input().split(', ')))
# numbers = input().split(', ')

print([i for i, d in enumerate(input().split(', ')) if int(d) % 2 == 0])
