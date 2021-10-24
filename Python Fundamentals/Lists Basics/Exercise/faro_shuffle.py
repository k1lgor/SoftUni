string = input().split(' ')
shuffle = int(input())
shuffled = []

for _ in range(shuffle):
    half1 = string[:len(string)//2]
    half2 = string[len(string)//2:]

    for j in zip(half1, half2):
        shuffled.extend(j)
    string = shuffled
    shuffled = []

print(string)
