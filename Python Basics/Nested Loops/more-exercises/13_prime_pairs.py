start1 = int(input())
start2 = int(input())
end1 = int(input())
end2 = int(input())

for x1 in range(start1, start1 + end1 + 1):
    for x2 in range(start2, start2 + end2 + 1):

        if x1 in [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101] and \
                x2 in [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]:
            print(f'{x1}{x2}')
