numbers = list(map(lambda x: int(x), input().split(', ')))
boundary = 10
old_boundary = 0
max_value = max(numbers)

while True:
    if max_value <= old_boundary:
        break
    group = [num for num in numbers if old_boundary < num <= boundary]
    print(f"Group of {boundary}'s: {group}")
    
    old_boundary = boundary
    boundary += 10
